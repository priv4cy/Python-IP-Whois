import socket
import re
import json

def lookup(ip):
    whois_server = "whois.iana.org"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((whois_server, 43))
    s.send(ip.encode('utf-8') + b'\r\n')
    response = b''
    while True:
        data = s.recv(1024)
        if not data:
            break
        response += data

    response_str = response.decode('utf-8')
    for line in response_str.split('\n'):
        if ":" in line:
            key, value = line.split(":", 1)
            if key.strip().lower() == "whois":
                whois_server = value.strip()
                break

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((whois_server, 43))
    s.send(ip.encode('utf-8') + b'\r\n')
    response = b''
    while True:
        data = s.recv(1024)
        if not data:
            break
        response += data

    response_str = response.decode('utf-8')
    lines = response_str.split('\n')
    whois_dict = {}
    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key in whois_dict:
                if type(whois_dict[key]) == list:
                    whois_dict[key].append(value)
                else:
                    whois_dict[key] = [whois_dict[key], value]
            else:
                whois_dict[key] = value

    json_output = json.dumps(whois_dict, indent=4)
    return json_output
