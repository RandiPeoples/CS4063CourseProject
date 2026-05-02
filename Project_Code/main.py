from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

from screens.login import LoginScreen
from screens.home import HomeScreen
from screens.profile import ProfileScreen
from screens.tracking import TrackingScreen
from screens.resources import ResourcesScreen
from screens.settings import SettingsScreen
from Burger.burger import BurgerNav

class WindowManager(ScreenManager):
    pass

class MyApp(App):

    def build(self):

        Builder.load_file("Burger/burger.kv")
        Builder.load_file("kv/login.kv")
        Builder.load_file("kv/home.kv")
        Builder.load_file("kv/profile.kv")
        Builder.load_file("kv/tracking.kv")
        Builder.load_file("kv/resource.kv")
        Builder.load_file("kv/settings.kv")

        sm = WindowManager()
        root = Builder.load_file("kv/main.kv")
        self.sm = root.ids.sm

        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ProfileScreen(name="profile"))
        sm.add_widget(TrackingScreen(name="tracking"))
        sm.add_widget(ResourcesScreen(name="resources"))
        sm.add_widget(SettingsScreen(name="settings"))
    
        self.menu = DropDown()

        self._add_menu_items("Home", "home")
        self._add_menu_items("Profile", "profile")
        self._add_menu_items("Tracking", "tracking")
        self._add_menu_items("Resources", "resources")
        self._add_menu_items("Settings", "settings")

        return root

    def _add_menu_items(self, label, name):
        bttn = Button(text = label, size_hint_y = None, height = 40)

        bttn.bind(on_release=lambda x: self.switch_to(name))
        self.menu.add_widget(bttn)
    
    def open_nav(self, widget):
        self.menu.open(widget)

    def switch_to(self, screen_name):
        #print("Available screens:", [s.name for s in self.sm.screens])
        #print("Trying to switch to:", screen_name)

        self.menu.dismiss()
        self.sm.current = screen_name

if __name__ == "__main__":
    MyApp().run()