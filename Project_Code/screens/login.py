from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class LoginScreen(Screen):
    error_message = StringProperty("")

    #hardcoded for now TODO: replace with actual auth later!!!!!!!!!!
    def validate_login(self, username, password):
        if username == "admin" and password == "1234":
            self.error_message = "Login successful!"
            self.manager.current = "home"
        else:
            self.error_message = "Login Unsuccessful!"

    def on_kv_post(self, base_widget):
        print("KV bound to LoginScreen!")

    