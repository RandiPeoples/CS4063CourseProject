from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.icon_definitions import md_icons

class ResourcesScreen(MDScreen):
    def on_enter(self):
        print("entered resources")
        if not self.children:
            self.add_widget(
                MDLabel(
                    text="PYTHON RESOURCES WORKS",
                    halign="center"
                )
            )

    #Helps control URLs
    import webbrowser

    def open_link():
        webbrowser.open("https://www.ehlers-danlos.com/what-is-eds/")
        webbrowser.open("http://www.triggerpoints.net/")

        