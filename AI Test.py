import requests

print ('\n\nscore = 1\nquestion_1 = "1+1"\nanswer_1 = "2"\nprint(question_1)\nuser_answer_1 = input("Your answer: ")\nif user_answer_1 == answer_1:\n    print("Correct!")\nelse:\nscore += 1\n    print("Incorrect. The correct answer is", answer_1)\ndata_S = {\n            "name": name,\n            "password": password,\n            "score": str(score)\n        }\nprint (data_S)\nresponse = requests.post("http://localhost:5000/send_data_score", json=data_S)\nprint ("score " + str(score))')

name = "joe"
password = "1234"
whatquiz = "1+1"

score = 0
question_1 = "1+1"
answer_1 = "2"
print(question_1)
user_answer_1 = input("Your answer: ")
if user_answer_1 == answer_1:
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is", answer_1)
data_S = {
            "name": name,
            "password": password,
            "score": str(score)
        }
print (data_S)
response = requests.post("http://localhost:5000/send_data_score", json=data_S)

print ("score " + str(score))