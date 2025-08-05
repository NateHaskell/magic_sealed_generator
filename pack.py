import json
import random
from parse_json import *


pack = []


# Determine if one common will be replaced by a Special Guests card - 1.8% chance
special_guests_roll = random.random()
if special_guests_roll <= 0.018:
    pack.append(random.choice(eoe_special_guests))

    for i in range(5):
        pack.append((random.choice(eoe_commons)))

else:
    for i in range(7):
        pack.append((random.choice(eoe_commons)))


wildcard_roll = random.random()

#<1% chance for mythic borderless triumphant or surreal space card
if wildcard_roll <= 0.0015:
    wildcard = random.choice(mythic_triumphant_and_surreal_cards)
    pack.append(wildcard)

#<1% chance for mythic borderless viewport land
elif wildcard_roll <= 0.0035:
    wildcard = random.choice(mythic_borderless_viewport_lands)
    pack.append(wildcard)

#<1% chance for rare borderless triumphant or surreal space card
elif wildcard_roll <= 0.006:
    wildcard = random.choice(rare_triumphant_and_surreal_cards)
    pack.append(wildcard)

#<1% chance for main set mythic less 
elif wildcard_roll <= 0.009:
    wildcard = random.choice(eoe_main_set_mythics)
    pack.append(wildcard)

#1% chance for rare borderless viewport land
elif wildcard_roll <= 0.019:
    wildcard = random.choice(rare_borderless_viewport_lands)
    pack.append(wildcard)

#2.5% chance for mythic stellar sights
elif wildcard_roll <= 0.044:
    wildcard = random.choice(mythic_stellar_sights)
    pack.append(wildcard)

#10% chance for rare stellar sights
elif wildcard_roll <= 0.144:
    wildcard = random.choice(rare_stellar_sights)
    pack.append(wildcard)  

#10.6% chance for main set rare
elif wildcard_roll <= 0.25:
    wildcard = random.choice(eoe_main_set_rares)
    pack.append(wildcard)  

#12.5% chance for common
elif wildcard_roll <= 0.375:
    wildcard = random.choice(eoe_commons)
    pack.append(wildcard)  

#62.5% chance for uncommon
elif wildcard_roll <= 1.0:
    wildcard = random.choice(eoe_uncommons)
    pack.append(wildcard)     


#add 3 random uncommons for the uncommon slots
for i in range(3):
        pack.append((random.choice(eoe_uncommons)))

#rare or mythic slot
rare_roll = random.random()

#<1% chance for mythic viewport land
if rare_roll <= 0.006:
    rare_slot = random.choice(mythic_borderless_viewport_lands)
    pack.append(rare_slot)

#<1% chance for mythic borderless surreal space or triumphant
elif rare_roll <= 0.0014:
    rare_slot = random.choice(mythic_triumphant_and_surreal_cards)
    pack.append(rare_slot)

#4% chance for rare borderless triumphant or surreal space card
elif rare_roll <= 0.054:
    rare_slot = random.choice(rare_triumphant_and_surreal_cards)
    pack.append(rare_slot)

#14.2% chance for main set mythic
elif rare_roll <= 0.196:
    rare_slot = random.choice(eoe_main_set_mythics)
    pack.append(rare_slot)

#14.2% chance for main set mythic
elif rare_roll <= 0.804:
    rare_slot = random.choice(eoe_main_set_rares)
    pack.append(rare_slot)


for card in pack:
    print(card["name"])
    print(card["rarity"])

# with open("rare_stellar_sights", "w") as json_file:
#         json.dump(rare_stellar_sights, json_file, indent=4)


# 14 Magic: The Gathering cards
# 6–7 Commons
# There are 81 commons from Edge of Eternities that can be found in these slots.
# In 1.8% of Play Boosters, 1 of 10 non-foil Special Guests cards will replace a common. Of note, Special Guests cards aren't found in the wildcard nor traditional foil slot in Play Boosters.

# 3 Uncommons
# There are 100 uncommons from Edge of Eternities that can be found in these slots.

# 1 Wildcard of any rarity
# A common (12.5%), uncommon (62.5%), rare (10.6%), or mythic rare (less than 1%) from Edge of Eternities's main set (EOE default frame cards)
# A rare (10%) or mythic rare (2.5%) Stellar Sights land
# A rare (1%) or mythic rare (less than 1%) borderless viewport land
# A rare (less than 1%) or mythic rare (less than 1%) borderless triumphant or surreal space card

# 1 Rare or mythic rare card
# There are 60 rares and 20 mythic rares from Edge of Eternities that can be found in these slots.
# A rare (80.4%) or mythic rare (14.2%) from Edge of Eternities's main set
# A rare (2%) or mythic rare (less than 1%) borderless triumphant card
# A rare (2%) or mythic rare (less than 1%) borderless surreal space card
# A mythic rare (less than 1%) borderless viewport land

# 1 Traditional foil card of any rarity
# A common (58%), uncommon (32%), rare (6.4%), or mythic rare (1.1%) from Edge of Eternities's main set
# A rare (1%) or mythic rare (less than 1%) Stellar Sights land
# A rare (less than 1%) or mythic rare (less than 1%) borderless viewport, triumphant, or surreal space card

# 1 Land
# A non-foil (64%) or traditional foil (16%) default frame basic land
# A non-foil (16%) or traditional foil (4%) borderless celestial basic land
# 1 Non-foil double-sided token
# Please note that Play Boosters no longer contain ad cards or art cards.