from flask import Flask, request
import json
import powerplants

app = Flask(__name__)

@app.route('/energyproduction', methods=['POST'])
def energyproduction():
#    with open('/example_payloads/payload3.json') as f:
#        data = json.load(f)
   
   data = request.json
   load = data['load']
   fuels = data['fuels']
   gas_price = fuels['gas(euro/MWh)']
   kerosine_price = fuels['kerosine(euro/MWh)']
   wind = fuels['wind(%)']
   powerplants_list = data['powerplants']
    
   powerplants_selected = powerplants.selected_powerplants(load, gas_price, kerosine_price, wind, powerplants_list)
   
   return powerplants_selected

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)