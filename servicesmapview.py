from kivy.garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App

class ServicesMapView(MapView):
    start_getting_markers_timer = None

    def start_getting_markers_in_fov(self):
        try:
            self.start_getting_markers_timer.cancel()
        except:
            pass
        self.start_getting_markers_timer = Clock.schedule_once(self.getting_markers_in_fov, 1)


    def getting_markers_in_fov(self, *args):
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        sql_stamtement = "SELECT * FROM main WHERE latitude > %s AND latitude < %s AND longitude > %s AND longitude < %s"%(min_lat, max_lat, min_lon, max_lon)
        app.cursor.execute(sql_stamtement)
        markets = app.cursor.fetchall()
        print(markets)