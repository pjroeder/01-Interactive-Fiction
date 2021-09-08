#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "BFBC52C0-E1D5-437F-888D-86CF05D51989",
  "name": "Interactive Fiction",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631064306838,
  "passages": [
    {
      "name": "HUNTER'S GUILD",
      "tags": "",
      "id": "1",
      "text": "You have joined a Bounty Hunting Guild named Crimson Dust. There are three options of bounties to choose from.\nLeutwin Oleg, Lian Geoffrey, Rakesh Eula\n\n[[LEUTWIN OLEG]]\n[[LIAN GEOFFREY]]\n[[RAKESH EULA]]",
      "links": [
        {
          "linkText": "LEUTWIN OLEG",
          "passageName": "LEUTWIN OLEG",
          "original": "[[LEUTWIN OLEG]]"
        },
        {
          "linkText": "LIAN GEOFFREY",
          "passageName": "LIAN GEOFFREY",
          "original": "[[LIAN GEOFFREY]]"
        },
        {
          "linkText": "RAKESH EULA",
          "passageName": "RAKESH EULA",
          "original": "[[RAKESH EULA]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have joined a Bounty Hunting Guild named Crimson Dust. There are three options of bounties to choose from.\nLeutwin Oleg, Lian Geoffrey, Rakesh Eula"
    },
    {
      "name": "LEUTWIN OLEG",
      "tags": "",
      "id": "2",
      "text": "Leutwin Oleg is wanted for Thievery on 17 accounts, Dead or Alive. This bounty is worth 500 Gold. They were last seen near the town of Yarrin.\nYou can go to Yarrin or choose a different bounty.\n\n[[YARRIN]]\n[[RAKESH EULA]] \n[[LIAN GEOFFREY]]",
      "links": [
        {
          "linkText": "YARRIN",
          "passageName": "YARRIN",
          "original": "[[YARRIN]]"
        },
        {
          "linkText": "RAKESH EULA",
          "passageName": "RAKESH EULA",
          "original": "[[RAKESH EULA]]"
        },
        {
          "linkText": "LIAN GEOFFREY",
          "passageName": "LIAN GEOFFREY",
          "original": "[[LIAN GEOFFREY]]"
        }
      ],
      "hooks": [],
      "cleanText": "Leutwin Oleg is wanted for Thievery on 17 accounts, Dead or Alive. This bounty is worth 500 Gold. They were last seen near the town of Yarrin.\nYou can go to Yarrin or choose a different bounty."
    },
    {
      "name": "LIAN GEOFFREY",
      "tags": "",
      "id": "3",
      "text": "Lian Geoffrey is wanted for being an alleged acomplice in murder, Dead or Alive. This bounty is worth 500 gold. They were last seen near the town of Arkaley.\nYou can go to Arkaley or choose a different bounty.\n\n[[RAKESH EULA]] \n[[LEUTWIN OLEG]] \n[[ARKALEY]]",
      "links": [
        {
          "linkText": "RAKESH EULA",
          "passageName": "RAKESH EULA",
          "original": "[[RAKESH EULA]]"
        },
        {
          "linkText": "LEUTWIN OLEG",
          "passageName": "LEUTWIN OLEG",
          "original": "[[LEUTWIN OLEG]]"
        },
        {
          "linkText": "ARKALEY",
          "passageName": "ARKALEY",
          "original": "[[ARKALEY]]"
        }
      ],
      "hooks": [],
      "cleanText": "Lian Geoffrey is wanted for being an alleged acomplice in murder, Dead or Alive. This bounty is worth 500 gold. They were last seen near the town of Arkaley.\nYou can go to Arkaley or choose a different bounty."
    },
    {
      "name": "RAKESH EULA",
      "tags": "",
      "id": "4",
      "text": "Rakesh Eula is wanted for Forgery, Dead or Alive. This bounty is worth 500 gold. They were last seen near the town of Padstow.\nYou can go to Padstown or choose a different bounty.\n\n[[LEUTWIN OLEG]] \n[[LIAN GEOFFREY]] \n[[PADSTOWN]]",
      "links": [
        {
          "linkText": "LEUTWIN OLEG",
          "passageName": "LEUTWIN OLEG",
          "original": "[[LEUTWIN OLEG]]"
        },
        {
          "linkText": "LIAN GEOFFREY",
          "passageName": "LIAN GEOFFREY",
          "original": "[[LIAN GEOFFREY]]"
        },
        {
          "linkText": "PADSTOWN",
          "passageName": "PADSTOWN",
          "original": "[[PADSTOWN]]"
        }
      ],
      "hooks": [],
      "cleanText": "Rakesh Eula is wanted for Forgery, Dead or Alive. This bounty is worth 500 gold. They were last seen near the town of Padstow.\nYou can go to Padstown or choose a different bounty."
    },
    {
      "name": "YARRIN",
      "tags": "",
      "id": "5",
      "text": "You arrive in the town of Yarrin. It is a small town near the border, known for being the town of thieves. You see two people, a shady man dressed in dark clothes, and a older woman in a rocking chair knitting.\nWho do you talk to?\n\n[[SHADY MAN]]\n[[OLD WOMAN]]",
      "links": [
        {
          "linkText": "SHADY MAN",
          "passageName": "SHADY MAN",
          "original": "[[SHADY MAN]]"
        },
        {
          "linkText": "OLD WOMAN",
          "passageName": "OLD WOMAN",
          "original": "[[OLD WOMAN]]"
        }
      ],
      "hooks": [],
      "cleanText": "You arrive in the town of Yarrin. It is a small town near the border, known for being the town of thieves. You see two people, a shady man dressed in dark clothes, and a older woman in a rocking chair knitting.\nWho do you talk to?"
    },
    {
      "name": "ARKALEY",
      "tags": "",
      "id": "6",
      "text": "You arrive in Arkaley, a port town in the eastern region. You see two places of intrest, the Tavern or the Inn.\n\n[[TAVERN]]\n[[INN]]",
      "links": [
        {
          "linkText": "TAVERN",
          "passageName": "TAVERN",
          "original": "[[TAVERN]]"
        },
        {
          "linkText": "INN",
          "passageName": "INN",
          "original": "[[INN]]"
        }
      ],
      "hooks": [],
      "cleanText": "You arrive in Arkaley, a port town in the eastern region. You see two places of intrest, the Tavern or the Inn."
    },
    {
      "name": "PADSTOWN",
      "tags": "",
      "id": "7",
      "text": "You arrive at Padstown, a large city in the northern region. You see a fight break out infront of a store nearby. You see it is between the store owner and a young person. Do you want to watch or intervene?\n\n[[WATCH]]\n[[INTERVENE]]",
      "links": [
        {
          "linkText": "WATCH",
          "passageName": "WATCH",
          "original": "[[WATCH]]"
        },
        {
          "linkText": "INTERVENE",
          "passageName": "INTERVENE",
          "original": "[[INTERVENE]]"
        }
      ],
      "hooks": [],
      "cleanText": "You arrive at Padstown, a large city in the northern region. You see a fight break out infront of a store nearby. You see it is between the store owner and a young person. Do you want to watch or intervene?"
    },
    {
      "name": "SHADY MAN",
      "tags": "",
      "id": "8",
      "text": "The shady man says that he can lead you to Leutwin Oleg, in the nearby forest.\nDo you go to the forest or talk to the Old woman?\n[[FOREST]]\n[[OLD WOMAN]]",
      "links": [
        {
          "linkText": "FOREST",
          "passageName": "FOREST",
          "original": "[[FOREST]]"
        },
        {
          "linkText": "OLD WOMAN",
          "passageName": "OLD WOMAN",
          "original": "[[OLD WOMAN]]"
        }
      ],
      "hooks": [],
      "cleanText": "The shady man says that he can lead you to Leutwin Oleg, in the nearby forest.\nDo you go to the forest or talk to the Old woman?"
    },
    {
      "name": "OLD WOMAN",
      "tags": "",
      "id": "9",
      "text": "The Old Woman says that Leutwin Oleg is her grandson. She would prefer that Leutwin Oleg remains alive. The shady man watches you from the corner of his eye.\n\n[[SHADY MAN]]",
      "links": [
        {
          "linkText": "SHADY MAN",
          "passageName": "SHADY MAN",
          "original": "[[SHADY MAN]]"
        }
      ],
      "hooks": [],
      "cleanText": "The Old Woman says that Leutwin Oleg is her grandson. She would prefer that Leutwin Oleg remains alive. The shady man watches you from the corner of his eye."
    },
    {
      "name": "FOREST",
      "tags": "",
      "id": "10",
      "text": "The Shady Man leads you into a clearing in the Forest. You lose the Shady Man as he seems to disapear from sight. He reapears behind you and says that he is Leutwin Oleg and that you have made a huge mistake. Do you want to Flee or Fight?\n\n[[FLEE]]\n[[FIGHT]]",
      "links": [
        {
          "linkText": "FLEE",
          "passageName": "FLEE",
          "original": "[[FLEE]]"
        },
        {
          "linkText": "FIGHT",
          "passageName": "FIGHT",
          "original": "[[FIGHT]]"
        }
      ],
      "hooks": [],
      "cleanText": "The Shady Man leads you into a clearing in the Forest. You lose the Shady Man as he seems to disapear from sight. He reapears behind you and says that he is Leutwin Oleg and that you have made a huge mistake. Do you want to Flee or Fight?"
    },
    {
      "name": "FIGHT",
      "tags": "",
      "id": "11",
      "text": "You fight back against Leutwin Oleg. You are able to pin him down. Do you take him Dead or Alive? Or do you refuse to take them in?\n\n[[DEAD]]\n[[ALIVE]]\n[[REFUSE]]",
      "links": [
        {
          "linkText": "DEAD",
          "passageName": "DEAD",
          "original": "[[DEAD]]"
        },
        {
          "linkText": "ALIVE",
          "passageName": "ALIVE",
          "original": "[[ALIVE]]"
        },
        {
          "linkText": "REFUSE",
          "passageName": "REFUSE",
          "original": "[[REFUSE]]"
        }
      ],
      "hooks": [],
      "cleanText": "You fight back against Leutwin Oleg. You are able to pin him down. Do you take him Dead or Alive? Or do you refuse to take them in?"
    },
    {
      "name": "FLEE",
      "tags": "",
      "id": "12",
      "text": "You attempt to flee but Leutwin Oleg stops you. You are Dead.\nReturn to the Forest to try again.\n[[FOREST]]",
      "links": [
        {
          "linkText": "FOREST",
          "passageName": "FOREST",
          "original": "[[FOREST]]"
        }
      ],
      "hooks": [],
      "cleanText": "You attempt to flee but Leutwin Oleg stops you. You are Dead.\nReturn to the Forest to try again."
    },
    {
      "name": "DEAD",
      "tags": "",
      "id": "13",
	  "score":500,
      "text": "You kill your target and bring them back to the guild.\nCongratulations!\nTo play again type \"Hunter's Guild\"\nTo stop playing type \"quit\"\n\n[[HUNTER'S GUILD]]",
      "links": [
        {
          "linkText": "HUNTER'S GUILD",
          "passageName": "HUNTER'S GUILD",
          "original": "[[HUNTER'S GUILD]]"
        }
      ],
      "hooks": [],
      "cleanText": "You kill your target and bring them back to the guild.\nCongratulations!\nTo play again type \"Hunter's Guild\"\nTo stop playing type \"quit\""
    },
    {
      "name": "ALIVE",
      "tags": "",
      "id": "14",
	  "score":500,
      "text": "You bring your target back to the guild Alive.\nCongratulations!\nTo play again type \"Hunter's Guild\"\nTo stop playing type \"quit\"\n\n[[HUNTER'S GUILD]]",
      "links": [
        {
          "linkText": "HUNTER'S GUILD",
          "passageName": "HUNTER'S GUILD",
          "original": "[[HUNTER'S GUILD]]"
        }
      ],
      "hooks": [],
      "cleanText": "You bring your target back to the guild Alive.\nCongratulations!\nTo play again type \"Hunter's Guild\"\nTo stop playing type \"quit\""
    },
    {
      "name": "TAVERN",
      "tags": "",
      "id": "15",
      "text": "You enter the small Tavern and speak to the bar keep. They tell you that they have heard rumors of Lian Geoffrey being somewhere in town. They tell you to check out the Inn. \n\n[[INN]]",
      "links": [
        {
          "linkText": "INN",
          "passageName": "INN",
          "original": "[[INN]]"
        }
      ],
      "hooks": [],
      "cleanText": "You enter the small Tavern and speak to the bar keep. They tell you that they have heard rumors of Lian Geoffrey being somewhere in town. They tell you to check out the Inn."
    },
    {
      "name": "INN",
      "tags": "",
      "id": "16",
      "text": "You enter the Arkaley Inn. It seems very welcoming and comfortable. The Inn keeper tells you that Lian Geoffrey had just checked out of his room the night before. They believe that Lian Geoffrey is on the way towards a settlement to the west. They recomend checking the stables for a rental horse to help you get there, or you can go on foot and risk losing him.\n\n[[STABLES]] \n[[SETTLEMENT]]",
      "links": [
        {
          "linkText": "STABLES",
          "passageName": "STABLES",
          "original": "[[STABLES]]"
        },
        {
          "linkText": "SETTLEMENT",
          "passageName": "SETTLEMENT",
          "original": "[[SETTLEMENT]]"
        }
      ],
      "hooks": [],
      "cleanText": "You enter the Arkaley Inn. It seems very welcoming and comfortable. The Inn keeper tells you that Lian Geoffrey had just checked out of his room the night before. They believe that Lian Geoffrey is on the way towards a settlement to the west. They recomend checking the stables for a rental horse to help you get there, or you can go on foot and risk losing him."
    },
    {
      "name": "STABLES",
      "tags": "",
      "id": "17",
      "text": "You enter the Stables and see three different Horses. A small and Skinny Horse that seems to be on the edge of starvation,  large and muscular War Horse, and a lean but strong Race Horse. Which do you choose?\n\n[[SKINNY HORSE]]\n[[WAR HORSE]]\n[[RACE HORSE]]",
      "links": [
        {
          "linkText": "SKINNY HORSE",
          "passageName": "SKINNY HORSE",
          "original": "[[SKINNY HORSE]]"
        },
        {
          "linkText": "WAR HORSE",
          "passageName": "WAR HORSE",
          "original": "[[WAR HORSE]]"
        },
        {
          "linkText": "RACE HORSE",
          "passageName": "RACE HORSE",
          "original": "[[RACE HORSE]]"
        }
      ],
      "hooks": [],
      "cleanText": "You enter the Stables and see three different Horses. A small and Skinny Horse that seems to be on the edge of starvation,  large and muscular War Horse, and a lean but strong Race Horse. Which do you choose?"
    },
    {
      "name": "SETTLEMENT",
      "tags": "",
      "id": "18",
      "text": "You arrive at the Settlement. There are a few tents set up with a campfire in between them. You ask around and find Lian Geoffrey. You should confront him.\n\n[[CONFRONT]]",
      "links": [
        {
          "linkText": "CONFRONT",
          "passageName": "CONFRONT",
          "original": "[[CONFRONT]]"
        }
      ],
      "hooks": [],
      "cleanText": "You arrive at the Settlement. There are a few tents set up with a campfire in between them. You ask around and find Lian Geoffrey. You should confront him."
    },
    {
      "name": "SKINNY HORSE",
      "tags": "",
      "id": "19",
      "text": "You chose the Skinny Horse who appears to be on the edge of starvation. You are able to make it half way to the settlement before the horse collapses. \nContinue to the settlement.\n\n[[SETTLEMENT]]",
      "links": [
        {
          "linkText": "SETTLEMENT",
          "passageName": "SETTLEMENT",
          "original": "[[SETTLEMENT]]"
        }
      ],
      "hooks": [],
      "cleanText": "You chose the Skinny Horse who appears to be on the edge of starvation. You are able to make it half way to the settlement before the horse collapses. \nContinue to the settlement."
    },
    {
      "name": "WAR HORSE",
      "tags": "",
      "id": "20",
      "text": "You chose the large and muscular War Horse. You should be able to reach the settlement in a good amount of time.\ncontinue to the settlement.\n\n[[SETTLEMENT]]",
      "links": [
        {
          "linkText": "SETTLEMENT",
          "passageName": "SETTLEMENT",
          "original": "[[SETTLEMENT]]"
        }
      ],
      "hooks": [],
      "cleanText": "You chose the large and muscular War Horse. You should be able to reach the settlement in a good amount of time.\ncontinue to the settlement."
    },
    {
      "name": "RACE HORSE",
      "tags": "",
      "id": "21",
      "text": "You chose the lean but strong Race Horse. You are able to catch up to Lian Geoffrey before he reaches the settlement. You should confront them.\n\n[[CONFRONT]]",
      "links": [
        {
          "linkText": "CONFRONT",
          "passageName": "CONFRONT",
          "original": "[[CONFRONT]]"
        }
      ],
      "hooks": [],
      "cleanText": "You chose the lean but strong Race Horse. You are able to catch up to Lian Geoffrey before he reaches the settlement. You should confront them."
    },
    {
      "name": "CONFRONT",
      "tags": "",
      "id": "22",
      "text": "You confront Lian Geoffrey. He tells you that he had no part in the murder and that he was just working in the store that the crime scene was located. They plead for your mercy.\nDo you take them Dead or Alive? Or do you refuse to take them in?\n[[DEAD]] \n[[ALIVE]] \n[[REFUSE]]",
      "links": [
        {
          "linkText": "DEAD",
          "passageName": "DEAD",
          "original": "[[DEAD]]"
        },
        {
          "linkText": "ALIVE",
          "passageName": "ALIVE",
          "original": "[[ALIVE]]"
        },
        {
          "linkText": "REFUSE",
          "passageName": "REFUSE",
          "original": "[[REFUSE]]"
        }
      ],
      "hooks": [],
      "cleanText": "You confront Lian Geoffrey. He tells you that he had no part in the murder and that he was just working in the store that the crime scene was located. They plead for your mercy.\nDo you take them Dead or Alive? Or do you refuse to take them in?"
    },
    {
      "name": "WATCH",
      "tags": "",
      "id": "23",
      "text": "You watch the fight play out. It is very one sided. The young person is knocked down on the ground, and the store owner walks off telling the young person to never come back to the store. Who do you want to talk to?\n\n[[YOUNG PERSON]]\n[[STORE OWNER]]",
      "links": [
        {
          "linkText": "YOUNG PERSON",
          "passageName": "YOUNG PERSON",
          "original": "[[YOUNG PERSON]]"
        },
        {
          "linkText": "STORE OWNER",
          "passageName": "STORE OWNER",
          "original": "[[STORE OWNER]]"
        }
      ],
      "hooks": [],
      "cleanText": "You watch the fight play out. It is very one sided. The young person is knocked down on the ground, and the store owner walks off telling the young person to never come back to the store. Who do you want to talk to?"
    },
    {
      "name": "INTERVENE",
      "tags": "",
      "id": "24",
      "text": "You break up the fight between the Store Owner and the Young Person. Who do you want to talk to?\n\n[[STORE OWNER]] \n[[YOUNG PERSON]]",
      "links": [
        {
          "linkText": "STORE OWNER",
          "passageName": "STORE OWNER",
          "original": "[[STORE OWNER]]"
        },
        {
          "linkText": "YOUNG PERSON",
          "passageName": "YOUNG PERSON",
          "original": "[[YOUNG PERSON]]"
        }
      ],
      "hooks": [],
      "cleanText": "You break up the fight between the Store Owner and the Young Person. Who do you want to talk to?"
    },
    {
      "name": "YOUNG PERSON",
      "tags": "",
      "id": "25",
      "text": "The Young person informs you that they are Rakesh Eula. They were caught trying to use counterfeit gold in the store. They tell you that they are only using counterfeit gold because their family is sick and are unable to work, but they need medicine in order to treat their illness.\nThe store owner may know more information, or you can make your decision.\n\n[[STORE OWNER]] \n[[DECISION]]",
      "links": [
        {
          "linkText": "STORE OWNER",
          "passageName": "STORE OWNER",
          "original": "[[STORE OWNER]]"
        },
        {
          "linkText": "DECISION",
          "passageName": "DECISION",
          "original": "[[DECISION]]"
        }
      ],
      "hooks": [],
      "cleanText": "The Young person informs you that they are Rakesh Eula. They were caught trying to use counterfeit gold in the store. They tell you that they are only using counterfeit gold because their family is sick and are unable to work, but they need medicine in order to treat their illness.\nThe store owner may know more information, or you can make your decision."
    },
    {
      "name": "STORE OWNER",
      "tags": "",
      "id": "26",
      "text": "You speak to the store owner. They inform you that the young person is Rakesh Eula. They claim that their family is sick even though it is well known in this town that Rakesh does not have a family and is using the medicince for other, illegal purposes.\nThe young person could have more information, or you could make your decision.\n\n[[YOUNG PERSON]] \n[[DECISION]]",
      "links": [
        {
          "linkText": "YOUNG PERSON",
          "passageName": "YOUNG PERSON",
          "original": "[[YOUNG PERSON]]"
        },
        {
          "linkText": "DECISION",
          "passageName": "DECISION",
          "original": "[[DECISION]]"
        }
      ],
      "hooks": [],
      "cleanText": "You speak to the store owner. They inform you that the young person is Rakesh Eula. They claim that their family is sick even though it is well known in this town that Rakesh does not have a family and is using the medicince for other, illegal purposes.\nThe young person could have more information, or you could make your decision."
    },
    {
      "name": "REFUSE",
      "tags": "",
      "id": "27",
      "text": "You refused to complete your bounty. You let your target go and you are expelled from the guild.\nTo play again type \"Hunter's Guild\"\nTo stop playing type \"quit\"\n\n[[HUNTER'S GUILD]]",
      "links": [
        {
          "linkText": "HUNTER'S GUILD",
          "passageName": "HUNTER'S GUILD",
          "original": "[[HUNTER'S GUILD]]"
        }
      ],
      "hooks": [],
      "cleanText": "You refused to complete your bounty. You let your target go and you are expelled from the guild.\nTo play again type \"Hunter's Guild\"\nTo stop playing type \"quit\""
    },
    {
      "name": "DECISION",
      "tags": "",
      "id": "28",
      "text": "You must decide who's story to believe. The store owner or Rakesh?\nDo you take your target Dead or Alive? Or do you refuse to take them in?\n\n[[DEAD]] \n[[ALIVE]] \n[[REFUSE]]",
      "links": [
        {
          "linkText": "DEAD",
          "passageName": "DEAD",
          "original": "[[DEAD]]"
        },
        {
          "linkText": "ALIVE",
          "passageName": "ALIVE",
          "original": "[[ALIVE]]"
        },
        {
          "linkText": "REFUSE",
          "passageName": "REFUSE",
          "original": "[[REFUSE]]"
        }
      ],
      "hooks": [],
      "cleanText": "You must decide who's story to believe. The store owner or Rakesh?\nDo you take your target Dead or Alive? Or do you refuse to take them in?"
    }
  ]
}


# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
		#print("Moves: " + str(moves) + ", Score: " + str(score))
		print("Moves: {}, Score: {}".format(moves, score))
		print("You chose " + str(current_location["name"]))
		print(current_location["cleanText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "HUNTER'S GUILD"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	moves = moves + 1
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score = score + current_location["score"]
	render(current_location, score, moves)
	response = get_input()


print("Thanks for playing!")