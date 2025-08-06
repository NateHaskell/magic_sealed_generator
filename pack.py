import json
import random
from parse_json import *


packs = []


def generate_sealed_pool():

    pack_count = 0
    while pack_count < 6:

        # Determine if one common will be replaced by a Special Guests card - 1.8% chance
        special_guests_roll = random.random()
        if special_guests_roll <= 0.018:
            packs.append(random.choice(eoe_special_guests))

            for i in range(6):
                packs.append((random.choice(eoe_commons)))

        else:
            for i in range(7):
                packs.append((random.choice(eoe_commons)))


        # Add 3 random uncommons for the uncommon slots
        for i in range(3):
                packs.append((random.choice(eoe_uncommons)))


        # Choose card for wildcard slot
        wildcard_roll = random.random()

        # 0.15% chance for mythic borderless triumphant or surreal space card
        if wildcard_roll <= 0.0015:
            wildcard = random.choice(mythic_triumphant_and_surreal_cards)
            packs.append(wildcard)

        # 0.2% chance for mythic borderless viewport land
        elif wildcard_roll <= 0.0035:
            wildcard = random.choice(mythic_borderless_viewport_lands)
            packs.append(wildcard)

        # 0.25% chance for rare borderless triumphant or surreal space card
        elif wildcard_roll <= 0.006:
            wildcard = random.choice(rare_triumphant_and_surreal_cards)
            packs.append(wildcard)

        # 0.3% chance for main set mythic less 
        elif wildcard_roll <= 0.009:
            wildcard = random.choice(eoe_main_set_mythics)
            packs.append(wildcard)

        # 1% chance for rare borderless viewport land
        elif wildcard_roll <= 0.019:
            wildcard = random.choice(rare_borderless_viewport_lands)
            packs.append(wildcard)

        # 2.5% chance for mythic stellar sights
        elif wildcard_roll <= 0.044:
            wildcard = random.choice(mythic_stellar_sights)
            packs.append(wildcard)

        # 10% chance for rare stellar sights
        elif wildcard_roll <= 0.144:
            wildcard = random.choice(rare_stellar_sights)
            packs.append(wildcard)  

        # 10.6% chance for main set rare
        elif wildcard_roll <= 0.25:
            wildcard = random.choice(eoe_main_set_rares)
            packs.append(wildcard)  

        # 12.5% chance for common
        elif wildcard_roll <= 0.375:
            wildcard = random.choice(eoe_commons)
            packs.append(wildcard)  

        # 62.5% chance for uncommon
        elif wildcard_roll <= 1.0:
            wildcard = random.choice(eoe_uncommons)
            packs.append(wildcard)     


        # Rare or mythic slot
        rare_roll = random.random()

        # 0.6% chance for mythic viewport land
        if rare_roll <= 0.006:
            rare_slot = random.choice(mythic_borderless_viewport_lands)
            packs.append(rare_slot)

        # 0.8% chance for mythic borderless surreal space or triumphant
        elif rare_roll <= 0.014:
            rare_slot = random.choice(mythic_triumphant_and_surreal_cards)
            packs.append(rare_slot)

        # 4% chance for rare borderless triumphant or surreal space card
        elif rare_roll <= 0.054:
            rare_slot = random.choice(rare_triumphant_and_surreal_cards)
            packs.append(rare_slot)

        # 14.2% chance for main set mythic
        elif rare_roll <= 0.196:
            rare_slot = random.choice(eoe_main_set_mythics)
            packs.append(rare_slot)

        # 80.4% chance for main set rare
        elif rare_roll <= 1.0:
            rare_slot = random.choice(eoe_main_set_rares)
            packs.append(rare_slot)

        # Foil slot
        foil_roll = random.random()

        # 0.35% chance for mythic triumphant or surreal space card
        if foil_roll <= 0.0035:
            foil_slot = random.choice(mythic_triumphant_and_surreal_cards)
            packs.append(foil_slot)

        # 0.5% chance for mythic Stellar Sights land
        elif foil_roll <= 0.0085:
            foil_slot = random.choice(mythic_stellar_sights)
            packs.append(foil_slot)

        # 0.65% chance for rare borderless triumphant or surreal space card
        elif foil_roll <= 0.015:
            foil_slot = random.choice(rare_triumphant_and_surreal_cards)
            packs.append(foil_slot)

        # 1% chance for rare Stellar Sights land
        elif foil_roll <= 0.025:
            foil_slot = random.choice(rare_stellar_sights)
            packs.append(foil_slot)

        # 1.1% chance for main set mythic
        elif foil_roll <= 0.036:
            foil_slot = random.choice(eoe_main_set_mythics)
            packs.append(foil_slot)

        # 6.4% chance for rare
        elif foil_roll <= 0.1:
            foil_slot = random.choice(eoe_main_set_rares)
            packs.append(foil_slot)

        # 32% chance for uncommon
        elif foil_roll <= 0.42:
            foil_slot = random.choice(eoe_uncommons)
            packs.append(foil_slot)

        # 58% chance for common
        elif foil_roll <= 1.0:
            foil_slot = random.choice(eoe_commons)
            packs.append(foil_slot)
        
        pack_count += 1

    return packs
    

