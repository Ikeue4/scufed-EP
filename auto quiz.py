import requests
import ast

name = ("joe")
password = ("1234")

while True:
    WhatToDo = input("-------------------------------\nUSER OPTIONS\n-------------------------------\nprofile\njoin class\nmake quiz\ndownload/play quiz  ")
    if WhatToDo == ("profile"):
        data_N = {
            "name": name,
            "password": password
        }
        response = requests.post("http://localhost:5000/send_data_level", json=data_N)
        level = response.text
        print (response.text)
        print ("-------------------------------\nPROFILE\n-------------------------------\n""name: " + name, "password " + password, "level " + level + "\n")
    
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
            outputadd = ('question_1 = "' + question + '"\nanswer_1 = "' + answer + '"\nprint(question_1)\nuser_answer_1 = input("Your answer: ")\nif user_answer_1 == answer_1:\n    print("Correct!")\nelse:\n    print("Incorrect. The correct answer is", answer_1)')
            output = (str(output) + "\n" + str(outputadd))

        wantstoseethecode = input("do you want to see the code?Y/N...")
        if wantstoseethecode == ("Y"):
            print("start of code-------------------------------\n" + output + ("\n\n-------------------------------\nend of code\n"))
            runcode = input ("would you like to run this code?Y/N...")
        
        else:
            runcode = input ("would you like to run this code(the code will be run inside with ast or Abstract Syntax Trees witch provides a way to parse and analyze Python code in a more controlled and secure manner?Y/N...")

        if runcode == ("Y"):
            code = output
            parsed = ast.parse(code)
            exec(compile(parsed, "<string>", "exec"))
            wanttoupload = input("do you want to uplaod you quiz?Y/N...")
            whatisthename = input("what do you want the name of the quiz to be?...")
        
        else:
            wanttoupload = input("do you want to uplaod you quiz(you can only have one quiz on the cloud it will overwrite a old quiz)?Y/N...")
            whatisthename = input("what do you want the name of the quiz to be?...")

        if wanttoupload == ("Y"):
            data_Q = {
                "name": "^" + whatisthename,
                "code": output
            }            
            response = requests.post("http://localhost:5000/send_data_new_quiz", json=data_Q)

    elif WhatToDo == ("download/play quiz"):
        response = requests.get("http://localhost:5000/send_data_ask_quiz")
        contents = response.text
        print(contents)