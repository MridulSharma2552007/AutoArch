from textual.screen import Screen
from textual.widgets import ListView, ListItem, Label, Header, Footer
from textual.containers import Vertical
from core.disk import get_disks

class DiskScreen(Screen):

    CSS = """
    Screen {
        align: center middle;
    }

    #container {
        width: 60%;
        height: 70%;
        border: round orange;
        padding: 1 2;
    }

    #title {
        text-align: center;
        text-style: bold;
        
        margin-bottom: 1;
    }

    ListView {
        height: 1fr;
        border: solid orange;
    }

#disk_view {
    border: round orange;
}

#disk_view ListItem {
    color: white;
}

#disk_view ListItem:focus {
    background: transparent;
}

#disk_view ListItem:focus Label {
    color: orange;
    text-style: bold;
}
    """

    def compose(self):
        disks = get_disks()

        items = []
        for d in disks:
            text = f"{d['path']} ({d['size']})"
            items.append(ListItem(Label(text)))

        yield Header(show_clock=False,icon="⋆˚꩜｡✮⋆˙",)

        yield Vertical(
            Label("[bold orange]Select Disk to Install Arch Linux [/bold orange]⋆˚꩜  ｡✮⋆˙", id="title"),
            ListView(*items,id="disk_view"),
            id="container"
        )

    

    def on_list_view_selected(self, event):
        selected = event.item.query_one(Label).renderable
        self.app.exit(f"Selected: {selected}")