from kivymd.app import MDApp

from searchpopupmenu import SearchPopupMenu
from servicesmapview import ServicesMapView
import sqlite3

class MainApp(MDApp):
    database = None
    cursor = None
    search_pop = None

    def on_start(self):
        self.database = sqlite3.connect("mydb.sqlite")
        self.cursor = self.database.cursor()
        self.search_pop = SearchPopupMenu()
        self.theme_cls.primary_palette = "DeepPurple"



MainApp().run()