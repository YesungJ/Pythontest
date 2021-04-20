#Theory Chapter3
#about immutable sequence
#tuple is immutable
days = ("mon", "tue" , "web", "thur","fri")

print(type(days))

name = "nico"
age = 29
korean = True

#make dictionary
#apple = ringo, people = saram etc...
#key and value
nico = {
  "name": "Jang",
  "age": 29,
  "korean": True,
  "fav_food": ["kimchi", "sushi"]
}

print(nico)
nico["handsome"] = True
print(nico)