from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json, glob
from datetime import datetime
from pathlib import Path
import random

"""
Kivy organization:
------------------
1. App (MainApp)
2.      ScreenManager(RootWidget)
3.          Screen (LoginScreen)
4.              GridLayout
5.                  Gridlayout
6.                      Label/TextInput/Button
"""

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        # print("Sign up button pressed")
        self.manager.current = "sign_up_screen" 
        #manager is property of Screen.
    
    def login(self, uname, pwd):
        with open('users.json') as userfile:
            users = json.load(userfile)
        if uname in users and users[uname]['password'] == pwd:
            self.manager.transition.direction = 'left'
            self.manager.current = 'login_screen_success'
        else:
            # self.manager.transition.direction = 'left'
            # self.manager.current = 'login_screen_failure'
            self.ids.login_failure.text = "Wrong username or password!"


class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self,uname,pwd):
        # print(f"Username : {uname}, Password: {pwd}")
        with open('users.json') as userfile:
            users = json.load(userfile)
        
        users[uname] = {'username': uname, 
                        'password': pwd,
                        'created' : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
        # print(users)
        with open('users.json','w') as file:
            json.dump(users, file)

        self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def get_quote(self, feeling):
        feeling = feeling.lower()
        available_feelings = glob.glob("quotes/*.txt")
        available_feelings = [Path(filename).stem for filename in available_feelings]
        print(available_feelings)
        if feeling in available_feelings:
            with open('quotes/' + feeling + ".txt") as file:
                quotes = file.readlines()
                print(quotes)
                self.ids.feeling_text.text = random.choice(quotes)
                print("Error fetching quotes")
                print(f"Error opening file {feeling}")
        else:
            self.ids.feeling_text.text = "No available quotes"
                
class ImageButton(ButtonBehavior, HoverBehavior, Image): #Order need to kept inorder to work
    pass

class LoginScreenFailure(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()