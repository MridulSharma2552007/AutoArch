from textual.screen import Screen
from textual.widgets import ListView, ListItem, Label, Header
from textual.containers import Vertical
from core.disk import get_disks
from ui.screens.mode_screen import ModeScreen

ASCII_ART = r"""
   ░███                  ░██                  ░███                        ░██        
  ░██░██                 ░██                 ░██░██                       ░██        
 ░██  ░██  ░██    ░██ ░████████  ░███████   ░██  ░██  ░██░████  ░███████  ░████████  
░█████████ ░██    ░██    ░██    ░██    ░██ ░█████████ ░███     ░██    ░██ ░██    ░██ 
░██    ░██ ░██    ░██    ░██    ░██    ░██ ░██    ░██ ░██      ░██        ░██    ░██ 
░██    ░██ ░██   ░███    ░██    ░██    ░██ ░██    ░██ ░██      ░██    ░██ ░██    ░██ 
░██    ░██  ░█████░██     ░████  ░███████  ░██    ░██ ░██       ░███████  ░██    ░██ 

                                                                             By k4rt_c0b                                                                                   
                                                                                     
                                                                                     
"""


class DiskScreen(Screen):

    CSS = """
    Screen {
        align: center middle;
    }
    #ascii_art{
       
        margin-bottom: 1;
        color: orange;
        text-style: bold;
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
            items[-1].disk_path=d['path']


        yield Header(show_clock=False,icon="⋆˚꩜｡✮⋆˙",)

        yield Vertical(
            Label(ASCII_ART,id="ascii_art"),
            Label("[bold orange]Select Disk to Install Arch Linux [/bold orange]⋆˚꩜  ｡✮⋆˙", id="title"),
            ListView(*items,id="disk_view"),
            id="container"
        )

    

    def on_list_view_selected(self, event):
        selected = event.item.disk_path
        self.app.push_screen(ModeScreen(selected))
