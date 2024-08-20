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

def test_all_ports_and_ips(ips, ports):
    for ip in ips:
        for port in ports:
            check_port(ip, port)

if __name__ == "__main__":
    ips = ["8.8.8.8", "8.8.4.4"]  # เพิ่ม IP ที่ต้องการทดสอบ
    ports = [22, 80, 443]  # เพิ่มพอร์ตที่ต้องการทดสอบ
    test_all_ports_and_ips(ips, ports)
