import ipinfo
import sys
import folium
import webbrowser   

# take the ip address 
try:
    ip_address = sys.argv[1]
except IndexError:
    ip_address = None

# token of ipinfo.io
token = 'c4f8fe77084e5c'
handler = ipinfo.getHandler(token)
details = handler.getDetails(ip_address)

# Print all details
for key, value in details.all.items():
    print(f"{key}: {value}")

# Get latitude and longitude if available
latitude = details.all.get("latitude")
longitude = details.all.get("longitude")

if latitude and longitude:
    print("\n--- Map Options ---")

    # Option 1: Google Maps link
    maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    print("Google Maps Link:", maps_link)

    # Auto-open in default browser
    webbrowser.open(maps_link)

    # Option 2: Folium interactive map
    try:
        lat = float(latitude)
        lon = float(longitude)

        m = folium.Map(location=[lat, lon], zoom_start=10)
        folium.Marker([lat, lon], popup=f"IP: {ip_address}").add_to(m)

        m.save("ip_location_map.html")
        print("Interactive map saved as: ip_location_map.html")

        # Auto-open the HTML map too
        webbrowser.open("ip_location_map.html")

    except ValueError:
        print("Could not generate folium map due to invalid coordinates.")
else:
    print("No latitude/longitude data found for this IP.")
