import socket

def nslookup(domain):
    try:
        ip_addresses = socket.gethostbyname_ex(domain)[-1]
        return ip_addresses
    except socket.gaierror as e:
        return [str(e)]

def main():
    domain = 'awaland.xyz' # A cloudflare proxy domain
    ip_list = nslookup(domain)
    