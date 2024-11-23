import argparse
import requests
import json

parser = argparse.ArgumentParser(description="Send a JSON file to API's endpoint.")
parser.add_argument("filepath", type=str, help="Path to the JSON file.")
parser.add_argument("filename", type=str, help="Name of the JSON file.")
args = parser.parse_args()

try:
    with open(args.filepath, "r") as file:
        data = json.load(file) 
except FileNotFoundError:
    print(f"Error: The file {args.filepath} does not exist.")
    exit(1)
except json.JSONDecodeError:
    exit(1)

#####
try:
    X = int(args.filename.split('payload')[1].split('.json')[0])  # Extraer X de 'payloadX.json'
except (IndexError, ValueError):
    print("Error: Invalid filename format. It should be 'payloadX.json'.")
    exit(1)
#####

url = "http://127.0.0.1:8888/energyproduction"
headers = {"Content-Type": "application/json",
            "X-File-Name": args.filename }

try:
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status() 
    print("Server answer:")
    print(response.json())  
except requests.exceptions.RequestException as e:
    print(f"Somenthing went wrong: {e}")
    exit(1)
    







