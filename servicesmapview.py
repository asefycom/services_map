from kivy.garden.mapview import MapView
from kivy.clock import Clock

class ServicesMapView(MapView):
    start_getting_markers_timer = None

    def start_getting_markers_in_fov(self):
        try:
            self.start_getting_markers_timer.cancel()
        except:
            pass
        self.start_getting_markers_timer = Clock.schedule_once(self.getting_markers_in_fov, 1)


    def getting_markers_in_fov(self, *args):
        print("Moved!")