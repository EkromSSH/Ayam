# test_script.py
import socket

def check_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} on {ip} is open")
        else:
            print(f"Port {port} on {ip} is closed")

if __name__ == "__main__":
    check_port("8.8.8.8", 80)  # ทดสอบพอร์ต 80 บน IP 8.8.8.8
