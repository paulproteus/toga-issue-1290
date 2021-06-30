"""
My Repro
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

def my_callback(field):
    print(field.validate())

def is_x_validator(val):
    if val == 'x':
        return None
    return 'too bad, i was looking for x'


class Repro(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        field = toga.TextInput(on_change=my_callback, validators=[is_x_validator])
        main_box = toga.Box(children=[field])

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return Repro()
