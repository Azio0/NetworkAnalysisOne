from utils.config.worker import *
from utils.requests.worker import *
from utils.vpnapi.worker import *

class NetworkAnalysisOne():
    def LookupIP(IP):
        try:
            if IP == None:
                raise Exception("No IP address provided")

            response, status = QueryIP(IP)

            if status != 200:
                raise Exception(response)
            
            return response, 200
        except Exception as error:
            return f"[NetworkAnalysisOne] [LookupIP] Error: {error}", 500
        
    def CheckType(data):
        try:
            if data == None:
                raise Exception("No data provided")
            
            response, status = QueryAnonymisers(data)

            if status != 200:
                raise Exception(response)
            
            return response, 200
        except Exception as error:
            return f"[NetworkAnalysisOne] [CheckType] Error: {error}", 500
        
    def CheckLocation(data):
        try:
            if data == None:
                raise Exception("No data provided")
            
            response, status = QueryLocation(data)

            if status != 200:
                raise Exception(response)
            
            return response, 200
        except Exception as error:
            return f"[NetworkAnalysisOne] [CheckLocation] Error: {error}", 500

    def CheckNetworkInfo(data):
        try:
            if data == None:
                raise Exception("No data provided")
            
            response, status = QueryNetworkInfo(data)

            if status != 200:
                raise Exception(response)
            
            return response, 200
        except Exception as error:
            return f"[NetworkAnalysisOne] [CheckNetworkInfo] Error: {error}", 500
