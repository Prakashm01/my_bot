import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

# Get the current ISS data
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

# Save data to a text file
file = open("iss.txt", "w")
file.write("There are currently " +
            str(result["number"]) + " astronauts on the ISS: \n\n")
people = result["people"]

# Save the crew names to the file
for p in people:
    file.write(p['name'] + " - on board" + "\n")

# Get current latitude and longitude
g = geocoder.ip('me')
file.write("\nYour current lat / long is: " + str(g.latlng))
file.close()

# Open the text file in the browser
webbrowser.open("iss.txt")

# Setup the world map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# Load the world map image
screen.bgpic("images/map.gif")
screen.bgpic("imagesvlc")
screen.register_shape("images/iss.gif")
iss = turtle.Turtle()
iss.shape("images/iss.gif")
iss.setheading(45)
iss.penup()
print("my nw chnges")


print("hey this is the chinu")
while True:
    
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    
    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']

    
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    
    iss.goto(lon, lat)

  
    time.sleep(5)
