import requests
import time

score = ("0")

#checks to see if they are new or not
#problem you only need one charater in a paswerd

while True:
    hasacc = input("Do you have an account Y/N? ")
    if hasacc.upper() == "Y":
        time.sleep (1)
        name = input("What is your name? ")
        password = input("What is your password? ")
        data_P = {
            "name": name,
            "password": password
        }
        response = requests.post("http://localhost:5000/send_data_log", json=data_P)
        if response.status_code == 200:
            print("Password validation status received")
            # You can extract the password validation status from the response text
            password_validation_status = response.text
            print ("succses")
            break
        else:
            print ("password or name is incorrect please try again or make a account")
        time.sleep (1)
    elif hasacc.upper() == "N":
        while True:
            WAP = input("Do you want to make an account? Y/N? ")
            if WAP.upper() == "Y":
                name_new = input("What is your name? ")
                password_new = input("What would your password be? ")
                data_P_New = {
                    "name": name_new,
                    "password": password_new
                }
                response = requests.post("http://localhost:5000/send_data_log_new", json=data_P_New)
                break
            elif WAP.upper() == "N":
                print("Some functions will not work")
            else:
                print("enter Y/N")
            break
    else:
        print("Enter Y/N")




response = requests.get("http://localhost:5000/send_file")
file_contents = response.text

print (file_contents)

data = {
    "name": name,
    "score": score
}
response = requests.post("http://localhost:5000/send_data_score", json=data)