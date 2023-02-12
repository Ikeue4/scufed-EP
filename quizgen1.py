import requests

output = ("\n")

while True:
    questionamount = input("how many questions do you want (limit of 5 and hole numbers)? ")
    questionamount = int(questionamount)
    if questionamount >= 1 and questionamount <= 5 and isinstance(questionamount, int):
        break
    else:
        print("between 1 and 5")

    
for i in range(questionamount):
    question = input("what is the first question?...")
    answer = input("what is the answer to this question")
    outputadd = ('question_1 = "' + question + '"\nanswer_1 = "' + answer + '"\nprint(question_1)\nuser_answer_1 = input("Your answer: ")\nif user_answer_1 == answer_1:\n    print("Correct!")\nelse:\n    print("Incorrect. The correct answer is", answer_1)')
    output = (str(output) + "\n" + str(outputadd))

print(output)






'''
questionfab = ('')

print("Python Quiz")
print("-----------")

# Question 1
question_1 = "What is the output of print(2 + 3)?"
answer_1 = "5"
print(question_1)
user_answer_1 = input("Your answer: ")
if user_answer_1 == answer_1:
    print("Correct!")
else:
    print("Incorrect. The correct answer is", answer_1)

# Question 2
question_2 = "What is the data type of the result of 5 / 2?"
answer_2 = "float"
print(question_2)
user_answer_2 = input("Your answer: ")
if user_answer_2 == answer_2:
    print("Correct!")
else:
    print("Incorrect. The correct answer is", answer_2)

# Question 3
question_3 = "What is the value of x after executing x = [1, 2, 3]?"
answer_3 = "[1, 2, 3]"
print(question_3)
user_answer_3 = input("Your answer: ")
if user_answer_3 == answer_3:
    print("Correct!")
else:
    print("Incorrect. The correct answer is", answer_3)

print("-----------")
print("Quiz complete!")'''