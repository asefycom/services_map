from kivy.garden.mapview import MapMarkerPopup
from servicesmarkerpopup import ServicesMarkerPopup

class ServicesMarker(MapMarkerPopup):
    marker_data = []

    def on_release(self):
        pop = ServicesMarkerPopup(self.marker_data)
        pop.open()