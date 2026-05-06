from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivy.metrics import dp
from components.track_pain_slide import init_db

class HomeScreen(MDScreen):
    pass

class ProfileScreen(MDScreen):
    pass

class TrackingScreen(MDScreen):
    pass

class ResourcesScreen(MDScreen):
    pass

class SettingsScreen(MDScreen):
    pass

class SymptomQForm(MDScreen):
    pass

class DrQForm(MDScreen):
    pass

class MedQForm(MDScreen):
    pass

class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"

        Builder.load_file("kv/screens/home.kv")
        Builder.load_file("kv/screens/profile.kv")
        Builder.load_file("kv/screens/tracking.kv")
        Builder.load_file("kv/screens/resources.kv")
        Builder.load_file("kv/screens/settings.kv")
        Builder.load_file("kv/forms/symptomQForm.kv")
        Builder.load_file("kv/forms/drQForm.kv")
        Builder.load_file("kv/forms/medQForm.kv")

        self.root = Builder.load_file("main.kv")

        #Nav menu items
        menu_items = [
            {
                "text": "Home",
                "on_release": lambda: self.change_screen("home")
            },
            {
                "text": "Profile",
                "on_release": lambda: self.change_screen("profile")
            },
            {
                "text": "Tracking",
                "on_release": lambda: self.change_screen("tracking")
            },
            {
                "text": "Resources",
                "on_release": lambda: self.change_screen("resources")
            },
            {
                "text": "Settings",
                "on_release": lambda: self.change_screen("settings")
            }
            ]
        self.nav_menu = MDDropdownMenu(items=menu_items)

        #Nav menu items
        menu_items = [
            {
                "leading_icon": "magnify", 
                "text": "Add Symptom", 
                "on_release": lambda: self.bubble_callback("symptomQForm"),

            }, 
            { 
                "leading_icon": "stethoscope", 
                "text": "Add Doctor", 
                "on_release": lambda: self.bubble_callback("drQForm") 
            }, 
            {
                "leading_icon": "medication", 
                "text": "Track Medication", 
                "on_release": lambda: self.bubble_callback("medQForm") 
            }
        ]
        self.bubble_menu = MDDropdownMenu(items = menu_items, width = dp(220))

        #initialize track_pain_slide's database functions to use user data
        init_db()

        return self.root

    def on_start(self):
        # IMPORTANT: switch AFTER build is complete
        self.root.ids.sm.current = "home"

    def submit_form(self):
        print("form submitted")
        self.change_screen("home")
        
    #resets current screen
    def change_screen(self, screen_name):
        self.root.ids.sm.current = screen_name
        print("current screen:", screen_name)
        self.nav_menu.dismiss()
        self.bubble_menu.dismiss()
        
    #opens the vertical dots nav menu for the persistent topAppBar
    def open_nav(self, btn):
        self.nav_menu.caller = btn
        self.nav_menu.open()

        #opens the bubble menu for the persistent quick add menu
    def open_bubble(self, btn):
        self.bubble_menu.caller = btn
        self.bubble_menu.open()

    #Controls behavior within the navigation menu
    def nav_callback(self, screen_name):
        self.nav_menu.dismiss()
        self.change_screen(screen_name)
        MDSnackbar(
            MDSnackbarText(
                text=screen_name,
            ),
            y="24dp",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

    #Controls behavior within the persistent bubble menu
    def bubble_callback(self, text_item):
        self.bubble_menu.dismiss()
        self.change_screen(text_item)
        MDSnackbar(
            MDSnackbarText(
                text=text_item,
            ),
            y="24dp",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

    def open_symptom_form(self, form_name):
        self.bubble_menu.dismiss()
        self.change_screen("symptomQForm")

    #Controls URL links in resources screen
    def open_link(self):
        import webbrowser
        webbrowser.open("https://www.ehlers-danlos.com/what-is-eds/")
        webbrowser.open("http://www.triggerpoints.net/")

if __name__ == "__main__":
    MainApp().run()