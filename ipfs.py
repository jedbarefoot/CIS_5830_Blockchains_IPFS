import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	
	url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
	headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiIxNjUxYmY1Yi1kZjQzLTQyZjMtODkwYy01NmZjOGIwM2VmNjkiLCJlbWFpbCI6ImplZGJhcmVmb290QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6IkZSQTEifSx7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6Ik5ZQzEifV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiJjMTI0NWJkMjE0OTU4OWJjM2NlZiIsInNjb3BlZEtleVNlY3JldCI6Ijg0M2FjYjIzNmJmNWM4ZTdhNTIxM2NiMWE4Y2I3YjI5ZDM4ZjZlNzMxZGVhZjUyNjQyN2FkMzdjM2E5MmVjMDAiLCJleHAiOjE3NzMxNjgzMTR9.LwD_DMXnyGxsA_RwDCoX_t6aS_6aygxt1sSCRzeBzz",
		"Content-Type": "application/json"
    }

	response = requests.post(url, headers=headers, json=data)

	cid = response.json().get("IpfsHash")

	print(str(cid))

	return str(cid)

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	url = f"https://gateway.pinata.cloud/ipfs/{cid}"
	response = requests.get(url)

	data = response.json()

	print(data)

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return 
