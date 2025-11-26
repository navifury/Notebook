

import phonenumbers
from phonenumbers import geocoder, carrier
import folium
import webbrowser
from geopy.geocoders import Nominatim

# Parse the phone number (clean string)
number = phonenumbers.parse("+9779862101428")  # Example: Nepal

# Get region and carrier
region = geocoder.description_for_number(number, "en")
sim_carrier = carrier.name_for_number(number, "en")

print(f"Region: '{region}'")
print(f"Carrier: {sim_carrier}")

# Get coordinates automatically using geopy
geolocator = Nominatim(user_agent="phone_locator")
location_data = geolocator.geocode(region)

if location_data:
    location = [location_data.latitude, location_data.longitude]
else:
    # fallback (default location if geocoding fails)
    location = [20.5937, 78.9629]  # India

# Create map
m = folium.Map(location=location, zoom_start=6)
folium.Marker(location, tooltip=f"{region} - {sim_carrier}").add_to(m)

# Save and open
m.save("phone_location.html")
webbrowser.open("phone_location.html")
