from json import load as json_load

class Passman:
    def __init__(self):
        with open('creds.txt') as file:
            creds = json_load(file)
            self.login = creds['login']
            self.password = creds['password']
