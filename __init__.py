from flask import Flask, request, jsonify
import json
import powerplants

app = Flask(__name__)

@app.route('/energyproduction', methods=['POST'])
def energyproduction():

    json_filename = request.headers.get('X-File-Name') 
    if json_filename:
        try:
            X = int(json_filename.split('payload')[1].split('.json')[0])  
        except ValueError:
            return jsonify({"error": "Invalid filename format"}), 400
    else:
        return jsonify({"error": "No file name provided"}), 400
   
    data = request.json
    load = data['load']
    fuels = data['fuels']
    gas_price = fuels['gas(euro/MWh)']
    kerosine_price = fuels['kerosine(euro/MWh)']
    wind = fuels['wind(%)']
    powerplants_list = data['powerplants']
        
    powerplants_selected = powerplants.selected_powerplants(load, gas_price, kerosine_price, wind, powerplants_list)

    response_filename = f'example_payloads/response{X}.json'
    with open(response_filename, 'w') as response_file:
            json.dump(powerplants_selected, response_file, indent=4)
    
    return jsonify(powerplants_selected)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)