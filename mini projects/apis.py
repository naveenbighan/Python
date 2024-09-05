import requests
import json
x=requests.get("https://www.w3schools.com")
print(x.status_code)
print(x)


x= requests.get("https://swapi.dev/api/people/1/")
a=x.json()

print(f"person name is {a['name']}")
print(f"person height:{a['height']} person mass:{a['mass']}")

hello = """{
	"name": "Leia Organa",
	"height": "150",
	"mass": "49",
	"hair_color": "brown",
	"skin_color": "light",
	"eye_color": "brown",
	"birth_year": "19BBY",
	"gender": "female",
	"homeworld": "https://swapi.dev/api/planets/2/",
	"films": [
		"https://swapi.dev/api/films/1/",
		"https://swapi.dev/api/films/2/",
		"https://swapi.dev/api/films/3/",
		"https://swapi.dev/api/films/6/"
	],
	"species": [],
	"vehicles": [
		"https://swapi.dev/api/vehicles/30/"
	],
	"starships": [],
	"created": "2014-12-10T15:20:09.791000Z",
	"edited": "2014-12-20T21:17:50.315000Z",
	"url": "https://swapi.dev/api/people/5/"
}"""


a = json.loads(hello)
a["name"]="Naveen kumar"
print(a)
print(a["films"])

