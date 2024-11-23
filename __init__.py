from flask import Flask, request
import json
import powerplants

app = Flask(__name__)

@app.route('/energyproduction', methods=['POST'])
def energyproduction():

   #powerplants.selected_powerplants(load, gas_price, kerosine_price, wind, powerplants_list)
   return True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)