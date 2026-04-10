from textual.app import App
from textual.widgets import Header, Footer

class Test(App):
    TITLE = "Hello world"
    SUB_TITLE = "My installer"

    def compose(self):
        yield Header()
        yield Footer()

Test().run()