result = []

def selected_powerplants(load, gas_price, kerosine_price, wind, powerplants):
    global result
    result = []
    merit_order = []
    
    for powerplant in powerplants:
        if powerplant["pmin"] > load:
            result.append({"name": powerplant["name"], "p": 0})
        else: 
            merit_order.append(calculated_cost(powerplant, gas_price, kerosine_price, wind))         
    
    merit_order = sorted(merit_order, key=lambda x: x["cost"])
    combined_powerplants(merit_order, load)
    return result


def calculated_cost(powerplant, gas_price, kerosine_price, wind):
    if powerplant["type"] == "gasfired":
        cost = round(gas_price / powerplant["efficiency"], 2)
        power_range = (powerplant["pmin"], powerplant["pmax"])
        return ({"name": powerplant["name"], "power_range": power_range, "cost": cost,})
    elif powerplant["type"] == "turbojet":
        cost = round(kerosine_price / powerplant["efficiency"], 2)
        power_range = (powerplant["pmin"], powerplant["pmax"])
        return ({"name": powerplant["name"], "power_range": power_range, "cost": cost,})
    else: 
        power_range = (0, powerplant["pmax"] * wind / 100)
        return ({"name": powerplant["name"], "power_range": power_range, "cost": 0,})
    
# Original (basic) solution    
# def combined_powerplants(merit_order, load):
#     solution =  0
#     missing = load
#     for powerplant in merit_order:
#         missing = load - solution
#         if powerplant["power_range"][1] <= missing and missing != 0:
#             solution += powerplant["power_range"][1]
#             result.append({"name": powerplant["name"], "p": powerplant["power_range"][1]})
#         elif powerplant["power_range"][0] <= missing and missing <= powerplant["power_range"][1] and missing != 0:
#             solution += missing
#             result.append({"name": powerplant["name"], "p": missing})
#         else: 
#             result.append({"name": powerplant["name"], "p": 0.0})

# <Problem solve after de 4h limit time>
def combined_powerplants(merit_order, load, tmp_solution=0, plant_index=0):
    global result

    if tmp_solution == load:
        for i in range(plant_index, len(merit_order)):
            result.append({"name": merit_order[i]["name"], "p": 0.0})
        return True

    if plant_index >= len(merit_order):
        return False

    current_plant = merit_order[plant_index]
    pmin, pmax = current_plant["power_range"]

    if tmp_solution + pmax <= load:
        result.append({"name": current_plant["name"], "p": pmax})
        if combined_powerplants(merit_order, load, tmp_solution + pmax, plant_index + 1):
            return True
        result.pop()

    falta = load - tmp_solution
    if pmin <= falta <= pmax:
        result.append({"name": current_plant["name"], "p": falta})
        if combined_powerplants(merit_order, load, tmp_solution + falta, plant_index + 1):
            return True
        result.pop()

    if pmin > 0:
        result.append({"name": current_plant["name"], "p": pmin})
        if combined_powerplants(merit_order, load, tmp_solution + pmin, plant_index + 1):
            return True
        result.pop()

    result.append({"name": current_plant["name"], "p": 0.0})
    if combined_powerplants(merit_order, load, tmp_solution, plant_index + 1):
        return True
    result.pop()  

    return False