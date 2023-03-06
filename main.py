import requests
import ast
import sys
import time

#checks to see if they are new or not
#problem you only need one charater in a paswerd

print("^_^")

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
            print (password_validation_status)
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
                password_validation_status = "succses"
                break
            elif WAP.upper() == "N":
                print("most functions will break work")
                break
            else:
                print("enter Y/N")
            
    else:
        print("Enter Y/N")

if password_validation_status == ("succses"):
    lev0 = ("[░░░░░░░░░░]")
    lev1 = ("[█░░░░░░░░░]")
    lev2 = ("[██░░░░░░░░]")
    lev3 = ("[███░░░░░░░]")
    lev4 = ("[████░░░░░░]")
    lev5 = ("[█████░░░░░]")
    lev6 = ("[██████░░░░]")
    lev7 = ("[███████░░░]")
    lev8 = ("[████████░░]")
    lev9 = ("[█████████░]")
    lev10 = ("[██████████]")


    while True:
        WhatToDo = input("-------------------------------\nUSER OPTIONS\n-------------------------------\nprofile\njoin class\nview class members\nmake quiz\ndownload/play quiz\nquit\n")
        if WhatToDo == ("profile"):
            data_N = {
                "name": name,
                "password": password
            }
            response = requests.post("http://localhost:5000/send_data_level", json=data_N)

            level = response.text
            levelprogres = lev0
            if response.text == "1":
                levelprogres = lev1
            elif response.text == "2":
                levelprogres = lev2
            elif response.text == "3":
                levelprogres = lev3
            elif response.text == "4":
                levelprogres = lev4
            elif response.text == "5":
                levelprogres = lev5
            elif response.text == "6":
                levelprogres = lev6
            elif response.text == "7":
                levelprogres = lev7
            elif response.text == "8":
                levelprogres = lev8
            elif response.text == "9":
                levelprogres = lev9
            else:
                levelprogres = lev10

            print ("-------------------------------\nPROFILE\n-------------------------------\n""name: " + name, "password " + password, "level " + level + " progres to goal(level 10)" + levelprogres + "\n")
        
        elif WhatToDo == ("join class"):
            newclass = input ("what is your class code ")
            data_C = {
                "name": name,
                "password": password,
                "class": newclass
            }
            response = requests.post("http://localhost:5000/send_data_new_class", json=data_C)

        elif WhatToDo == ("make quiz"):
            output = ("\n")

            while True:
                questionamount = input("how many questions do you want (limit of 5 and hole numbers)? ")
                questionamount = int(questionamount)
                if questionamount >= 1 and questionamount <= 5 and isinstance(questionamount, int):
                    break
                else:
                    print("between 1 and 5")

        
            for i in range(questionamount):
                question = input("what is the question?...")
                answer = input("what is the answer to this question?...")
                outputadd = ('score = 0\nquestion_1 = "' + question + '"\nanswer_1 = "' + answer + '"\nprint(question_1)\nuser_answer_1 = input("Your answer: ")\nif user_answer_1 == answer_1:\n    print("Correct!")\nelse:\n    score += 1\n    print("Incorrect. The correct answer is", answer_1)\ndata_S = {\n            "name": name,\n            "password": password,\n            "score": str(score)\n        }\nprint (data_S)\nresponse = requests.post("http://localhost:5000/send_data_score", json=data_S)\nprint ("score " + str(score))')
                output = (str(output) + "\n" + str(outputadd))

            wantstoseethecode = input("do you want to see the code?Y/N...")
            if wantstoseethecode == ("Y"):
                print("start of code\n-------------------------------\n" + output + ("\n\n-------------------------------\nend of code\n"))
            
            runcode = input ("would you like to run this code(the code will be run inside with ast or Abstract Syntax Trees witch provides a way to parse and analyze Python code in a more controlled and secure manner)?Y/N...")

            if runcode == ("Y"):
                code = output
                parsed = ast.parse(code)
                exec(compile(parsed, "<string>", "exec"))
            
            wanttoupload = input("do you want to uplaod you quiz?Y/N...")

            if wanttoupload == ("Y"):
                whatisthename = input("what do you want the name of the quiz to be?...")

            if wanttoupload == ("Y"):
                data_Q = {
                    "name":"#" + whatisthename + "^",
                    "code": output
                }            
                response = requests.post("http://localhost:5000/send_data_new_quiz", json=data_Q)

        elif WhatToDo == ("download/play quiz"):
            response = requests.get("http://localhost:5000/send_data_ask_quiz")
            contents = response.text
            print('\nplease one of the names below (includ the # but not the " and other stuff\n-------------------------------\n' + contents + '-------------------------------')
            whatquiz = input()
            data_WQ = {
                "quiz":whatquiz
            } 
            response = requests.post("http://localhost:5000/send_data_quiz", json=data_WQ)
            contents_quiz = response.text
            loadedquiz = contents_quiz
            print(loadedquiz)
            runcode = input ("would you like to run this quiz in AST?Y/N...")
            if runcode == ("Y"):
                code = loadedquiz
                parsed = ast.parse(code)
                exec(compile(parsed, "<string>", "exec"))

        elif WhatToDo == ("view class members"):
            data_VC = {
                "name": name,
                "password": password
            }
            response = requests.post("http://localhost:5000/send_data_view_class", json=data_VC)
            poepleinclass = response.text
            print ("\n-------------------------------\n" + "class\n-------------------------------\n" + poepleinclass)

        elif WhatToDo == ("quit"):
            sys.exit()

else:
    sys.exit()
