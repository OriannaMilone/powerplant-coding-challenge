import argparse
import requests
import json

parser = argparse.ArgumentParser(description="Send a JSON file to API's endpoint.")
parser.add_argument("file", type=str, help="JSON file to send.")
args = parser.parse_args()

try:
    with open(args.file, "r") as file:
        data = json.load(file) 
except FileNotFoundError:
    print(f"Error: The file {args.file} does not exist.")
    exit(1)
except json.JSONDecodeError:
    exit(1)

url = "http://127.0.0.1:8888/energyproduction"
headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status() 
    print("Server answer:")
    print(response.json())  
except requests.exceptions.RequestException as e:
    print(f"Somenthing went wrong: {e}")
    exit(1)