from kivymd.uix.boxlayout import MDBoxLayout
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from matplotlib.figure import Figure


class ChartWidget(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        fig = Figure()
        ax = fig.add_subplot(111)

        days = [1, 2, 3, 4, 5, 6, 7]

        pain = [3, 4, 6, 5, 7, 4, 3]
        fatigue = [5, 6, 4, 7, 8, 6, 5]
        sleep = [7, 6, 8, 5, 4, 7, 8]

        ax.plot(days, pain, label="Pain")
        ax.plot(days, fatigue, label="Fatigue")
        ax.plot(days, sleep, label="Sleep")

        ax.set_title("Weekly Symptom Trends")
        ax.set_xlabel("Day")
        ax.set_ylabel("Severity")

        ax.legend()

        self.add_widget(FigureCanvasKivyAgg(fig))

        super().__init__(
        orientation="vertical",
        **kwargs
        )