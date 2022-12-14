# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

ROAD_EVENTS = [
{
    "id": 4,
    "number": 1,
    "text":
      '"Heading out a little late, aren\'t you?" The guard at the wall looks at you passively. You grunt in response and head through the opened gate.\n\n"Nobody\'s gonna go looking for your corpse if you don\'t return!" the guard shouts at your back.\n\nYou ended up embarking out on the road much later than you had hoped — events in town saw to that — but as dusk settles on the horizon you feel confident that you are up to any threat you might face.\n\nAnd then begins the howling of wolves — vicious, foul beasts — and, judging from their sounds, they seem to be getting closer.',
    "optionA": {
      "choice": 'Run from the howling to safety.',
      "outcome":
        'You pick up and run as fast as you can through the underbrush and away from the ominous sounds. They seem to be receding as you stumble headlong into some sort of thicket filled with sticky spines.\n\nYou pull yourself out, but not before your skin is pierced in numerous places and becomes inflamed. Best to avoid this plant in the future.\n\nAll start scenario with {Poison}.',
      "imageUrl": '/assets/cards/events/base/road/re-01-b-a.png',
    },
    "optionB": {
      "choice": 'Let the wolves come.',
      "outcome":
        'Confident that the wolves pose no significant threat, you stand your ground and prepare for battle, The pack comes — ragged and hungry, slowly emerging from the dark — and surrounds your party.\n\nThere are more of them than you expected, but not enough to take you down. You suffer a bite or two, but are able to fight them off.\n\nAll start scenario with 3 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-01-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-01-f.png',
    "verified": False,
  },
  {
    "id": 2,
    "number": 2,
    "text":
      'You are feeling a tad hungry as you walk down the road. You are considering stopping for a meal when you come across a thicket of bushes covered in green berries.\n\nThe berries look delicious, but you hesitate. They could be poisonous.',
    "optionA": {
      "choice": 'Eat the berries.',
      "outcome":
        "You shrug and grab a handful of berries to stuff in your mouth, they are incredibly sweet and just the right amount of tart. You couldn't feel better about your decision.\n\nAll start scenario with {Bless}.",
      "imageUrl": '/assets/cards/events/base/road/re-02-b-a.png',
    },
    "optionB": {
      "choice": 'Pass by the berries and just eat your normal rations.',
      "outcome":
        'Not wanting to regret making a stupid decision, you refrain from eating the berries and continue on down the road.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/road/re-02-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-02-f.png',
    "verified": False,
  },
  {
    "id": 8,
    "number": 3,
    "text":
      'You are feeling a tad hungry as you walk down the road. You are considering stopping for a meal when you come across a thicket of bushes covered in red berries.\n\nThe berries look delicious, but you hesitate. They could be poisonous.',
    "optionA": {
      "choice": 'Eat the berries.',
      "outcome":
        "You shrug and grab a handful of berries to stuff in your mouth, they are incredibly sweet and just the right amount of tart. You couldn't feel better about your decision. That is, until you start vomiting. Your stomach is incredibly unhappy with you, and the situation doesn't improve much by the time you arrive at your destination.\n\nAll start scenario with {Poison}.",
      "imageUrl": '/assets/cards/events/base/road/re-03-b-a.png',
    },
    "optionB": {
      "choice": 'Pass by the berries and just cat your normal rations.',
      "outcome":
        'Not wanting to regret making a stupid decision, you refrain from eating the berries and continue on down the road.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/road/re-03-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-03-f.png',
    "verified": False,
  },
  {
    "id": 6,
    "number": 4,
    "text":
      'You see fresh wagon tracks in the dirt as you walk along the road. You continue forward and begin to pick out a number of distinct tracks. They must be from a large caravan.\n\nSure enough, as you crest a hill, you see a group of four wagons headed down the road in the same direction as you. You count perhaps three or four guards among them.',
    "optionA": {
      "choice": 'Approach the caravan and offer to travel with them until your paths diverge.',
      "outcome":
        'The merchants in the caravan seem grateful, though the guards eye you skeptically. After traveling for half a day without event, you head off down a side road and wave good bye. The merchants express their appreciation with a bit of coin.\n\nGain 2 gold each.\n\nReputation > 9: Gain 1 additional gold each.',
      "imageUrl": '/assets/cards/events/base/road/re-04-b-a.png',
    },
    "optionB": {
      "choice": 'Attack the caravan.',
      "outcome":
        'With so few guards protecting it, the caravan makes an ideal mark. You charge down the hill, weapons at the ready. The merchants scatter, and the guards are easily dispatched, leaving you with a nice stash of valuables.\n\nGain 10 gold each.\n\nLose 2 reputation.',
      "imageUrl": '/assets/cards/events/base/road/re-04-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-04-f.png',
    "verified": False,
  },
  {
    "id": 11,
    "number": 5,
    "text":
      "You are traveling through a small wooded area when you round a bend and find a group of Inox warriors fighting a band of armored humans.\n\nWith all the commotion, it's hard to discern more details, but the humans look like guards from Gloomhaven. You are not sure why they would be out here fighting the Inox, though.",
    "optionA": {
      "choice": 'Help the Inox fight off the humans.',
      "outcome":
        'Fearing the battle could go either way, you charge into the fray laying low the human attackers. When the dust settles, the Inox offer you a skeptical thanks.\n\n"Humans think they own all this land." one of the Inox says as he spits on the ground. "We thank you for helping us with the nuisance. Allow us to bless you with a gift."\n\nGain 1 collective "Necklace of Teeth" (Item 106).',
      "imageUrl": '/assets/cards/events/base/road/re-05-b-a.png',
    },
    "optionB": {
      "choice": 'Help the humans fight off the Inox.',
      "outcome":
        'With your arrival, the Inox retreat back into the woods, one of them casting hexes as he flees.\n\n"Blast it all." one of the guards says. "Patrol duty is the absolute worst. No matter what we tell those savages, they\'re convinced were going to take over their forest. Anyway, thanks for your help. I thought we were done for"\n\nAll start scenario with {Curse}.\n\nGain 1 reputation.',
      "imageUrl": '/assets/cards/events/base/road/re-05-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-05-f.png',
    "verified": False,
  },
  {
    "id": 12,
    "number": 6,
    "text":
      'Stumbling through the woods, you are alarmed to hear the sudden sounds of a large animal rummaging through the underbrush. You crouch down, gauging the grunts and growls.\n\nThrough the trees, you see a large bear approaching your location. It has not noticed you yet, but you imagine it will soon.',
    "optionA": {
      "choice": 'Take the opportunity to run from the bear before it gets any closer.',
      "outcome":
        "You bolt from hiding as fast as you can. Luckily the hear was still a ways off, and it gets bored with the chase before it can catch you. Still, you keep running and running until you can't catch your breath.",
      "imageUrl": '/assets/cards/events/base/road/re-06-b-a.png',
    },
    "optionB": {
      "choice": 'Attack the bear, hopefully catching it by surprise.',
      "outcome":
        'The bear roars as you approach, making powerful swipes with its claws. Still, with the surprise and the commotion, the bear is not all that committed to the fight. After a bit of back and forth, the animal grunts and runs off into the trees.\n\nAll start scenario with {Wound}.',
      "imageUrl": '/assets/cards/events/base/road/re-06-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-06-f.png',
    "verified": False,
  },
  {
    "id": 16,
    "number": 7,
    "text":
      "Walking along the edge of a forest, you begin to hear strange, unfamiliar sounds coming from beyond the trees. You stop and listen closer.\n\nThere's a rhythm to the sounds, and with that established, you begin to pick out different human voices in the mix. You'd venture to say that the noise vaguely sounds like chanting.",
    "optionA": {
      "choice": 'Head into the forest to investigate the chanting.',
      "outcome":
        'You quietly move through the forest toward the noise. Eventually you come upon a clearing where you see a circle of cultists performing some strange ritual. One of them notices you and shouts to the others. The situation devolves into a bloody battle. You are, of course, victorious, but it saps some of your strength.\n\nGain 5 experience each.\n\nLose 1 {Check} each.',
      "imageUrl": '/assets/cards/events/base/road/re-07-b-a.png',
    },
    "optionB": {
      "choice": 'Keep moving on down the road. No need to get mixed up in whatever is going on.',
      "outcome":
        'Without a second thought, you get back onto the main road and continue moving toward your destination.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/road/re-07-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-07-f.png',
    "verified": False,
  },
  {
    "id": 15,
    "number": 8,
    "text":
      'You see a lone man walking toward you on the road. As you meet on the path, he turns to you and begins to speak.\n\n"Oi there. I wouldn\'t suppose you lot might spare me some coin?" he asks. "A lot of coin, actually."\n\nYou look at him quizzically as he continues. "You see, I lead a lotta thieves and bandits in this area and we gotta make sure all the mouths are fed."\n\nAt this, a large number of bandits come out of hiding around you, emerging from the bushes.\n\n"So about that coin," the man says with a smile. "Five gold per head oughta do it."',
    "optionA": {
      "choice": 'Pay the thieves.',
      "outcome":
        'You sigh and hand over what coins you have.\n\nThe man maintains his grin. "Well, thank you, kind sirs. It was a pleasure meeting you, and have pleasant day!"\n\nThe bandits move off in one direction as you continue in the other.\n\nLose 5 gold each.',
      "imageUrl": '/assets/cards/events/base/road/re-08-b-a.png',
    },
    "optionB": {
      "choice": 'Resist the robbery, killing as many thieves as you can.',
      "outcome":
        "Unfazed by the ambush, you draw your weapons and attack the bandits in the bushes. The leader tries to withdraw, but you cut him down as well. There are a lot of bandits, but they don't put up too much of a fight. They seem weak and malnourished. You guess the leader wasn't kidding about needing to buy food.\n\nAll start scenario with 3 damage.",
      "imageUrl": '/assets/cards/events/base/road/re-08-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-08-f.png',
    "verified": False,
  },
  {
    "id": 19,
    "number": 9,
    "text":
      'Walking through a stretch of lowlands, you see a man in armor sitting against a large boulder. As you get closer, you see that he is bleeding from his side.\n\n"Ah, what luck," he says "I got separated from my detail and then had an unfortunate run-in with a bear. I\'m afraid I no longer have the strength to stand."\n\nHe looks at you imploringly. "You wouldn\'t happen to have a potion or something you wouId be willing to give me? I Just need a little extra energy to make it back to Gloomhaven."',
    "optionA": {
      "choice": 'Help out the guard.',
      "outcome":
        'You happily oblige the request; letting the man partake of some of your supplies. He slowly stands up, thanks you, and then heads toward Gloomhaven as you head in the opposite direction.\n\nConsume 1 collective {SmallItem} item.',
      "imageUrl": '/assets/cards/events/base/road/re-09-b-a.png',
    },
    "optionB": {
      "choice": 'Claim you have no aid to give and move on.',
      "outcome":
        'You adopt an expression of regret and apologize for a lack of supplies. You then quickly move on your way as he shouts at your back.\n\n"But...please! You\'re not just going to leave me here, are you?"\n\nLose 1 reputation.',
      "imageUrl": '/assets/cards/events/base/road/re-09-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-09-f.png',
    "verified": False,
  },
  {
    "id": 18,
    "number": 10,
    "text":
      'You have only wandered off the main road in search of your destination when the ground begins to shift, beneath your feet.\n\nWhat was once solid now gives way, and you find yourself falling down into a dark pit. You land twenty feet down, cushioned by the soil that fell with you.\n\nYou stand up with alertness and look around, trying to get your bearings. You have fallen into a man made cavern with smooth stone walls and floors.\n\nThis could be a trap or just some long-forgotten structure.',
    "optionA": {
      "choice": 'Use weights and ropes to climb out of tbe hole as quickly as possible.',
      "outcome":
        'You tie one of your weapons to a long rope and manage to hook it onto a sturdy tree root hanging over the pit. With enough effort, you are able to extricate yourself from the pit and get as far away as possible before the situation gets worse. You suffered some minor scrapes and bruises in the fall, but you count yourself lucky.\n\nAll start scenario with 1 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-10-b-a.png',
    },
    "optionB": {
      "choice": 'Explore the area.',
      "outcome":
        'Lighting a torch, you see a number of passages leading out of the stone room. Unfazed, you head down one of them and begin exploring the network of chambers. In one, you find a pedestal and, sitting atop that, a small, metal sphere.\n\nYou take the strange sphere and continue your search, but the only other remarkable thing you find is an exit.\n\nAdd City Event 71 to the deck.\n\nAll start scenario with 1 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-10-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-10-f.png',
    "verified": False,
  },
  {
    "id": 24,
    "number": 11,
    "text":
      'You are headed through a mountainous region when the ground begins to shift and shake beneath you. Taken off guard you fall to your knees.\n\nThe tremors continue unabated and grow stronger. You hear rumbling as rocks begin to tumble down the mountainside.',
    "optionA": {
      "choice": 'Try to find a clearing where you can avoid the falling rocks.',
      "outcome":
        'You race forward, scanning the area for an open space where the danger from rock slides will be less severe. After dodging some rocks and getting hit by others, you find a relatively safe area and wait for the chaos to subside.\n\nAll start scenario with 2 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-11-b-a.png',
    },
    "optionB": {
      "choice": 'Take cover under a nearby outcropping and wait out the earthquake.',
      "outcome":
        '{Cragheart} {Spellweaver} {Triangles} {Circles}: You jump under an outcropping, but something is not right. Those among you attuned to the elements turn toward the face of the mountain and step into it, as though the rocks were gone. Inside, you see an odd crystal jutting out of the earth. You snatch it up and the tremors stop.\n\nAdd City Event 73 to the deck.\n\nOTHERWISE: The outcropping proves to be an unstable place to hide. You are quickly buried in rubble.\n\nAll start scenario with 4 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-11-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-11-f.png',
    "verified": False,
  },
  {
    "id": 22,
    "number": 12,
    "text":
      'A rustling in a nearby thicket stops you in your tracks. You crouch down and assume a defensive stance.\n\nSuddenly, a tiny ball of fur with short stubby legs leaps out at you. It barks at you twice in a ineffectual, high-pitched tone and then begins to wag its tail.\\nYou relax your weapons. What is such a small defenseless puppy doing out in the wilderness?',
    "optionA": {
      "choice": 'Leave the puppy to fend for itself.',
      "outcome":
        "Adorable as the puppy is, you are not the ones to care for it. You are headed into danger, and you can't let anything distract you from the task at hand. It follows you for a while, barking in indignation, but it eventually wanders off.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/road/re-12-b-a.png',
    },
    "optionB": {
      "choice": 'Take the puppy and bring it back to Gloomhaven.',
      "outcome":
        'You sigh and lift the puppy into your arms. It barks happily and licks your face. This will surely prove a distraction in your upcoming battle, but once you get back to Gloomhaven, you should be able to find it a nice home.\n\nOne starts scenario with {MinusOneAttackModifier}x3.\n\nGain 1 reputation.',
      "imageUrl": '/assets/cards/events/base/road/re-12-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-12-f.png',
    "verified": False,
  },
  {
    "id": 26,
    "number": 13,
    "text":
      'Traveling off the beaten path, you are surprised to see a large group of figures on the horizon. You take out your weapons and move cautiously forward.\n\nAs you get closer, it becomes clear that the figures are not alive, but sculptures of some kind, made haphazardly out of branches, garbage, and scrap metal. There are fifty or so in the middle of a field, with no other signs of life as far as you can see.\n\nYou see a necklace that may be valuable on one of them and go to grab it.\n\n"Don\'t touch her!" You wheel around to see an old man in rags emerge from a hole in the ground and charge at you with a broken broom handle. "These women are all mine!"',
    "optionA": {
      "choice": 'Defend yourself with lethal force.',
      "outcome":
        "With a single swing of your sword, the old man's head separates from his body and tumbles to the ground. The stench coming from his rags is terrible, so you grab what valuables you can find and quickly move on.\n\nGain 2 gold each.",
      "imageUrl": '/assets/cards/events/base/road/re-13-b-a.png',
    },
    "optionB": {
      "choice": 'Attempt to calm down the hermit and resolve the situation peacefully.',
      "outcome":
        'You grab the broom handle and wrestle the old man to the ground, attempting to restrain bis flailing limbs. You try to explain that this is all a misunderstanding, but he just keeps warning you not to defecate on bis wives. The man is surprisingly agile and the stench of his rags also makes keeping him pinned difficult. He slips free and scrambles around for his broom handle, muttering about the "stars" gift. You run away with all haste, but his odor is much harder to escape.\n\nAll start scenario with {Curse}.',
      "imageUrl": '/assets/cards/events/base/road/re-13-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-13-f.png',
    "verified": False,
  },
  {
    "id": 25,
    "number": 14,
    "text":
      'You are walking down the road when the sound of many wings pulls your gaze to the sky. Above you, you see a flock of white birds flying southward.\n\nAt that height, you figure a well-aimed arrow could bring one of them down to make a nice meal',
    "optionA": {
      "choice": 'Shoot at the birds.',
      "outcome":
        'You pull back your bow and take aim. The arrow flies true and connects with one of the birds. You retrieve it, pluck it, cook it, and eat it. Definitely beats the field rations you carry with you.\n\nAll start scenario with {Bless}.',
      "imageUrl": '/assets/cards/events/base/road/re-14-b-a.png',
    },
    "optionB": {
      "choice": 'Let the birds pass undisturbed.',
      "outcome":
        "The shot would be difficult, and you'd prefer not to waste the arrow. You simply move on toward your destination.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/road/re-14-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-14-f.png',
    "verified": False,
  },
  {
    "id": 29,
    "number": 15,
    "text":
      'You are walking down the road when the sound of many wings pulls your gaze to the sky. Above you, you see a large flock of red birds flying southward.\n\nAt that height, you figure a well-aimed arrow could bring one of them down to make a nice meal.',
    "optionA": {
      "choice": 'Shoot at the birds.',
      "outcome":
        'You pull back your bow and take aim. The instant you loose the arrow, however you notice something odd about the birds. They are much farther away than you realized and much bigger. The arrow misses, but it gets their attention. As the flock turns and descends toward your you realize you just shot at a group of drakes. You run for cover among the trees, but are hit by their acidic spit a number of times in the process.\n\nAll start scenario with {Muddle}.\n\nAll start scenario with 2 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-15-b-a.png',
    },
    "optionB": {
      "choice": 'Let the birds pass undisturbed.',
      "outcome":
        "The shot would be difficult, and you'd prefer not to waste the arrow. You simply move on toward your destination.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/road/re-15-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-15-f.png',
    "verified": False,
  },
  {
    "id": 32,
    "number": 16,
    "text":
      "The route to your destination is less direct than you had hoped, and you end up taking a shortcut through a small forest.\n\nThere you happen upon a family of deer. They are still a ways off in the distance and haven't noticed you.\n\nYou approach cautiously.",
    "optionA": {
      "choice": 'Shoot at one of the deer.',
      "outcome":
        'You notch your bow and take a few steps forward to find a better shooting position. Unfortunately, the deer notice your presence and bound off. You shoot a few arrows as they go, but nothing connects.\n\nThen an arrow flies out of the brush and into your shoulder. "Foul city-dwellers!" a voice cries out from the trees. "I had been stalking that herd for hours and you spooked them!" More arrows rain down as you run away.\n\nAll start scenario with {Curse}.\n\nAll start scenario with 2 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-16-b-a.png',
    },
    "optionB": {
      "choice": 'Just watch the deer for a litte bit.',
      "outcome":
        'You are enjoying watching the animals graze when an arrow flies out and hits the larger of the deer in its center chest. It bolts away, but doesn\'t make it very far before collapsing. Then you see a large Inox emerge from the brush and turn toward you. "I thought you were going to do something stupid there for a second. Thanks for not scaring away my quarry. Allow me to share some of the spoils with you."\n\nAll start scenario with {Bless}.',
      "imageUrl": '/assets/cards/events/base/road/re-16-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-16-f.png',
    "verified": False,
  },
  {
    "id": 34,
    "number": 17,
    "text":
      'Not far outside of Gloomhaven, you look up to see a large bird flying overhead. Something is odd, though. It\'s movements are jerky, and there is smoke billowing out of it. Then you see it plunge into a sudden nosedive and crash to the ground off in the east.\n\nYou rush to the scene and find a limping, soot-covered Quatryl kicking a giant winged contraption made of leather and metal.\n\n"Curse this wretched thing!" He yells in frustration. "I thought I\'d worked it out, and then I suddenly lost pressure in the piston chamber!"\n\nHe looks over at you. "You there! Wonderful timing! Help me get this thing back into the air. There is no time to waste!"',
    "optionA": {
      "choice": 'Do whatever the Quatryl says.',
      "outcome":
        "You set the wings and bang out a few dents while the Quatryl repairs his pressure problem. In under an hour, the Quatryl declares the contraption airworthy and jumps in the cockpit. You stand clear and watch in awe as the thing begins flapping wildly, then sputters forward and lifts off the ground.\n\nUnfortunately, the flight is short-lived, and the second crash is not nearly as forgiving. You find the Quatryl dead on impact, and there's nothing more to do except harvest the machine for valuable parts.\n\nGain 5 collective gold.",
      "imageUrl": '/assets/cards/events/base/road/re-17-b-a.png',
    },
    "optionB": {
      "choice": 'Demand an explanation before you help in any way.',
      "outcome":
        'You force the Quatryl to slow down and talk to you, but his eyes keep darting around in a panic. "Don\'t you understand? The world needs my technology now! I must perfect it! It will revolutionize everything!" You agree that the power of flight is pretty great, but you convince the Quatryl that the world can wait a day for him to get some rest and organize his thoughts. You help him transport the broken machine back to town.\n\nGain 1 prosperity.',
      "imageUrl": '/assets/cards/events/base/road/re-17-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-17-f.png',
    "verified": False,
  },
  {
    "id": 36,
    "number": 18,
    "text":
      'The road contains many dangers, and chief among them are the barbaric tribes of Inox that inhabit the wilderness around the city. This is why your heart sinks when you see a mounted group of them ride up to you and surround your party.\n\n"Ah, agents of that wretched monstrosity you call a town," the largest of the Inox says as he looks down at you. "Tell me, scum. What business do you have out here on my land? Have those fools sent you out to murder more of my people?"',
    "optionA": {
      "choice": 'Attempt to come to a peaceful resolution.',
      "outcome":
        'REPUTATION < -4: You begin to agree with the Inox that Gloomhaven is a blight on the land in need of cleansing, and the Inox seems to believe you. "Go in peace, then," the leader says. "And stay off my land."\n\nNo effect.\n\nOTHERWISE: You try to explain that you mean the Inox no ill will, but the leader eyes you skeptically. "Foul creature. I curse you and your kind! Run — get off my land and never come back!"\n\nAll start scenario with {Curse}.',
      "imageUrl": '/assets/cards/events/base/road/re-18-b-a.png',
    },
    "optionB": {
      "choice": 'Attack the insulting, contemptuous Inox.',
      "outcome":
        "Enraged by the Inox's insulting tongue,you take up your weapons and attack. Even the Inox were not expecting a move so bold. The fight is brutal, especially with your enemy mounted, but after felling a number of their warriors, the rest retreat.\n\nAll start scenario with 3 damage.",
      "imageUrl": '/assets/cards/events/base/road/re-18-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-18-f.png',
    "verified": False,
  },
  {
    "id": 38,
    "number": 19,
    "text":
      'Heading down the main road, you see an odd-looking wagon in front of you. It is covered in metal bars and a number ragged men in chains walk behind it. On either side of the wagon, you see city guards on horseback keeping a watchful eye on everything.\n\nYou get closer and one of the guards calls out to you. "Keep your distance! We are transporting dangerous criminals."\n\nA moment later, one of the prisoners in back slips out of his manacles and begins to sprint full speed into the tall grass.',
    "optionA": {
      "choice": 'Help the guards catch the escaping man.',
      "outcome":
        "REPUTATION < -4: You chase after the sprinting man, but the guards conclude you must be an accomplice trying to help him. They shoot arrows in your direction, forcing you to retreat from the situation.\n\nNo effect.\n\nOTHERWISE: The man's speed after spending months in a jail cell is no match for your own. With the help of the guards on horseback, you quickly have him cornered and returned to the wagon.\n\nGain 1 reputation.",
      "imageUrl": '/assets/cards/events/base/road/re-19-b-a.png',
    },
    "optionB": {
      "choice": 'Interfere with the guards to help the an escape.',
      "outcome":
        'Criminals deserve freedom as much as the next man. While the guards are distracted by the one escapee, you rush to the wagon and release the others. Chaos erupts as the prisoners scatter in every direction. Many manage to escape, and you find a mysterious gift of thanks waiting on your doorstep when you return to Gloomhaven.\n\nLose 2 reputation.\n\nReputation < -9: Gain 1 collective "Major Power Potion" (Item 041).',
      "imageUrl": '/assets/cards/events/base/road/re-19-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-19-f.png',
    "verified": False,
  },
  {
    "id": 40,
    "number": 20,
    "text":
      'You are trudging through some foothills when you hear the strangest sound in the distance. It sounds vaguely like wolves howling, but higher pitched, and there is a rhythm and a melody to it.\n\nYou crest a nearby hill and survey the area, spying a pack of Vermlings standing in a circle and singing. "Singing" is the best way you can think to describe it, anyway. Occasionally during the song they also clap and dance around.',
    "optionA": {
      "choice": 'The song must serve some nefarious purpose. Attack the Vermlings.',
      "outcome":
        "You take the pack by surprise. Fully distracted by their ritual they don't even see you coming. The Vermlings still get in a few good attacks before they are slain, though.\n\nAll start scenario with {Poison}.\n\nAll start scenario with 2 damage.",
      "imageUrl": '/assets/cards/events/base/road/re-20-b-a.png',
    },
    "optionB": {
      "choice": 'Move closer and enjoy the music.',
      "outcome":
        'Not wanting to disturb the ritual, you inch a little closer, staying out of sight, and then sit and listen. They go through a number of different tunes, and you feel enriched by the experience.\n\nGain 3 experience each.',
      "imageUrl": '/assets/cards/events/base/road/re-20-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-20-f.png',
    "verified": False,
  },
  {
    "id": 43,
    "number": 21,
    "text":
      'You find yourself cutting through the dense underbrush of a forest when you notice a number of small woodland animals running along the forest floor in opposite direction.\n\nMice, squirrels, ferrets — they all appear to be running from something up ahead of you. You are filled with a troubling sense of foreboding as you catch a whiff of smoke in the air.',
    "optionA": {
      "choice": 'Keep moving forward.',
      "outcome":
        "By the time you see the flames, it is too late. A great forest fire is raging around you. You try to run, but you don't make it out of the blaze without serious injuries and smoke inhalation.\n\nAll start scenario with {Wound}.\n\nAll start scenario with 3 damage.\n\nLose 1 {Check} each.",
      "imageUrl": '/assets/cards/events/base/road/re-21-b-a.png',
    },
    "optionB": {
      "choice": "Follow the animals' cue and run in the opposite direction.",
      "outcome":
        'Fearing the worst, you turn around and head out of the forest the way you came in. You reach a clearing just before a great fire consumes everything with its blaze. It takes a while to orient yourself and find the road again, but considering the alternative, you feel lucky.\n\nDiscard 2 cards each.',
      "imageUrl": '/assets/cards/events/base/road/re-21-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-21-f.png',
    "verified": False,
  },
  {
    "id": 44,
    "number": 22,
    "text":
      'There was a heavy rain last night, and the roads are now dark streaks of mud. And as bad as it is for you walking, you see that others up ahead on the road are having worse trouble. You come upon a collection of wagons stuck in the mud on the side of the road.\n\nYou look around and see an odd assortment of people dressed in garish clothing. They are working to push their brightly painted wagons, all emblazoned with a "Marvelous and Magical Techno-Circus" logo, out of the muck.\n\n"We just stopped for a quick meal, and now the wheels have sunk into this mess," a Quatryl with a fancy top hat says as you approach. "I\'m sure our strongmen will get us out eventually but we certainly wouldn\'t begrudge a little extra help."',
    "optionA": {
      "choice": "Help push out the Quatryl ringmaster's wagon.",
      "outcome":
        'You put down some boards and then heave and push until the great wagon is out of the ditch and moving back on the road. The diminutive Quatryl tips his hat.\n\n"Well, I certainly could not have done that on my own. Your assistance is greatly appreciated. I tell you what — the next time were back in Gloomhaven, why don\'t you stop by our circus, and we \'ll let you in for free."\n\nAdd City Event 74 to the deck.',
      "imageUrl": '/assets/cards/events/base/road/re-22-b-a.png',
    },
    "optionB": {
      "choice": 'Help push out the fortune-tellers wagon.',
      "outcome":
        'You take pity on an old Orchid woman trying to extricate her fortune-teller\'s wagon by herself. You help her get it back on the road, and then she grabs you and looks deep into your eyes.\n\n"Your path is dark and cursed. There is a shadow around you — a Gloom. You must leave this place. Be rid of it before it consumes you."\n\nGain 2 experience each.\n\nAll start scenario with {Curse}.',
      "imageUrl": '/assets/cards/events/base/road/re-22-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-22-f.png',
    "verified": False,
  },
  {
    "id": 47,
    "number": 23,
    "text":
      'A knapsack and a walking stick on the side of the road catch your attention as you pass. You look around and see a man squatting in the hushes a small distance away.\n\n"Oh, hello!" he says. "Good timing, actually. You wouldn\'t mind grabbing me some leaves, would you? It\'s seems I\'ve made quite a mess over here."',
    "optionA": {
      "choice": 'Bring the man some leaves.',
      "outcome":
        'You gather up a handful of leaves and walk over to him. If you weren\'t quite sure what was going on before, the smell definitely confirms it.\n\n"Thanks a lot!" he says cheerily. "Sometimes nature calls, am I right?"\n\nYou cough in affirmation and quickly move on.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/road/re-23-b-a.png',
    },
    "optionB": {
      "choice": "Grab his stuff and run off while he's indisposed.",
      "outcome":
        'You look from the squatting man down to his bag. Surely he has something of value in there. You quickly grab it and run off down the road.\n\n"Hey!" the man yells at you. "What are you doing? My stuff!"You don\'t look back.\n\nGain 2 gold each.\n\nLose 1 reputation.',
      "imageUrl": '/assets/cards/events/base/road/re-23-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-23-f.png',
    "verified": False,
  },
  {
    "id": 55,
    "number": 24,
    "text":
      'You come across a group of brow-beaten Inox trudging down the path in the opposite direction as you. Some are pulling carts laden with various miscellany, mostly furs and crudely crafted goods. The rest have armloads of much of the same.\n\nIt is obvious that this is everything the Inox have — their life\'s worth in their arms and wagons. They are all covered in what appears to be soot.\n\nThe shaman at the head of the group calls to you. "The beast awakens! The mountain is aflame! Beware you do not anger it!"\n\nLooking to the horizon, you can see black smoke rising from a far-off peak.',
    "optionA": {
      "choice": 'Aid the Inox with what they are carrying.',
      "outcome":
        'You take pity on the disheveled group of Inox, forced from their home by a natural disaster. You travel with them fora time, treating their wounds and helping to lighten their loads.\n\nThe Shaman thanks you and hands you an amulet. "We can\'t return to our homes until the beast rests. I fear what this may mean for us all. I hope this keeps you safe."\n\nGain 10 collective gold.\n\nDiscard 2 cards each.\n\nUnlock "Burning Mountain" 82 (M-6).',
      "imageUrl": '/assets/cards/events/base/road/re-24-b-a.png',
    },
    "optionB": {
      "choice": 'Ignore the Shamans ramblings.',
      "outcome":
        'You brush off the plight of the Inox tribe, but as you continue to your destination, you begin to feel a certain amount of uncase. There is a slight tremble in the soles of your feet, and, in the distance, the black cloud of smoke grows.\n\nUnlock "Burning Mountain" 82 (M-6).',
      "imageUrl": '/assets/cards/events/base/road/re-24-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-24-f.png',
    "verified": False,
  },
  {
    "id": 49,
    "number": 25,
    "text":
      'You are far off the main road when you see a small band of Inox approaching from the west. You try to divert your path to go around them, but they are moving directly into your path.\n\nIn a few minutes\' time they overtake you.\n\n"You\'ve wandered into our territory travelers," the biggest one says. "We don\'t much like visitors."\n\nYou stare at her blankly.\n\n"Such acts can be forgiven, but it will cost you."',
    "optionA": {
      "choice": 'Try to reason with the Inox',
      "outcome":
        "{Brute} {LightningBolts}: The Inox in your party talks with the leader for a while and they are able to come to an agreement. They punch each other's chests, and the group lets you through.\n\nNo effect.\n\nOTHERWISE: The Inox don't seem to be budging on this payment issue, so you are forced to pass along a handful of coins. The big one smiles and lets you continue on your way.\n\nLose 5 gold each.",
      "imageUrl": '/assets/cards/events/base/road/re-25-b-a.png',
    },
    "optionB": {
      "choice": "Fight off the Inox. They'll get no payments from you.",
      "outcome":
        'You raise your weapons and state that no payments will be made this day. The group of Inox snarls and attacks. After you land a few solid blows, though, they break off and run away back to the west, leaving you to tend to your wounds.\n\nAll start scenario with 3 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-25-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-25-f.png',
    "verified": False,
  },
  {
    "id": 52,
    "number": 26,
    "text":
      'You see a lone wagon off to the side of the road up ahead. You approach cautiously.\n\nAs you near, a jovial man with a wide hat waves at you. "Ho there! I don \'t suppose you have any expertise in fixing a broken axle? The road wasn\'t even that bumpy, and then BAM!" The man claps his hands together.\n\n"Just splits in half. I need to have all these goods up north in two days, and I am just at a loss about how to get myself out of this pickle!"',
    "optionA": {
      "choice": 'Attempt to help the man with his axle problem.',
      "outcome":
        "{Tinkerer} {ThreeSpears}: The man talks the whole way through the process, but after an hour or so, the axle is repaired and the man leaves in a radiant mood, bestowing blessings upon you.\n\nAll start scenario with {Bless}.\n\nGain 1 reputation.\n\nOTHERWISE: You happily agree to help the man, but quickly realize you don't know what you are doing. The man thanks you anyway, and you move on.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/road/re-26-b-a.png',
    },
    "optionB": {
      "choice": 'Tie up the man and take all of the goods he is so concerned about.',
      "outcome":
        "You smile widely and approach the man. He doesn't even put up a fight. The first thing you do is gag him, because he is a talker. You select the lightest of the valuables to take with you and leave the man tied up on the side of the road. You could say his day just went from bad to worse, but that s not your problem.\n\nGain 10 collective gold.\n\nLose 1 reputation.",
      "imageUrl": '/assets/cards/events/base/road/re-26-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-26-f.png',
    "verified": False,
  },
  {
    "id": 63,
    "number": 27,
    "text":
      'Walking a path between a small grove and a steep cliff, you suddenly find yourself facing a massive group of felled trees blocking the road.\n\nThe placement of the trees seems odd, and you have a wary, suspicious feeling about the whole situation.',
    "optionA": {
      "choice": 'Clear the trees from the road. It is the best way through and will help other travelers.',
      "outcome":
        "{Spellweaver} {Triangles} {Circles}: The trees are too massive and dense to remove through conventional means, but with elemental power, they are destroyed and swept aside in no time.\n\nNo effect.\n\nOTHERWISE: The trees aren't part of an ambush, but that doesn't make them any easier to clear. It' s grueling work and by the time you arrive at your destination, you are exhausted.\n\nDiscard 3 cards each.",
      "imageUrl": '/assets/cards/events/base/road/re-27-b-a.png',
    },
    "optionB": {
      "choice": 'Take the time to find a way around the trees.',
      "outcome":
        'You head into the underbrush of the grove to get around the felled trees, but it is rough going. The growth is very dense and there are quite a few prickly thorns to contend with.\n\nAll start scenario with 2 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-27-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-27-f.png',
    "verified": False,
  },
  {
    "id": 56,
    "number": 28,
    "text":
      'As you walk down a dirt path, you see a hard-looking mercenary sitting in a patch of grass. He nods as you pass.\n\n"Hey, friends," he says. There is something off about his tone, though.\n\n"I don\'t suppose one of you might he willing to part with a stamina potion, would you? I\'m headed toward Gloomhaven, but I\'ve just come such a long way and I\'m not feeling too good about the stretch I have left."\n\nWith the clank of his sword sheath against his armor and a loud groan, the man stands up. "I\'ll pay you well for it."',
    "optionA": {
      "choice": 'Sell the man a stamina potion.',
      "outcome":
        'PAY 1 COLLECTIVE "MINOR STAMINA POTION" (ITEM 013): After some oddly tense negotiations, you are able to agree upon a price. With one hand firmly on his sword hilt, the man grabs a coin pouch with the other hand and extends it toward you. You exchange goods and continue on your journey without further incident.\n\nGain 10 collective gold.\n\n{Scoundrel} {Saw} {MusicNote}: Gain 10 additional collective gold.\n\nOTHERWISE:\n\nRead outcome B.',
      "imageUrl": '/assets/cards/events/base/road/re-28-b-a.png',
    },
    "optionB": {
      "choice": 'Politely decline and move quickly on your way.',
      "outcome":
        'There was something off-putting about that man. You are more than happy to move along and put some distance between you.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/road/re-28-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-28-f.png',
    "verified": False,
  },
  {
    "id": 57,
    "number": 29,
    "text":
      'Walking among some foothills, you enter a narrow valley and find a large pile of stones blocking your way. Clearly a rock slide occurred here recently.\n\nYou move closer to the pile and despair at just how large the stones are. Only someone of great strength and skill could clear a path efficiently.',
    "optionA": {
      "choice": 'Attempt to clear the stones from the path.',
      "outcome":
        "{Cragheart}: The Cragheart's combination of raw strength and an affinity for stonework is perfect for this task. In a matter of minutes, enough stones have been destroyed or thrown aside to open a path.\n\nNo effect.\n\nOTHERWISE: The situation is not ideal, but you work through the pain. By the time a path has been cleared away, you never want to see another rock in your life.\n\nDiscard 2 cards each.",
      "imageUrl": '/assets/cards/events/base/road/re-29-b-a.png',
    },
    "optionB": {
      "choice": 'Backtrack and find a way around the stone-filled valley.',
      "outcome":
        "You sigh and turn around. After some backward progress, you find another path through the foothills and work your way through it. Unfortunately it leads you directly into a den of wolves, and they don't seem too happy about your sudden arrival. You fend them off, but they leave you wounded.\n\nAll start scenario with {Wound}.",
      "imageUrl": '/assets/cards/events/base/road/re-29-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-29-f.png',
    "verified": False,
  },
  {
    "id": 58,
    "number": 30,
    "text":
      'You see smoke on the horizon and catch the vague stench of burning flesh. You hasten your step see what catastrophe lies ahead of you on the road.\n\nAfter a few minutes, you come upon a trade caravan ravaged by a pack of Vermlings, if the tracks in the mud are any indication.\n\nDead bodies and broken, upturned carts lie across the path, but you can also see a few survivors, wounded and bloody on the ground. A woman limps across the road, carrying pieces of wreckage.',
    "optionA": {
      "choice": 'Help the survivors deal with the carnage.',
      "outcome":
        "{Mindthief} {TwoMinis}: You approach to help those still alive, but the woman in the road screams, gesturing at the Vermling in your group. You try to calm her, but it is of no use. You abandon the cause.\n\nNo effect.\n\nOTHERWISE: You disperse through the scene, tending to people's wounds and getting them back on their feet. It takes a few supplies, but they seem grateful in the end.\n\nConsume 1 {SmallItem} item each.\n\nGain 1 reputation.",
      "imageUrl": '/assets/cards/events/base/road/re-30-b-a.png',
    },
    "optionB": {
      "choice": 'Finish the job the Vernilirtgs started and loot whatever is left.',
      "outcome":
        'It takes very little effort to finish off those who survived and put them out of their misery. Unfortunately, the Vermlings were quite thorough in their raid. You only manage to find a handful of goods, with the rest presumably either taken or burned.\n\nGain 2 gold each.',
      "imageUrl": '/assets/cards/events/base/road/re-30-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-30-f.png',
    "verified": False,
  },
  {
    "id": 61,
    "number": 31,
    "text":
      'You approach the crest of a hill to the sound of yelling and swords clashing. Advancing, you see a trade caravan fighting off a swarm of Vermlings.\n\nYou can easily see that the caravan guards are not doing well. They are vastly outnumbered and forced to remain in a defensive position to protect their employers. You expect they will be overwhelmed and killed in a manner of minutes.',
    "optionA": {
      "choice": 'Charge into the fray to protect the caravan from the savage attack.',
      "outcome":
        '{Brute} {Sun} {ThreeSpears}: Fortunately, some of your group excels when in a defensive position, and the tide of the battle clearly turns once they take command of the situation. The Vermlings are driven off and the caravan is saved.\n\nGain 2 reputation.\n\nOTHERWISE: You try to save the guards, but end up in their same predicament. You manage to fight off the Vermlings, but not before all the guards and merchants are killed.\n\nAll start scenario with 3 damage.\n\nGain 5 gold each.',
      "imageUrl": '/assets/cards/events/base/road/re-31-b-a.png',
    },
    "optionB": {
      "choice": 'Watch lor a while and wait for an opportune moment to strike.',
      "outcome":
        "You wait for a good long while, until after the guards have all been slaughtered and the Vermlings are softened up a bit. They're going through the goods in the wagons when you hit them with a surprise attack. Caught off guard, they go down without much of a fight.\n\nAll start scenario with 1 damage.\n\nGain 5 gold each.",
      "imageUrl": '/assets/cards/events/base/road/re-31-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-31-f.png',
    "verified": False,
  },
  {
    "id": 65,
    "number": 32,
    "text":
      'You encounter two Valraths with a small horse and cart on the side of the road. They seem a little uncomfortable at your approach, their hands instinctively going for their weapons.\n\nYou make a sign of peace and they relax a little.\n\n"Perhaps it is good that you happen by, travelers, " the one on the left says. "Our horse is completely spent and we fare little better. We are in desperate need of some supplies to finish our journey."\n\n The Valrath offers a crude smile. "Do you think you could help us in this matter?"',
    "optionA": {
      "choice": 'Give the Valraths a portion of your supplies.',
      "outcome":
        "{ThreeSpears}: The Quartermaster steps forward with smile and hands over a sack of food and gear. He is always well-stocked and the Valraths are grateful for the aid.\n\nGain 1 reputation.\n\nOTHERWISE: You'll need to replace the supplies the next time you're in town, but you decide you can spare them. The Valraths thank you with relief.\n\nLose 5 gold each.\n\nGain 1 reputation.",
      "imageUrl": '/assets/cards/events/base/road/re-32-b-a.png',
    },
    "optionB": {
      "choice": 'You spent good money on these supplies. Refuse to help.',
      "outcome":
        "You apologize curtly and continue on your way. The Valraths seem disappointed, but vaguely understanding. It doesn't stop them from whispering things about you to each other as you walk away.\n\nLose 1 reputation.",
      "imageUrl": '/assets/cards/events/base/road/re-32-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-32-f.png',
    "verified": False,
  },
  {
    "id": 64,
    "number": 33,
    "text":
      "Something is..off.\n\nYou step in the middle of the road and feel a rippling in your skin. You're not sure what it is, but some strange forces are at work.\n\nThere is a faint whisper on the wind and you feel as though at any moment, one step could send you plummeting off the face of the earth.",
    "optionA": {
      "choice": 'Investigate further. Whatever forces are at work must be put in check.',
      "outcome":
        '{Eclipse} {Circles}: The Aesther in your group leads you to an area off the road that feels...fuzzy. It is hard to focus your vision, as if the space in front of you is only half there. With a few words from the Aesther, the blur is gone.\n\nNo effect.\n\nOTHERWISE: You wander around for a while before a massive demon suddenly appears before you, ripped from another plane. Your presence surprises it, though, and you dispatch it before too much trouble is caused.\n\nAll start scenario with 1 damage.\n\nDiscard 1 card each.',
      "imageUrl": '/assets/cards/events/base/road/re-33-b-a.png',
    },
    "optionB": {
      "choice": 'Get out of this place as quickly as you can.',
      "outcome":
        'You head forward with all haste, eager to get back your bearings. You seem to be out of the worst of it when you are suddenly ambushed by a giant demon from behind. You fight it off, but not before it tears into you and burns your flesh.\n\nAll start scenario with 3 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-33-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-33-f.png',
    "verified": False,
  },
  {
    "id": 68,
    "number": 34,
    "text":
      "Your travels leave you out in the wilderness overnight, so you make camp and start a fire.\n\nIt's hard to sleep outside of the comfort of the city, always on guard, looking for the next fatal threat. Luckily the night proves fairly dull. That is, until you hear the sound of voices approaching your camp.\n\nThey are faint and low — almost like growling, but you can hear indications of language.",
    "optionA": {
      "choice": 'Quickly put out the fire and sneak out into the brush to get a look.',
      "outcome":
        '{Scoundrel} {Mindthief} {Eclipse}: Your stealth skills prove sufficient enough to remain unnoticed by a large group of Inox. You decide to let them pass by without incident.\n\nNo effect.\n\nOTHERWISE: You attempt to hide and stay quiet, but a snapped twig at an unfortunate moment startles the passing band of inox, and they pull out weapons and attack. The scene turns bloody, and you are barely able fight them off.\n\nAll start scenario with 4 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-34-b-a.png',
    },
    "optionB": {
      "choice": 'Wait by the fire for whatever comes.',
      "outcome":
        '{Brute} {LightningBolts}: A group of Inox appears at the edge of your campsite. Seeing their kind among you, they greet you in a friendly manner and stay for some time to talk. After they leave, you find the remainder of the night restful.\n\nNo effect.\n\nOTHERWISE: A group of irate Inox appears at the edge of your campsite. They claim you are trespassing and force you to pack up and leave. You walk through the rest of the night and arrive at your destination tired.\n\nDiscard 2 cards each.',
      "imageUrl": '/assets/cards/events/base/road/re-34-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-34-f.png',
    "verified": False,
  },
  {
    "id": 69,
    "number": 35,
    "text":
      'You are enjoying a pleasant, peaceful stroll down the road when you find yourself suddenly surrounded by a beleaguered group of men. One of them steps forward, a pox covering half his face.\n\n"Good day to you." He smiles weakly. "We hate to be a burden, but you see, my camp has been taken ill with a strange malady, and we must kindly beg you for some money for medicine."\n\nYou look around to see that some disfiguring disease has indeed come over the lot of them.\n\nThe man scratches the side of his face with one hand while he slowly pulls out a sword with the other. "I\'m afraid we can\'t take no for an answer."',
    "optionA": {
      "choice": 'Fight oft the men. This is highway robbery, whatever the motive.',
      "outcome":
        "{Cthulu}: The Plagueherald stretches out his arms and the men around him immediately double over in pain. You can almost sense it smiling, even though it doesn't have a face. The fight doesn't last long, especially once the men's wounds start bursting with maggots.\n\nAll start scenario with 1 damage.\n\nOTHERWISE: The men are weakened, but they are still hardened fighters. You fight them off, but it gets ugly.\n\nAll start scenario with {Poison}.\n\nAll start scenario with 3 damage.",
      "imageUrl": '/assets/cards/events/base/road/re-35-b-a.png',
    },
    "optionB": {
      "choice": 'Pay the men and be on your way.',
      "outcome":
        'PAY 5 GOLD EACH: You smile as non-threateningly as you can and reach for your coin purse. You try to give them just a couple coins, but he encourages you to donate more. Eventually the men seem satisfied and move on their way.\n\nNo effect.\n\nOTHERWISE: When you try to pay with what few coins you have, the man thinks you are holding out on him and grows angry.\n\nRead outcome A.',
      "imageUrl": '/assets/cards/events/base/road/re-35-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-35-f.png',
    "verified": False,
  },
  {
    "id": 72,
    "number": 36,
    "text":
      "Up ahead, you see the path you are on leads into a dark and unfamiliar wood. It gives you an eerie feeling.\n\nAs you step closer, you can feel your skin crawl and it forces you to pause, you can't help, but think that this wood might best be avoided.",
    "optionA": {
      "choice": 'Continue down the path into the wood. You are not afraid.',
      "outcome":
        '{LightningBolts} {TwoMinis} {PointyHead}: The wood is overgrown and rampant with all manner of insects, but with difficulty, you follow the path. Somewhere deep inside, you come across a stone pedestal with the following scratched into its base:\n\n{RuneR}{RuneE}{RuneC}{RuneO}{RuneR}{RuneD} {RuneT}{RuneH}{RuneE} {RuneP}{RuneA}{RuneG}{RuneE}, {RuneT}{RuneH}{RuneE} {RuneW}{RuneO}{RuneD}{RuneD}, {RuneA}{RuneN}{RuneD} {RuneT}{RuneH}{RuneE} {RuneL}{RuneR}{RuneT}{RuneT}{RuneE}{RuneR} - {Rune8}{Rune3}{Rune4}.\n\nOTHERWISE: You follow the path into the wood and become hopelessly lost. The going is hard and painful.\n\nAll start scenario with {Poison}.\n\nAll start scenario with 2 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-36-b-a.png',
    },
    "optionB": {
      "choice": 'Find another way to your destination.',
      "outcome":
        "The wood is large and you spend a little more time than you 'd like trying to get around it. With enough effort, you arrive at your destination just a little bit more tired than you d like.\n\nDiscard 1 card each.",
      "imageUrl": '/assets/cards/events/base/road/re-36-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-36-f.png',
    "verified": False,
  },
  {
    "id": 73,
    "number": 37,
    "text":
      "What starts as a light rain quickly turns into something much worse, with torrents of water battering your skin and lightning piercing the sky.\n\nYou're able to find a small rock outcropping and rush under it as thunder shakes the ground. This should protect you from the worst of it, but you don't know how long the storm will last.",
    "optionA": {
      "choice": "Brave the storm and continue on your way. It's not that bad.",
      "outcome":
        "{MusicNote}: You feel positively dismal trudging through the mud and the rain, until you hear the Soothsinger's voice rise above the thunder. She's singing a song in the middle of the storm, and everyone starts to feel better.\n\nNo effect.\n\nOTHERWISE: Walking down the road in a storm is just awful. You are wet and cold and miserable and you cannot wait for the whole experience to end. By the time you reach your destination, you are not feeling well at all.\n\nDiscard 2 cards each.",
      "imageUrl": '/assets/cards/events/base/road/re-37-b-a.png',
    },
    "optionB": {
      "choice": 'Wait out the storm under the outcropping',
      "outcome":
        'It is far from ideal, but the outcropping keeps you mostly dry and protects you from the howling wind. You wait hours and hours, huddled up under the rock until the storm passes. By the time you arrive at your destination, you are a bit slow on your feet due to lack of sleep.\n\nAll start scenario with {Disarm}.',
      "imageUrl": '/assets/cards/events/base/road/re-37-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-37-f.png',
    "verified": False,
  },
  {
    "id": 75,
    "number": 38,
    "text":
      'It is something small that catches your eye: a button on the ground glinting in the sun. A button in the shape of an Oak Leaf.\n\nYou stop to investigate, and then you begin to see the bigger things. Splatters of blood in the dirt. Signs of multiple bodies being dragged into the forest.\n\nYou stand and peer into the underbrush. You see a few broken branches and crushed plants. Maybe you could track the bodies through the forest.',
    "optionA": {
      "choice": 'Head off into the forest to find out what happened.',
      "outcome":
        '{LightningBolts} {TwoMinis} {PointyHead}: You are able to track the trail with ease. It leads to a couple of priests, bloody and unconscious, but still alive. You revive them and bring them back to the main road. They are very grateful.\n\nGain 1 prosperity.\n\nOTHERWISE: You try to follow the trail, but end up getting turned around and lost. Then you have an incredibly difficult and painful way back out.\n\nLose 1 {Check} each.\n\nDiscard 1 card each.',
      "imageUrl": '/assets/cards/events/base/road/re-38-b-a.png',
    },
    "optionB": {
      "choice": 'Move on. That forest does not look friendly.',
      "outcome":
        "Whatever happened here could not have been good, but also it doesn't concern you and you're not about to head into that dark, dense forest ill-prepared. You find it best to move along and attend to your own matters.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/road/re-38-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-38-f.png',
    "verified": False,
  },
  {
    "id": 78,
    "number": 39,
    "text":
      'You see movement in the tall grass to your left, and a weak voice calls out.\n\n"Help... me...please..."\n\nYou approach the stirring to see a Valrath man writhing on the ground, his skin covered in boils and pus-filled sores.\n\n"The sickness burns..." he moans at you. "Please... help..."',
    "optionA": {
      "choice": 'Help the poor Valrath.',
      "outcome":
        '{Saw}: The Sawbones knows exactly what to do, covering his hands and face as he cleans the wounds. After an hour of tending to him, the Valrath seems good enough to travel.\n\nGain 1 reputation.\n\nOTHERWISE: You help the Valrath as best you can, but it takes many supplies and potions. When he finally looks better, you realize you are starting to feel sick as a result.\n\nAll start scenario with {Poison}.\n\nLose 10 collective gold.\n\nGain 1 reputation.',
      "imageUrl": '/assets/cards/events/base/road/re-39-b-a.png',
    },
    "optionB": {
      "choice": 'This is clearly some sort of plague. Avoid it at all costs.',
      "outcome":
        'You recoil in terror and quickly move along. You can hear the Valrath sobbing as you do so, but you know well enough to avoid a plague when you see it.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/road/re-39-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-39-f.png',
    "verified": False,
  },
  {
    "id": 80,
    "number": 40,
    "text":
      "There were heavy rains last night for sure, but you didn't realize the full extent of it until you come face-to-face with a river raging right through the middle of the road.\n\nThis river is no small matter, either — it is several feet deep and fast-flowing. It's rather troubling, too, since you have no idea how long it might take to find a decent crossing point.",
    "optionA": {
      "choice": 'Ford the river where you are. It is not ideal, but it should be possible.',
      "outcome":
        '{Spellweaver} {Triangles} {Circles}: With the power of the elements on your side, crossing the river turns out to be incredibly easy. One frozen bridge later, you are on the other side and on your way.\n\nNo effect.\n\nOTHERWISE: The water is surprisingly cold, but it will take more than that to end your day. You are still water-logged and shivering when you reach your destination, however.\n\nAll start scenario with {Muddle}.\n\nAll start scenario with {Immobilize}.',
      "imageUrl": '/assets/cards/events/base/road/re-40-b-a.png',
    },
    "optionB": {
      "choice": 'Head downriver and find a better place to cross.',
      "outcome":
        'It takes an hour, but you finally find a rocky area where the river has been diverted into many smaller streams. It is no problem to cross, but just finding the spot and then getting back on track takes some of the fire out or you.\n\nDiscard 2 cards each.',
      "imageUrl": '/assets/cards/events/base/road/re-40-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-40-f.png',
    "verified": False,
  },
  {
    "id": 82,
    "number": 41,
    "text":
      "Your path is taking you through a small wooded area when you suddenly see a large bear charging directly at you through the trees.\n\nYou may have gotten too close to its den, but you can't know for sure. All you know is that it is clearly enraged, and you have very little time to react.",
    "optionA": {
      "choice": 'Attemp to calm the bear and back away slowly.',
      "outcome":
        "{TwoMinis}: The Beast Tyrant steps forward with his hand outstretched and makes a low humming sound. The bear stops mid-charge with a perplexed look. You leave the animal there and continue on your way unharmed.\n\nNo effect.\n\nOTHERWISE: Two seconds later, you can't help, but feel this was a terrible idea. The bear wounds you severely before you are able to arm yourself and fight it off.\n\nAll start scenario with {Wound}.\n\nAll start scenario with 3 damage.",
      "imageUrl": '/assets/cards/events/base/road/re-41-b-a.png',
    },
    "optionB": {
      "choice": 'Arm yourself and fight off the bear.',
      "outcome":
        'You quickly grab your weapons as the bear comes down on you. The fight is brutal and ugly, but it could have been much worse.\n\nAll start scenario with 2 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-41-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-41-f.png',
    "verified": False,
  },
  {
    "id": 84,
    "number": 42,
    "text":
      "A trade caravan passes by you on the road. This event isn't too uncommon, but what catches your eye is a familiar-looking Inox traveliing with the caravan as a guard.\n\nAt the sight of you, the Brute lights up and gives you a big wave, then rushes over to greet you. He is positively joyful to see you and immediately starts to reminisce about all the exciting battles you fought together.\n\nSlapping you on the back, he implores you to travel with the caravan for a while to give you all a chance to catch up.",
    "optionA": {
      "choice": "Agree to travel with the Brute for a little while. So what if it's in the wrong direction?",
      "outcome":
        'As you walk with the Brute and talk with him about your early adventuring days, you find a hint of sadness behind his enthusiasm. He explains how he fell on hard times after leaving the group and had to resort to jobs like this to make ends meet. The Brute seems uplifted by your conversation, but the day grows late. By the time you head back and arrive at your destination, you are incredibly tired.\n\nDiscard 3 cards each.',
      "imageUrl": '/assets/cards/events/base/road/re-42-b-a.png',
    },
    "optionB": {
      "choice": 'Regretfully leave the Brute to his duties and continue on your way.',
      "outcome":
        "You explain to the Brute that you have a long day's travel ahead of you and cannot take the time to travel in the other direction. As you make your good-byes, a shadow falls over him. He walks away forlorn.\n\nAdd Road Event 60 to the deck.",
      "imageUrl": '/assets/cards/events/base/road/re-42-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-42-f.png',
    "verified": False,
  },
  {
    "id": 88,
    "number": 43,
    "text":
      "You probably wouldn't normally noticed it, but sometimes nature calls and you need to head off the beaten path to get some privacy.\n\nHidden in the bushes, you come across the smoking wreckage of some crude machine. It looks to have broken down at some point and was left here to rust and decay.\n\nMost of it is scrap, but thanks to your time with the Tinkerer, you know a good power core when you see one. Its a bit heavier than you'd hoped, but it should fetch a good price back in Gloomhaven.",
    "optionA": {
      "choice": 'Take the core with you.',
      "outcome":
        'The core sure is heavy. You manage it rather well, but it will be a bit of hindrance in battle. You hope the payoff is worth the trouble.\n\nOne starts scenario with {MinusOneAttackModifier}x3.\n\nGain 10 collective gold.',
      "imageUrl": '/assets/cards/events/base/road/re-43-b-a.png',
    },
    "optionB": {
      "choice": "Leave the core alone. You don't want anything weighing you down in battle.",
      "outcome":
        'You decide the risk is not worth the reward and walk away from the contraption before you scratch yourself on the rusted metal and give yourself some foul disease. And just the thought of haggling with the Quatryls in the Mixed District about a fair price makes you tired and irritable.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/road/re-43-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-43-f.png',
    "verified": False,
  },
  {
    "id": 89,
    "number": 44,
    "text":
      'Due to a late start, night falls before you can get to where you are going. You are on your guard throughout the night, but nothing can quite prepare you for Night Demon attack.\n\nThey come upon you silent and invisible, so you are unaware of their presence until their claws sink into your flesh.\n\nThe darkness erupts into chaos with flashing swords and horrific shrieks. And then a bolt of fire streaks through the darkness and incinerates one of the demons.\n\nSomeone else is out there.',
    "optionA": {
      "choice": 'Renew your efforts to slay the demons.',
      "outcome":
        'With the help of the mysterious firecaster, the battle turns and the demons are slain without much pain. Out of the darkness steps the familiar face of a female Orchid.\n\n"Sorry about that. I think they were looking for this." The Spell weaver holds up a black censer. "It\'s a good thing I ran into you, though. I could use your help."\n\nShe draws out a crude map. "Meet me here as soon as you can, and I\'ll explain more."\n\nUnlock "Demonic Rift" 90 (J-7).',
      "imageUrl": '/assets/cards/events/base/road/re-44-b-a.png',
    },
    "optionB": {
      "choice": 'Use the distraction to disengage from the demons and run away.',
      "outcome":
        "This mysterious third party seems to have things under control, and the demons appear more interested in them anyway. You take the opportunity to retreat from the fight and run off into the night. You don't feel great about it, but at least you're alive.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/road/re-44-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-44-f.png',
    "verified": False,
  },
  {
    "id": 91,
    "number": 45,
    "text":
      'Riding up on horses, a band of dirty, rough men quickly overtake and surround your group. They look hard and dangerous, and you immediately pull out your weapons as they approach.\n\nThen you hear a familiar laugh.\n\n"Well, if it isn\'t my old crew." A woman in dark leather armor leaps off her horse to comes greet you. "You know whatt boys? This lot gets a pass."\n\nShe winks at you and turns around. "Plus, they\'d probably kill you all if things turned ugly."\n\nJumping back onto her horse, the Scoundrel looks back at you. "Well, it was nice seeing you. Just remember — you never saw me."',
    "optionA": {
      "choice": 'Attack. Friend or not, those who prey on the weak should be brought to justice.',
      "outcome":
        'You see the bandits relax a little and begin to form up. That is when you strike. Some are scared off by the sudden attack, but others engage you hungrily. The Scoundrel throws a few good daggers, too, before she rides off, criticizing your poor decision-making.\n\nAll start scenario with {Poison}.\n\nAll start scenario with 2 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-45-b-a.png',
    },
    "optionB": {
      "choice": 'Let the bandits go.',
      "outcome":
        'The bandits seem a little disappointed as they form up and ride off in the opposite direction.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/road/re-45-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-45-f.png',
    "verified": False,
  },
  {
    "id": 93,
    "number": 46,
    "text":
      'Walking among the foothills, you see a steep ridge in front of you and on top of it, a very odd rock formation.\n\n The formation calls to you somehow, but the way up is not readily apparent. In fact, climbing the ridge looks pretty dangerous, but you just feel like you need to get up there and look at the rocks.',
    "optionA": {
      "choice": 'Take the risk to climb tbe ridge and investigate the rocks.',
      "outcome":
        'Fearing the possibility of falling from a great height, you choose your steps carefully. Still, the climb to the top takes a long time and is exhausting. Reaching the top, you approach the unnatural rock formation, a giant mound of stones stacked one on top of another. At the base of the bottom stone, you see the following etched with charcoal:\n\n{RuneT}{RuneH}{RuneE} {RuneR}{RuneU}{RuneI}{RuneN}{RuneS} {RuneO}{RuneF} {RuneT}{RuneH}{RuneE} {RuneD}{RuneE}{RuneE}{RuneP} {RuneT}{RuneA}{RuneK}{RuneE} {RuneS}{RuneH}{RuneA}{RuneP}{RuneE}',
      "imageUrl": '/assets/cards/events/base/road/re-46-b-a.png',
    },
    "optionB": {
      "choice": 'Forget about the rocks and continue on your journey.',
      "outcome":
        "You shake your head and move past the ridge. You have more important things to do than climb rocks. Still, you fed the pull of the site, even after it fades from view. You get the feeling that this won't be the last time you see it.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/road/re-46-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-46-f.png',
    "verified": False,
  },
  {
    "id": 94,
    "number": 47,
    "text":
      'A single Vermling jumps out of the brush at you, surprising you briefly. Within moments, though, you have your weapons out and pressed against his throat.\n\n"EEEEEEEeeeahh!" The Vermling drops his weapon and cowers. "No attack! My brothers in the bushes say you had stink of city-dwelling outcast on you. I wanted to be sure."\n\nThe Vermling waves his hands. "It\' s not bad! Just curious. Being stinky city-dwelling outcast is fine. Please, don\'t hurt me!"',
    "optionA": {
      "choice": 'Move on, leaving the strange Vermling in peace.',
      "outcome":
        '"Stink very faint," the Vermling continues as you walk on. "Outcast no longer with you, but I still smell it!"\n\nHe then jumps back into the brush. Vermlings are very odd creatures.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/road/re-47-b-a.png',
    },
    "optionB": {
      "choice": 'Kill the savage little beast.',
      "outcome":
        'You attack the Vermling anyway; despite his protests. It turns out he wasn\'t lying about his "brothers" nearby, though. As you wipe the blood from your blade, ten more of the little furry creatures jump out at you, brandishing small knives. They are not nearly as easy to dispatch.\n\nAll start scenario with {Poison}.\n\nAll start scenario with 2 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-47-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-47-f.png',
    "verified": False,
  },
  {
    "id": 96,
    "number": 48,
    "text":
      'You see them long before they get close to you — radiant balls of light blazing against the horizon.\n\nSun Demons.\n\nAs they approach, you prepare for an attack, but the demons have other plans. They menace you with their glowing claws, but they would rather have information than kill you.\n\n"Where is the one you call a Sunkeeper?" one of them hisses. "The Valrath neglects her duties, and now we must resolve matters personally."\n\nYou press for further information, but the demons get angry. "These are not your concerns! Tell us where she is or die at our hands!"',
    "optionA": {
      "choice": "Give them whatever information you can on the Sunkeeper's whereabouts.",
      "outcome":
        "You're not sure exactly what happened to the Sunkeeper after she left the party, but you tell the demons everything you know. They seem satisfied with your response and even offer a bitter thanks as they fly off to the west.\n\nAdd Road Event 61 to the deck.",
      "imageUrl": '/assets/cards/events/base/road/re-48-b-a.png',
    },
    "optionB": {
      "choice": 'Attack the demons. There are a lot of them, but you do not take kindly to threats.',
      "outcome":
        'Without even speaking, you draw your weapons and attack. The demons are caught off guard, but they bounce back with great ferocity. It is a long, brutal battle, and you continue on in your adventure greatly wounded and bloody.\n\nAll start scenario with {Muddle}.\n\nAll start scenario with {Wound}.\n\nAll start scenario with 3 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-48-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-48-f.png',
    "verified": False,
  },
  {
    "id": 98,
    "number": 49,
    "text":
      'You are approached on the road by a group of men on horseback. They don\'t immediately seem menacing, but they are formidable and well organized.\n\nOne of the men, who wears plate armor and has a sword at his side, addresses you coldly. "You hail from Gloomhaven, correct? What say you about the politics of the place? Are you for or against military rule in the region? Do you think those fool merchants could do a better job, like they\'re doing with the rest of this doomed land?"\n\nLooking closer, you see all the men wear the signet of a tower with an eye at its center',
    "optionA": {
      "choice": 'Claim allegiance to the military.',
      "outcome":
        'The armored men seem satisfied with your response and take their hands off their weapons.\n\n"Good to find some fellow patriots," the one in front says with a disturbing smile. "You know, we have a stronghold not far from here up in the mountains. Feel free to visit there if you ever get serious about your loyalties.\n\nUnlock "Vigil Keep" 80 (K-1).',
      "imageUrl": '/assets/cards/events/base/road/re-49-b-a.png',
    },
    "optionB": {
      "choice": 'Claim allegiance to the merchant guilds.',
      "outcome":
        'Well then, today\'s your unlucky day, the man in front says. "Because we of the Vigil make it a point to execute any and all commerce sympathizers we can find in this land."\n\nThe men grimly draw swords and advance. After a hard battle, the survivors retreat, leaving you to pick through the corpses. Among the loot you find a map.\n\nUnlock "Vigil Keep" 80 (K-1).\n\nAll start scenario with 4 damage.\n\nGain 5 gold each.',
      "imageUrl": '/assets/cards/events/base/road/re-49-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-49-f.png',
    "verified": False,
  },
  {
    "id": 100,
    "number": 50,
    "text":
      'Up ahead of you, you see a staff stuck in the very center of the road pointing straight up out of the ground. You get closer, and an odd sense of foreboding comes over you.\n\nYou recognize the staff as the one wielded by the Summoner. The fact that it is now in front of you with such a strange and ominous placement makes you very wary.\n\nYou quickly look around, but nothing else of note is in sight.',
    "optionA": {
      "choice": 'Take the staff and move on.',
      "outcome":
        'You shrug and grab the staff, half expecting something exciting to happen when you do. Instead, nothing happens at all. In fact, the staff seems rather mundane. You feel no power running through it at all. Still, no sense in leaving it behind. It could be important.\n\nAdd City Event 68 to the deck.',
      "imageUrl": '/assets/cards/events/base/road/re-50-b-a.png',
    },
    "optionB": {
      "choice": 'Investigate the area and get to the bottom of this.',
      "outcome":
        'You spend a good hour looking over the area, scouring every bush and divot you can find. Unfortunately, you find no other clues about what happened here and end up just tiring yourself out.\n\nDiscard 2 cards each.\n\nRead outcome A.',
      "imageUrl": '/assets/cards/events/base/road/re-50-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-50-f.png',
    "verified": False,
  },
  {
    "id": 102,
    "number": 51,
    "text":
      'You reach a crossroad and decide to rest for a bit. As you eat some of your rations, something sticking up out of the ground in the distance catches your attention.\n\nYou move closer, and what you thought was a signpost turns out to be a human skull impaled on a spike.\n\nThere is something sticking out of the skulls mouth.',
    "optionA": {
      "choice": 'Investigate further.',
      "outcome":
        'You get closer to the pike. The skull looks pretty fresh. There are still bits of decayed flesh attached to the bone, and flies buzz around it. You can see there is a small paper card stuck in its mouth so you carefully reach in and pull it out. The card is black and depicts a skull with blades running through it. Come to think of it you remember rumors of an assassins\' guild that has been known to use the same imagery You get out of the area as quickly as you can.\n\nGain 1 collective "Black Card" (Item 129).',
      "imageUrl": '/assets/cards/events/base/road/re-51-b-a.png',
    },
    "optionB": {
      "choice": 'Arm yourself and make a defensive retreat from the area.',
      "outcome":
        "You remember rumors of an assassins' guild that places a skull on a pike outside the houses of their victims before they strike. Fearing the worst, you pull out your weapons and survey the scene as you back away from the pike. Everything looks clear, so you quickly get as far away from the area as possible. Perhaps the skull was not meant for you.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/road/re-51-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-51-f.png',
    "verified": False,
  },
  {
    "id": 105,
    "number": 52,
    "text":
      'You smell the corpses before you see them. A group of five or so, spread across the road, flies buzzing around in a frenzy.\n\nAs you get closer, you see the wretched, deformed looks on their faces and the boils covering their skin. You also see their crude armor and weapons — likely a group of cutthroats.\n\nWhat is truly odd though, is that their weapons are out of their sheaths in the first place. It appears they were engaged in battle when they suddenly succumbed to some horrible disease.\n\nYou can think of at least one way that could have happened. Fine handiwork from the Plagueherald.',
    "optionA": {
      "choice": 'Leave the corpses alone.',
      "outcome":
        'Knowing better than to get too close to the machinations of the Plaguehcrald, you keep a wide berth between you and the corpses and continue down the road.\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/road/re-52-b-a.png',
    },
    "optionB": {
      "choice": 'Inspect the corpses for valuables.',
      "outcome":
        'You rifle through the corpses, grabbing stray coins and valuables as you go. You make off with a good haul, but you start feeling sick as soon as you re done.\n\nAll start scenario with {Poison}.\n\nAll start scenario with {Curse}.\n\nGain 10 collective gold.',
      "imageUrl": '/assets/cards/events/base/road/re-52-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-52-f.png',
    "verified": False,
  },
  {
    "id": 104,
    "number": 53,
    "text":
      "You hear the distinctive sound of metal on metal in the distance and race up a hill in the road to investigate.\n\nIn front of you, you see a familiar female Inox in heated battle with a group of Gloomhaven guards. Though outnumbered and bloodied, you've never seen that stop the Berserker before. With every wound they inflict, she becomes more and more enraged, cleaving off limbs with the ease of cutting grass.",
    "optionA": {
      "choice": 'Help the Berserker fight off the guards.',
      "outcome":
        "You enter the battle to aid the Berserker, but in her blood rage, she can't distinguish friend from foe. She begins hacking away at you with her axe as much as she swings at the guards. You concentrate on taking out the remaining guards, but when you turn back to the Berserker, she seems to have vanished into the nearby forest.\n\nAll start scenario with 3 damage.",
      "imageUrl": '/assets/cards/events/base/road/re-53-b-a.png',
    },
    "optionB": {
      "choice": "Wait and see what happens. It looks like she's handling herself well enough.",
      "outcome":
        'After a brutal and bloody fight, only the Berserker remains standing. After her blood rage subsides, she collapses from exhaustion. You race to her side and attempt to revive her using a number of powerful potions. She finally awakes and expresses her begrudging gratitude. You ask about the fight, but she just shakes her head. She offers her axe as thanks and then dashes off into the forest. Consume {SmallItem} item each.\n\nGain 1 collective "Bloody Axe" (Item 117).',
      "imageUrl": '/assets/cards/events/base/road/re-53-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-53-f.png',
    "verified": False,
  },
  {
    "id": 107,
    "number": 54,
    "text":
      'Deep inside a dense forest, you begin to hear the jangling of bells and see a small troupe of performers approaching you through the trees.\n\n"Well, look who it is!" The small voice belongs to a garishly dressed female Quatryl with a lute and a feathered hat. "Fancy running into you out here."\n\n"This actually may be a stroke of luck," the Soothsingcr says. "You see, my compatriots and I seem to be a bit lost. We were headed toward the Capital when my drummer said he knew a shortcut. Now here we are in the middle of a forest without an inkling of a clue. I don\'t suppose you could find it in your heart to escort us back to the main road, could you?"',
    "optionA": {
      "choice": 'Take the time to escort the troupe back out of the forest.',
      "outcome":
        'While escorting the Soothsinger and her troupe out of the forest, you are able to catch up a bit. She is very happy now as a traveling performer, playing to sold out concerts across the land. When you reach the main road, you say your good-byes and then make the long trek back to where you were going.\n\nGain 1 reputation.\n\nDiscard 2 cards each.',
      "imageUrl": '/assets/cards/events/base/road/re-54-b-a.png',
    },
    "optionB": {
      "choice": 'Give detailed directions about the way out and hope that is sufficient.',
      "outcome":
        '{LightningBolts} {TwoMinis} {PointyHead}: You gauge your bearings and then give precise directions on the easiest way out of the forest and back to the main road. The Soothsinger seems impressed and waves good-bye as she heads off.\n\nGain 1 reputation.\n\nOTHERWISE:You hem and haw and then give some vague directions back to the road. The Soothsinger looks at you skeptically and heads off.\n\nAdd City Event 69 to the deck.',
      "imageUrl": '/assets/cards/events/base/road/re-54-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-54-f.png',
    "verified": False,
  },
  {
    "id": 109,
    "number": 55,
    "text":
      'You come to a fork in the road. One path looks clear and easy, but the other path is overgrown with thorns and nettles. Either one will likely get you to where you are going.\n\nThe whole situation feels off, though — as if someone or something is watching you.\n\nStill a decision must be made.',
    "optionA": {
      "choice": 'Take the clear path.',
      "outcome":
        "You walk down the clear path for a few minutes, and, just when you think the whole weird feeling was your imagination, a group of human bandits jumps out at you from the nearby brush. Before they can engage, however, an arrow suddenly spears the chest of the closest bandit, followed very quickly by a second. The bandits have paused to look around in panic when a third arrow flies into another bandit's skull. The bandits scatter and run off. You look around for the shooter, but no trace is found.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/road/re-55-b-a.png',
    },
    "optionB": {
      "choice": 'Take the overgrown path.',
      "outcome":
        'The trek through the overgrown path is unpleasant. You are constantly getting pricked by sharp thorns covered in a strange sap. You think you recognize them from a previous foray into harsh, unforgiving foliage. Sure enough, you start feeling sick pretty soon after you emerge from the bushes.\n\nAll start scenario with {Poison}.',
      "imageUrl": '/assets/cards/events/base/road/re-55-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-55-f.png',
    "verified": False,
  },
  {
    "id": 113,
    "number": 56,
    "text":
      "At first the man looks dead, with numerous open wounds and lying in a pool of blood in the dirt/\n\nBut then he coughs and whispers something unintelligible. The man looks pretty bad off, likely attacked by some wild animal, but it's possible he could be saved.",
    "optionA": {
      "choice": 'Help the wounded man as best you can.',
      "outcome":
        "The man's wounds actually look worse than they really are, and your time with the Sawbones has given you some experience in what to do. You bind the wounds to stop the bleeding and then give him something to eat. He lost a lot of blood, but after some nursing, he's able to stand and make his way back to Gloomhaven, thanking you profusely in the process.\n\nGain 1 reputation.",
      "imageUrl": '/assets/cards/events/base/road/re-56-b-a.png',
    },
    "optionB": {
      "choice": 'Let the man die and take his belongings.',
      "outcome":
        "You riffle through the man's pockets as he speaks his last words. They're too soft to make out, but the tone is one of anger and disappointment. You make off with a decent amount of money and leave the corpse to rot.\n\nGain 3 gold each.",
      "imageUrl": '/assets/cards/events/base/road/re-56-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-56-f.png',
    "verified": False,
  },
  {
    "id": 117,
    "number": 57,
    "text":
      'You are wandering through an abysmal fog, cursing the very fact you woke up this morning. You can\'t see two feet in front of your face and everything is just so cold and damp.\n\nWalking down what you think is the road, you nearly bump into an elderly Savvas.\n\n"Ah, how fortuitous is such a meeting," the Savvas says. "You look like the ones whom my protégé worked with for some time. Normally I would not give the lesser races a second glance, but the master of elements must have seen something in you."\n\nIt stretches its joints and looks around. "Hmm, you must be having a rough time with this weather I could offer you something that may help."',
    "optionA": {
      "choice": 'Accept the gift of the Savvas.',
      "outcome":
        'The Savvas concentrates and lays its hand on you. You suddenly feel very warm and all the fog within ten feet of you dissipates.\n\n"There you go. That should make things easier. The effect should last for at least as long as the fog does. Have a pleasant day!"\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/road/re-57-b-a.png',
    },
    "optionB": {
      "choice": "Downplay your struggle and politely decline the Savvas's offer.",
      "outcome":
        'Ah, 1 see," the Savvas says. "You\'d rather grow from an experience than take the easy way out. A noble path."\n\nThe Savvas slaps you on the back. "Well, get to it, then! It\'s just fog after all. You\'ll survive."\n\nDiscard 2 cards each.\n\nAdd Road Event 63 to the deck.',
      "imageUrl": '/assets/cards/events/base/road/re-57-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-57-f.png',
    "verified": False,
  },
  {
    "id": 114,
    "number": 58,
    "text":
      "Despite your best efforts, you find yourself lost in a forest. You thought you were taking a shortcut, but then you got turned around and lost your bearings.\n\nAnd just when you think things couldn't get worse, a wolf suddenly jumps out of the brush in front of you. Oddly; though, it doesn't appear aggressive.\n\nIt howls once and then slowly and deliberately begins to walk through the trees in front of you, as if expecting you to follow it.",
    "optionA": {
      "choice": 'Follow the wolf.',
      "outcome":
        "Miraculously, following the wolf leads you right to the edge of the forest and back on track to your destination. The wolf howls once more and then bounds off back into the brush. You can't help, but wonder who might have sent that wolf to assist you.\n\nNo effect.",
      "imageUrl": '/assets/cards/events/base/road/re-58-b-a.png',
    },
    "optionB": {
      "choice": 'Find your own way through the forest.',
      "outcome":
        "Not willing to trust a wild animal, you refuse to go in the same direction as the wolf and continue down an ill-fated path of your own choosing. It doesn't go well, and by the time you emerge from the dense forest and find your bearings, you are exhausted.\n\nDiscard 3 cards each.",
      "imageUrl": '/assets/cards/events/base/road/re-58-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-58-f.png',
    "verified": False,
  },
  {
    "id": 116,
    "number": 59,
    "text":
      "The air is especially humid and muggy as you walk towards your destination, but even that couldn't explain the sight that greets you on the road.\n\nDirectly in front of you, completely blocking the only available path, is a massive swarm of insects. There must be millions of them.\n\nYou take a hesitant step forward and the bugs do not react. They are not concerned by your presence at all.",
    "optionA": {
      "choice": 'Cover yourself as best you can and try to walk through the swarm.',
      "outcome":
        'If you were to list the top ten worst moments of your fife, this would probably be up there. You walk into the swarm and the insects are everywhere, biting and clawing at your flesh. You move as quickly as you can, emerging from the other side with your life intact but your sanity in shambles. Oddly, though, you also feel as though you were just in the presence of a powerful, divine force.\n\nAll start scenario with 2 damage.\n\nAll start scenario with {Poison}, {Muddle}, and {Bless}.',
      "imageUrl": '/assets/cards/events/base/road/re-59-b-a.png',
    },
    "optionB": {
      "choice": 'Use whatever you can to burn a path through the swarm.',
      "outcome":
        'It takes a monumental effort, but you are eventually able to disperse the cloud of insects enough to run through to the other side. As you do so, however. you hear an odd voice among the buzzing, cursing you for your violent actions.\n\nDiscard 2 cards each.\n\nAll start scenario with {Curse}.',
      "imageUrl": '/assets/cards/events/base/road/re-59-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-59-f.png',
    "verified": False,
  },
  {
    "id": 118,
    "number": 60,
    "text":
      "You see smoke on the horizon expecting the worst and sigh, expecting the worst. Sure enough, you approach the scene to find a ransacked caravan — burned, pillaged, and destroyed by what appears to be Vermlings.\n\nYou find one survivor among the victims who laments that when the Vermlings came upon them, one of the guards, a large Inox, seemed to throw aside his weapon and simply accept his fate.\n\nThat's when you find the body of the Brute, torn and bloody among the wreckage. Seeing him this way, the fire gone from his eyes, he appears unnaturally small.",
    "optionA": {
      "choice": 'Respectfully bury the dead and mourn their loss.',
      "outcome":
        "Though you didn't take the time to talk with the Brute earlier, now you take the time to bury his corpse and say a few words about his strength of body and character. The survivor thanks you for your help, and you continue on your way once more.\n\nGain 1 reputation.",
      "imageUrl": '/assets/cards/events/base/road/re-60-b-a.png',
    },
    "optionB": {
      "choice": 'Take what you can find and move on.',
      "outcome":
        'Near the corpse of the Brute, you find an axe, presumably the weapon he threw away. There\'s really nothing else among the debris, so you wordlessly pick it up and move on.\n\nGain 1 collective "Battle-Axe" (Item 018).',
      "imageUrl": '/assets/cards/events/base/road/re-60-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-60-f.png',
    "verified": False,
  },
  {
    "id": 121,
    "number": 61,
    "text":
      'You are heading through a small forest when you hear the sound of a woman screaming off to the west. You silently move closer, catching a glimpse of multiple radiant figures through the tress.\n\nThey are Sun Demons, perhaps the same ones who accosted you earlier. That suspicion is confirmed when you get closer and see they are hovering around an armored Valrath woman bound to a tree, torturing her for information.\n\n"Don\'t you see how important this is!" one of the demons says. "Give us the location of the temple!"\n\n"Lies and tricks of a demon," the Sunkeeper responds. "The temple is in no danger except from you."',
    "optionA": {
      "choice": 'Leave the scene quietly and return to your own business.',
      "outcome":
        'Not wanting to get involved, you simply move on. Eventually the screams of the Sunkeeper fade away.\n\nAdd Road Event 62 to the deck.',
      "imageUrl": '/assets/cards/events/base/road/re-61-b-a.png',
    },
    "optionB": {
      "choice": 'Attack the demons and free the Sunkeeper.',
      "outcome":
        'You charge out of the trees and attack the Sun Demons. Fueled by righteous indignation and a bit of guilt, you slay them all. The battle leaves you wounded, but the Sunkeeper happily mends your wounds once you free her.\n\n"They seemed to think the Sun Temple is under attack by Night Demons," she says. "I have no reason to believe them, but still, would you mind helping me look into it?"\n\nUnlock "Sun Temple" 85 (M-3)',
      "imageUrl": '/assets/cards/events/base/road/re-61-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-61-f.png',
    "verified": False,
  },
  {
    "id": 123,
    "number": 62,
    "text":
      'By now, the Sun Demons cut a very recognizable portrait against the horizon as they move toward you. You sincerely had hoped you were done with these creatures.\n\n"We have urgent need of your assistance," one of them starts. "Night Demons have infested the Sun Temple, attempting to desecrate it and send the world into eternal darkness.\n\n"We have tried to stop them, but they are too fortified inside the temple. We regrettably need more strength.\n\n"Please, you cannot want an absence of a sun on this plane any less than we do. It would be disastrous."',
    "optionA": {
      "choice": 'Agree to help the Sun Demons.',
      "outcome":
        'You sigh and agree, warning them that this had better be the last time they ask you for a favor. They give you the location of the Sun Temple and implore you to hurry.\n\nUnlock "Sun Temple" 85 (M-3).',
      "imageUrl": '/assets/cards/events/base/road/re-62-b-a.png',
    },
    "optionB": {
      "choice": 'Attack the Sun Demons. It may be the only way to stop them from bothering you.',
      "outcome":
        'Without even speaking, you draw your weapons and attack. The demons are caught off guard, but they bounce back with great ferocity. It is a long, brutal battle, and you continue on in your adventure greatly wounded and bloody.\n\nAll start scenario with {Muddle}.\n\nAll start scenario with {Wound}.\n\nAll start scenario with 3 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-62-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-62-f.png',
    "verified": False,
  },
  {
    "id": 128,
    "number": 63,
    "text":
      'As you walk through some foothills, the ground suddenly shakes violently beneath you. Two massive demons built of earth and stone rise up in front of you.\n\n"Today we shall feast on your flesh, foolish travelers!"\n\nJust as the demons take a step toward you, a massive ball of fire streaks through the air from behind and connects squarely with one of the demons, which erupts into a pillar of flame. Then lightning streaks toward the other, destroying one of its arms.\n\nLooking around, you see the old Savvas you met earlier, who continues to throw out powerful attacks until the demons are forced to retreat.\n\n"Well, fancy meeting you again!"',
    "optionA": {
      "choice": 'Thank the Savvas for his timely assistance.',
      "outcome":
        '"More and more demons around these parts these days. Stopping them from attacking travelers is becoming a time-intensive job, but at least it\'s fun."\n\nThe Savvas smiles at you and then turns to leave. "Have a pleasant day!"\n\nNo effect.',
      "imageUrl": '/assets/cards/events/base/road/re-63-b-a.png',
    },
    "optionB": {
      "choice": 'Admonish the Savvas, claiming you could have handled the demons without his help.',
      "outcome":
        'The Savvas adopts a look of serious contemplation. "You are right, of course. I presumed to think that a lesser race would need my help, but I forgot your dedication to growth and learning. I have made a grave mistake and must now beg your forgiveness."\n\nIt holds out a small trinket toward you. "Please, accept this with my apologies."\n\nGain 1 collective "Sun Earring" (Item 049).',
      "imageUrl": '/assets/cards/events/base/road/re-63-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-63-f.png',
    "verified": False,
  },
  {
    "id": 126,
    "number": 64,
    "text":
      'You reach a crossroads and deecide to rest for a bit. As you eat some of your rations, something sticking up out of the ground in the distance catches your attention.\n\nYou move closer, and what you thought was a signpost turns out to be a human skull impaled on a spike.\n\nThere is something sticking out of the skulls mouth.',
    "optionA": {
      "choice": 'Investigate further.',
      "outcome":
        "Against your better judgment, you approach the skull, which looks suspiciously like the Sin-Ras calling card. Sure enough, a group of dark-clad warriors appears before you from out of thin air. Wordlessly they draw their long, curved blades and attack. Caught by surprise, you don't fare well in the battle. You do fight them off, but in the end, you are severely wounded, exhausted, and demoralized.\n\nLose 1 {Check} each.\n\nDiscard 4 cards each.\n\nAll start scenario with 4 damage.",
      "imageUrl": '/assets/cards/events/base/road/re-64-b-a.png',
    },
    "optionB": {
      "choice": 'Arm yourself and make a defensive retreat from the area.',
      "outcome":
        "Recognizing the pike as a symbol of the Sin-Ra Syndicate, you arm yourself and run from the area. Unfortunately you don't make it far before you see a number of black-clad assassins bearing down on you. You move into a defensive position and prepare for battle. The fight is arduous, but in the end, the assassins are dead, and you hope they don t come back.\n\nLose 1 {Check} each.\n\nDiscard 2 cards each.\n\nAll start scenario with 2 damage.",
      "imageUrl": '/assets/cards/events/base/road/re-64-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-64-f.png',
    "verified": False,
  },
  {
    "id": 130,
    "number": 65,
    "text":
      "As you crest a hill, you see a flock of carrion birds scatter to the east. They must have been feasting on something, so you decide to investigate.\n\nAfter a short walk, you come upon a man's corpse, badly decayed and mangled, lying in the dirt. His face is a bloody mess, but you do see a distinctive chain around his neck and recall the description the man from the Sleeping Lion gave you of his brother. This is very likely him.",
    "optionA": {
      "choice": 'Bury the man and bring the chain back to his brother.',
      "outcome":
        'Not wanting to tell the brother that you left the corpse out in the sun to rot, you take the time to dig a hole and give it a proper burial.\n\nWhen you bring the chain back, the brother is understandably distraught, but he thanks you forgiving him closure about what happened.\n\nGain 2 reputation.',
      "imageUrl": '/assets/cards/events/base/road/re-65-b-a.png',
    },
    "optionB": {
      "choice": "Take the chain for yourself and don't tell the brother.",
      "outcome":
        'The birds get the corpse. You get the chain. Everyone wins, except the man from the Sleeping Lion. But he should know better than to trust mercenaries.\n\nGain 3 gold each.',
      "imageUrl": '/assets/cards/events/base/road/re-65-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-65-f.png',
    "verified": False,
  },
  {
    "id": 138,
    "number": 66,
    "text":
      'The first sign of the Inox raiding party was a cloud of dust on the horizon. It was so large, however, there was nowhere to run.\n\n"City-dwelling scum!" one of the Inox in front calls out to you as you approach. "We march now to attack your city and wipe it from the face of this land. What do you say to that?"\n\nYour first thought, as you prepare for a fight, is that they will need a larger army. Before you can strike, though, the sky grows dark. You assume it is a cloud, but then look up to see a giant drake descending on you from above.',
    "optionA": {
      "choice": 'Take cover.',
      "outcome":
        'You jump into a ditch and cover your head just as the Elder Drake glides over the raiding party, breathing a heavy gout of flame into their midst. Those not incinerated scream and flee for their lives. The drake lands in front of you.\n\n"Intrepid adventurers! I hope I was able to offer you some aid against your aggressors. It really was my pleasure after all you have done for me. I hope you find some things of value among the corpses. It is my gift to you."\n\nGain 25 gold each.',
      "imageUrl": '/assets/cards/events/base/road/re-66-b-a.png',
    },
    "optionB": {
      "choice": 'Attack the Inox.',
      "outcome":
        'You attack the large group of Inox while they are distracted by the giant creature above you. Things suddenly get very hot, however, when the drake begins spitting fire into the melee. The Inox scatter and you are suffering from severe burns when the Elder Drake lands in front of you.\n\n"My apologies, I was only trying to help."\n\nGain 25 gold each.\n\nAll start scenario with {Wound}.\n\nAll start scenario with 2 damage.',
      "imageUrl": '/assets/cards/events/base/road/re-66-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-66-f.png',
    "verified": False,
  },
  {
    "id": 132,
    "number": 67,
    "text":
      'Not too far down the main road outside of Gloomhaven, you run across a merchant wagon headed into town.\n\n"Ah, I was afraid for a second you might be bandits!" The merchant says. "But now I see you are mercenaries from the town, correct? Most excellent! I have heard good things about the mercenaries of Gloomhaven. Hard to believe, coming from such a backwater place, but they are true, correct?"',
    "optionA": {
      "choice": 'Demonstrate your virtue by offering to escort the merchant back to Gloomhaven.',
      "outcome":
        '"Ah, well...no, I don\'t want to be a bother. But, I mean, yes, I can\'t pay you, though I\'d love the company. It is rather terrifying traveling the East Road by yourself."\n\nIt is a relatively short journey back to town, but the merchant is very grateful. "I am quite impressed, sirs. I\'II be sure to tell everyone back in the capital that Gloomhaven is a safe place to do business."\n\nGain 1 prosperity.',
      "imageUrl": '/assets/cards/events/base/road/re-67-b-a.png',
    },
    "optionB": {
      "choice": 'Demonstrate your lack of virtue by robbing the merchant.',
      "outcome":
        '"Well I just — I mean, I\'d never..." the merchant trails of incredulously. "To think there are places in the world where such barbarism still exists. It boggles the mind.\n\n I\'m going to tell everyone back in the Capital what a horrible, backward shrrggggllg..." Blood bubbles up into his mouth as you slit his throat, making it very difficult for him to continue complaining.\n\nGain 20 gold each.',
      "imageUrl": '/assets/cards/events/base/road/re-67-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-67-f.png',
    "verified": False,
  },
  {
    "id": 135,
    "number": 68,
    "text":
      'Not too far down the main road outside of Gloomhaven, you run across a merchant wagon headed into town.\n\n"Oh no...ah, mercenaries, I see," the merchant stammers as you approach, "Look, ah, I know the reputation of your like around Gloomhaven. Please, just take what you want and move on. I-I don t want any trouble."',
    "optionA": {
      "choice": 'Take what you want and move on.',
      "outcome":
        "The merchant remains dead silent as you sift through his cart and pull out any valuables. There's not a whole lot in his wares, but the ease in which you are able to take what he has makes it all the sweeter.\n\nOnce you are finished, you continue on your way and he continues on his.\n\nGain 10 gold each.",
      "imageUrl": '/assets/cards/events/base/road/re-68-b-a.png',
    },
    "optionB": {
      "choice": 'Calm the merchant and explain that not all mercenaries are bloodthirsty thieves.',
      "outcome":
        '"Oh, ah, really?" The merchant looks at you incredulously. "Well then, color me embarrassed. I sincerely apologize for my uneducated assumptions. Sometimes you just expect the worst traveling to such backwater locales.\n\n"I\'ll be sure to tell everyone I see that not everyone in Gloomhaven is a criminal," he says as he rides off, tipping his hat to you.\n\nGain 2 reputation.',
      "imageUrl": '/assets/cards/events/base/road/re-68-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-68-f.png',
    "verified": False,
  },
  {
    "id": 137,
    "number": 69,
    "text":
      'Walking along the trail, you are surprised by a group of demons who appear to your left, charging over a hill toward you. Something is off, however. Their pace is slow, and they are significantly smaller than the demons you normally deal with.\n\nHalfway down the hill, the demons pause and take stock of you. Seeing you are far from easy prey, they turn around and begin to retreat.',
    "optionA": {
      "choice": 'Chase them down quickly and kill them.',
      "outcome":
        'You roar and charge up the hill. The demons are no match for you, either in speed or in strength. You kill them quickly, but painfully.\n\nGain 5 experience each.',
      "imageUrl": '/assets/cards/events/base/road/re-69-b-a.png',
    },
    "optionB": {
      "choice": 'Follow them more slowly, attempting to discover where they came from.',
      "outcome":
        'You creep slowly to the crest of the hill, watching as the demons retreat to the south. You follow them, eventually arriving at a weak, fluctuating rift in a small, earthen cave. Having experienced enough planar manipulation in your travels, you are able to mutter a few incantations and close the rift. It takes a lot out of you, but now there is one less way for demons to invade this plane.\n\nLose 1 {Check} each.\n\nGain 1 prosperity.',
      "imageUrl": '/assets/cards/events/base/road/re-69-b-b.png',
    },
    "imageUrl": '/assets/cards/events/base/road/re-69-f.png',
    "verified": False,
  },
]