from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel


class SettingsScreen(MDScreen):
    
    def on_enter(self):
        
        if not self.children:
            
            self.add_widget(MDLabel(text="Settings LOADED", halign="center"))