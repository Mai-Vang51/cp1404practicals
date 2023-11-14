""" CP1404 Practical - Dynamic Label"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class Names(App):
    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.names = ["George", "Mary", "Billy"]

    def build(self):
        """Build kivy app from kv file"""
        self.title = "Name Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_label()
        return self.root

    def create_label(self):
        """Create label for data input and display in app window"""
        for name in self.names:
            name_label = Label(text=name)
            self.root.ids.main.add_widget(name_label)


Names().run()
