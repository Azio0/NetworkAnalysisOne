from utils.requests.worker import *

def QueryIP(IP):
    try:
        if IP == None:
            raise Exception("No IP address provided")

        response, status = SendVPNApiRequest(IP)

        if status != 200:
            raise Exception(response)

        return response.json(), 200
    
    except Exception as error:
        return f"[QueryIP] {error}", 500

def QueryAnonymisers(data):
    try:
        if data == None:
            raise Exception("No data provided")
        
        detections = []

        for protocol in data['security']:
            detections.append(f"{protocol}: {data['security'][protocol]}")

        return detections, 200 

    except Exception as error:
        return f"[QueryAnonymisers] {error}", 500

def QueryLocation(data):
    try:
        if data == None:
            raise Exception("No data provided")
        
        locationData = data['location']

        return locationData, 200

    except Exception as error:
        return f"[QueryLocation] {error}", 500

def QueryNetworkInfo(data):
    try:
        if data == None:
            raise Exception("No data provided")
        
        networkData = data['network']

        return networkData, 200
    except Exception as error:
        return f"[QueryNetworkInfo] {error}", 500
