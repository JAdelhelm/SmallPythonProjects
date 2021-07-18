import re
import json

class Username():
    def __init__(self):
        pass

    def get_user(self):
        try:
            with open('username.json') as file:
                username = json.load(file).title()
            option = input(f"Are you {username}? Y or N\n")
            if option == 'N':
                raise Exception
            else:
                print(f"Hi {username}, welcome back!\n")
        except:
            username = input("What is your name?\n")
            with open('username.json','w') as file:
                json.dump(username, file)
