import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + "!@#$%^&*()"
numbers = "12345678"

url = "https://www.battlesure.net/steam/login";

names = json.loads(open("names.json").read())

lastnames = json.loads(open("lastnames.json").read())

animals = json.loads(open("animals.json").read())
users = json.loads(open("users.json").read())
passwords = json.loads(open("passwords.json").read())



for user in users:
    name_extra = "".join(random.choice(string.digits))
    # username = name.lower() + name_extra + "@google.com"
    username = random.choice(users) 
    # password = random.choice(animals) + "".join(random.choice(numbers) for i in range(8))
    password = random.choice(passwords)

    requests.post(url, allow_redirects=False, data={
        "login": username,
        "password": password
    })
    print('sending %s username and %s password' % (username, password))



