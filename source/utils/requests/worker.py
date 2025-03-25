import requests
from utils.config.worker import *

def SendVPNApiRequest(IP):
    try:
        if IP == None:
            return "No IP address provided"
        
        response = requests.get(f"https://vpnapi.io/api/{IP}?key={ConfigParser('vpnapi', 'key')}")

        if response.status_code != 200:
            raise Exception(response.text)

        return response, 200

    except Exception as error:
        return f"[SendVPNApiRequest] {error}", 500
