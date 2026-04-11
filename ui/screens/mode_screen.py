from textual.screen import Screen
from textual.widgets import Label,ListView,ListItem
from textual.containers import Vertical

class ModeScreen(Screen):

    CSS="""
    Screen {
        align: center middle;
    }

    #container {
        width: 60%;
        height: 70%;
        border: round orange;
        padding: 1 2;
    }
        ListView {
        height: 1fr;
        border: solid orange;
    }
    """

    def __init__(self,disk):
        super().__init__()
        self.disk = disk

    def compose(self):
        yield Vertical(
            Label(f"[bold orange]Disk:[/bold orange] {self.disk}"),
            Label("Select installation type:"),
            ListView(
                ListItem(Label("Use entire disk (Auto)")),
                ListItem(Label("Manual partitioning")),
                ListItem(Label("Dual boot (use free space)")),
            )
            ,id="container"
        )
    def on_list_view_selected(self, event):
        choice = event.item.query_one(Label).renderable
        self.app.exit(f"{choice} selected on {self.disk}")
        # test