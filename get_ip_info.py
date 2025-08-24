import ipinfo
import sys
# take the ip address 
try:
    ip_address = sys.argv[1]
except IndexError:
    ip_address = None

# token of ipinfo.io
token = 'c4f8fe77084e5c'

handler = ipinfo.getHandler(token)
details = handler.getDetails(ip_address)

for key, value in details.all.items():
    print(f"{key}: {value}")