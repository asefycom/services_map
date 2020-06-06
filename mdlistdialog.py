"""
Dialog
======

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Dialogs <https://material.io/design/components/dialogs.html>`_

Example
-------

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.utils import get_hex_from_color

from kivymd.uix.dialog import MDInputDialog, MDDialog
from kivymd.theming import ThemeManager


Builder.load_string('''
<ExampleDialogs@BoxLayout>
    orientation: 'vertical'
    spacing: dp(5)

    MDToolbar:
        id: toolbar
        title: app.title
        left_action_items: [['menu', lambda x: None]]
        elevation: 10
        md_bg_color: app.theme_cls.primary_color

    FloatLayout:
        MDRectangleFlatButton:
            text: "Open input dialog"
            pos_hint: {'center_x': .5, 'center_y': .7}
            opposite_colors: True
            on_release: app.show_example_input_dialog()

        MDRectangleFlatButton:
            text: "Open Ok Cancel dialog"
            pos_hint: {'center_x': .5, 'center_y': .5}
            opposite_colors: True
            on_release: app.show_example_okcancel_dialog()
''')


class Example(MDApp):
    title = "Dialogs"

    def build(self):
        return Factory.ExampleDialogs()

    def callback_for_menu_items(self, *args):
        from kivymd.toast.kivytoast import toast
        toast(args[0])

    def show_example_input_dialog(self):
        dialog = MDInputDialog(
            title='Title', hint_text='Hint text', size_hint=(.8, .4),
            text_button_ok='Yes',
            events_callback=self.callback_for_menu_items)
        dialog.open()

    def show_example_okcancel_dialog(self):
        dialog = MDDialog(
            title='Title', size_hint=(.8, .3), text_button_ok='Yes',
            text="Your [color=%s][b]text[/b][/color] dialog" % get_hex_from_color(
                self.theme_cls.primary_color),
            text_button_cancel='Cancel',
            events_callback=self.callback_for_menu_items)
        dialog.open()


Example().run()
"""

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.dialog import BaseDialog
from kivymd import images_path

Builder.load_string(
    """
#:import images_path kivymd.images_path
#:import webbrowser webbrowser
#:import parse urllib.parse
<ThinLabel@MDLabel>:
    size_hint: 1, None
    valign: 'middle'
    height: self.texture_size[1]

<ThinLabelButton@ThinLabel+MDTextButton>:
    size_hint_y: None
    valign: 'middle'
    height: self.texture_size[1]

<ThinBox@BoxLayout>:
    size_hint_y: None
    height: self.minimum_height
    padding: dp(10), dp(0), dp(10), dp(0)


<MDListDialog>
    title: ""
    BoxLayout:
        orientation: 'vertical'
        padding: dp(15)
        spacing: dp(10)
    
        MDLabel:
            id: title
            text: root.title
            font_style: 'H6'
            halign: 'left' if not root.device_ios else 'center'
            valign: 'top'
            size_hint_y: None
            text_size: self.width, None
            height: self.texture_size[1]
    
        ScrollView:
            id: scroll
            size_hint_y: None
            height:
                root.height - (title.height + dp(48)\
                + sep.height)
    
            canvas:
                Rectangle:
                    pos: self.pos
                    size: self.size
                    source: '{}transparent.png'.format(images_path)
    
            MDList:
                id: list_layout
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(15)
                canvas.before:
                    Rectangle:
                        pos: self.pos
                        size: self.size
                    Color:
                        rgba: [1,0,0,.5]   
                ThinBox:
                    ThinLabel:
                        text: "Name: "
                    ThinLabelButton:
                        text: root.Name
                        on_release:
                            webbrowser.open("http://maps.apple.com/?address="+parse.quote(self.text))
                ThinBox:
                    ThinLabel:
                        text: "State: "
                    ThinLabel:
                        text: root.State
                ThinBox:
                    ThinLabel:
                        text: "City: "
                    ThinLabel:
                        text: root.City
                ThinBox:
                    ThinLabel:
                        text: "Village: "
                    ThinLabel:
                        text: root.Village
                ThinBox:
                    ThinLabel:
                        text: "Phone: "
                    ThinLabel:
                        text: root.Phone
                ThinBox:
                    ThinLabel:
                        text: "Website: "
                    ThinLabelButton:
                        text: root.Website
                        on_release:
                            webbrowser.open(self.text)
                ThinBox:
                    ThinLabel:
                        text: "Instagram: "
                    ThinLabelButton:
                        text: root.Instagram
                        on_release:
                            webbrowser.open(self.text)
                ThinBox:
                    ThinLabel:
                        text: "AccessRoad: "
                    ThinLabel:
                        text: root.AccessRoad
                ThinBox:
                    ThinLabel:
                        text: "Trad. Residence: "
                    ThinLabel:
                        text: root.TraditionalResidence
                ThinBox:
                    ThinLabel:
                        text: "Organic Food: "
                    ThinLabel:
                        text: root.OrganicFood
                ThinBox:
                    ThinLabel:
                        text: "Indigenous Music: "
                    ThinLabel:
                        text: root.IndigenousMusic
                ThinBox:
                    ThinLabel:
                        text: "Score: "
                    ThinLabel:
                        text: root.Score
                ThinBox:
                    ThinLabel:
                        text: "Update Time: "
                    ThinLabel:
                        text: root.Update_Time
        MDSeparator:
            id: sep

"""
)

class MDListDialog(BaseDialog):
    Name = StringProperty("No data")
    State = StringProperty("No data")
    City = StringProperty("No data")
    Village = StringProperty("No data")
    Phone = StringProperty("No data")
    Website = StringProperty("No data")
    Instagram = StringProperty("No data")
    AccessRoad = StringProperty("No data")
    TraditionalResidence = StringProperty("No data")
    OrganicFood = StringProperty("No data")
    IndigenousMusic = StringProperty("No data")
    Score = StringProperty("No data")
    Update_Time = StringProperty("No data")
    background = StringProperty('{}ios_bg_mod.png'.format(images_path))




