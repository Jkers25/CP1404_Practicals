from kivy.app import App
from kivy.lang import Builder

class miles_to_kilometres(App):
    def build(self):
        self.title = "Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres.kv')

    def handle_calculate_miles_to_kilometres(self, miles):
        miles = test(miles)
        kilometres = miles * 1.621371
        self.root.ids.output_label.text = str(kilometres)
        return self.root

    def handle_up(self, miles):
        miles = test(miles)
        miles += 1
        self.root.ids.miles_input.text = str(miles)

    def handle_down(self, miles):
        miles = test(miles)
        miles -= 1
        self.root.ids.miles_input.text = str(miles)


def test(user_input):
    try:
        if user_input != '':
            miles = int(user_input)
        else:
            miles = 0
    except ValueError:
            miles = 0

    return miles


miles_to_kilometres().run()
