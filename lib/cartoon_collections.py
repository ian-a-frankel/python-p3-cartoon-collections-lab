def roll_call_dwarves(dwarf_list):
    roll = ""
    for index, dwarf in enumerate(dwarf_list, 1):
        roll = roll + f"{index}. {dwarf}"
        if index < len(dwarf_list):
            roll = roll + f"\n"
    print(roll)

def summon_captain_planet(element_list):
    return [element.title() + '!' for element in element_list]

def long_planeteer_calls(calls):
    not_all_short = False
    for call in calls:
        not_all_short = not_all_short or len(call) > 4
    return not_all_short

def find_the_cheese(ingredients):
    cheeses = ["cheddar", "gouda", "camembert"]

    has_cheese = None

    for cheese in cheeses:
        if cheese in ingredients:
            has_cheese = cheese
            return cheese
        
    return None
