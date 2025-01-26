import requests
import json


# Replace with your API key and contract ID
api_key = 'YOUR_ACCESS_TOKEN'
contract_id = 'YOUR_CONTRACT_ID'
# Set API endpoint and headers
url = f'https://api.ionos.com/billing/{contract_id}/utilization'
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}


def main():
    try:
        # Send GET request to API endpoint
        response = requests.get(url, headers=headers)
        # Check if the request was successful
        if response.status_code == 200:
            # Load JSON data from response
            data = json.loads(response.text)
            visualize(data)
        else:
            print(f'Failed to retrieve data. Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')


def visualize(data):
    model_util = {}
    meters = []
    for meter in data['datacenters'][0]['meters']:
        meters.append(meter)
    
    for meter in meters:
        if meter['resourceId'] not in model_util:
            model_util[meter['resourceId']] = {}
            # remove text before model name "meterDesc": "1 milion output tokens for Llama 3.1 405B",
            model_util[meter['resourceId']]['mdl_name'] = meter['meterDesc'].split('for')[1].strip()        
            model_util[meter['resourceId']]['input'] = 0
            model_util[meter['resourceId']]['output'] = 0
        if 'input' in meter['meterDesc']:
            model_util[meter['resourceId']]['input'] += (meter['quantity']['quantity'] * 1000000)
        else:
            model_util[meter['resourceId']]['output'] = (meter['quantity']['quantity'] * 1000000)
    print(json.dumps(model_util, indent=4))


if __name__ == "__main__":
    main()