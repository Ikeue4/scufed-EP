from flask import Flask, request, jsonify, make_response

createfile = input("this code needs to make two files on your computer one to hold passwords and profiles and one to save quizes that people uplaod this server can only be seen by you computer and no other computer is uses local host are you ok with this Y/N...")

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


'''@app.route("/send_data_score", methods=["POST"])
def send_data():
    data = request.get_json()
    print (data)
    formatted_string = "{}: {}".format(data['name'], data['score'])
    print(formatted_string)
    with open("scoretest.txt", "a") as f:
        f.write('\n' + formatted_string)
    return "Data received", 200'''

#dose not work
@app.route("/send_data_log_new_name", methods=["POST"])
def send_data_NN():
    data_P_New_N = request.get_json()
    print (data_P_New_N)
    formatted_string1 = "{}:".format(data_P_New_N.get("name", "not found"))
    print (formatted_string1)
    formatted_string2 = "{}:".format(data_P_New_N.get("oldname", "not found"))
    print (formatted_string2)
    filename = "passwords.txt"
    with open(filename, "r") as file:
        content = file.read()

    content = content.replace(formatted_string1, formatted_string2)
    print(content)

    with open(filename, "w") as file:
        file.write(content)
    return "Data received and written to file", 200

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
                s = 'joe: 1234; 9^ yy'
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

if __name__ == "__main__":
    app.run()