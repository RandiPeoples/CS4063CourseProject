from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.icon_definitions import md_icons
from components.symptomLineChart import ChartWidget


class TrackingScreen(MDScreen):
    def on_kv_post(self, *args):
        import os
        print("CWD", os.getcwd())
        chart = ChartWidget()
        self.ids.chart_container.add_widget(chart)

        import matplotlib.pyplot as plt
        
        # Placeholder sample data
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        values = [3, 5, 4, 6, 5, 7, 4]

        plt.figure(figsize=(6, 4))
        plt.plot(days, values, marker="o")
        plt.title("Weekly Symptom Trend")
        plt.xlabel("Day")
        plt.ylabel("Severity Score")
        plt.grid(True)

        plt.savefig("placeholder_graph.png")

        
        plt.close()
        print("hey")

    def load_symptoms():
        conn, cur = get_db()

        cur.execute("SELECT symptom, severity, area of pain FROM symptoms")
        data = cur.fetchall()

        conn.close()
        return data
    
    