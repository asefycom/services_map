from kivy.clock import Clock

from customdialogs import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
import certifi
import json

class SearchPopupMenu(MDInputDialog):
    title = "Find a City"
    text_button_ok = "Go!"

    def __init__(self):
        super().__init__()
        self.size_hint = [0.9, 0.3]
        self.events_callback = self.callback

    def open(self):
        super().open()
        Clock.schedule_once(self.set_field_focus, 0.5)

    def callback(self, *args):
        address = self.text_field.text
        if len(address) != 0:
            self.geocode_get_lat_lon(address)


    def geocode_get_lat_lon(self, address):
        address_url = parse.quote(address)
        url = 'https://map.ir/search/v2?text=%s'%(address_url)
        key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImVkOWFkYmI5ODQxZDJmYzBmMzg1MTA3ODQ2Y2MzNDI3MGFmODM2NzRjOGNlMDZiMjU1NThiMWRlYzdkNTc3ODdhMzM4Njg3ZTdiMDI1MzZkIn0.eyJhdWQiOiI5NTQxIiwianRpIjoiZWQ5YWRiYjk4NDFkMmZjMGYzODUxMDc4NDZjYzM0MjcwYWY4MzY3NGM4Y2UwNmIyNTU1OGIxZGVjN2Q1Nzc4N2EzMzg2ODdlN2IwMjUzNmQiLCJpYXQiOjE1OTE1Mzk5MTgsIm5iZiI6MTU5MTUzOTkxOCwiZXhwIjoxNTk0MTMxOTE4LCJzdWIiOiIiLCJzY29wZXMiOlsiYmFzaWMiXX0.h0fP6zQDdnmo0nsCePd0VbH95WKWIlm22JFR1ULWZHptARL45PdsHYHcOt7Z-iaUI1t3T5Ec2obkOeWS6yxtXOi3cOMJlA_NnpaY2xcK49GH5QwVCZnchk1-Fhqxe0Q-SXCBqG4sE_PDeGey8Ftgz9CRoRBeM1HJyEdrAQIo3DeT4uXrfvR5jjFBO0lMuIuskw7rQLlmqZFQv2gydN1UQfoiK8Wlc2nX99liHWO2lUTIPXR97qqAccwxPpZ4LtpiVKsnM0p89XvVN3tI-XkE3bUCl7t1pYkwyYZqazVsOzksJKEg--TJJrw4sS-pZYW2rPukxroHMPjXjY7Gh2p8sQ"
        key_header = {'x-api-key': key}
        UrlRequest(url, on_success=self.success, on_failure=self.failure,
                   on_error=self.error, req_headers=key_header, ca_file=certifi.where())


    def success(self, urlrequest, result):
        print("Success")
        # print(result)
        json_obj_to_str = json.dumps(result)
        pasre_json_str = json.loads(json_obj_to_str)
        lat = pasre_json_str["value"][0]["geom"]["coordinates"][1]
        lon = pasre_json_str["value"][0]["geom"]["coordinates"][0]
        cur_app = App.get_running_app()
        cur_mapview = cur_app.root.ids.mapview
        cur_mapview.center_on(lat, lon)
        self.text_field.text = ""

    def failure(self, urlrequest, result):
        print("Failure")
        print(result)

    def error(self, urlrequest, result):
        print("Error")
        print(result)










