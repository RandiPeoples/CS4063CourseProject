from components.track_pain_slide import get_db

class SymptomQForm(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("INIT SymptomQForm loaded")
        print("HAS change_value:", hasattr(self, "change_value"))
        
    def save_form(self):
        name = self.ids.symptom_input.text
        severity = int(self.ids.symptom_lvl.value)
        area = self.ids.symptom_area.text

        conn, cur = get_db()

        cur.execute("""
            INSERT INTO symptoms (name, severity, area)
            VALUES (?, ?, ?)
        """, (name, severity, area))

        conn.commit()
        conn.close()

        print("Saved to database")

    def change_value(self, delta):
        self.value = 5
        self.ids.number_field.text = str(self.value)

        field = self.ids.number_field

        text = (field.text or "").strip()

        if not text.isdigit():
            value = 0
        else:
            value = int(text)

        value = max(0, min(10, value + delta))
        field.text = str(value)

    def on_kv_post(self, *args):
        print("SCREEN LOADED:", self)
        print("Has change_value?", hasattr(self, "change_value"))
        