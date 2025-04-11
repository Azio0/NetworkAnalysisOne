import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'source')))

from naom import NetworkAnalysisOne

# Create an instance of the NetworkAnalysisOne class
NAOM = NetworkAnalysisOne()

# Example of ports module usage
def PingIP(ip):
    # Call the ping method from the ports module
    response, status = NAOM.ports.Ping(ip)

    if status != 200:
        return (f"Ping failed: {response}")

    return response, status

# Example of vpnAPI module usage
def QueryIP(ip):
    # Call the LookupIP method from the vpnAPI module
    response, status = NAOM.vpnAPI.LookupIP(ip)

    if status != 200:
        return (f"QueryIP failed: {response}")

    # Use the data set returned by the API and return the location
    location, status = NAOM.vpnAPI.CheckLocation(response)

    if status != 200:
        return (f"QueryIP failed: {location}")
    
    return location, status

# Example of ports module usage
ip = input("Enter an IP address: ")
ip_ping = PingIP(ip)

print(f"Ping result: {ip_ping}")

# Example of vpnAPI module usage
ip_query = QueryIP(ip)

print(f"Query result: {ip_query}")
