# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

CITY_EVENTS = [
  {
    "id": 3,
    "number": 1,
    "text":
      'You decide to unwind at the Sleeping Lion, but just as you are starting to relax, a bear of a man crashes into your table, scattering your drinks across the floor.\n\nTowering over him is a massive Inox. "What did you say about my horns?" the Inox shouts.\n\nThe man stands up and brushes shards of glass from his tunic. "I said the sight of them makes me want to vomit!"\n\nThe Inox roars and charges headlong into the man, crashing through more tables in the process. At this, the entire tavern erupts into violence. After all, when a man is deep into his drink, the last thing you want to do is knock that drink over.',
    "optionA": {
      "choice": 'Join the fray! These insults will not go unanswered!',
      "outcome":
        "Nothing like busting some drunken skulls to lift one's spirits. It turns out to be a great way to unwind. Unfortunately, the proprietor of the Sleeping Lion doesn't exactly see it that way, and he sullenly asks for compensation for the damage you caused.\n\nGain 10 experience each.\n\nEither lose 5 gold each or lose 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-01-b-a.png',
    },
    "optionB": {
      "choice": 'Do your best to stop the fighting. This is a respectable establishment.',
      "outcome":
        'After restraining the enraged Inox and offering to replace the drinks of a few of the more belligerent patrons, you calm the place down a bit. Some of the non-human patrons are understandably on edge, but the proprietor thanks you for your efforts and reimburses you for the drinks.\n\nGain 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-01-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-01-f.png',
    "verified": False,
  },
  {
    "id": 1,
    "number": 2,
    "text":
      'As the daylight fades, you find yourselves wandering through a half-crowded market street, browsing wares.\n\n"Hey! Over here!" You turn in the direction of the voice to see a filthy Vermling gesturing from a dark alley. "Yeah, you grim-looking chaps. I have something you might be interested in."\n\nThe Vermling holds out a piece of metal covered in sludge. "Found this in the sewer. Writing on it I don\'t understand, but I know it\'s valuable. You can have it for ten gold!"',
    "optionA": {
      "choice": 'Pay for the thing. You never know.',
      "outcome":
        'PAY 10 COLLECTIVE GOLD: You hand over the gold and take hold of the piece of garbage. Amidst troubling brown smears you see a lot of meaningless scratches likely made by rats and bugs. Oh well. Sometimes the long shot doesn\'t pay off.\n\nNo effect.\n\nOTHERWISE: "Bah! You don\'t have enough. Come back when you do!"\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-02-b-a.png',
    },
    "optionB": {
      "choice": 'Refuse to pay. Never trust a Vermling.',
      "outcome":
        'You laugh and gesture the Vermling away. You can recognize a low-life swindler when you see one. And that piece of garbage was just...foul.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-02-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-02-f.png',
    "verified": False,
  },
  {
    "id": 5,
    "number": 3,
    "text":
      'As the daylight fades, you find yourselves wandering through a half-crowded market street, browsing wares.\n\n"Hey! Over here!" You turn in the direction a of the voice to see a filthy Vermling gesturing from a dark alley "Yeah, you grim-looking chaps. I have something you might be interested in."\n\nThe Vermling holds out a piece of metal covered in sludge. Found this in the sewer. Writing on it I don\'t understand, but I know its valuable. You can have it for ten gold!"',
    "optionA": {
      "choice": 'Pay for the thing. You never know.',
      "outcome":
        'PAY 10 COLLECTIVE GOLD: You hand over the gold and take hold of the metal. You wipe off the grime and slop to discover a foreign contraption made of large gears and many moving parts. If you can figure out what it is, this device might actually be of some worth.\n\nGain 1 collective "Curious Gear" (Item 125).\n\nGlobal Achievement: "Ancient Technology."\n\nOTHERWISE: "Bah! You don\'t have enough. Come back when you do!"',
      "imageUrl": '/assets/cards/events/base/city/ce-03-b-a.png',
    },
    "optionB": {
      "choice": 'Refuse to pay. Never trust a Vermling.',
      "outcome":
        'You laugh and gesture the Vermling away. You can recognize a low-life swindler when you see one. And that piece of garbage was just..foul.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-03-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-03-f.png',
    "verified": False,
  },
  {
    "id": 7,
    "number": 4,
    "text":
      'Having recently returned from your latest adventure, you are approached by a ratty-looking boy in tears.\n\n"Please, sirs, could you please help me with my cat? He went over there, and I\'m afraid." The boy points a dirty finger at a decrepit, abandoned building. "I don\'t know what else to do."',
    "optionA": {
      "choice": 'Find a cat? You have more important things to do.',
      "outcome":
        'You shake your head and direct the boy to go find his mother. With any luck she will knock some sense into him so that he stops troubling strangers with such trivial matters.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-04-b-a.png',
    },
    "optionB": {
      "choice": 'Reassure the boy and go find the cat.',
      "outcome":
        "You approach the foreboding house full of heroic bravado. There's certainly nothing otherworldly about the structure, but its fallen beams and piles of rubble do make it difficult to look around. By the time you find the cat hiding under a burned-out bed frame, you are utterly exhausted. At least the boy is ecstatic his cat has been found.\n\nLose 1 {Check} each.\n\nGain 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-04-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-04-f.png',
    "verified": False,
  },
  {
    "id": 9,
    "number": 5,
    "text":
      'After resting for the evening, you start out your day noticing a great number of prominent, commanding posters around the city. Reading one, you learn that the Sanctuary of the Great Oak is laying down the foundation for a new building on the east side of Gloomhaven. Everyone is encouraged to come and help. This could be an important community event.',
    "optionA": {
      "choice": 'Go help lay the foundation.',
      "outcome":
        'Amidst a great deal of revelry, you put all you have into laying the foundation of the sanctuary. Surely much good will be done here healing the sick and wounded. After all your exhaustive efforts, though, you might end up being their first patients.\n\nLose 1 {Check}\n\nGain 1 reputation.\n\nGain 1 prosperity.',
      "imageUrl": '/assets/cards/events/base/city/ce-05-b-a.png',
    },
    "optionB": {
      "choice": 'Take the opportunity to steal some valuables in the area while people are distracted.',
      "outcome":
        'You head to the prosperous east side of town, not to help lay down the foundation, but to steal some goods from shopkeepers too silly to lock up their wares during the festivities. You make off with a good deal of money and the distracted guards are none the wiser.\n\nGain 5 gold each.\n\nReputation < -4: Gain 5 additional gold each.',
      "imageUrl": '/assets/cards/events/base/city/ce-05-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-05-f.png',
    "verified": False,
  },
  {
    "id": 10,
    "number": 6,
    "text":
      "You awake in the middle of the night to the sound of alarms ringing in the west. You recognize them as the warning clangs of an attack on the wall.\n\nAny force bold enough to assault the defenses of Gloomhaven can't be good, For a moment you are grateful for the prolific number of guards defending the city. But still, there is always the possibility that the guards may not be enough.",
    "optionA": {
      "choice": 'Go aid in the defense of the city.',
      "outcome":
        'You rush toward the West Gate, eager to fight back the invaders. As you approach, you see a mass of Vermlings climbing over the wall and attacking the guards with daggers and arrows. You yell and charge into the battle. It is a rough fight, but you emerge victorious, covered in fur and blood. The citizens of Gloomhaven remain safe, and the town is free to grow and prosper.\n\nGain 5 experience each.\n\nGain 1 prosperity.',
      "imageUrl": '/assets/cards/events/base/city/ce-06-b-a.png',
    },
    "optionB": {
      "choice":
        'If the guards are distracted by an attacking force, now would be the perfect time to steal some valuables.',
      "outcome":
        'The town erupts into chaos with panicked cries of "Vermlings!" — a perfect opportunity to collect some valuables. Slinking around to an abandoned shop, you find a way in and pilfer the safe. In the morning, the devastation from the assault is noticeable. Downtrodden looks greet you as you passr and you wonder if your presence was missed along the walls.\n\nGain Random Item Design.\n\nReputation > 4: Lose 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-06-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-06-f.png',
    "verified": False,
  },
  {
    "id": 13,
    "number": 7,
    "text":
      'Occasionally your dealings in town lead you past the bustling docks. All conversation gets drowned out by the constant din of loading and unloading cargo and crew. This makes it all the more surprising when you hear a voice above the noise directed straight at you.\n\n"Oi! You with the hard looks and big arms! I desperately need some help o\'er here! Spare a few minutes to help make sure I get out of port on time? Otherwise I\'ll be stuck here until tomorrow!"',
    "optionA": {
      "choice": 'Help the captain load his ship.',
      "outcome":
        "What was advertised as a few minutes turns out to be an hour or two as you lug large crates full of some foul-smelling liquid from a nearby warehouse into the hold of the ship, At least the captain is relieved that he'll be able to set sail on time, though. He gratefully pays you, but you can't help, but think that such menial labor might be beneath you.\n\nGain 5 gold each.\n\nReputation > 9: Lose 1 reputation.\n\nReputation < -4: Gain 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-07-b-a.png',
    },
    "optionB": {
      "choice": "Move on with your business. You don't have the time or inclination for such things.",
      "outcome":
        'Unwilling to be bothered by such trivial matters, you continue on your way amidst curses from the ship\'s captain. "Blast it all! You\'ll get nowhere in life with that sort of attitude!"\n\nReputation > 4: Gain 1 reputation.\n\nReputation < -9: Lose 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-07-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-07-f.png',
    "verified": False,
  },
  {
    "id": 14,
    "number": 8,
    "text":
      'On a trip to the New Market, you see a curious sea chart prominently displayed in a Valrath merchants stall.\n\n"Ah. I see this interests you!" he says while holding it up, taking great care not to damage it. "I\'ve been told this map will lead you to a location of untold riches! Wondrous beyond anything you have seen before!"\n\nThe Valrath gestures grandly with his free hand and his smile grows wide. "How can you say no to this? Just make me an offer!"',
    "optionA": {
      "choice": 'The map docs look valuable. Decide to bargain for it.',
      "outcome":
        'PAY 20 (reputation < 10) or 15 (reputation > 9) COLLECTIVE GOLD: After some amount of haggling back and forth, you settle on a price and pay for the map. You recognize some of the landmarks and should be able to find this place of "untold treasure "by hiring a ship.\n\nUnlock "Sunken Vessel" 93 (N-17).\n\nParty Achievement: "A Map to Treasure."\n\nOTHERWISE: Despite your valiant efforts, you cannot get the merchant to lower his price to something you can afford.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-08-b-a.png',
    },
    "optionB": {
      "choice": 'Refuse to deal with the merchant.',
      "outcome":
        "Wary of the merchant's overly exuberant nature, you politely decline his offer and go about your intended business.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/city/ce-08-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-08-f.png',
    "verified": False,
  },
  {
    "id": 17,
    "number": 9,
    "text":
      'After a night of heavy drinking, you get turned around while navigating the back alleys and find yourself standing before a collapsed section of bricked road that leads down into an underground tunnel.\n\nFueled by curiosity and a bit of liquid courage, you descend in search of adventure. Stumbling around in the vast network of tunnels proves rather fruitless, however, until a well-concealed passage leads you to a long-forgotten stash of weaponry and dried food.\n\nThe stuff could fetch a decent price at the Sunken Market, or you could turn it over to the city guard, which is always in need arms and rations.',
    "optionA": {
      "choice": 'Sell the goods.',
      "outcome":
        "Using a few less-than-savory contacts, you're able to unload the goods for a respectable price. Who knew drunken strolls could prove so profitable?\n\nGain 10 gold each.\n\nReputation < -9: Gain 5 additional gold each.",
      "imageUrl": '/assets/cards/events/base/city/ce-09-b-a.png',
    },
    "optionB": {
      "choice": 'Donate the goods to the city.',
      "outcome":
        'You sleep off the previous nights revelries and approach the Captain of the Guard. "This is wonderful news! With attacks on the city becoming ever more frequent our blacksmiths are having trouble keeping up with our demands. And the food should help considerably if we ever find ourselves under siege. This is truly a big help to the city."\n\nGain 1 prosperity.',
      "imageUrl": '/assets/cards/events/base/city/ce-09-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-09-f.png',
    "verified": False,
  },
  {
    "id": 20,
    "number": 10,
    "text":
      'Relaxing for the evening at the Sleeping Lion, a shifty-looking man approaches you, hand outstretched. In it are a pair of pale dice with crude marks scratched on them.\n\n"Greetings, friends. You look like you could stand to liven things up a bit. Care for a quick game of bone dice with me? I\'m sure we could make it interesting." His other hand pats a coin purse at his side.',
    "optionA": {
      "choice": 'Play a game with the man. It may prove to be a good time.',
      "outcome":
        'REPUTATION > -5: You get into the game, but after a few rounds, your enthusiasm wanes as the man displays a streak of luck that can only be described as "uncanny" You leave the table empty handed.\n\nLose 5 gold each.\n\nOTHERWISE: The man clearly intends to cheat you out of your hard-earned money. He\'s not the only one capable of cheating, however. After a few rounds,you wipe that smile right off his face.\n\nGain 5 gold each.',
      "imageUrl": '/assets/cards/events/base/city/ce-10-b-a.png',
    },
    "optionB": {
      "choice": 'Refuse the game of dice.',
      "outcome":
        "You laugh and wave away the man's offer. You get all the excitement you need fighting toe-to-toe against vicious monsters. In combat, what matters most is planning and tactics, which are far more interesting than some random roll of the dice.\n\nGain 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-10-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-10-f.png',
    "verified": False,
  },
  {
    "id": 21,
    "number": 11,
    "text":
      '"Please, something of interest, sirs." The words come through in chitters and hisses. You turn your head toward an alley in the Ward of Scales to see a Harrower dressed in crude robes and a mask, it holds out a piece of parchment.\n\n"Something for sirs. Very powerful just five gold."\n\nYou can see the parchment has the designs for something on it, but still — you recognize this Harrower. It is known for trading in disreputable goods. You can\'t know where that parchment came from and if anyone saw you dealing with this creature...well, they might get the wrong idea.',
    "optionA": {
      "choice": 'Make a deal wilh the Harrower.',
      "outcome":
        'PAY 5 COLLECTIVE GOLD: Intrigued by the parchment, you quickly make a decision to buy it off the Harrower. The exchange is fast, and then you move on your way, hoping no one saw you.\n\nGain Random Item Design.\n\nReputation > 9: Lose 1 reputation.\n\nOTHERWISE: You try to pay the Harrower less than it asks for, which only manages to anger it. It hisses loudly and shuns you.\n\nLose 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-11-b-a.png',
    },
    "optionB": {
      "choice": 'Shake your head and walk away. Best not to take chances in such situations.',
      "outcome":
        "You loudly refuse the Harrower's offer and continue about your business. That thing should know better than to stray from the Sinking Market.\n\nReputation < -4: Gain 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-11-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-11-f.png',
    "verified": False,
  },
  {
    "id": 23,
    "number": 12,
    "text":
      'A great revelry is underway at the New Market when you arrive to purchase supplies. Investigating further, you discover the town is in the midst of a pie-eating contest.\n\nA group of large sailors sits triumphantly at a long table on a makeshift stage, crumbs and bits of fruit scattered all around. A man in the center stands and addresses the crowd.\n\n"Can no one best our pie-eating prowess? Step up and test your mettle!" With nothing better to do, you head up to the stage.\n\nThe contest goes well for a while as you match the others pie-for-pie, but soon your eating starts to slow, and the sailors are still going strong.',
    "optionA": {
      "choice": 'Yield to the pie and admit defeat.',
      "outcome":
        "You put down uour utensils and yield to the sailors. They roar with pride and slap you on the back. Unfortunately, the sudden jolt doesn't sit well with your stomach, and soon all the pies you ate are coming back up, much to the disgust of the gathered crowd.\n\nLose 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-12-b-a.png',
    },
    "optionB": {
      "choice": 'Power through the pain. You will not be bested!',
      "outcome":
        "You emit a primal yell and continue eating. Pie after pie, your willpower cannot be broken, and eventually the sailors are forced to concede. However, you cannot even stand to shake your foes' hands. Your legs are boneless and your stomach feels worse than it has ever felt before. You have earned glory and prize money, but all you want to do is lie down and wait for the horror to pass.\n\nLose 1 {Check}.\n\nGain 10 gold each.\n\nGain 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-12-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-12-f.png',
    "verified": False,
  },
  {
    "id": 31,
    "number": 13,
    "text":
      'You are walking across the Silent Bridge, headed toward the Sleeping Lion to get a quick meal, when you see a Quatryl standing in front of a small cart laden with plates of food and curious contraptions.\n\n"Come try the delicacies of the East!" the Quatryl barks. "Food enhanced with science! Flavors beyond your wildest imagination!"',
    "optionA": {
      "choice": 'Stop and try the food.',
      "outcome":
        'You decide to indulge in the unknown and see what the Quatryl is offering. He looks very pleased at your approach and instructs you to inhale a tube of vapors, then take a bite from a bowl full of tiny golden spheres. As the spheres melt in your mouth, the taste mixes with the aroma of the vapors to create a wonderful experience. You pay what you can, but the Quatryl seems solely focused on how much you enjoyed the meal.\n\nAll start scenario with {Bless}.\n\nLose 3 gold each.',
      "imageUrl": '/assets/cards/events/base/city/ce-13-b-a.png',
    },
    "optionB": {
      "choice": 'Continue on your way to a less adventurous meal.',
      "outcome":
        'After a quick glance at the cart, you are not even sure how you would go about eating most of the food Best to play it safe in these situations and stick to what you know will fill you up cheaply.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-13-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-13-f.png',
    "verified": False,
  },
  {
    "id": 27,
    "number": 14,
    "text":
      'You hear screams from the south as you approach the docks and see a group of women running toward you in a panic.\n\n"An invasion! They yell as they race by you, nearly knocking you over.\n\nYou hurry to the docks and find a crowd of workers on edge, armed with makeshift weapons and circling one particular pier.\n\nStanding at the far end of the wooden planks is a group of Lurkers — terrifying crab-like monsters as big as an Inox and equally ferocious. Except these Lurkers don\'t appear to be hostile. They are simply standing on the dock, clacking their claws in a strange rhythm.',
    "optionA": {
      "choice": 'Raise arms and fight the Lurkers back into the sea.',
      "outcome":
        'The crowd parts as you approach the dock with weapons drawn. You step onto the soft wood and the Lurkers turn toward you and stop clacking. They all hiss and brandish their claws in aggression. You charge forward and meet the threat head-on, hacking away at their carapaces until they scuttle off the dock and back into the water.\n\nGain 10 experience each.',
      "imageUrl": '/assets/cards/events/base/city/ce-14-b-a.png',
    },
    "optionB": {
      "choice": 'Approach the Lurkers cautiously and attempt to communicate with them.',
      "outcome":
        'The crowd parts as you move toward the dock with both confidence and care. The Lurkers notice your approach and continue to clack in your direction. You call out to them and ask why they are here, but all you get in response is a change in the tempo of their clacking. When you express confusion, they clack again in frustration and scuttle back into the ocean. The crowd is very impressed that you managed to ward off the creatures without using force.\n\nGain 2 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-14-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-14-f.png',
    "verified": False,
  },
  {
    "id": 28,
    "number": 15,
    "text":
      'It was a truly marvelous night, full of alcohol and fuzzy memories. You are heading back to your rooms in high spirits when you take a wrong turn into an alley and trip over a mutilated corpse.\n\n"What\'s all this then?" You look up to see a city guard walk into the alley, annoyed by all the noise you were making in your revelry.\n\nBefore you can react, he draws his sword. "You... what did you do?"\n\nYou look and see that, due to the fall, your clothes are now covered in blood. The guard clearly thinks you are responsible for the man\'s death, This night just took a serious turn for the worse.',
    "optionA": {
      "choice": 'Do your best to explain that the man was like this when you found him.',
      "outcome":
        "REPUTATION > 5: You sober up pretty quickly and explain the situation. Luckily the guard is familiar with your reputation and believes your story. After a few more questions, he allows you to leave and clean up.\n\nNo effect.\n\nOTHERWISE: Attempts to explain yourself just seem to make the situation worse. More guards show up and everyone eyes you suspiciously. Luckily your weapons don't match the man's wounds and the guards let you go, but they do so with a mistrustful glare.\n\nLose 2 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-15-b-a.png',
    },
    "optionB": {
      "choice": 'Panic and kill the guard, then dispose of both corpses.',
      "outcome":
        "The unlucky guard falls to your blade before he is able to call for help. If the bodies are found, it could cause a lot of trouble for you.\n\nPAY 15 COLLECTIVE GOLD: You go looking someone who can properly dispose of the mess. It's not cheap, but one of your contacts promises to make the bodies disappear.\n\nNo effect.\n\nOTHERWISE: Knowing you don't have enough to professional help, you spend all night cleaning up the mess before anyone discovers it.\n\nLose 1 {Check}.",
      "imageUrl": '/assets/cards/events/base/city/ce-15-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-15-f.png',
    "verified": False,
  },
  {
    "id": 30,
    "number": 16,
    "text":
      '"Stop struggling! You\'re coming with me and there\'s nothing you can do about it!"\n\nAhead of you in the street, you see a pair of guards scuffling with a young boy dressed in rags. "You snatch purses, you go to the Ghost Fortress. No way around that."\n\n"But my family is starving." the boy cries. You recognize his voice from some of your dealings in the Sunken Market. He\'s given you helpful tips for mercenary work on a number of occasions.',
    "optionA": {
      "choice": "Intervene on the boy's behalf.",
      "outcome":
        "PAY 10 COLLECTIVE GOLD: You entreat the guards to let the boy go, but they are unmoved. With further pressing, they agree to do so only if you pay his criminal fine. The guards cuff the boy's ear and set him free.\n\nAdd City Event 70 to the deck.\n\nOTHERWISE: You entreat the guards to let the boy go, but they are unmoved. It seems like you may be able to grease their palms a bit, but, unfortunately, you do not have enough money to sway their minds. The boy is hauled off to the Ghost Fortress.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/city/ce-16-b-a.png',
    },
    "optionB": {
      "choice": 'Let the guards haul the boy away to prison.',
      "outcome":
        "There are repercussions to getting caught, and like the guard said, sometimes there's no way out of it. You owe the boy nothing, and so let the guards take him away.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/city/ce-16-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-16-f.png',
    "verified": False,
  },
  {
    "id": 33,
    "number": 17,
    "text":
      "Returning to Gloomhaven with your latest haul of treasure, you approach the market in search of a good trade. Unfortunately, there are only a few visible stands around that are not yet packing up for the day.\n\nA robed Savvas catches your eye. It has a few strange artifacts on display, but you approach with no great expectation, hoping your goods will fetch a decent price.\n\nThe Savvas silently nods as you approach. It picks through your haul and lifts up a single item, holding out a small bag for you in exchange.\n\nPouring out the bag's contents, a single rectangular black-and-white coin lands in your palm.",
    "optionA": {
      "choice": 'Demand a different payment. The single coin is an insult.',
      "outcome":
        "You slam the strange coin back down onto the Savvas' display in anger. It reaches out to grab the coin, but you take hold of its arm and demand a proper payment. Wordlessly, it looks at you with disdain and throws a handful of gold in your face. You shield your eyes and move to draw your weapon, but when you look around, the Savvas and its goods are no longer to be found. You sullenly gather the coins it threw and move on.\n\nGain 10 collective gold.",
      "imageUrl": '/assets/cards/events/base/city/ce-17-b-a.png',
    },
    "optionB": {
      "choice": 'Accept the strange coin and research it for hidden value.',
      "outcome":
        'You calmly assess that the coin may possess much more value than it appears to have. You head to the University and spend hours looking through old records to no avail. You end the day in a tavern, easing the frustration with a drink and loud laments about the coin.\n\n"Those markings are very interesting." You look up to see an Aesther standing over you. "They describe a special meeting place. I can show you where."\n\nUnlock "Temple of the Eclipse" 81 (D-2).',
      "imageUrl": '/assets/cards/events/base/city/ce-17-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-17-f.png',
    "verified": False,
  },
  {
    "id": 35,
    "number": 18,
    "text":
      'You are attending to business in the Sinking Market when a frail white-haired woman approaches you and grabs you by the arm.\n\n"Oh my, don\'t you lot look strong." she says. "Could you possibly assist me with a small problem I am having in my cellar?"\n\nHer eyes grow narrow. "Rats! So many rats! I don\'t know where they\'re coming from, but they are a right nuisance. Ruined three jars of preserves just yesterday!"\n\nShe tugs weakly at your sleeve. "Please, can you help me?"',
    "optionA": {
      "choice": 'Decline to help the old woman.',
      "outcome":
        'You pull your arm away from her filthy grasp and step away, making apologies for being too busy. Your excuses lack the proper tact, however, and soon the woman is bawling in the street, lamenting that no one will help her and how the rats will kill her in her sleep, then feast on her corpse. The whole speech is very graphic, and passersby begin to give you odd looks, wondering what you could have done to upset the poor woman so intensely.\n\nLose 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-18-b-a.png',
    },
    "optionB": {
      "choice": 'Agree to help with the rat infestation.',
      "outcome":
        'You smile broadly and ask the woman to lead you to her house. It is a ramshackle dwelling half sunk into the muddy foundation. And inside there are certainly a lot of rats. You kill as many as you can, but in her cellar you find a large hole leading to a section of sewer that recently collapsed, leaving the pests with nowhere else to go. The woman thanks you for at least helping her to be able to sleep tonight and hands you a few coins.\n\nGain 2 gold each.',
      "imageUrl": '/assets/cards/events/base/city/ce-18-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-18-f.png',
    "verified": False,
  },
  {
    "id": 37,
    "number": 19,
    "text":
      "A curious invitation is slipped under your door in the early morning. It is for a wedding ceremony between the children of two wealthy Gloomhaven merchants. Your exploits seem to have placed you in their good graces, and so they would like you to join them on this special occasion, provided you don't show up in hlood-soaked armor. And for the love of the Great Oak, bring a gift.",
    "optionA": {
      "choice": 'Attend the wedding with an expensive gift.',
      "outcome":
        "REPUTATION > 9, PAY 20 COLLECTIVE GOLD: You head to the New Market and find a magnificent vase to bring as a gift. When the father of the bride sees it, he declares it the most wonderful piece he's ever encountered. You are the talk of the town.\n\nGain 2 reputation.\n\nREPUTATION < 10, PAY 20 COLLECTIVE GOLD: You bring a very expensive vase as a gift, but you can't seem to catch the father of the bride's eve to present it at the right time.\n\nNo effect.\n\nOTHERWISE:\n\nRead outcome B.",
      "imageUrl": '/assets/cards/events/base/city/ce-19-b-a.png',
    },
    "optionB": {
      "choice": 'Attend the wedding and bring a mundane gift.',
      "outcome":
        'REPUTATION < -4: You pick up an unremarkable set of silverware on the way to the event. When you arrive, the father of the bride casts a scornful look your way and begins whispering to those around him. Maybe you received the invitation by mistake.\n\nLose 5 collective gold.\n\nLose 1 reputation.\n\nOTHERWISE: You are one guest among many, and everyone is having too good of a time to notice your poor choice in gifts.\n\nLose 5 collective gold.',
      "imageUrl": '/assets/cards/events/base/city/ce-19-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-19-f.png',
    "verified": False,
  },
  {
    "id": 39,
    "number": 20,
    "text":
      'You are relaxing at the Sleeping Lion when an immaculately dressed man approach your table, a fake smile plastered to his face.\n\n"Ah, you must be the mercenaries everyone is talking about, yes? My name is Lord Greymane and I have a delicate matter to discuss. May I sit?"\n\nYou gesture to a chair and he sits with a faint grimace. "I am transporting some valuable goods this evening from one of my warehouses, and I have reason to believe that some of the less desirable elements of this city wish to steal from me. I would like to hire you to help guard the undertaking."',
    "optionA": {
      "choice": 'Agree to guard the goods. It should be easy money.',
      "outcome":
        'REPUTATION > 9: You head to the warehouse and watch in silence as a number of heavy crates are loaded onto a cart. You then escort the cart to the West Gate. No thefts are attempted, and you are paid well.\n\nGain 10 collective gold.\n\nOTHERWISE: You head to the warehouse and are immediately set upon by a group of thieves. However, they prove no match for your expertise and are quickly dispatched. Greymane thanks you.\n\nGain 5 experience each.\n\nGain 10 collective gold.',
      "imageUrl": '/assets/cards/events/base/city/ce-20-b-a.png',
    },
    "optionB": {
      "choice": 'Politely decline. Yon have much better things to do tonight.',
      "outcome":
        'This is your night off, and you are going to spend it drinking, not guarding some snobby "lord."\n\nIn the morning, you hear news that a shipment of rare minerals bound for the capital was stolen in the night. People are calling it a huge blow to the economy of the town.\n\nLose 1 prosperity.',
      "imageUrl": '/assets/cards/events/base/city/ce-20-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-20-f.png',
    "verified": False,
  },
  {
    "id": 41,
    "number": 21,
    "text":
      '"I\'ve been told you are the group to talk to if you want to get something done around here."\n\nYou look up from your table at the Sleeping Lion to see a rustic man in leather armor standing in front of you.\n\nThis tavern may as well be your office, due to the number of people coming through the doors looking for your help. You nod at the man, and he makes his request.\n\n"My brother went out hunting in the Corpsewood two days ago and hasn\'t returned since, I fear the worst. If you are traveling in that direction, I hope you wouldn\'t mind keeping an eye out for him."',
    "optionA": {
      "choice": "Demand payment up front before agreeing to look for the man's brother.",
      "outcome":
        'REPUTATION > 7: "What? I... Oh, very well." the man stutters. "Since I trust you to keep your word, I\'ll give you a little money for your trouble." The man describes his brother and hands you a small coin pouch.\n\nGain 5 collective gold.\n\nAdd Road Event 65 to the deck.\n\nOTHERWISE: The man puffs up in indignation, letting you know he is insulted by your behavior. He storms out of the tavern in a rage.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-21-b-a.png',
    },
    "optionB": {
      "choice": 'Agree to help the man in his search.',
      "outcome":
        'The man thanks you profusely and gives a detailed description of his brother "If you find him, no matter the condition, please let me know right away."\n\nAdd Road Event 65 to the deck.',
      "imageUrl": '/assets/cards/events/base/city/ce-21-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-21-f.png',
    "verified": False,
  },
  {
    "id": 46,
    "number": 22,
    "text":
      'You decide to head to the Brown Door for the evening to enjoy a Quatryl concert.\n\nCorruption and crime run rampant in the bar, but the music is unmatched in all of Gloomhaven.\n\nYou are enjoying yourself immensely when you catch a glimpse of a man in a dark, tattered robe near the back of the room. He appears to be handing vials full of red liquid to a second man.',
    "optionA": {
      "choice": 'Further investigate the exchange between the men.',
      "outcome":
        'You subtly move in the direction of the men, monitoring their actions with your peripheral vision. You recognize the dark robes from the run-ins you have had with cultists in the area, and as you get closer, you become convinced that the vials being traded contain blood. You grab the men and cause a huge amount of commotion as you fight to drag them outside and foil their dealings. You are able to hand them off to the proper authorities, but it may be a while before you are allowed back in the Brown Door. The concert was ruined.\n\nGain 2 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-22-b-a.png',
    },
    "optionB": {
      "choice": 'Leave the criminal element alone and continue enjoying the show.',
      "outcome":
        'The music is too good to be interrupted. You ignore the men in the back and simply have a great time.\n\nGain 1 {Check} each.',
      "imageUrl": '/assets/cards/events/base/city/ce-22-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-22-f.png',
    "verified": False,
  },
  {
    "id": 42,
    "number": 23,
    "text":
      'You are walking home late at night when you hear some suspicious sounds coming from a nearby garden.\n\nYou move to investigate, and a shadowy figure bolts in the opposite direct carrying an armful of vegetables.',
    "optionA": {
      "choice": 'Give chase. Thieves must be brought to justice.',
      "outcome":
        'The figure overburdened with vegetables is no match for your speed. You quickly run him down and deliver him to the city guard. Thankfully very little of the produce was damaged in the pursuit, and you are able to return it to the owner of the garden.\n\nGain 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-23-b-a.png',
    },
    "optionB": {
      "choice": 'The thief had the right idea. Grab some vegetables for yourself.',
      "outcome":
        "In an area cut off from civilization with no viable farmland, fresh vegetables are a rare commodity. The thief already made off with an armful so what's the harm in taking some more? When you get back to your room, you cook up a nice hearty soup and have a great meal.\n\nAll start scenario with {Bless}.",
      "imageUrl": '/assets/cards/events/base/city/ce-23-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-23-f.png',
    "verified": False,
  },
  {
    "id": 45,
    "number": 24,
    "text":
      'Upon returning to the city after your latest adventure, you are approached by a high-ranking guard at the gate.\n\n"Ah. good, I\'m glad to have caught you, the guard begins. The capital has fallen behind on shipments of wood to Gloomhaven, so now it falls to us to pick up the slack so that construction of important city buildings doesn\'t stagnate."\n\nThe guard points to the east. We\'re forming an expedition to gather logs from the Corpsewood. We could use your help, either to guard against enemies or to chop down trees."',
    "optionA": {
      "choice": 'Join the expedition as a guard.',
      "outcome":
        'The logging expedition heads to the outskirts of the Corpsewood and begins felling trees and transporting them back to Gloomhaven. You stay on your guard, patrolling the area and making sure there are no surprise attacks. A couple hours in, a tribe of Vermlings appear through the woods, but you are alert and prepared, dispatching them without a single casualty. The rest of the day goes by uneventfully.\n\nGain 10 experience each.',
      "imageUrl": '/assets/cards/events/base/city/ce-24-b-a.png',
    },
    "optionB": {
      "choice": 'Join the expedition as a logger.',
      "outcome":
        'You journey out to the Corpsewood, axe in hand and begin chopping away at the trees. You seem to have a natural skill with it, probably due to all the practice you get swinging a blade. Thanks to your help, the city is able to gather a large amount of extra wood for construction. You encounter some dangers throughout the day, but nothing you cannot handle.\n\nGain 1 prosperity.',
      "imageUrl": '/assets/cards/events/base/city/ce-24-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-24-f.png',
    "verified": False,
  },
  {
    "id": 48,
    "number": 25,
    "text":
      'On a trip to the Coin District, you catch sight of an old wiry Valrath carrying a large, intricate vase out his front door.\n\nAs you get closer, the Valrath begins to struggle with the vase, sweat pouring from his brow. Under the strain, the Valrath loses his balance, and the fragile vase topples downward as he yells a string of curses.',
    "optionA": {
      "choice": 'Attempt to catch the vase.',
      "outcome":
        '{Brute} {Cragheart} {LightningBolts}: You race forward and wrap your arms around the vase. You manage to keep grip of it, preventing tragedy. The Valrath is relieved and offers to pay you for your trouble if you carry it the rest of the way.\n\nGain 5 collective gold.\n\nOTHERWISE: You race forward and attempt to catch the vase, but it is too much for you. Your grip loosens and the vase shatters into a hundred pieces. The Valrath is irate, demanding compensation from you for breaking it. You pay him what you can.\n\nLose 10 collective gold.',
      "imageUrl": '/assets/cards/events/base/city/ce-25-b-a.png',
    },
    "optionB": {
      "choice": 'With no time to react watch the vase fall to the ground.',
      "outcome":
        'You watch helplessly as the vase careens out of the Valraths grasp and, once it connects with the hard ground shatters into a hundred pieces. The Valrath looks distraught and a little angry: You exchange a sympathetic glance with him and then continue about your business.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-25-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-25-f.png',
    "verified": False,
  },
  {
    "id": 51,
    "number": 26,
    "text":
      'While enjoying your customary post-adventure drink at the Sleeping Lion, you notice something weird going on with the lamps in the bar.\n\nYour first thought is that it is your imagination, but after staring at the lamps intently, you see they are flickering in and out. Tech lamps, as opposed to normal gas-burning ones, have been known to be a bit unreliable.\n\nAs if on cue, the lamps suddenly go out completely, leaving the room pitch-black.',
    "optionA": {
      "choice": "Offer to fix the lamps. It shouldn't be too hard with a bit of technical know-how.",
      "outcome":
        "{Tinkerer}: You quickly identify the source of the problem — some frayed wiring in the kitchen — and have it replaced in no time. The proprietor seems very impressed by your work and gives free drinks all around in your name.\n\nGain 2 reputation.\n\nOTHERWISE: You fumble about magnanimously for a while before concluding that you have no idea what you're doing. The proprietor looks disappointed and sends out for a real tinkerer.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/city/ce-26-b-a.png',
    },
    "optionB": {
      "choice": 'Take the opportunity to steal some valuables from drunk patrons in the dark.',
      "outcome":
        '{Scoundrel} {Mindthief} {Eclipse}: The darkness gives the less scrupulous among you a good chance to perform their craft. Within a matter of minutes, your coin purses are much heavier.\n\nGain 10 collective gold.\n\nOTHERWISE: You attempt to lighten some purses, but even in the dark, you find the task a little outside your skill set. One patron catches your hand as it searches his belt. He starts yelling, and you flee as quickly as possible.\n\nLose 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-26-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-26-f.png',
    "verified": False,
  },
  {
    "id": 50,
    "number": 27,
    "text":
      'You are out in the Ward of Scales when you see a crowd of people forming to the south, growing louder and more dense by the second.\n\nAs you approach, you see through the angry mob a terrified Vermling being pulled in your direction by a group of gruff men.\n\n"Dirty thief!" a woman next to you screams. "String it up"\n\nGlancing behind you to where the crowd appears to be headed, you see a disused gibbet in the market square.\n\nThe men — clearly not guards — move closer.',
    "optionA": {
      "choice": 'Attempt to stop the crowd from hanging the Vermling,',
      "outcome":
        "{Spellweaver} {PointyHead} {MusicNote}: You keep a calm demeanor as you try to talk down the mob. It takes some effort, but the men finally agree to turn the thief over to the authorities, which stops the situation from devolving into chaos.\n\nGain 1 prosperity.\n\nOTHERWISE: You kindly entreat the crowd to back down, and when that doesn't work, you resort to force. No one seems happy that you stopped the hanging, but it was the right thing to do.\n\nLose 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-27-b-a.png',
    },
    "optionB": {
      "choice": 'lake no action and see this through to its logical conclusion.',
      "outcome":
        "You watch as the men move past you toward the gibbet. One carries a thick rope that he ties around the Vermling's neck. The other end of the rope is thrown over the cross beam and then the men begin pulling, hoisting the helpless thief up off his feet. He struggles in vain, a panicked look in his eyes, but eventually he stops moving. The men tie off the rope, leaving the lifeless thief hanging. People begin to mill about, many stopping to spit on the ground before returning to work.\n\nAdd City Event 60 to the deck.",
      "imageUrl": '/assets/cards/events/base/city/ce-27-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-27-f.png',
    "verified": False,
  },
  {
    "id": 54,
    "number": 28,
    "text":
      'Ah, the Sleeping Lion. Surely there is no better place to get a drink and relax after clearing out some dank dungeon.\n\nOn this particular occasion, though, you are approached by a heavily scarred Inox. She sits at your table and pushes forward a piece of paper.\n\n"An interested party would like to hire you to steal a valuable figurine from a residence in the Battlements." she says matter-of-factly. "The details are on the paper. Meet me in the back alley in two days\' time after the job is done."',
    "optionA": {
      "choice": 'Accept the mysterious job. You can handle anything.',
      "outcome":
        "{Scoundrel} {Mindthief} {Eclipse}: The job proves easy enough with the proper expertise. The plans are simple, and you are in and out of the estate easily, free to meet up with the Inox and claim your payment.\n\nGain 10 gold each.\n\nOTHERWISE: It turns out confidence isn't enough when it comes to sneaking in and out of a well-guarded estate without being seen. You didn't get the figurine, and one of the guards got a pretty good look at you.\n\nLose 3 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-28-b-a.png',
    },
    "optionB": {
      "choice": "Incredulously explain she must have the wrong people and you won't take the job.",
      "outcome":
        "You grab the Inox's arm as she is getting up to leave and push the paper back toward her. She looks incredibly angry as you explain that your group doesn't do this sort of thing. She wordlessly grabs the plans and storms out of the bar.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/city/ce-28-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-28-f.png',
    "verified": False,
  },
  {
    "id": 53,
    "number": 29,
    "text":
      'You get word from a contact that there is trouble brewing down at the East Walls and decide to investigate.\n\nWhat you find is a large contingency of the city\'s Savvas workforce — the best builders you\'ll find anywhere — in open rebellion against the construction managers, demanding better pay for the specialized work they perform. "This city would be a lifeless pile of rocks without us!" one of the Savvas yells. "It\'s time we see some of its prosperity!"\n\nThe manager on the other side of the argument looks like a captured mouse, not sure at all how to get out of the situation.',
    "optionA": {
      "choice": 'Talk to the Savvas, appealing to their sense of duty and community.',
      "outcome":
        "{Cragheart} {Triangles}: The workers' hard expressions soften a bit when they see a Savvas among you. You talk for a while and explain that they need the city just as much as the city needs them. In the end, you sell them on a smaller wage increase, and everyone returns to work.\n\nGain 1 prosperity.\n\nOTHERWISE: Even after much effort, the workers won't speak to you at all, calling you part of the problem. The strike is eventually resolved, but no one seems happy.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/city/ce-29-b-a.png',
    },
    "optionB": {
      "choice": 'Talk to the managers and attempt to get the Savvas better pay.',
      "outcome":
        '{Scoundrel} {Saw} {MusicNote}: "I-I just can\'t give them more money!" the manager pleads. After some persuasion, though, he seems to open up to negotiation, The workers and management meet halfway and everyone seems content.\n\nGain 1 prosperity.\n\nOTHERWISE: You just can\'t get the manager to budge on his position, and he only gets angrier with continued pushing. The Savvas eventually agree tentatively to continue work, but the underlying problem remains.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-29-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-29-f.png',
    "verified": False,
  },
  {
    "id": 60,
    "number": 30,
    "text":
      "As you shop for supplies at the Sinking Market, your hand instinctively goes for the purse at your waist.\n\nIt's gone!\n\nYou quickly scan the crowd and see a small Vermling darting away from you, heading directly toward a sewer grating.",
    "optionA": {
      "choice": 'Give chase! No one steals from you and gets away with it.',
      "outcome":
        '{Mindthief}: The Vermling escapes into the sewers, but the Mindthief is able to give chase, catching up as the cutpurse enters his nest. There you find more wealth than what was lost.\n\nGain 5 gold each.\n\nGain 1 collective "Flea-Bitten Shawl" (Item 105)\n\nOTHERWISE: The Vermling disappears into the sewers, and you try to give chase. But after a few minutes you are hopelessly lost and are forced to give up.\n\nLose 5 gold each.',
      "imageUrl": '/assets/cards/events/base/city/ce-30-b-a.png',
    },
    "optionB": {
      "choice": 'Take a clear shot at him with a bow before he disappears into the grating.',
      "outcome":
        'You raise your bow and take aim at the thief. A woman screams, but you try not to let it faze you. As the Vermling pauses to open the grate, you fire the arrow and see the furry figure drop. You smile and go to retrieve your gold from the corpse. You get a lot of dirty looks, though. Apparently firing a bow on a crowded street is frowned upon.\n\nLose 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-30-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-30-f.png',
    "verified": False,
  },
  {
    "id": 59,
    "number": 31,
    "text":
      'You find yourself incredibly drunk and gambling away your hard-earned gold at the Brown Door when a robed woman approaches you.\n\n"Please," she says. "You must help me. They\'ve taken my only daughter. I beg you!"\n\nShe slides a parchment toward you. "They left this behind..."\n\nYou look down to see nothing, but the symbol of an upside-down black bird.\n\n"The Ravens!" a man mutters. "Bad business."\n\nA bouncer approaches. "Take that garbage outside. You\'re troubling the customers."',
    "optionA": {
      "choice": 'Leave with the woman to help her find her missing daughter.',
      "outcome":
        'Once outside, the woman hands you a large pouch of gold. "My father saw the whole thing, but then he went mad and ran toward the Silent Bridge. Please find him and he\'ll help you find my daughter!"\n\nGain 20 collective gold.\n\nUnlock "Shadows Within" 83 (C-15).\n\nParty Achievement: "Bad Business."',
      "imageUrl": '/assets/cards/events/base/city/ce-31-b-a.png',
    },
    "optionB": {
      "choice": 'Refuse to help the woman and go back to gambling.',
      "outcome":
        '{Sun}: You try to turn away the woman and get back to gambling, but the Sunkeeper won t hear of it. She forces you to follow the woman outside.\n\nRead outcome A.\n\nOTHERWISE: You return to your gambling, but you feel as though a pall has fallen over the revelry. Your luck has turned and you end the night much poorer than when you started.\n\nLose 10 gold each.',
      "imageUrl": '/assets/cards/events/base/city/ce-31-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-31-f.png',
    "verified": False,
  },
  {
    "id": 70,
    "number": 32,
    "text":
      'As you return to town after your latest adventure, a high-ranking guard approaches and gestures you to the side of the road.\n\n"I am embarrassed to admit this," he begins in a low voice,  but we could really use some help. With all the attacks recently and very little support from the capital the city guard finds itself woefully lacking in both equipment and training for the new recruits."\n\nThe guard looks you over. You are experienced warriors, and anything you could do to help the situation would be greatly appreciated."',
    "optionA": {
      "choice": 'Agree to help the city guard.',
      "outcome":
        "{ThreeSpears}: You not only help to train the new recruits, but the Quartermaster is able to repair a lot of the guards' damaged armor and weaponry. At the end of the day, the city is very pleased with your contribution.\n\nGain 15 collective gold.\n\nGain 1 reputation.\n\nOTHERWISE: You spend the day training the new recruits. By the time the sun goes down, their skills are much improved, and they are grateful to you because of it.\n\nGain 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-32-b-a.png',
    },
    "optionB": {
      "choice": 'Decline to help and instead sell this information to interested parties.',
      "outcome":
        'Whenever there is bad news, there is always someone who delights in it and profits from it. Who would be happy to hear the city guards are having trouble? Thieves. And they pay surprisingly well for the information.\n\nGain 15 collective gold.',
      "imageUrl": '/assets/cards/events/base/city/ce-32-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-32-f.png',
    "verified": False,
  },
  {
    "id": 62,
    "number": 33,
    "text":
      'The Void is a troubling area in Gloomhaven — a vast, barren expanse of black sand amid the bustling streets of the city. No one enters its perimeter.\n\nOn a trip to the University, however, you see a young girl playing near the edge of the Void. Before you can warn her, she trips and falls onto the sand.\n\nShe immediately emits a blood-curdling scream and begins to tear at her skin.',
    "optionA": {
      "choice": 'Run to the girl and attempt to pull her out of the Void.',
      "outcome":
        "{Circles} {Eclipse}: You grab the child and lift her clear of the haunting area. She is still screaming madly when the Aesther in your group lays a hand upon the child in deep concentration. Slowly, the crying subsides, and the child gets up and runs off.\n\nGain 2 reputation.\n\nOTHERWISE: You get the child off the sand as quickly as you can, but it doesn't do much good. The girl screams and screams no matter what aid is administered.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/city/ce-33-b-a.png',
    },
    "optionB": {
      "choice": 'Watch what happens with morbid curiosity.',
      "outcome":
        'Unable to resist, you watch to see what will happen to the girl. Her skin turns ashen and begins to flake away. She stops screaming eventually and begins coughing up a black bile. She tries to stand, but her legs crumble away into dust. She makes a pitiful croak and then falls over into a cloud of sand. When the cloud settles, no evidence of her presence remains.',
      "imageUrl": '/assets/cards/events/base/city/ce-33-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-33-f.png',
    "verified": False,
  },
  {
    "id": 66,
    "number": 34,
    "text":
      "After a night of revelry at the Sleeping Lion, you head out into the streets and notice a suspicious man in black robes skulking toward an allevway\n\nYou've been hearing reports about a cult inside the city, calling themselves the Ravens and performing all sort of terrible acts.\n\nPerhaps this is one of them.",
    "optionA": {
      "choice": "Follow the man in an attempt to discover the Ravens' lair.",
      "outcome":
        '{Eclipse}: Using the night like a cloak, you follow the man unseen and unheard. Eventually he stops at a small dwelling nestled under the west wall of the city.\n\nUnlock "Sacrifice Pit" 78 (B-14).\n\nOTHERWISE: You sneak forward, confident in your stealth abilities. After a few minutes, though, the man suddenly bolts around a corner. By the time you get there, he is long gone.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-34-b-a.png',
    },
    "optionB": {
      "choice": 'Confront him on the spot and turn him over to the authorities',
      "outcome":
        "Not confident in your stealth abilities, you decide speed and force are a better way to go. You charge forward, catching the man completely by surprise. You block off all avenues of escape and surround him. He snarls as you tie him up and hand him over to the city guards. Hopefully they'll be able to get some useful information out of him.\n\nGain 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-34-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-34-f.png',
    "verified": False,
  },
  {
    "id": 67,
    "number": 35,
    "text":
      'Harrowers are a rare sight, both outside of Gloomhaven and within. Which explains why you are bit surprised when you find yourself standing before three Harrowers in ornate robes unlike any you\'ve ever seen.\n\n"We require spices from across the sea," one chitters at you. \'Can you direct us to the appropriate merchant?"\n\nA bit caught offguard, you ask about the specihc kind of spice, but the Harrower makes only unintelligible hisses.\n\n"It is hard to describe. We will know it when we see it. It is very important to our hive."',
    "optionA": {
      "choice": 'Point the way to the Sinking Market — the only place that would deal with them.',
      "outcome":
        'You quickly point in the direction of the Sinking Market, assuring the Harrowers they will find exactly what they need there. They chitter and hand you a gold piece, then move on their way.\n\nGain 1 collective gold.',
      "imageUrl": '/assets/cards/events/base/city/ce-35-b-a.png',
    },
    "optionB": {
      "choice": 'Escort the Harrowers to the New Market and help them find a spice merchant.',
      "outcome":
        "{Cthulu}: You make your way to the market with the Harrowers in tow. It's easy to find a reputable spice merchant, but difficult to get the merchant and the Harrowers to trust each other. In the end, they find common ground through the Plagueherald and make a deal.\n\nGain 1 prosperity.\n\nOTHERWISE: You bring the Harrowers to the market, but even after great effort, you cannot find any merchants willing to deal with them, they depart empty handed.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/city/ce-35-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-35-f.png',
    "verified": False,
  },
  {
    "id": 77,
    "number": 36,
    "text":
      'You decide to unwind at the Sleeping Lion, but just as you are starting to relax, a bear of a man crashes into your table, scattering your drinks across the floor.\n\nTowering over him is a massive Inox. "What did you say about my horns?" the Inox shouts.\n\nThe man stands up and brushes shards of glass from his tunic. "I said the sight of them makes me want to vomit!"\n\nthe Inox roars and charges headlong into the man, crashing through more tables in the process. At this, the entire tavern erupts into violence. After all when a man is deep into his drink, the last thing you want to do is knock that drink over.',
    "optionA": {
      "choice": 'Join the fray! These insults will not go unanswered!',
      "outcome":
        "{LightningBolts}: You break a chair over the man's back, kick him in the teeth, and then you really get into it. It's a bar brawl that could only be described as \"epic\" fueled by pure, raw rage. The carnage is extreme.\n\nGain 5 experience each.\n\nLose 2 reputation.\n\nOTHERWISE: You jump into the melee, breaking heads and chairs in equal measure. You've seen worse brawls, but the proprietor still isn't very happy when it's over.\n\nLose 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-36-b-a.png',
    },
    "optionB": {
      "choice": 'Do your best to stop the fighting. This is a respectable establishment.',
      "outcome":
        "{LightningBolts}: You get up to calm down the room, but the Berserker has other ideas, laying into the man before you can get a word out. She goes into a furious rage, and there's really not much to be done about it except pay what you can for the damages afterward.\n\nLose 10 collective gold.\n\nOTHERWISE: It takes some work, but you manage to calm down the Inox and buy off the rest of the room with some extra drinks. The proprietor looks positively relieved.\n\nGain 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-36-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-36-f.png',
    "verified": False,
  },
  {
    "id": 71,
    "number": 37,
    "text":
      'As you return to town after your latest adventure, you see smoke rising from the walls of the city. You enter the broken gates and see a scene of despair as the citizens of Gloomhaven recover from a catastrophic attack.\n\n"Demons," a wounded guard at the gate says. "Wish you lot could have been around to help fight them off. Now look at the place. Luckily the rest of the city remained safe."',
    "optionA": {
      "choice": 'Attempt to console and cheer up those affected by the attack.',
      "outcome":
        "{MusicNote}: The citizens are downtrodden, but the uncanny power of the Soothsinger's music seems to lift their spirits considerably. Still far from cheerful, the people find new resolve in repairing the damage and rebuilding.\n\nGain 1 prosperity.\n\nOTHERWISE: The citizens view you with a cynical eye as you walk around, attempting to encourage them and lift their spirits. Despite the effort, it seems as though they are in a worse mood than when you arrived.\n\nLose 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-37-b-a.png',
    },
    "optionB": {
      "choice": "Help repair the gate. You wouldn't want another attack to further cripple the town.",
      "outcome":
        '{ThreeSpears} {Spellweaver} {Tinkerer} {Triangles} {Circles}: You set to work repairing the gate, and by the time night falls, it is at least functional. The downtrodden citizens are inspired by your work, and you have little doubt that the community will bounce bock with little permanent damage.\n\nGain 1 prosperity.\n\nOTHERWISE: You fiddle with the gate for a bit until it becomes clear that you are doing nothing to help. You decide to head back to your rooms instead and get some rest.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-37-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-37-f.png',
    "verified": False,
  },
  {
    "id": 74,
    "number": 38,
    "text":
      'Walking through the crowded streets of the Ward of Scales, you suddenly hear a commotion behind you. You turn to see a gruff shirtless man badgering a male Orchid.\n\n"I assure you, I did nothing of the sort." the Orchid says calmly.\n\n"You calling me a liar now?" bellows the man. "I think somebody needs to teach you a lesson." The man careens forward with his fist and knocks the Orchid to the ground.\n\nA gasp emerges from the crowd, but very quickly the attitude turns to excitement and encouragement. Nothing like a good fight to get a crowd worked up.',
    "optionA": {
      "choice": "Intervene on the Orchid's behalf.",
      "outcome":
        "{Spellweaver} {PointyHead}: The Orchid on the ground puts up no defense, but your group is a different matter. The man quickly backs down at the sight of a powerful Orchid ready to attack, and the crowd disperses, muttering disappointment.\n\nGain 1 prosperity.\n\nLose 1 reputation.\n\nOTHERWISE: You try to talk some sense into the man, and when that doesn't work, you beat him senseless. The crowd seems happy and the Orchid thanks you for your aid.\n\nGain 1 prosperity.",
      "imageUrl": '/assets/cards/events/base/city/ce-38-b-a.png',
    },
    "optionB": {
      "choice": 'Watch the fight with the crowd.',
      "outcome":
        '{Spellweaver} {PointyHead}: After a good beating, the crowd is riled up. Many people start looking in your direction, muttering about how you have the nerve to associate with Orchids as well. You make a quick exit.\n\nLose 1 reputation.\n\nOTHERWISE: The Orchid puts up no defense and the "fight "becomes rather one-sided. A solid beating is administered, and the crowd is sated. You go about your business while the Orchid bleeds on the ground.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-38-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-38-f.png',
    "verified": False,
  },
  {
    "id": 76,
    "number": 39,
    "text":
      'You are awakened in your room by a decisive knock at the door. You answer it to find a man in the robes of the Great Oak.\n\n"Greetings," the man begins. "Our sanctuary is having a bit of trouble, and I\'ve been directed to you as persons who could possibly help.\n\n"You see, some of our relics have gone missing, and we suspect the worst. We are hoping you might grace us with your assistance in investigating this matter."',
    "optionA": {
      "choice": 'Agree to help the priest and accompany him to the sanctuary.',
      "outcome":
        "The pious man seems incredibly happy you've decided to help the sanctuary. When you arrive at the great building, he explains in detail all that has happened. Using that information, you inquire around town, putting out feelers to possible fences for the goods.\n\n{Scoundrel} {Mindthief} {Eclipse} {Saw} {MusicNote}: Add City Event 65 to the deck.\n\nOtherwise:\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/city/ce-39-b-a.png',
    },
    "optionB": {
      "choice": 'Refuse to help, making some excuse about being too busy.',
      "outcome":
        "You mutter something about hunting drakes and close the door on the priest. He becomes rather distraught as the door slams shut in his face, but surely he'll get over it. You've got much more important things to do anyway.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/city/ce-39-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-39-f.png',
    "verified": False,
  },
  {
    "id": 79,
    "number": 40,
    "text":
      "You are shopping for supplies in the Boiler's District when an intense explosion knocks you off your feet. You look in the direction of the heat waves to see plumes of fire and smoke rising from a building less than a block a way.\n\nThe fire rages uncontrollably and there are many wounded residents laying near the blast, screaming in pain.\n\nYou also spot something else — a hooded figure in a dark robe fleeing from the scene.",
    "optionA": {
      "choice": 'Rush to the aid of the residents and help put out the fire.',
      "outcome":
        "{Tinkerer} {Saw} {Sun}: Some of your group immediately begin to tend to the wounded, bandaging cuts and administering potions.\n\nGain 2 reputation.\n\n{Spellweaver} {Triangles} {Circles}: Some of your group begin to controfthe fire and snuff it with their elemental prowess, preventing further damage.\n\nGain 1 prosperity.\n\nOTHERWISE: You do your best, but without the proper skills, it isn't much.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/city/ce-40-b-a.png',
    },
    "optionB": {
      "choice": 'Pursue the hooded figure and make him answer for this attack.',
      "outcome":
        'You jump to your feet and sprint as fast as you can in pursuit. The figure races toward the city wall and begins to climb the stairs. You close the gap, but look on in frustration as he moves to jump over the wall and out of the city. You lunge and grab his robe as be falls. His body twists awkwardly, freeing him of the robe. You look over the edge to see him land face-first on the ground and not get up.\n\nGain 1 collective "Sacrificial Robes" (Item 102).\n\nGain 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-40-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-40-f.png',
    "verified": False,
  },
  {
    "id": 81,
    "number": 41,
    "text":
      'The Sinking Market is a varied area or decrepit huts and merchants unable to sell their wares anywhere else. It doesn\'t surprise you as you walk through to see a scraggly Vermling approach with a small sack.\n\n"A potion for the big, strong adventurers!" she says as she waves you down. "Help you in battle, it will!"\n\nYou are about to push her aside and keep walking when she pulls the potion out of the sack. It glows green in the daylight — an impressive, large flask of master craftsmanship.\n\n"Aha, I knew it catch your eye! How much you pay?"',
    "optionA": {
      "choice": 'Barter with the Vermling for the potion.',
      "outcome":
        '{TwoMinis}, PAY 10 COLLECTIVE GOLD: The Vermling knows it is valuable, but she is more interested in flirting with the Beast Tyrant. She is happy to sell the potion at a discount.\n\nGain 1 collective "Major Stamina Potion" (Item 034)\n\nPAY 25 COLLECTIVE GOLD: No amount of haggling can lower the Vermling\'s high price.\n\nGain 1 collective "Major Stamina Potion" (Item 034).\n\nOTHERWISE: The Vermling will not accept the tiny sum you offer. Maybe next time.',
      "imageUrl": '/assets/cards/events/base/city/ce-41-b-a.png',
    },
    "optionB": {
      "choice": "Move along. You don't need any more potions.",
      "outcome":
        'Shaking your head, you move past the Vermling and get back to your business. She begins to make sobbing sounds behind you. "But, but you die without potion! Is life worth nothing?"\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-41-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-41-f.png',
    "verified": False,
  },
  {
    "id": 83,
    "number": 42,
    "text":
      'Walking near the West Gate, you are approached by a scrawny kid in a guard uniform, which is clearly too big for his small frame.\n\n"Hey, you all are famous!" he says with a big smile. "I worked as a caravan guard before I got this job. Met with a big Inox guy who always talked about you. He made you seem like the nicest, most amazing people."\n\nHis smile and excitement doesn\'t waver. "Say, my detail is doing some work to repair the wall damage from the last Vermling attack. Would you mind helping us! It\'ll be fun!"',
    "optionA": {
      "choice": 'Agree to help the presumptuous kid.',
      "outcome":
        "It's hard work, but the kid's enthusiasm is infectious. He wants to know all about your exploits and adventures, and he and his detail prove to be a great audience. By the end of the day, it hardly feels like you've worked at all.\n\nGain 1 prosperity.\n\nGain 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-42-b-a.png',
    },
    "optionB": {
      "choice": 'Tell this kid that he must have the wrong group of adventurers.',
      "outcome":
        'You shake your head and avert your gaze. You claim that the kid must have you confused with a different adventuring party. He looks crushed as you walk a way.\n\nLose 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-42-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-42-f.png',
    "verified": False,
  },
  {
    "id": 85,
    "number": 43,
    "text":
      "You return to your rooms for the evening to find a small note resting on the ground in front of your door.\n\nIt is from the Tinkerer, explaining that he has been pursuing further studies in flammable liquid delivery methods. He asks for your help in delivering to him a small robotic contraption that he absentmindedlv left behind in a secret stash under the floorboards of his old room.\n\nHe details the device's location and gives an address to deliver it to some small village far to the northwest.",
    "optionA": {
      "choice": 'Oblige the Tinkerer and send along the contraption.',
      "outcome":
        "PAY 5 COLLECTIVE GOLD: Sure enough, under the floorboards of his old room, you find a bunch of parts, tools, and an intricately crafted metal spider. You package it up and ship it off to the Tinkerer. Anything for an ola friend.\n\nAdd City Event 61 to the deck.\n\nOTHERWISE: You don't have the money to send him the contraption, so you decide just to keep it for yourself.\n\nRead outcome B.",
      "imageUrl": '/assets/cards/events/base/city/ce-43-b-a.png',
    },
    "optionB": {
      "choice": "You don't want to pay for postage. Just keep the thing for yourself.",
      "outcome":
        'Like an eager treasure hunter, you pry up the floorboards in the Tinkcrers old room and find a trove of useless junk, plus a detailed robotic spider that is anything, but useless. You switch it on and let it scurry around the room. This could be a significant help in battle. No way its getting shipped off.\n\nGain 1 collective "Remote Spider" (Item 126).',
      "imageUrl": '/assets/cards/events/base/city/ce-43-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-43-f.png',
    "verified": False,
  },
  {
    "id": 86,
    "number": 44,
    "text":
      'In the very early morning, you are wakened by a knock at your door. Standing behind it is giant, dirty Inox wearing a leather apron.\n\n"Oh, uh...ahem,\'" he coughs. "Sorry, I was looking for a female Orchid. She used to help me on occasion with my forge. Her control over fire was astounding and I paid her well for her assistance completing some of my specialty work."\n\nHe scratches his head. "I guess she\'s not around anymore. You wouldn\'t happen to know where I could find someone who could help me in her absence, would you?"',
    "optionA": {
      "choice": 'Offer to help the blacksmith yourself.',
      "outcome":
        "{Spellweaver} {Triangles} {Circles}: Despite the early hour, you head down to the Inox's forge and get an incredibly strong fire going for him so he can complete his order. He seems very pleased.\n\nGain 1 reputation.\n\nGain 10 collective gold.\n\nOTHERWISE: The Inox is completely dumbfounded when you walk all the way down to his forge and then proceed to exhibit zero aptitude at manipulating or controlling fire.\n\nLose 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-44-b-a.png',
    },
    "optionB": {
      "choice": 'Direct him to the Savvas Elemental Guild and go back to sleep.',
      "outcome":
        '"Ah, yes, that is probably a good idea," he says. "Thanks for your time and I hope your friend the Spellweaver is doing well!"\n\nGain 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-44-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-44-f.png',
    "verified": False,
  },
  {
    "id": 87,
    "number": 45,
    "text":
      '"You there! Stop!"\n\nYou turn to see a city guard walking briskly toward you.\n\n"You are known associates of this woman, yes?" He holds up a crude sketch of the Scoundrel. "We believe she is behind a number of high profile robberies and demand that you give us any information you have on her whereabouts and activities."\n\nHis face softens a bit. Look, I know you guys do a lot of good for the city, but the merchant guild is breathing down my neck on this one, and I could really use a lead."',
    "optionA": {
      "choice": 'Cooperate with the guard and tell him everything you know.',
      "outcome":
        'The guard taps his notes with a smile on his face/\n\n"This is great," he says. "I understand that you haven\'t seen her in a while, but the information you\'ve provided should still be useful. Have a nice day!"\n\nGain 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-45-b-a.png',
    },
    "optionB": {
      "choice": 'Be as vague and unhelpful as possible, giving no useful information.',
      "outcome":
        'The guard scratches his head and looks down at his notes.\n\n"Well, that wasn\'t very helpful." he sighs. But thanks lor your time, I guess. Let me know if you remember anything or get any new information."\n\nAdd City Event 62 to the deck.',
      "imageUrl": '/assets/cards/events/base/city/ce-45-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-45-f.png',
    "verified": False,
  },
  {
    "id": 90,
    "number": 46,
    "text":
      'Anticipating an enjoyable night of drinks at the Sleeping Lion, you enter the tavern to see a familiar Savvas sitting at your usual table. The Cragheart stands and extends both its arms.\n\n"Ah, friends! So good to see you," it says. "Sit! Have a drink with me!"',
    "optionA": {
      "choice": 'Have a drink with the Cragheart.',
      "outcome":
        "One drink turns into five, and five turns into even more. It is a great night of revelry at the Sleeping Lion. You see sadness in the Cragheart's eyes when you finally stand up to leave. It tells you it's been hard to find people to relate to since leaving the party and it thanks you for your continued friendship.\n\nGain 1 reputation.\n\nLose 5 gold each.",
      "imageUrl": '/assets/cards/events/base/city/ce-46-b-a.png',
    },
    "optionB": {
      "choice": 'Encourage the Cragheart to move on with its life.',
      "outcome":
        'Not fitting in with its own kind or with a city of mostly humans, the Cragheart thought it could depend on a misfit group of mercenaries for friendship. It understands that its adventuring life is now in the past, though, and that it should go find a new place to belong. It sadly admits that it has no idea where that would be, but the Cragheart gets up and leaves the tavern nonetheless.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-46-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-46-f.png',
    "verified": False,
  },
  {
    "id": 92,
    "number": 47,
    "text":
      'Walking near Gloomhaven Square, you see a peculiar scene. A group of guards is dragging along a Vermling in tattered robes toward the Ghost Fortress. Getting a little closer, you recognise the Mindthief.\n\n"Hssss," she spits. "Why do you do this? I came to you! I tell you that this town is being poisoned, and you respond by imprisoning me?"\n\n"Well see what the Captain of the Guard has to say about this," one of her captors says. "Keep moving!"',
    "optionA": {
      "choice": 'Intervene with the guards and find out what is going on.',
      "outcome":
        'The guards look incredibly perturbed when you step in front of them and ask that they leave the Mindthief to you. After some effort, they begrudgingly hand her over. The Mindthief thanks you, explaining that her colony in the sewers is being poisoned, and the poison is quickly migrating to the city\'s water supply. She says she\'s tracked the source to a small cove along the Hook Coast.\n\nLose 1 reputation.\n\nUnlock "Corrupted Cove" 87 (I-9).\n\nParty Achievement: "The Poison\'s Source."',
      "imageUrl": '/assets/cards/events/base/city/ce-47-b-a.png',
    },
    "optionB": {
      "choice": 'Let the guards continue their business and just continue with yours.',
      "outcome":
        "The Mindthief flicks her tail and throws insults around, but it doesn't seem to have any positive effect. She is led away and out of view. You get about your business, hoping that bit about the town being poisoned wasn't too serious.\n\nAdd City Event 63 to the deck.",
      "imageUrl": '/assets/cards/events/base/city/ce-47-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-47-f.png',
    "verified": False,
  },
  {
    "id": 95,
    "number": 48,
    "text":
      'You are haggling over the price of road rations with an irritating Valrath merchant when a messenger boy approaches you holding a note.\n\n"Sir, I have a pressing letter from an important Valrath Sunkeeper," the messenger says. "I was told to deliver it to you."\n\nYou reach for it, but the messenger moves back a little. "Sir, this note has traveled a long distance to get to you. If you could, please pay a small fee to take possession of it."',
    "optionA": {
      "choice": 'Begrudgingly pay for the note.',
      "outcome":
        'PAY 5 COLLECTIVE GOLD: You throw the kid a few coins and grab the note. Enclosed with the note is a small medallion engraved with the image of the sun. Apparently the Sunkeeper thinks the object may help you at some point in the future. The note doesn\'t say exactly how and the thing has no apparent use. You stow it away in your pack.\n\nParty Achievement: "Sun-Blessed.".\n\nOTHERWISE: You reach into your pocket to pay the kid, but come up empty-handed. He slinks off in indignation.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-48-b-a.png',
    },
    "optionB": {
      "choice": 'Refuse to pay for the note.',
      "outcome":
        'You laugh in indignation and push the messenger away. He opens his mouth to object, then thinks better of it and runs off. You turn back to bartering, now leveraging the proof of your extreme thriftiness against the merchant.\n\nGain 3 collective gold.',
      "imageUrl": '/assets/cards/events/base/city/ce-48-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-48-f.png',
    "verified": False,
  },
  {
    "id": 97,
    "number": 49,
    "text":
      '"Your Quartermaster friend sent me." You look quizzically at the Valrath standing at your door.\n\n"I\'m from the Capital and I deal in arms and armor," he says. "I\'m looking to set up a contract with the Gloomhaven military and our friend says that you may have some contacts with them. He suggested I meet up with you once I got here"\n\nThe Valrath shifts his feet nervously. "So, can you help me?"',
    "optionA": {
      "choice": 'Agree to help him make contact with the military.',
      "outcome":
        'You take the Valrath over to the Ghost Fortress, where you make introductions to the Captain of the Guard. The Captain seems skeptical at first, but admits that they could use an additional supply of weapons. Terms are made, and a contract is signed.\n\nGain 1 prosperity.',
      "imageUrl": '/assets/cards/events/base/city/ce-49-b-a.png',
    },
    "optionB": {
      "choice": "Demand a finder's fee for setting him up with buyers.",
      "outcome":
        '{Scoundrel} {Saw} {MusicNote}: The Valrath looks at you with trepidation, but after some persuasion you get him to agree.\n\nGain 15 collective gold.\n\nRead outcome A.\n\nOTHERWISE: The Valrath recoils, insulted by the notion. He storms off, grumbling about the lost value of friendship.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-49-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-49-f.png',
    "verified": False,
  },
  {
    "id": 99,
    "number": 50,
    "text":
      '"A monstrous creature approaches the walls!" A guard with a truly terrified look runs toward you, waving his arms with manic energy. "Please! You must help!" Before you can even agree, he grabs you by the wrist and pulls you toward the East Gate.\n\nYou hear the beast before you see it, bellowing with rage and pounding at the gates. Each time it hits, the entire city shakes. You climb the ramparts and look down at the massive creature with six legs as thick as trees, two spiraling horns, and a spiked tail.\n\nThis is truly a demon from the abyss," the guard laments. It must be from another plane, so he\'s not too far off.',
    "optionA": {
      "choice": 'Attack the beast from the wall, shooting arrows at it until it stops moving.',
      "outcome":
        "You grab a bow and start sending arrows down into the things thick hide. Each individual arrow doesn't do much, but over time the creature slows. By the time it manages to break through the gates it has been considerably hobbled as black blood pours from its countless wounds. It charges forward, laying waste to a small shop, but as more arrows continue to rain down upon it, it soon stops and falls over lifeless.\n\nGain 5 experience each.\n\nGain 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-50-b-a.png',
    },
    "optionB": {
      "choice": 'Work on reinforcing the walls. Hold it off for as long as possible.',
      "outcome":
        'You set to work reinforcing the gate with anything you can find — planks of wood, carts full of stones, your own bodies. Due to your tremendous effort, the guards on the walls manage to bring down the beast before it breaks through. The various merchants of the Boilers District thank you for your valiant service.\n\nGain 10 gold each.',
      "imageUrl": '/assets/cards/events/base/city/ce-50-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-50-f.png',
    "verified": False,
  },
  {
    "id": 101,
    "number": 51,
    "text":
      'You are wandering through the city streets late at night when you hear a terrifying scream high above you. You look up just in time to see a body falling toward you and jump out of the way.\n\nIt lands with a wet thud on the ground. You were not the only ones to hear the scream, and quickly a small crowd forms around the corpse, including a couple of city guards.\n\nThe body is clad in black leather armor, and a long, thin blade conspicuously protrudes from its back. You remark that the sword somehow looks familiar.\n\n"What?" asks a guard. "This is the third murder like this in a week. Tell me everything you know!"',
    "optionA": {
      "choice": 'Tell the guard that the sword belongs to the Nightshroud, your former party member.',
      "outcome":
        'You explain that you recognize the sword from the time you spent traveling with the Nightshroud. As a capable assassin, he is likely to be the one behind the murders. You explain, however, that since he left the group, you have no knowledge of his whereabouts or dealings. The guard thanks you for the information.\n\nGain 1 reputation.\n\nAdd City Event 64 to the deck.',
      "imageUrl": '/assets/cards/events/base/city/ce-51-b-a.png',
    },
    "optionB": {
      "choice": 'Lie and claim you know nothing.',
      "outcome":
        '{Scoundrel} {Saw} {MusicNote}: You shake your head at the guard, saying you must have been mistaken. You thought the sword looked similar to one carried by a friend, but, looking closer, there are distinct differences. The guard shrugs and goes back to examining the scene.\n\nNo effect.\n\nOTHERWISE: You laugh and make up some poor explanation about seeing a similar sword on a bandit in a crypt. The guard eyes you suspiciously.\n\nLose 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-51-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-51-f.png',
    "verified": False,
  },
  {
    "id": 103,
    "number": 52,
    "text":
      "You have been hearing rumors in the bars: a pox is spreading through Gloomhaven, affecting lower class citizens — street urchins and back-alley thugs.\n\nAnd then one night you see it: a Harrower dressed in a ragged green cloak holding a man down in an alley as its swarm spreads out and consumes him. The man's screams are muffled as the insects skitter down his throats.\n\nKilling monsters and demons is one thing, but the Plagueherald shouldn't be preying on people in the city. You approach it, intent on stopping its attack.",
    "optionA": {
      "choice": 'Calmly explain the situation to the Plagueherald, imploring it to move on.',
      "outcome":
        'With the man dead at its feet, the Plagueherald makes a chittering sound that sounds almost like laughing.\n\n"You cannot see it, but this city needs to be cleansed. You will see, and you will thank me."\n\nAt this, the Plagueherald bursts out into a massive swarm of insects and flies up into the sky.\n\nThe deaths continue, and new rumors start about how you are associated with the killer.\n\nLose 2 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-52-b-a.png',
    },
    "optionB": {
      "choice": "Threaten the Plagueherald with retribution if it doesn't stop attacking residents.",
      "outcome":
        'The Plagueherald recoils at your threat, genuinely concerned that you would attack it.\n\n"But, the cleansing...the city isn\'t ready."\n\nYou shake your head, and the Harrower chitters in disappointment.\n\n"Very well, but you will be responsible when the Harbinger comes." It turns and floats off into the darkness.\n\nGain 1 prosperity.',
      "imageUrl": '/assets/cards/events/base/city/ce-52-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-52-f.png',
    "verified": False,
  },
  {
    "id": 106,
    "number": 53,
    "text":
      "Walking near the northern gates, you see some commotion as a group of wounded guards is ushered into town.\n\nThey look pretty bad off, suffering from many severe wounds. Some even have lost limbs.\n\nBringing up the rear, one guard is carried in by a couple of others. He's missing a leg and has a vicious looking axe embedded in his side. You realize that the axe looks kind of familiar.",
    "optionA": {
      "choice": "Let the guards know you recognize the Berserker's axe.",
      "outcome":
        'You approach the wounded detail, explaining how that axe belonged to a former member of your party.\n\n"Yeah, we know," one of them says with an icy stare. "Said we were desecrating her land or some such nonsense and just went crazy. But we weren\'t doing anything, but patrolling! Quite a piece of work your friend, just take the axe if you want and get out of here."\n\nLose 1 reputation.\n\nGain 1 collective Bloody Axe (Item 117).',
      "imageUrl": '/assets/cards/events/base/city/ce-53-b-a.png',
    },
    "optionB": {
      "choice": 'Stay silent and keep out of it.',
      "outcome":
        "You casually move on, wondering how the guards found themselves on the wrong side of the Berserkers rage. It probably wasn't very difficult.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/city/ce-53-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-53-f.png',
    "verified": False,
  },
  {
    "id": 108,
    "number": 54,
    "text":
      "Posters spring up in town announcing the performance of a master Quatryl musician and her merry band of performers. Looking closely at the image, you're pretty sure you recognize that foppish feathered hat.\n\nThe poster says the next show is tonight. You decide to attend for one purpose or another.",
    "optionA": {
      "choice": 'Go to the show and cheer on the Soothsinger.',
      "outcome":
        "You go and enjoy the Soothsinger's concert. There is even a song or two party and its adventures arount Gloomhaven.\n\nGain 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-54-b-a.png',
    },
    "optionB": {
      "choice": 'Seems like a good opportunity to pick some pockets while people are distracted.',
      "outcome":
        "{Scoundrel} {Mindthief} {Eclipse}: The rubes are much too distracted to mind their coin purses. You make off with a good amount of cash and get to listen to some nice music as well.\n\nGain 20 collective gold.\n\nOTHERWISE: You put forth a valiant effort, but, due to a lack of skill, you don't make much headway parting people from their money. At least the music is good.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/city/ce-54-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-54-f.png',
    "verified": False,
  },
  {
    "id": 110,
    "number": 55,
    "text":
      '"Ah, they said I might find you here." A portly Valrath woman looks down at you as you are enjoying a cold beverage at the Sleeping Lion.\n\n"A group of wild-looking Orchids came to the Temple of Coin today hoping to engage in trade with the merchants of the city. One particularly dour-looking one with a bow said you lot would vouch for them.\n\n"Were always wary of traps and betrayal out here on the edge of the wilderness, but if you think these Orchids can be trusted, then the Merchant\'s Guild may consider opening trade with them."',
    "optionA": {
      "choice": 'Vouch for the Orchids.',
      "outcome":
        '"Well, we\'ll take it under advisement. Personally, I don\'t even know why your opinion matters, but some people in the Merchant\'s Guild seem to like you.\n\n"Anyway, feel free to get back to your life of consumption and murder."\n\nGain 1 prosperity.',
      "imageUrl": '/assets/cards/events/base/city/ce-55-b-a.png',
    },
    "optionB": {
      "choice": 'Advise against trading with the Orchids.',
      "outcome":
        'The Valrath woman nods. "I agree. Orchids are not to be trusted. Personally, I thought you lacked the brains to make a proper decision, but I\'m happy to be proven wrong."\n\nGain 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-55-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-55-f.png',
    "verified": False,
  },
  {
    "id": 112,
    "number": 56,
    "text":
      'Looking for a little bit of variety, you head down to the Brown Door as night falls. After some wait, you pass through the doors and are surprised to see the Sawbones sitting near the back of the room by himself. Considering this bar is about as seedy and corrupt as they come, it is just about the last place you would expect to find him.\n\n"I just...I don\'t know what to do now," the Sawbones confesses after you sit down. "I\'d like to join the sanctuary and lead a nice, quiet life, but after adventuring with all of you, that just doesn\'t seem fulfilling anymore."\n\nHe shakes his head. "I don\'t know. This life seems so boring now. What do you think?"',
    "optionA": {
      "choice": 'Tell him that joining the sanctuary is the right thing to do.',
      "outcome":
        '"I guess you re right," he shrugs. "Here\'s to one last night of freedom." He lifts his gfass and gulps down the contents. You follow his lead and the rest is a blur.\n\nGain 1 prosperity.',
      "imageUrl": '/assets/cards/events/base/city/ce-56-b-a.png',
    },
    "optionB": {
      "choice": 'Tell him to follow his dreams.',
      "outcome":
        "\"You're right! I'm in command of my own life, and I'm going to do what I want with it. Maybe I'll go to the Capital and start my own business or something. Who knows?\"\n\nHe lifts his glass and looks at you. \"To endless possibilities! The next round's on me.\n\nAdd City Event 66 to the deck.",
      "imageUrl": '/assets/cards/events/base/city/ce-56-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-56-f.png',
    "verified": False,
  },
  {
    "id": 111,
    "number": 57,
    "text":
      'You are haggling over the price of road rations with an irritating Valrath merchant when a messenger boy approaches you holding a note.\n\n"Sir, I have a pressing letter written by a powerful Savvas that has come to you from all the way across the Misty Sea," the messenger says. "I was told to deliver it directly."\n\nYou reach for it, but the messenger moves back a little. "Sir, this note has traveled a very long distance to get to you. If you could, please pay a small fee to take possession of it."',
    "optionA": {
      "choice": 'Pay tor the note.',
      "outcome":
        'PAY 10 COLLECTIVE GOLD: You open the note to discover it is from the Elementalist, who has sailed to the eastern continent to gain a deeper understanding of the elements. During this time, the Elementalist also spent some effort on the construction of a powerful staff and wanted to share the design.\n\nGain "Staff of Elements" design (Item 118).\n\nOTHERWISE: You reach into your pocket to pay the kid, but come up empty-handed. He slinks off in indignation.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-57-b-a.png',
    },
    "optionB": {
      "choice": 'Refuse to pay for the note.',
      "outcome":
        'You laugh in indignation and push the messenger away. He opens his mouth to object, then thinks better of it and runs off. You turn back to bartering, now leveraging the proof of your extreme thriftiness against the merchant.\n\nGain 3 collective gold.',
      "imageUrl": '/assets/cards/events/base/city/ce-57-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-57-f.png',
    "verified": False,
  },
  {
    "id": 115,
    "number": 58,
    "text":
      '"There were fifty of them, I swear. Tearing my mates apart!"\n\nYou look over to the bar where a group of drunkards are all laughing at a disheveled man in the middle of a story.\n\n"And commanding them all riding atop a giant armored bear, there was a Vermling with a staff that shot lightning!"\n\nAt this the crowd erupts into more laughter, drowning out the rest of the man\'s story.\n\n"This man\'s had too much to drink, I\'d say," ridicules one of the crowd. "Vermlings riding bears! I thought I\'d heard of everything!"',
    "optionA": {
      "choice": 'Join the crowd in laughing at the man.',
      "outcome":
        'You move closer and join in on the fun. After a while, the man gives up and resigns himself to his glass. But his story provides entertainment for weeks.\n\nGain 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-58-b-a.png',
    },
    "optionB": {
      "choice": 'Calm down the crowd and get more details from the man about the attack.',
      "outcome":
        'It\'s not easy, but you quiet down the crowd and take the staggering man over to a secluded corner of the tavern to get the full story out of him. Apparently he was part of a group of ruffians working to harvest the Dagger Forest for wood. In the middle of their logging expedition, however, they were attacked by the Beast Tyrant and an army of forest animals. Though he ran off in the middle of the fight, the man swears he also heard the howl of angry spirits in the chaos.\n\nUnlock "Wild Melee" 91 (E-2).',
      "imageUrl": '/assets/cards/events/base/city/ce-58-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-58-f.png',
    "verified": False,
  },
  {
    "id": 124,
    "number": 59,
    "text":
      'You head to the Sinking Market, hoping to find some cheap supplies, when you are surprised to see a crowd gathering in the distance. You push your way through and see a host of dead bodies in the street, covered in insects and strange pustules in their skin.\n\nNearby, a woman screams in terror and runs away. Other more curious onlookers inch closer, trying to get a better view of the grotesque scene.',
    "optionA": {
      "choice": 'Help to dispose of the corpses as quickly as possible.',
      "outcome":
        "Finding it probable that these corpses harbor some sort of disease, you ward everyone away while you carefully load the bodies onto a cart, take them outside the city, and burn them.\n\nThe crowd is a little disappointed that you took away the morning entertainment. Especially annoyed are the guards, who don't appreciate you disposing of dead bodies before they can investigate them.\n\nLose 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-59-b-a.png',
    },
    "optionB": {
      "choice": 'Investigate the corpses.',
      "outcome":
        'Curiosity gets the better of you, as well and you approach the corpses with morbid fascination, hoping to find some clue about what happened. The number of insects is alarming, as is the diseased nature of the skin. If you had to guess, a Harrower could be responsible, or perhaps Xorn, who you so helpfully revived. Over the next few days, the disease spreads throughout the Sinking Market, killing many more people.\n\nLose 1 prosperity.',
      "imageUrl": '/assets/cards/events/base/city/ce-59-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-59-f.png',
    "verified": False,
  },
  {
    "id": 119,
    "number": 60,
    "text":
      'You are wandering the Ward of Scales in the evening when a crowd of people begins to form outside one of the shops, growing louder and more dense by the second.\n\nAs you approach, you see a terrified family of Quatryls through a familiar angry mob. The father pleads with a group of disheveled men with torches.\n\n"Cheats!" A woman next to you screams. "Burn the store down!"\n\nOne of the men — clearly not a guard — backhands the father away from the door and pushes his way inside the shop.',
    "optionA": {
      "choice": 'Attempt to stop the men from burning down the shop.',
      "outcome":
        "{Spellweaver} {PointyHead} {MusicNote}: You push your way to the front of the mob and stop the men as they enter the store. Clearly emotions have gotten the better of these people. Through a calm demeanor, you are able to talk the mob down. A sense of relief washes over the crowd.\n\nGain 1 reputation.\n\nOTHERWISE: You kindly entreat the crowd to back down. It gets a little rough, but it becomes clear the crowd isn't fully into it. After knocking a few heads, the mob disperses.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/city/ce-60-b-a.png',
    },
    "optionB": {
      "choice": 'Take part in the looting and burning of the store.',
      "outcome":
        "You watch as one of the men picks up a wooden crate and throws it through the shop window. In a frenzy, the crowd rushes into the store, breaking and looting with mad glee. It's easy enough to move in with the crowd and pick up a few valuable items in the chaos. After you get clear of the crowd, you look back to see billows of smoke rising up from the door and broken window. Not a good day to be a Quatryl.\n\nGain 5 gold each.\n\nLose 1 prosperity.",
      "imageUrl": '/assets/cards/events/base/city/ce-60-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-60-f.png',
    "verified": False,
  },
  {
    "id": 120,
    "number": 61,
    "text":
      "The day proves uneventful until you head back to your room in the evening to find a small package waiting at your doorstep. Resting on it is another note from the Tinkerer.\n\nHe thanks you profusely for sending along the mechanical spider, saying it was a great help in his work. He doesn't need it any longer, however and decided to send it back.\n\nHe explains that he made a few improvements to it as well while it was in his possession, and that it should help you significantly in your adventures.",
    "optionA": {
      "choice": 'Gratefully keep the spider.',
      "outcome":
        'You open the package to find a much larger, but equally intricate robotic spider staring back at you. This one appears to specialize in scurrying around its user, picking up and returning anything that might have been dropped. Should prove useful.\n\nGain 1 collective "Giant Remote Spider" (Item 127).',
      "imageUrl": '/assets/cards/events/base/city/ce-61-b-a.png',
    },
    "optionB": {
      "choice": "You can't decide who should keep it, so sell the spider and split the money.",
      "outcome":
        'You head down to the Mixed District with the newly improved spider and barter with some Quatryls who seem incredibly impressed with the craftsmanship. After some back-and-forth, you walk away with a nice sum of gold coins.\n\nGain 30 collective gold.',
      "imageUrl": '/assets/cards/events/base/city/ce-61-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-61-f.png',
    "verified": False,
  },
  {
    "id": 122,
    "number": 62,
    "text":
      '"So, I hear you stood up for me with the city guards the other day. Such annoying pests, aren\'t they?"\n\nYou turn around in the street to see the Scoundrel emerge from a dark alley with a smile on her face.\n\n"I just wanted to thank you in person," she says. "I\'ve known quite a few persons who would have ratted me out for their chance at a piece of gold. It\'s good to know some friendships last."\n\nShe looks over her shoulder. "Listen, I\'m leaving town for a good long while. You wanna grab a drink before I take off?"',
    "optionA": {
      "choice": 'Have a drink and reminisce about old times.',
      "outcome":
        'You laugh for a while and trade tales. As the sun drops below the tavern windows, the Scoundrel gets up to leave.\n\n"Listen, I really did enjoy our time together, and, well, I just wanted to leave you with something to remember me by."\n\nA piece of black cloth flutters down onto the table. When you look back up, the Scoundrel is gone.\n\nGain 1 collective "Thief\'s Hood" (Item 109).',
      "imageUrl": '/assets/cards/events/base/city/ce-62-b-a.png',
    },
    "optionB": {
      "choice": 'Overpower the Scoundrel and deliver her to the city guards.',
      "outcome":
        "A look of horrid surprise flashes in the Scoundrel's eyes as you leap forward and throw her to the ground. She doesn't even speak as you bind her arms and take her to the city guard. They thank you for your service, but their words aren't much counter to the cold angry stare of the Scoundrel as she's taken away.\n\nGain 3 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-62-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-62-f.png',
    "verified": False,
  },
  {
    "id": 125,
    "number": 63,
    "text":
      '"I assume you are aware of an increased amount of sickness in the city."\n\nYou were summoned to the Ghost Fortress and now stand before the Captain of the Guard.\n\n"We believe it could have something to do with a poisoning threat brought to our attention by your Mindthief friend a while ago. We ignored it, but now she is nowhere to be found, the Hook Coast is a bed of disease, and Gloomhaven proper is on its way there, too."\n\nHe looks at you firmly. "I need you to head down to the Hook Coast and figure out what is going on. Then eliminate the source of the poison."',
    "optionA": {
      "choice": 'Agree to help.',
      "outcome":
        'The Hook Coast is outside the walls of Gloomhaven and can be a dangerous place. And since this spread of poison, the city has become even more defenseless than normal. You hope you\'ll be able to find a solution to the problem quickly.\n\nUnlock "Harried Village" 86 (D-15).',
      "imageUrl": '/assets/cards/events/base/city/ce-63-b-a.png',
    },
    "optionB": {
      "choice": 'Tell the captain to fix his own problem.',
      "outcome":
        'The Captain of the Guard sighs.\n\n"I really thought you were the ones for the job. What business could you possibly have that is more important than making sure this city is safe?"\n\nHe holds up his hand. "No matter. Fine, just get out of here! We will deal with this ourselves."\n\nLose 1 prosperity.\n\nLose 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-63-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-63-f.png',
    "verified": False,
  },
  {
    "id": 127,
    "number": 64,
    "text":
      'Late in the evening, you are returning to your rooms when you hear a cry for help coming from a nearby alleyway. Racing into the shadows, you expect to find someone in distress, but instead find a group of men clad in black leather armor eying you maliciously.\n\n"We have a message for your Nightshroud friend," one of them says, drawing a wicked looking curved blade. Suddenly, the Nightshroud appears among them in a flash of fatal sword strikes. Before the men even have a chance to react, half of them lie dead on the ground. The other half quickly flee.\n\n"Well, it looks like you\'re into it now, too. Which is good, because I need help taking them down."',
    "optionA": {
      "choice": 'Stay and listen to what the Nightshroud has to say.',
      "outcome":
        'The Nightshroud kicks one of the corpses. "This is the Sin-Ra Syndicate, a group of assassins trying to gain a foothold in the region. I\'m trying to stop them, and somehow they found out you and I were friends. They decided to go after you as retribution. Lucky for you. I\'ve located their hideout, so were going to sneak in there and end this whole business once and for all."\n\nUnlock "Syndicate Hideout" 89 (C-17).\n\nParty Achievement: "Sin-Ra."',
      "imageUrl": '/assets/cards/events/base/city/ce-64-b-a.png',
    },
    "optionB": {
      "choice": 'Claim you want nothing to do with this and walk away.',
      "outcome":
        'The Sin-Ra Syndicate seems to think you have something to do with this," the Nightshroud yells at you as you leave. "That\'s all that matters! They\'ll strike again, and I won\'t be there to protect you!" You keep walking.\n\nAdd Road Event 64 to the deck.',
      "imageUrl": '/assets/cards/events/base/city/ce-64-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-64-f.png',
    "verified": False,
  },
  {
    "id": 129,
    "number": 65,
    "text":
      'In the middle of the night, you are awakened by a hard knocking at your door. You answer and it takes you a second to recognize the man standing on the other side.\n\n"Those Oak relics you was lookin\' for," the man says as he scratches a blister on the side of his face. "Some cut purses tried to sell them to me. I can take you to their place, but we gotta move fast, and I want a cut of the loot."\n\nYou hurriedly agree and make your way to a ramshackle warehouse next to the old docks.\n\n"This is it," the man says. "Looks like no one\'s home, though."',
    "optionA": {
      "choice": 'Raid the warehouse and recover the stolen goods.',
      "outcome":
        'You head into the warehouse and search, eventually finding a hidden cache of stolen goods. The thieves, however, are nowhere to be found. You think about waiting for them to return, but it s possible they have already been alerted to your presence. You return to the sanctuary, where the priest is pleased to have the artifacts returned, but troubled that the thieves are still out there.\n\nGain 2 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-65-b-a.png',
    },
    "optionB": {
      "choice": 'Wait until the thieves return so you can apprehend them.',
      "outcome":
        "You hide behind some barrels and wait for the thieves to return. It takes the rest of the night, but just as you are about to give up, two men approach the door. It's easy enough to get the drop on them, overpower them, and deliver them to the authorities. When you return the stolen artifacts to the sanctuary, the priest is incredibly pleased with your work.\n\nGain 1 prosperity.\n\nGain 2 reputation.\n\n{Saw}: Gain 1 additional reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-65-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-65-f.png',
    "verified": False,
  },
  {
    "id": 131,
    "number": 66,
    "text":
      'You head back to your rooms for the night when you see the Sawbones sitting in front of your doorstep, looking rather dejected.\n\n"I, uh, well, you see..." he stammers. "I followed your advice. Chased my dreams and all that, but I ended up in debt to some rather unscrupulous people. They\'ve threatened to kill me if I don\'t pay them off, but, uh, but I simply don\'t have the money."\n\nHe hesitates. "Seeing as how, uh, you bear some responsibility for setting me down this path, I was wondering if you\'d be willing to offer some assistance in getting me out of this mess?"',
    "optionA": {
      "choice": "Offer to pay off the Sawbones' debt.",
      "outcome":
        'PAY 40 COLLECTIVE GOLD: It\'s a hefty chunk of money, but the Sawbones is incredibly grateful.\n\n"This is wonderful! I knew I could count on you. This should be enough to put this mess behind me and finally allow me to live free."\n\nHe hands you a potion and thanks you once again for all your help.\n\nGain 1 collective Super Healing Potion (Item 055).\n\nOTHERWISE: Read outcome B.',
      "imageUrl": '/assets/cards/events/base/city/ce-66-b-a.png',
    },
    "optionB": {
      "choice": 'Get the Sawbones on a boat across the Misty Sea. New adventures surely await there.',
      "outcome":
        "You flatly refuse to pay off the Sawbones' debt and convince him the only way to escape his pursuers is to board a ship bound for the eastern continent, far out of their reach. He is reluctant but eventually agrees when you remind him what unknown adventures await in the land across the ocean. You see him off in the night and desperately hope that is the last you hear of this situation.\n\nAdd City Event 67 to the deck.",
      "imageUrl": '/assets/cards/events/base/city/ce-66-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-66-f.png',
    "verified": False,
  },
  {
    "id": 133,
    "number": 67,
    "text":
      'You are trying to enjoy a relaxing drink at the Sleeping Lion when a number of large men and Inox burst into the tavern and approach your table.\n\n"So, you must be that little creep\'s collateral," one of the Inox says."We\'re here to collect."\n\nWhen you stare at her in silence, she tries again. "Little grey-bearded man. Wore symbols of the Great Oak. He said you lot would pay off his debt if he couldn\'t."\n\nShe pats an axe at her side. "Now, seeing as how he apparently skipped town, you can pay us, or things are gonna get ugly."',
    "optionA": {
      "choice": 'Pay off the thugs.',
      "outcome":
        "PAY 60 COLLECTIVE GOLD: You sigh and hand over the Sawbones' debt, plus interest. Though it feels terrible, the thugs are satisfied and walk out the same way they came in. At least it is over now.\n\nNo effect.\n\nOTHERWISE: Seeing as how you don't have enough money, you decide to pursue other options.\n\nRead outcome B.",
      "imageUrl": '/assets/cards/events/base/city/ce-67-b-a.png',
    },
    "optionB": {
      "choice": "Refuse to pay. You won't be strongarmed by anyone.",
      "outcome":
        'You laugh and wave your hand dismissively. There\'s no way you will be paying such a large amount of money to these thugs. Unfortunately, the Inox is not amused.\n\n"Then your payment will be blood!" she says. "Meet us in the back alley, and we\'ll see if we can\'t come to terms.\n\nUnlock "Back Alley Brawl" 92 (C-14).\n\nParty Achievement: "Debt Collection."',
      "imageUrl": '/assets/cards/events/base/city/ce-67-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-67-f.png',
    "verified": False,
  },
  {
    "id": 134,
    "number": 68,
    "text":
      "You wake in the middle of the night to the sound of rushing water. In the corner of your room, you see a flood gushing out of the head of the Summoner's staff which you had previously picked up in your travels.\n\nYou jump out of bed and splash through a growing puddle of water to investigate the staff, but you can't make any sense of it. It seems to be materializing the water out of thin air, possibly channeling it from another plane of existence. You scratch your head, unsure of what to do next.",
    "optionA": {
      "choice": 'Find some way to get the water to stop gushing.',
      "outcome":
        '{Circles} {Eclipse}: You take a moment to attune yourself to the staff, which you feel now has a direct link another plane. The water stops and you are left with an open gate.\n\nUnlock "Plane of Water" 88 (D-16).\n\nParty Achievement: "Water Staff."\n\nOTHERWISE: You figure out how to work the staff but not before your entire room is flooded. The innkeeper will not be happy.\n\nLose 15 collective gold.\n\nUnlock "Plane of Water" 88 (D-16).\n\nParty Achievement: "Water Staff."',
      "imageUrl": '/assets/cards/events/base/city/ce-68-b-a.png',
    },
    "optionB": {
      "choice": 'Get the staff out of your room and throw it into the bay.',
      "outcome":
        "You race out of the inn, trying to minimize the damage caused by the never-ending stream of water. Not knowing what else to do, you head toward the river. Standing on the banks, you shrug and toss the staff into the current. You guess you'll never know how the staff ended up where it did or why it suddenly turned into a faucet.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/city/ce-68-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-68-f.png',
    "verified": False,
  },
  {
    "id": 136,
    "number": 69,
    "text":
      'You are rather surprised to walk into the Brown Door one night to see your old friend the Soothsinger playing a song on the corner stage. You are even more surprised when you get closer and discover the song is about you.\n\nIt is a raucous talc about the time she met you in a forest and you gave her terrible directions — just the worst, most backward directions possible.\n\nEveryone in the crowd is tearing up with laughter as she eloquently describes your bumbling and ineptitude.',
    "optionA": {
      "choice": 'Embrace the joke and go with it.',
      "outcome":
        "You make your way to the front of the crowd and join in the fun. When the Soothsinger notices you in the crowd, she brings you up on stage for the chorus. It's a little embarrassing, but people are enjoying your positive attitude about it.\n\nGain 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-69-b-a.png',
    },
    "optionB": {
      "choice": 'Leave the bar before someone recognizes you.',
      "outcome":
        "You flee the bar to escape the tune, but it doesn't prove to be that simple. The next day, everyone on the street is humming the tune. They all seems to be looking at you and laughing. It's a nightmare.\n\nLose 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-69-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-69-f.png',
    "verified": False,
  },
  {
    "id": 140,
    "number": 70,
    "text":
      'You are wandering the Sinking Market looking for possible work when you are approached by a dirty-looking boy with a scar on his cheek.\n\nYou greet him warmly. He has given you leads on a number of mercenary jobs and you recently helped him avoid a jail cell.\n\n"I need some help, and I really don\'t know who else to turn to," he begins. "All of us here in the Sinking Market are in a bad way. Our houses are collapsing, our water is foul, and we don\'t even have enough money for food.\n\n"We are dying here, and the city is doing nothing to help us. You have friends in high places, right? Please, there\'s gotta be someone you can talk to.',
    "optionA": {
      "choice": 'Talk to some merchants about revitalizing the area.',
      "outcome":
        "REPUTATION > 9: You head to the Coin District and meet with a member of the merchant s guild you've had dealings with before. He looks at you skeptically, but says he will see what he can do about making the area more livable.\n\nGain 1 prosperity.\n\nOTHERWISE: Every merchant you try to talk to about the issue laughs you out of the room. Why help others when there is no profit in it for them?\n\nLose 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-70-b-a.png',
    },
    "optionB": {
      "choice": "Regretfully explain that you don't have the power to effect change like this.",
      "outcome":
        "You explain that while you do have some power in the town, the Sinking Market may be a lost cause. More and more of the district is sinking into the sea every day; as it has been doing for as long as the town has existed. You can't convince merchants to spend money on something that will one day be underwater.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/city/ce-70-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-70-f.png',
    "verified": False,
  },
  {
    "id": 139,
    "number": 71,
    "text":
      "You are walking along the river's edge in the Mixed District late at night when something in your pack begins to vibrate. The sensation is odd and you quickly fish out the small metal sphere you found out on the road. It shakes uncontrollably and then begins pulling your arm toward the river.\n\nYou walk to the bank, but still the sphere pulls. It is drawn to something in the water.",
    "optionA": {
      "choice": 'Let the sphere go.',
      "outcome":
        "The sphere leaps from your hand, hovers over the water, and then emits an intense beam of light straight down into the river, illuminating something below.\n\nYou shrug and jump into the river, following the beam of light down to the bottom. There you find a wooden chest half buried under the rocks. You bring it back to shore and open it to find a small metal rod covered in strange carvings. When you pick it up, the sphere immediately flies back over to you and attaches itself to the rod's end.\n\nAdd City Event 72 to the deck.",
      "imageUrl": '/assets/cards/events/base/city/ce-71-b-a.png',
    },
    "optionB": {
      "choice": "Jump into the river and continue the sphere's pull.",
      "outcome":
        "As soon as you jump into the cold, brackish waters, the sphere stops vibrating or pulling. You swim for a while in the direction it was pulling, but eventually you realize you are on a fool's errand. You emerge from the river wet and miserable with absolutely nothing to show for it.\n\nLose 1 {Check}.",
      "imageUrl": '/assets/cards/events/base/city/ce-71-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-71-f.png',
    "verified": False,
  },
  {
    "id": 143,
    "number": 72,
    "text":
      "The metal sphere and rod — you've had them in your possession for a while now and occasionally pull them out to mull over the carvings. You've brought it to the University, but they can't make any sense of it either.\n\nYou are fiddling with the device in the Sleeping Lion when you are tapped on the shoulder. You turn to see a wicked grin on the dirty face of an old bandit. \"They call me Fish, and that there is a key, friend — a key of the ancient sort.\"\n\nBefore you can ask, Fish pulls out a similar black sphere atop a metal rod. \"They're twins, ain't they, and Fish knows just what they open. A tomb of treasure, friend. Come, come, Fish will show you the way.\"",
    "optionA": {
      "choice": 'Follow the smelly old bandit.',
      "outcome":
        'Your curiosity gets the better of your judgment. You need to know the purpose of the device you found, so you follow Fish into a derelict shack where he pulls out a map of the area and lays it on a table. Fish directs you to pull out your rod and both you and he hold your respective rods over the table.\n\nA specific location on the map glows brightly and Fish laughs. "See? I told ya, didn\'t I? Meet me there with your rod and we\'ll get rich!"\n\nUnlock "Lost Temple" 79 (K-12).\n\nParty Achievement: "Fish\'s Aid."',
      "imageUrl": '/assets/cards/events/base/city/ce-72-b-a.png',
    },
    "optionB": {
      "choice": 'Refuse to go with the man. This whole situation seems...fishy.',
      "outcome":
        "This suspicious old man must have seen you in here before with the rod and fashioned some elaborate con to swindle you out of something. You won't be so easily fooled. There's no way he knows what the rod does when no one else in town does. You push him away and go back to your drink.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/city/ce-72-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-72-f.png',
    "verified": False,
  },
  {
    "id": 141,
    "number": 73,
    "text":
      "You awake in your bed to sensation of someone shaking you, but when you look around, you see no one else in your room. Instead, you see that it's the entire room that's shaking.\n\nYour thoughts immediately go to the crystal you found inside the mountain along the road. You quickly search through your belongings and grab the crystal in your hand. The earthquake immediately stops.\n\nClearly this thing has some power and you need to deal with it before more damage is done.",
    "optionA": {
      "choice": 'Seek help from the University.',
      "outcome":
        '"Yes, very interesting," a bookish Quatryl says as he rolls the crystal over in his hand. "It seems as if this crystal is attuned to a specific location, and once removed, it begins vibrating until mountains and houses start falling down. I\'d say you need to return it to its proper home. With the proper tools — which I\'ll need help paying for — I should be able to triangulate that location for you.\n\nLose 5 collective gold.\n\nUnlock "Crystalline Cave" 84 (D-12).\n\nParty Achievement: "Tremors."',
      "imageUrl": '/assets/cards/events/base/city/ce-73-b-a.png',
    },
    "optionB": {
      "choice": 'Throw the crystal into the bay.',
      "outcome":
        'Not wanting to waste your time with the problem, you walk to the docks and throw the crystal into the bay. When you hear reports of harsher weather and larger waves hitting the docks, you try not to pay them any mind.\n\nLose 1 prosperity.',
      "imageUrl": '/assets/cards/events/base/city/ce-73-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-73-f.png',
    "verified": False,
  },
  {
    "id": 142,
    "number": 74,
    "text":
      '"Welcome to the Marvelous and Magic Techno-Circus!" The Quatryl with a top hat you met on the road greets you as you enter the circus tent. "We always welcome our friends to come and see the wondrous sights!"\n\nYou wander around the pavilion for a while, looking at all signs for manner of improbable creatures. Ultimately you will have to decide on what to see first.',
    "optionA": {
      "choice": 'Go watch the dancing bear.',
      "outcome":
        'You enter a smaller tent off the main one and come face-to-face with what is indeed a dancing bear. Its handler stands to the side, prodding it on occasion, while the bear stands on its hind two legs and shuffles back and forth. It is amusing until the handler prods the bear one too many times and the bear becomes enraged and attacks. You quickly jump into action and subdue the bear, saving the handler from getting mauled to death.\n\nGain 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-74-b-a.png',
    },
    "optionB": {
      "choice": 'Visit the famed fortune-teller.',
      "outcome":
        'You enter the fortune-teller\'s tent and the old Orchid woman\'s expression immediately goes dark. She gestures you to sit at her table, and when you do, she grabs your arm and looks deep into your eyes.\n\n"Your path is dark and cursed. There is a shadow around you — a Gloom. You must leave this place. Be rid of it before it consumes you."\n\nAll start scenario with {Curse}.\n\nGain 2 experience each.',
      "imageUrl": '/assets/cards/events/base/city/ce-74-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-74-f.png',
    "verified": False,
  },
  {
    "id": 147,
    "number": 75,
    "text":
      'Returning to Gloomhaven after your latest outing, you are approached by the Captain of the Guard at the city gates.\n\n"Ah, I was hoping I might catch you here sooner or later," he says. "I have still been receiving reports about large, flying lizards from the scouts. Tell me, have you gotten to the bottom of that situation yet?"',
    "optionA": {
      "choice": 'Lie and say that you are still working on it.',
      "outcome":
        '"Oh, hmm...well, that\'s disappointing." The Captain looks at you with dejected frustration. "If you could, please look into the sightings as soon as you can. I\'d hate to think of some giant living creature attacking the city."\n\nLose 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-75-b-a.png',
    },
    "optionB": {
      "choice": 'Tell the Captain you decided not to kill the Elder Drake.',
      "outcome":
        '"Oh, my...well, okay." The Captain looks at you with stunned curiosity. "So there is a massive, fire-breathing drake up in the mountains, and you decided there was no reason to kill it? Interesting."\n\nThe Captain wanders off, mumbling about needing to find better help.\n\nLose 2 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-75-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-75-f.png',
    "verified": False,
  },
  {
    "id": 145,
    "number": 76,
    "text":
      'You are walking through the new docks when a well-dressed merchant flags you down.\n\n"Oh, my, what a fortuitous encounter," he whispers as you approach. "May I buy you a drink? I have a very sensitive job for you, and I \'d like to avoid the prying eyes around us."\n\nThe merchant, an iron dealer named Gavin, makes a gesture toward a large group of dock workers. "I can\'t trust anyone. Well, anyone except you of course."',
    "optionA": {
      "choice": 'Accept the drink.',
      "outcome":
        'REPUTATION > 14: "Excellent! Someone has been attacking my ships at sea and I need to get to the bottom of it. Come, I\'ll tell you the details."\n\nUnlock "Merchant Ship" 74 (I-14).\n\nParty Achievement: "High Sea Escort."\n\nOTHERWISE: "Oh. whoops." Gavin stammers. "From far away, you looked like someone else. Just ignore what I said.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-76-b-a.png',
    },
    "optionB": {
      "choice": 'Decline the suspicious offer and continue your business.',
      "outcome":
        'Gavin looks flabbergasted as you walk away. "Who will protect my ships when there is no one to trust? I guess I\'ll just have to keep looking."\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-76-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-76-f.png',
    "verified": False,
  },
  {
    "id": 144,
    "number": 77,
    "text":
      '"Well, well, well. If it isn\'t the most notorious band of mercenaries in all of Gloomhaven. The guards looking to throw you in the Ghost Fortress yet, or are they on the payroll?"\n\nYou turn around to see Red Nick, a well-known fence, leaning up against the wall. You\'ve had certain dealings with him in the past.\n\n"Fancy seeing you, actually," he says. "I\'ve got a big job, and I figure if anyone wouldn\'t mind digging up graves, it would be you miscreants."',
    "optionA": {
      "choice": 'Do the job.',
      "outcome":
        'REPUTATION < -14: "That\'s the money-loving criminals I know and love! Come take a walk with me, and I\'ll explain how we can all get rich."\n\nUnlock "Overgrown Graveyard" 75 (G-12).\n\nParty Achievement: "Grave Job."\n\nOTHERWISE: "Oh, whoops," Nick stammers. "From the back you looked like...uh, never mind. Forget I said anything."\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-77-b-a.png',
    },
    "optionB": {
      "choice": "Claim you've changed your ways and graverobbing is a step too far.",
      "outcome":
        '"A downright shame, I say," Nick shakes his head. "I guess I\'ll just have to find a group of mercenaries who actually are interested in making a mountain of money."\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/city/ce-77-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-77-f.png',
    "verified": False,
  },
  {
    "id": 146,
    "number": 78,
    "text":
      'The scene is typical. A nervous looking man stands in front of your table at the Sleeping lion. You eye him lazily until he speaks.\n\n"I was, um, told you might be able to help me," he starts. "I was in the Corpsewood conducting some, uh, business, when my partners and I were attacked by Vermlings. I barely escaped with my life, but my partners weren\'t so lucky.\n\n"One of them was carrying something valuable — an artifact we managed to find in our, uh, business. It s very important I get it back. I followed the Vermlings back to their nest, and I can assure you they have many valuables. I\'ll show you where it is, and you can take whatever you want. Just bring me back the artifact."',
    "optionA": {
      "choice": "Accept the man's deal.",
      "outcome":
        'The sweaty man is all too eager to give you the details of where to find this nest.\n\n"Once you clear the Vermlings and find the artifact, you should be able to locate a large stash of valuables in a pit back behind the main camp. Take whatever you want, just return the artifact to me."\n\nYou smile and nod. After taking the valuables, you should be able to squeeze quite a bit extra out of this fellow as well when you return.\n\nUnlock "Vermling Nest" 94 (F-12)',
      "imageUrl": '/assets/cards/events/base/city/ce-78-b-a.png',
    },
    "optionB": {
      "choice": 'Demand payment for the job up-front.',
      "outcome":
        '"Look...!, ah, don\'t have a whole lot of capital right now, but I will give you everything I have once you get back with that artifact."\n\nYou narrow your eyes at him. He coughs nervously and produces a small handful of coins.\n\n"All right, fine. Look, here. This is all I can offer you. Now can we get to the part where you go do your job?"\n\nGain 5 collective gold.\n\nRead outcome A.',
      "imageUrl": '/assets/cards/events/base/city/ce-78-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-78-f.png',
    "verified": False,
  },
  {
    "id": 148,
    "number": 79,
    "text":
      'The sun is out and you are enjoying a pleasant stroll across the Silent Bridge until you see two demons attacking a man ahead of you.\n\nYou get closer and can hear the demons berating the man as they swipe at him with their claws.\n\n"You dare spit on us as we walk past?" One of them yells. "We will show you the consequences of defying authority!"',
    "optionA": {
      "choice": "Intervene on the man's behalf.",
      "outcome":
        'There is only one method these demons respect: violence. You run forward and hack at one of the demons\' arms as it comes down to strike at the man. The arm falls limp to the ground and the rest of the demon soon follows.\n\nThe other demon looks at you with seething rage as you face it with raised weapons. "This grave insult will not go unpunished! This city will feel our wrath!"\n\nLose 1 prosperity.',
      "imageUrl": '/assets/cards/events/base/city/ce-79-b-a.png',
    },
    "optionB": {
      "choice": 'Keep walking.',
      "outcome":
        'You continue your stroll, trying to block the unpleasantness from your mind. Unfortunately, others around you cannot, and they are reminded of the actions you took that caused this horrible and all-too-frequent occurrence.\n\nLose 1 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-79-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-79-f.png',
    "verified": False,
  },
  {
    "id": 149,
    "number": 80,
    "text":
      'As you prepare to leave the city on another journey, you are suddenly surrounded by a large group of guards near the west gate.\n\n"We hear you\'ve been spreading rumors," one of them says. "Claiming that the guards are causing the Vermling attacks on the city. That\'s some high-grade garbage you\'re spewing."\n\n"My best friend died in the last Vermling raid!" another one yells. "You got something smart to say about that?"',
    "optionA": {
      "choice": 'Attempt to calm down the guards and explain the situation.',
      "outcome":
        "{Scoundrel} {Saw} {MusicNote}: You adopt a serious tone and do your best to communicate that you had nothing to do with what was written in the Town Records. You express remorse for their hardships, and, miraculously, the mob grows calmer and disperses.\n\nNo effect.\n\nOTHERWISE: You laugh and claim that this is all some big misunderstanding. The guards don't see it that way, but your lack of aggression at least stops them from attacking you. They leave, grumbling threats.\n\nLose 1 reputation.",
      "imageUrl": '/assets/cards/events/base/city/ce-80-b-a.png',
    },
    "optionB": {
      "choice": 'The guards are not interested in a friendly discourse. Prepare to defend yourself.',
      "outcome":
        'Seeing the situation turning south, you waste no time pulling your weapons and prepare for an attack. The guards are more than happy to oblige.\n\nLuckily your foes sustain only some minor injuries in the time it takes for another squad of guards to arrive and break up the scuffle. They let you go on your way, but you can see the disdain in all of their eyes.\n\nLose 2 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-80-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-80-f.png',
    "verified": False,
  },
  {
    "id": 150,
    "number": 81,
    "text":
      '"Hey aren\'t you the mercenaries who stopped that weird tornado from destroying the city?"\n\nYou turn to see a dirty dock worker pointing at you with wonder in his eyes. "What was that all about anyway?"\n\nMore people stop and stare at you. This has become and unfortunately common occurrence since the Gloom was destroyed. You have become something of a minor celebrity in Gloomhaven.',
    "optionA": {
      "choice": 'Take the time to relate the story of what happened.',
      "outcome":
        'You smile and nod explaining how an ancient force attempted to destroy the city, but it was banished to another plane. Everyone around you stands enraptured by your story and cheers and claps at its conclusion. After a few additional questions, you are finally able extricate yourself from the crowd and continue your business.\n\nGain 2 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-81-b-a.png',
    },
    "optionB": {
      "choice": "Claim it wasn't you and leave quickly.",
      "outcome":
        'You brusquely shake your head and wave your hand away saying the man has the wrong person. His excited face immediately turns to one of disappointment. And audible sigh of dejection emerges from the crowd as you rush away.\n\n"There\'s no need to be rude about it!" the dockworker yells at your back.\n\nLose 2 reputation.',
      "imageUrl": '/assets/cards/events/base/city/ce-81-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/city/ce-81-f.png',
    "verified": False,
  }]
