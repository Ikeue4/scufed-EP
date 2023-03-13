try:
    from flask import Flask, request, jsonify, make_response
    print ("flask installed ✔")
except ImportError:
    print("The flask library is not installed ✘")

try:
    import sys
    print ("sys installed ✔")
except ImportError:
    print("The sys library is not installed ✘")

try:
    import random
    print ("random installed ✔")
except ImportError:
    print("The random library is not installed ✘")

try:
    from flask_cors import CORS
    print ("flask_cors installed ✔")
except ImportError:
    print("The flask_cors library is not installed ✘")

print("^_^")

while True:
    createfile = input("This code needs to make two files on your computer: one to hold passwords and profiles, and one to save quizzes that people upload. This server can only be accessed from your computer and cannot be seen by other computers. Do you want to proceed? (Y/N)")
    if createfile.lower() == "n":
        sys.exit()
    elif createfile.lower() == "y":
        break
    else:
        print("Invalid input. Please enter Y or N.")

CS_1 = 0
CS_2 = 0
CS_3 = 0
CS1class = ""
CS2class = ""
CS3class = ""
chats1 = ""
chats2 = ""
chats3 = ""

app = Flask(__name__)
CORS(app)

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
        passwordvaild = "succses"
        return "succses", 200
    else:
        print("{} is not present in {}".format(name_to_check, filename))
        passwordvaild = "fail"
        return jsonify(passwordvaild), 300
    
@app.route("/send_data_log_new", methods=["POST"])
def send_data_NA():
    data_P_New = request.get_json()
    formatted_string = "{}: {}".format(data_P_New['name'], data_P_New['password'])
    print(formatted_string)
    random_number = random.randint(100, 1000)
    with open("passwords.txt", "a") as f:
        f.write("\n" + formatted_string + "; 0^ " + str(random_number))
    return "Data received and written to file", 200


@app.route("/send_file")
def send_file():
    with open("scoretest.txt", "r") as f:
        contents = f.read()
    return contents

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
                parts = value.split("^")
                value1 = parts[0].strip()                
                print(value1)
                return value1
    return "Not Found"

@app.route("/send_data_score", methods=["POST"])
def send_data_NL():
    data_P_NL = request.get_json()
    formatted_string = "{}: {}; {}^".format(data_P_NL['name'], data_P_NL['password'], data_P_NL['score'])
    filename = "passwords.txt"
    s = formatted_string
    result = s.split('; ')[1].split('^')[0]
    result1 = s.split('; ')[0]
    search_string = result1
    with open(filename, "r") as file:
        for line in file:
            if search_string in line:
                parts = line.split(";")
                value = parts[-1].strip()
                parts = value.split("^")
                value1 = parts[0].strip()                
                oldlev = int(value1)
                newlev = int(result)
                newprint = oldlev + newlev
                start = s.index(';') + 2
                end = s.index('^')
                result = s[:start] + str(newprint) + s[end:]
    with open(filename, 'r') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        if result1 in lines[i]:
            # Replace the line with the new line
            lines[i] = result + "\n"
    with open(filename, 'w') as file:
        file.writelines(lines)      
    response = make_response("Success", 200)
    return response

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

@app.route("/send_data_new_quiz", methods=["POST"])
def send_data_Q():
    data_new_Q = request.get_json()
    formatted_string = "{}: {}".format(data_new_Q['name'], data_new_Q['code'])
    filename = "quiz.txt"
    print (formatted_string + '|')
    with open(filename, "a") as f:
        f.write('\n' + formatted_string + '\n|')
    return "succses", 200

@app.route("/send_data_ask_quiz", methods=["GET"])
def send_data_AQ():
    filename = "quiz.txt"
    search_string = ("^")
    values = []
    with open(filename, "r") as file:
        for line in file:
            if search_string in line:
                parts = line.split("^")
                value = parts[0].strip()
                values.append(value)
    if values:
        return values
    else:
        return "error"

@app.route("/send_data_quiz", methods=["POST"])
def send_data_WQ():
    data_new_WQ = request.get_json()
    formatted_string = "{}".format(data_new_WQ.get("quiz", "not found"))
    formatted_string = (formatted_string + ("^:"))
    print (formatted_string)
    filename = "quiz.txt"
    text = []
    with open(filename, "r") as file:
        for line in file:
            text.append(line)
    start_index = -1
    end_index = -1
    sendback_lines = []
    for line in text:
        if formatted_string in line:
            start_index = text.index(line)
        if "|" in line:
            end_index = text.index(line)
            if start_index != -1:
                for i in range(start_index + 1, end_index):
                    sendback_lines.append(text[i])

                start_index = -1
                sendback = '\n'.join(sendback_lines)
    return sendback, 200

