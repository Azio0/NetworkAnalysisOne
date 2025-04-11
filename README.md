# NetworkAnalysisOne

**NetworkAnalysisOne** is an open-source utility for gathering information on a public IP (Internet Protocol) address by using public information and different networking methods, allowing easy verification of country, provider, response time etc.

To unlock NAOM's full potential, it is recommended to create a free account with [VPNAPI.io](https://www.VPNAPI.io), to access the vpnapi functions within this module.

## Features

- Port Scanning.
- Traceroute of hops between client and IP.
- VPN, Tor, Proxy and Relay detection.
- Country Information.
- ISP Information including ASN's.
- Easy to configure VpnAPI credentials in the config file.
- Flexible module to customise to fit your requirements.

## Requirements
- Python 3
- VpnAPI Account (Optional)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Azio0/NetworkAnalysisOne.git
   cd NetworkAnalysisOne
   ```
2. Install Python and PIP:
   ```bash
   sudo apt-get install python3
   sudo apt-get install python3-pip
   ```
4. Install the required Python Packages:
   ```bash
   pip install -r requirements.txt
   ```

## How It Works

NetworkAnalysisOne uses the following components:
- **configuration**: Reads configuration settings from a YAML file.
- **VPNAPI**: Returns more in deph information about the network type.
- **Requests**: To return data from the VpnAPI service.
- **Ports**: Used for pinging and scanning open ports.
- **Tracert**: Used to observe the flow of packets.
  
## Class: `NetworkAnalysisOne`

The `NetworkAnalysisOne` class provides methods to allow you to call certain endpoints. It has three main nested classes: `ports`, `tracert` and `vpnAPI`.

### Methods

#### `Ping(IP)`

Pings a network with a traffic to ensure the network is online.

- **Parent**: `ports` (class) - The class this method belongs to.
- **Parameters**: `IP` (str) - The network's IP.
- **Optional Parameters**: `port` and `timeout` (int) - A specific port and timeout amount.
- **Returns**: A string containing the attempt information and status code.

#### `CheckPort(IP, port)`

Scans the specified port to determine if it is exposed.

- **Parent**: `ports` (class) - The class this method belongs to.
- **Parameters**: `IP` (str), `Port` (int) - The network's IP and port.
- **Returns**: A string containing the ports information and status code.

#### `Trace(IP)`

Observes the hops (IP addresses) that traffic from client to destination IP takes.

- **Parent**: `tracert` (class) - The class this method belongs to.
- **Parameters**: `IP` (str) - The network's IP.
- **Returns**: A string containing the hop(s) IP addresses and status code.

#### `LookupIP(IP)`

Queries an IP address with the VpnAPI service (Requires API Key within Config).

- **Parent**: `vpnAPI` (class) - The class this method belongs to.
- **Parameters**: `IP` (str) - The network's IP.
- **Returns**: A data set containing the IP's information and status code.

#### `CheckType(data)`

Parses through a json dataset to return the `security` information (Tor, Proxy etc).

- **Parent**: `vpnAPI` (class) - The class this method belongs to.
- **Parameters**: `data` (The data set returned from LookupIP) - The network's information.
- **Returns**: A data set containing the IP's information and status code.

#### `CheckLocation(data)`

Parses through a json dataset to return the `location` information (United Kingdom, London, etc).

- **Parent**: `vpnAPI` (class) - The class this method belongs to.
- **Parameters**: `data` (The data set returned from LookupIP) - The network's information.
- **Returns**: A data set containing the location registered to an IP and status code.

#### `CheckNetworkInfo(data)`

Parses through a json dataset to return the `network` information (ASN Number, ISP Name, etc).

- **Parent**: `vpnAPI` (class) - The class this method belongs to.
- **Parameters**: `data` (The data set returned from LookupIP) - The network's information.
- **Returns**: A data set containing the IP's network information and status code.

## Example Usage

Refer to the [basic_use.py](example/basic_use.py) file for an example of how to use the `NetworkAnalysisOne` class.

```python
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

    # Use the dataset returned by the API and return the location
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
```

## Contributing

This is an open-source project, and contributions are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License.

## Contact

For any questions or suggestions, please open an issue or contact the project maintainers.

## Donations

This project is intended to be open-source and free from cost to use. I love coding, setting a target and accomplishing it, sometimes by using pre-existing technology or creating an original approach to a problem. It excites me and gives me a sense of purpose, but it is not always easy to find the time or motivation to keep pushing forward. Donations are welcome if you wish to give something towards the work I do, but it is completely optional and is certainly not a requirement.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/azio0)
