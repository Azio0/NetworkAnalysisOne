from utils.config.worker import *
from utils.requests.worker import *
from utils.vpnapi.worker import *
from utils.tracert.worker import *
from utils.ports.worker import *

class NetworkAnalysisOne():
    class ports():
        def Ping(IP, port=80, timeout=1):
            try:
                if IP == None:
                    raise Exception("No IP address provided")
                
                response, status = QueryPing(IP, port, timeout)
                
                if status != 200:
                    raise Exception(response)
                
                return response, 200
            
            except Exception as error:
                return f"[NetworkAnalysisOne] [Ping] Error: {error}", 500

        def CheckPort(IP, port):
            try:
                if IP == None:
                    raise Exception("No IP address provided")
                
                if port == None:
                    raise Exception("No port number provided")

                response, status = QueryPort(IP, port)

                if status != 200:
                    raise Exception(response)
                
                return response, 200

            except Exception as error:
                return f"[NetworkAnalysisOne] [CheckPort] Error: {error}", 500
    class tracert():
        def Trace(IP):
            try:
                if IP == None:
                    raise Exception("No IP address provided")
                
                response, status =  traceroute(IP)

                if status != 200:
                    raise Exception(response)
                
                return response, 200

            except Exception as error:
                return f"[NetworkAnalysisOne] [Trace] Error: {error}", 500

    class vpnAPI():
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
