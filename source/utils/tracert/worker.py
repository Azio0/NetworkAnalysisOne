import socket

def traceroute(destination, max_hops=30, timeout=5):
    try:
        if destination == None:
            raise Exception(f"No destination provided")
        
        dest_ip = socket.gethostbyname(destination)
        hops = []

        for ttl in range(1, max_hops + 1):
            recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
            recv_socket.settimeout(timeout)

            recv_socket.bind(("", 33434))

            send_socket.sendto(b"", (destination, 33434))

            try:
                data, addr = recv_socket.recvfrom(512)
                hops.append(addr[0])

                if addr[0] == dest_ip:
                    break

            except socket.timeout:
                pass
 
            finally:
                send_socket.close()
                recv_socket.close()

        return hops, 200

    except Exception as error:
        return f"[TraceRoute] {error}", 500
