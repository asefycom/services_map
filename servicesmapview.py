from kivy.garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from servicesmarker import ServicesMarker

class ServicesMapView(MapView):
    start_getting_markers_timer = None
    markers_name = []

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
        markers = app.cursor.fetchall()

        for marker in markers:
            if marker[1] in self.markers_name:
                continue
            else:
                print(marker)
                self.add_servicemarkers(marker)


    def add_servicemarkers(self, marker):
        lat, lon = marker[14], marker[15]
        temp_marker = ServicesMarker(lat=lat, lon=lon)
        temp_marker.marker_data = marker
        self.add_widget(temp_marker)
        self.markers_name.append(marker[1])