@app.route("/send_data_view_class", methods=["POST"])
def send_data_VC():
    data_new_VC = request.get_json()
    print(data_new_VC)
    formatted_string = "{}: {}".format(data_new_VC['name'], data_new_VC['password'])
    print(formatted_string)
    filename = "passwords.txt"
    text = []
    with open(filename, "r") as file:
        for line in file:
            text.append(line)  
    results = []
    for line in text:
        if formatted_string in line:
            parts = line.split("^")
            value = parts[1].strip()
            print(value)
    for line in text:
        if value in line:
            parts = line.split(":")
            people = parts[0].strip()
            s = line
            start = s.index(';') + 1
            end = s.index('^')
            substring = s[start:end]
            ret = people + ' ' + substring
            results.append(ret)
            print(results)
    return ', '.join(results)

@app.route("/class_chat_open", methods=["POST"])
def send_data_CO():
    global CS_1
    global CS_2
    global CS_3
    global CS1class
    global CS2class
    global CS3class
    data_new_CH = request.get_json()
    print(data_new_CH)
    formatted_string = "{}: {}".format(data_new_CH['name'], data_new_CH['password'])
    print(formatted_string)
    filename = "passwords.txt"
    text = []
    with open(filename, "r") as file:
        for line in file:
            text.append(line)  
    results = []
    for line in text:
        if formatted_string in line:
            parts = line.split("^")
            value = parts[1].strip()
            value
            print(value)
    if CS_1 == 0:
        CS1class = value
        CS_1 = CS_1 + 1
        print(CS_1)
        return "CS_1"
    elif CS1class == value:
        CS_1 = CS_1 + 1
        print(CS_1)
        return "CS_1"
    elif CS_2 == 0:
        CS2class = value
        CS_2 = CS_2 + 1
        print(CS_2)
        return "CS_2"
    elif CS2class == value:
        CS_2 = CS_2 + 1
        print(CS_2)
        return "CS_2"        
    elif CS_3 == 0:
        CS3class = value
        CS_3 = CS_3 + 1
        print(CS_3)
        return "CS_3"
    elif CS3class == value:
        CS_3 = CS_3 + 1
        print(CS_3)
        return "CS_3"
    else:
        return "servers full pleses wait"

@app.route("/CS_1", methods=["POST"])
def send_data_CS1():
    global CS_1
    global chats1
    if CS_1 == 0:
        chats1 = ""
    else:
        data_new_chat = request.get_json()
        print (data_new_chat)
        formatted_string = "{}: {}".format(data_new_chat['user'], data_new_chat['mess'])
        print(formatted_string)
        global CS1class
        chats1 = chats1 + "\n" + formatted_string
        print (chats1)
        return chats1

@app.route("/CS_1r", methods=["GET"])
def send_data_CS1r():
    global chats1
    return chats1

@app.route("/CS_2", methods=["POST"])
def send_data_CS2():
    global CS_2
    global chats2
    if CS_2 == 0:
        chats2 = ""
    else:
        data_new_chat = request.get_json()
        print (data_new_chat)
        formatted_string = "{}: {}".format(data_new_chat['user'], data_new_chat['mess'])
        print(formatted_string)
        global CS1class
        chats2 = chats2 + "\n" + formatted_string
        print (chats2)
        return chats2

@app.route("/CS_2r", methods=["GET"])
def send_data_CS2r():
    global chats2
    return chats2

@app.route("/CS_3", methods=["POST"])
def send_data_CS3():
    global CS_3
    global chats3
    if CS_3 == 0:
        chats3 = ""
    else:
        data_new_chat = request.get_json()
        print (data_new_chat)
        formatted_string = "{}: {}".format(data_new_chat['user'], data_new_chat['mess'])
        print(formatted_string)
        global CS1class
        chats3 = chats3 + "\n" + formatted_string
        print (chats3)
        return chats3

@app.route("/CS_3r", methods=["GET"])
def send_data_CS3r():
    global chats3
    return chats3

@app.route("/class_chat_close", methods=["POST"])
def send_data_COD():
    global CS_1
    global CS_2
    global CS_3
    global CS1class
    global CS2class
    global CS3class
    global chats1
    global chats2
    global chats3
    data_new_CH = request.get_json()
    print(data_new_CH)
    formatted_string = "{}: {}".format(data_new_CH['name'], data_new_CH['password'])
    print(formatted_string)
    filename = "passwords.txt"
    text = []
    with open(filename, "r") as file:
        for line in file:
            text.append(line)  
    results = []
    for line in text:
        if formatted_string in line:
            parts = line.split("^")
            value = parts[1].strip()
            value
            print(value)
    if CS1class == value:
        CS_1 = CS_1 - 1
        print(CS_1)
        if CS_1 == 0:
            chats1 = ""
        return "bye" 
    elif CS2class == value:
        CS_2 = CS_2 - 1
        print(CS_2)
        if CS_1 == 0:
            chats1 = ""
        return "bye"       
    elif CS3class == value:
        CS_3 = CS_3 - 1
        print(CS_3)
        if CS_1 == 0:
            chats1 = ""
        return "bye"
    else:
        return "something went wrong"
    
@app.route("/ping", methods=["GET"])
def ping():
    ping = "!server up! running on http://127.0.0.1:5000"
    return ping, 200

if __name__ == "__main__":
    app.run()