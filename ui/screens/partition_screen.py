from textual.screen import Screen
from textual.widgets import Label, ListView, ListItem
from textual.containers import Vertical
from core.disk import get_partitions

class PartitionScreen(Screen):

    def __init__(self, disk):
        super().__init__()
        self.disk = disk

    def compose(self):
        parts = get_partitions(self.disk)

        items = []

        for p in parts:
            text = f"{p['path']} ({p['size']}) {p['mount']}"
            item = ListItem(Label(text))
            item.partition = p
            items.append(item)

        yield Vertical(
            Label(f"[bold cyan]Disk:[/bold cyan] {self.disk}"),
            Label("Select a partition:"),
            ListView(*items)
        )

    def on_list_view_selected(self, event):
        selected = event.item.partition
        self.app.exit(f"Selected partition: {selected['path']}")