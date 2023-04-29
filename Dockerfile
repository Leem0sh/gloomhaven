# syntax = docker/dockerfile:1.5
# https://hub.docker.com/r/docker/dockerfile
# =====================================================================
# Build Image:
# ------------
#
#   >>> docker build -f ./Dockerfile -t services/segmentation .
#
# Run Image:
# ----------
#
#     >>> docker run -p 8080:8080 --rm -it services/segmentation
# =====================================================================
FROM python:3.10.9-slim AS POETRY

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=60 \
    POETRY_VERSION=1.4.1 \
    POETRY_CACHE_DIR="/opt/poetry/.cache"
SHELL ["/bin/bash", "-EeuxoC", "pipefail", "-c"]

RUN pip install --no-input "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.in-project true


WORKDIR /app
COPY --link pyproject.toml poetry.lock /app/
RUN --mount=type=cache,target=$POETRY_CACHE_DIR/cache \
    --mount=type=cache,target=$POETRY_CACHE_DIR/artifacts \
    poetry install -vv --without=dev --no-root --no-interaction --no-ansi

FROM python:3.10.9-slim AS BUILD
# ----------------------------------------------------------------------------------------------------
# 0. Metadata
# ----------------------------------------------------------------------------------------------------
LABEL authors="Šimon Líman"
LABEL maintainer="Šimon Líman"
LABEL org.opencontainers.image.title="Gloomhaven Service"

# ----------------------------------------------------------------------------------------------------
# 1. System Settings
# ----------------------------------------------------------------------------------------------------
ARG PYTHONUNBUFFERED=1
ARG PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1
ARG DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-EeuxoC", "pipefail", "-c"]

# ----------------------------------------------------------------------------------------------------
# 2. App directory
# ---------------------------------------------------------------------------------------------------
RUN groupadd --system user && \
    useradd --shell /sbin/nologin \
      --home /app \
      --comment "Runtime user" \
      --create-home \
      --system \
      --gid user user
RUN echo "alias ll='ls -alFh'" >> /app/.bashrc
RUN echo "alias ..='cd ..'" >> /app/.bashrc
WORKDIR /app

# ---------------------------------------------------------------------
# 3. Requirements
# ---------------------------------------------------------------------
COPY --link --chown=user --from=POETRY /app/.venv /app/.venv

# ---------------------------------------------------------------------
# 4. App sources
# ---------------------------------------------------------------------
COPY --link --chown=user ./gloomapp /app/gloomapp
COPY --link --chown=user ./gloomhaven /app/gloomhaven
COPY --link --chown=user ./manage.py /app/manage.py


# ----------------------------------------------------------------------------------------------------
# 5. Final cleanup
# ---------------------------------------------------------------------------------------------------
RUN (find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf) || true
RUN rm -rfv /tmp/* /var/lib/apt/lists/*
RUN apt-get autoclean && apt-get clean && apt-get autoremove

# ----------------------------------------------------------------------------------------------------
# 6. Prepare Python environment
# ---------------------------------------------------------------------------------------------------
USER user
ENV PATH="/app/.venv/bin:$PATH"

# ---------------------------------------------------------------------
# 7. Define process
# ---------------------------------------------------------------------
EXPOSE 42069
CMD [ "uvicorn", \
      "gloomhaven.asgi:app", \
      "--host=0.0.0.0", \
      "--port=42069", \
      "--workers=2", \
      "--loop=asyncio", \
      "--http=httptools", \
      "--access-log" \
    ]
