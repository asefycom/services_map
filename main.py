from kivymd.app import MDApp
from servicesmapview import ServicesMapView
import sqlite3

class MainApp(MDApp):
    database = None
    cursor = None

    def on_start(self):
        self.database = sqlite3.connect("mydb.sqlite")
        self.cursor = self.database.cursor()



MainApp().run()