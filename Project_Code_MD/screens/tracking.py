from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.icon_definitions import md_icons

class TrackingScreen(MDScreen):
    def on_enter(self):
        self.clear_widgets()
        from kivymd.uix.label import MDLabel
        self.add_widget(MDLabel(text="Tracking LOADED"))