import json

#lists to hold cards from the Edge of Eternities set
eoe_commons = []
eoe_uncommons = []
eoe_main_set_rares = []
eoe_main_set_mythics = []
eoe_special_guests = []
rare_stellar_sights = []
mythic_stellar_sights = []
eoe_basic_lands = []
rare_borderless_viewport_lands = []
mythic_borderless_viewport_lands = []
rare_triumphant_and_surreal_cards = []
mythic_triumphant_and_surreal_cards = []

#exlucde these collector numbers as the cards are only available in collector booster packs
excluded_numbers = {"350", "359", "382", "362", "363", "357", "364"}

#exlucde the Poster Stellar Sights cards as they are only available in collector booster packs
excluded_stellar_sights = {str(i) for i in range(46, 91)}

#include these special guests collector numbers
special_guests_collector_nums = {str(i) for i in range(119, 129)}

#borderless viewport lands to include
viewport_collector_nums = {str(i) for i in range(277, 287)}

#borderless triumphant and surreal space cards to include
triumphant_surreal_collector_nums = {str(i) for i in range(287, 317)}



try:
    with open("cards.json", "r") as file:
        card_data = json.load(file)

        
        for card in card_data:
            promo_types = card.get("promo_types") or []
            frame_effects = card.get("frame_effects") or []
            border_color = card.get("border_color") 
            type_line = card.get("type_line")
            set_name = card.get("set_name")
            collector_number = card.get("collector_number")
            rarity = card.get("rarity")

            if collector_number in excluded_numbers:
                continue

            #filter out the commons
            if (
                set_name == "Edge of Eternities" and 
                rarity == "common" and
                "Basic Land" not in type_line and
                not promo_types
            ):
                eoe_commons.append(card)
            
            #filter out the uncommons
            elif (
                set_name == "Edge of Eternities" and 
                rarity == "uncommon" and 
                not promo_types
            ):
                eoe_uncommons.append(card)
            
            #filter out the main set rares
            elif (
                set_name == "Edge of Eternities" and 
                rarity == "rare" and
                "extendedart" not in frame_effects and
                "borderless" not in border_color and
                not promo_types
            ):
                eoe_main_set_rares.append(card)
            
            #filter out the main set mythics
            elif (
                set_name == "Edge of Eternities" and 
                rarity == "mythic" and
                "extendedart" not in frame_effects and
                "borderless" not in border_color and
                not promo_types
            ):
                eoe_main_set_mythics.append(card)
            
            #filter out the rare stellar sights
            elif (
                set_name == "Edge of Eternities: Stellar Sights" and 
                rarity == "rare" and
                "galaxyfoil" not in promo_types and
                collector_number not in excluded_stellar_sights
            ):
                rare_stellar_sights.append(card)

            #filter out the mythic stellar sights
            elif (
                set_name == "Edge of Eternities: Stellar Sights" and 
                rarity == "mythic" and
                "galaxyfoil" not in promo_types and
                collector_number not in excluded_stellar_sights
            ):
                mythic_stellar_sights.append(card)
                
            #filter out the special guets
            elif (
                set_name == "Special Guests" and 
                collector_number in special_guests_collector_nums
            ):
                eoe_special_guests.append(card)

            #filter out the rare borderless viewport lands
            elif (
                set_name == "Edge of Eternities" and
                rarity == "rare" and
                collector_number in viewport_collector_nums
            ):
                rare_borderless_viewport_lands.append(card)
            
            #filter out the mythic borderless viewport lands
            elif (
                set_name == "Edge of Eternities" and
                rarity == "mythic" and
                collector_number in viewport_collector_nums
            ):
                mythic_borderless_viewport_lands.append(card)
            
            #filter out the rare triumphant and surreal space cards
            elif (
                set_name == "Edge of Eternities" and
                rarity == "rare" and
                collector_number in triumphant_surreal_collector_nums
            ):
                rare_triumphant_and_surreal_cards.append(card)
            
            #filter out the mythic triumphant and surreal space cards
            elif (
                set_name == "Edge of Eternities" and
                rarity == "mythic" and
                collector_number in triumphant_surreal_collector_nums
            ):
                mythic_triumphant_and_surreal_cards.append(card)
           
                
    # print(len(eoe_commons))
    # print(len(eoe_uncommons))
    # print(len(eoe_main_set_rares))
    # print(len(eoe_main_set_mythics))
    # print(len(rare_stellar_sights))
    # print(len(mythic_stellar_sights))
    # print(len(eoe_special_guests))
    # print(len(rare_borderless_viewport_lands))
    # print(len(mythic_borderless_viewport_lands))
    # print(len(rare_triumphant_and_surreal_cards))
    # print(len(mythic_triumphant_and_surreal_cards))

                

except Exception as e:
    print(f"Error: {e}")