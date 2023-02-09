import requests

name = ("joe")
password = ("1234")

while True:
    WhatToDo = input("USER OPTIONS\nprofile\njoin class\ndownload/play quiz  ")
    if WhatToDo == ("profile"):
        data_N = {
            "name": name,
            "password": password
        }
        response = requests.post("http://localhost:5000/send_data_level", json=data_N)
        level = response.text
        print (response.text)
        print ("PROFILE\n""name: " + name, "password " + password, "level " + level + "\n")
    
    elif WhatToDo == ("join class"):
        newclass = input ("what is your class code ")
        data_C = {
            "name": name,
            "password": password,
            "class": newclass
        }
        response = requests.post("http://localhost:5000/send_data_new_class", json=data_C)