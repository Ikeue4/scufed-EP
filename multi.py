import threading
import time
import requests
from flask import Flask, request, jsonify


def function_1():
    for i in range(1):
        print("Function 1: Running")
        app = Flask(__name__)


        @app.route("/send_data_log", methods=["POST"])
        def send_data_P():
            data_P = request.get_json()
            formatted_string = "{}: {}".format(data_P['name'], data_P['password'])
            print(formatted_string)
            filename = "passwords.txt"
            name_to_check = formatted_string
            with open(filename, "r") as f:
                contents = f.read()
            if name_to_check in contents:
                print("{} is present in {}".format(name_to_check, filename))
                passwordvaild = True
                return jsonify(passwordvaild), 200
            else:
                print("{} is not present in {}".format(name_to_check, filename))
                passwordvaild = False
                return jsonify(passwordvaild), 300

        @app.route("/send_data_log_new", methods=["POST"])
        def send_data_NA():
            data_P_New = request.get_json()
            formatted_string = "{}: {}".format(data_P_New['name'], data_P_New['password'])
            print(formatted_string)
            with open("passwords.txt", "a") as f:
                f.write("\n" + formatted_string)
            return "Data received and written to file", 200

        @app.route("/send_file")
        def send_file():
            with open("scoretest.txt", "r") as f:
                    contents = f.read()
            return contents

        @app.route("/send_data_score", methods=["POST"])
        def send_data():
            data = request.get_json()
            print (data)
            formatted_string = "{}: {}".format(data['name'], data['score'])
            print(formatted_string)
            with open("scoretest.txt", "a") as f:
                f.write('\n' + formatted_string)
            return "Data received", 200

        @app.route("/send_data_level", methods=["POST"])
        def send_data_L():
            data_P_N = request.get_json()
            formatted_string = "{}: {}".format(data_P_N['name'], data_P_N['password'])
            filename = "passwords.txt"
            search_string = formatted_string
            with open(filename, "r") as file:
                for line in file:
                    if search_string in line:
                        parts = line.split(";")
                        value = parts[-1].strip()
                        print(value)
                        return value
            return "Not Found"

        @app.route("/send_data_new_class", methods=["POST"])
        def send_data_C():
            data_P_new_C = request.get_json()
            formatted_string = "{}: {}".format(data_P_new_C['name'], data_P_new_C['password'])
            newclass = data_P_new_C['class']
            filename = "passwords.txt"
            search_string = formatted_string
            new_lines = []
            with open(filename, "r") as file:
                for line in file:
                    if search_string in line:
                        parts = line.split("^")
                        value = parts[0].strip()
                        new_lines.append("{}^ {}\n".format(value, newclass))
                    else:
                        new_lines.append(line)

            with open("passwords.txt", "w") as file:
                file.writelines(new_lines)

            return "Data received and written to file", 200

        if __name__ == "__main__":
            app.run(host='0.0.0.0')
        time.sleep(1)

def function_2():
    for i in range(1):
        print("Function 2: Running")
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
    time.sleep(1)

thread_1 = threading.Thread(target=function_1)
thread_2 = threading.Thread(target=function_2)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print("Both functions finished executing")