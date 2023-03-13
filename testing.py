import requests
import time
import threading

def function_1():
    for i in range(1):
        print("Function 1: Running")
        while True:
            response = requests.get("http://localhost:5000/ping")
            server = response.text
            print("\033[32m" + server, "\033[32m✔\033[0m")
            time.sleep(1)

def function_2():
    for i in range(1):
        print("Function 2: Running")
        while True:
            response = requests.get("http://localhost:5000/ping")
            server = response.text
            print("\033[32m" + server, "\033[32m✔\033[0m")
            time.sleep(1)

def function_3():
    for i in range(1):
        print("Function 3: Running")
        while True:
            response = requests.get("http://localhost:5000/ping")
            server = response.text
            print("\033[32m" + server, "\033[32m✔\033[0m")
            time.sleep(1)

def function_4():
    for i in range(1):
        print("Function 4: Running")
        while True:
            response = requests.get("http://localhost:5000/ping")
            server = response.text
            print("\033[32m" + server, "\033[32m✔\033[0m")
            time.sleep(1)

thread_1 = threading.Thread(target=function_1)
thread_2 = threading.Thread(target=function_2)
thread_3 = threading.Thread(target=function_3)
thread_4 = threading.Thread(target=function_4)

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

print("all good")