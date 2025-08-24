# 🌍 IP Info & Location Mapper

This Python script fetches information about any IP address using the [ipinfo.io](https://ipinfo.io/) API.  
It also provides a Google Maps link and generates an interactive map with [Folium](https://python-visualization.github.io/folium/).  
Both maps are automatically opened in your default browser.

---

## 📌 Features
- Get details about an IP (city, country, organization, latitude, longitude, etc.).  
- Generates a **Google Maps link** to view the location.  
- Creates an **interactive map (HTML)** with a pin on the IP location.  
- Automatically opens maps in your default browser.  

---

## ⚙️ Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/ip-info-mapper.git
cd ip-info-mapper
pip install -r requirements.txt
```

Or install manually:
```bash
pip install ipinfo folium
```

---

## 🚀 Usage

### Lookup a specific IP:
```bash
python get_ip_info.py 8.8.8.8
```

---

## 📊 Example Output
```
ip: 8.8.8.8
hostname: dns.google
city: Mountain View
region: California
country: US
loc: 37.4056,-122.0775
org: AS15169 Google LLC
postal: 94043
timezone: America/Los_Angeles

--- Map Options ---
Google Maps Link: https://www.google.com/maps?q=37.4056,-122.0775
Interactive map saved as: ip_location_map.html
```

✅ Google Maps opens automatically.  
✅ An interactive map is saved and opened in your browser.  

---

## 📂 Files
- `get_ip_info.py` → main script.  
- `requirements.txt` → dependencies (`ipinfo`, `folium`,`webbrowser`,`sys`).  

---

## 📌 Notes
- Location is approximate (based on IP address geolocation or ISP).  
- Requires an **ipinfo.io access token** (replace the token in the script).  
- Folium map is saved locally as `ip_location_map.html`.  
