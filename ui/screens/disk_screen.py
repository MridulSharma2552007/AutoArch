from textual.screen import Screen
from textual.widgets import ListView,ListItem,Label,Header,Footer
from textual.containers import Vertical
from core.disk import get_disks

class DiskScreen(Screen):

    def compose(self):
        disks=get_disks()
        items=[]
        for d in disks:
         text=f'{d['path']}({d['size']})'
         yield Header()
         items.append(ListItem(Label(text)))
        yield ListView(*items)

    def on_list_view_sekect(self,event):
        selected=event.item.query_one(Label).renderable
        self.app.exit(f"Selected: {selected}")