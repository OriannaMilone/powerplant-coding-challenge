result = []

def selected_powerplants(load, gas_price, kerosine_price, wind, powerplants):
    merit_order = []
    for powerplant in powerplants:
        if powerplant["pmin"] > load:
            result.append({"name": powerplant["name"], "p": 0})
        else: 
            merit_order.append(calculated_cost(powerplant, gas_price, kerosine_price, wind))         
    merit_order = sorted(merit_order, key=lambda x: x["cost"])
    #combined_powerplants(merit_order, load)
    return merit_order
    #return result


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
    return True 
    

def combined_powerplants(merit_order, load):
    return True