import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_data = json.dumps(data)
	url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
	files = {"file": ("data.json", json_data)}
	headers = {
        "pinata_api_key": "c1245bd2149589bc3cef",
        "pinata_secret_api_key": "843acb236bf5c8e7a5213cb1a8cb7b29d38f6e731deaf526427ad37c3a92ec00"
		}

	response = requests.post(url, headers=headers, files=files)
	cid = response.json().get("data", {}).get("cid")

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	url = f"https://gateway.pinata.cloud/ipfs/{cid}"
	response = requests.get(url)

	data = response.json()

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
