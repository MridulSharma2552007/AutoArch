from textual.app import App
from  ui.screens.disk_screen import DiskScreen
 
class AutoArchApp(App):

 def on_mount(self):
     self.push_screen(DiskScreen())