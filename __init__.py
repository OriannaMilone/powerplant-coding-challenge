from flask import Flask, request, jsonify
import json
import powerplants

app = Flask(__name__)

@app.route('/energyproduction', methods=['POST'])
def energyproduction():
   data = request.json
   load = data['load']
   fuels = data['fuels']
   gas_price = fuels['gas(euro/MWh)']
   kerosine_price = fuels['kerosine(euro/MWh)']
   wind = fuels['wind(%)']
   powerplants_list = data['powerplants']
    
   powerplants_selected = powerplants.selected_powerplants(load, gas_price, kerosine_price, wind, powerplants_list)
   
   with open('./response3.json', 'w') as response_file:
        json.dump(powerplants_selected, response_file, indent=4)
   
   return jsonify(powerplants_selected)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)