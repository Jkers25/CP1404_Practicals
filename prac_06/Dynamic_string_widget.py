from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label



class DynamicString(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Jake', 'Bob', 'Harry', 'Harold', 'Jim']

    def build(self):

        self.title = "Dynamic Strings"
        self.root = Builder.load_file('dynamic_string.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entriesBox.add_widget(temp_label)


    def clear_all(self):
        self.root.ids.entriesBox.clear_widgets()


DynamicString().run()

