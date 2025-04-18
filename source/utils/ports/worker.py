import socket

def QueryPort(IP, port):
    try:
        if IP == None:
            raise Exception("No IP address provided")
        
        if port == None:
            raise Exception("No port number provided")

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((IP, port))
        port_status = None

        if result == 0:
            port_status = f"Port {port} is open"
        else:
            port_status = f"Port {port} is closed"

        sock.close()

        return port_status, 200

    except Exception as error:
        return f"[QueryPorts] {error}", 500

def QueryPing(IP, port, timeout):
    try:
        if IP is None:
            raise Exception("No IP address provided")
        
        if port is None:
            raise Exception("No port number provided")
        
        if timeout is None:
            timeout = 1
        
        ip = socket.gethostbyname(IP)

        try:
            with socket.create_connection((ip, port), timeout=timeout):
                return "Ping Success", 200
            
        except socket.timeout:
            raise Exception("Ping failed")
    
    except Exception as error:
        return f"[Ping] Error: {error}", 500
