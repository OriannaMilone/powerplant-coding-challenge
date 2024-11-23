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
python sendAPIrequest.py "example_payloads/payload{X}.json" payload{X}.
```
Where {X} is the number of the payload you want to send.

