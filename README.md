# Powerplant Coding Challenge Project: Solution by Orianna Milone S.

This repository (which is a fork from the original: "https://github.com/gems-st-ib/powerplant-coding-challenge.git") contains the solution to the Powerplant coding challenge.

## Requirements

- Python 3.10.0
- Flask
- Requests

## Installation

To install the project dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## How to Build and Launch the API
Start the API. Make sure you have Flask installed.
Start the server by running the following command:
```bash
python powerplant-coding-challenge/__init__.py 
```
This will launch the API at http://127.0.0.1:8888.

## Send a Request to the API
Use the following script to send a POST request with a JSON file:
``` bash
python sendAPIrequest.py "example_payloads/payload{X}.json" payload{X}.json
```
Where {X} is the number of the payload you want to send.

## Powerplant Energy Production 
This app simulates the energy production optimization process based on the load, fuel prices, and available powerplants. It selects the most efficient powerplants to meet the required energy load by evaluating their cost-effectiveness and power generation capabilities. The process involves:

* Cost Calculation: Each powerplant's cost is calculated based on its type (gas-fired, turbojet, or wind). Gas and kerosene prices are used to determine the cost of energy for gas-fired and turbojet plants, while wind plants have zero cost but are affected by wind efficiency.

* Merit Order Sorting: Powerplants are sorted by their cost-effectiveness (lowest cost first). This allows the system to select the most cost-efficient plants to meet the load.

* Load Allocation: Once sorted, the app allocates the required load to the selected powerplants, starting with the most cost-effective ones, until the full load is met.

The result is a list of powerplants, each with the amount of energy it will contribute to meet the load.
