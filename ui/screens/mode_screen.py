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
        auto_item = ListItem(Label("Use entire disk (Auto)"))
        auto_item.mode_key = "auto"

        manual_item = ListItem(Label("Manual partitioning"))
        manual_item.mode_key = "manual"

        dual_item = ListItem(Label("Dual boot (use free space)"))
        dual_item.mode_key = "dual"

        yield Vertical(
            Label(f"[bold orange]Disk:[/bold orange] {self.disk}"),
            Label("Select installation type:"),
            ListView(
                auto_item,
                manual_item,
                dual_item,
            )
            ,id="container"
        )
    def on_list_view_selected(self, event):
     choice = getattr(event.item, "mode_key", None)

     if choice == "auto":
        self.app.exit("Auto install selected")
     elif choice == "manual":
        self.app.exit("Manual install selected")
     elif choice == "dual":
        self.app.exit("Dual boot selected")
     else:
        self.app.exit("Unknown install Selected")
