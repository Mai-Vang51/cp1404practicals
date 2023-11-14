"""CP1404 Practical - GUI program to convert miles to kilometres"""


from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

M_KM_CONVERSION = 1.60934


class MilesKmConversion(App):
    output = StringProperty()

    def build(self):
        """Build kivy app from kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output = ""
        return self.root

    def handle_conversion(self, value):
        """Convert valid mile into kilometre"""
        try:
            km_distance = float(value) * M_KM_CONVERSION
            self.output = self.root.ids.output.text = str(km_distance)
        except ValueError:
            self.root.ids.output.text = str(0.0)

    def handle_increment(self, user_input, value):
        """Change mile number via up and down button"""
        try:
            result = float(user_input) + value
            self.root.ids.user_input.text = str(result)
        except ValueError:
            user_input = 0
            result = user_input + value
            self.root.ids.user_input.text = str(result)


MilesKmConversion().run()
