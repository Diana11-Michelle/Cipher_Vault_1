from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.config import Config
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDIconButton
from kivymd.font_definitions import fonts



Config.set('graphics', 'window_backend', 'x11')  # Replace 'x11' with the desired backend
# Other Config settings (optional)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '300')

colors = {
    "Brown": {
        "200": "#212121",
        "500": "#212121",
        "700": "#212121",
    },
    "Red": {
        "200": "#C25554",
        "500": "#C25554",
        "700": "#C25554",
    },
    "Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "#202020",
        "Background": "#2E3032",
        "CardsDialogs": "#FFFFFF",
        "FlatButtonDown": "#CCCCCC",
    },
}

kv = '''
BoxLayout:
    orientation: 'vertical'
  
    MDTextField:
        hint_text: "Enter plain text"
        helper_text: "This is Required"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint_x: .5 
        multiline: True
        mode:"rectangle"

    MDBoxLayout:
        orientation: "vertical"

    MDTopAppBar:
        title: "Cipher Vault"

    MDTabs:
        id: tabs
<Tab>

    MDIconButton:
        id: icon
        icon: root.icon
        icon_size: "48sp"
        theme_icon_color: "Custom"
        icon_color: "white"
        pos_hint: {"center_x": .5, "center_y": .5}
        
    MDSpinner: #Spinner
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': .5, 'center_y': .5}
        active: True if check.active else False
    MDCheckbox:
        id: check
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {'center_x': .5, 'center_y': .4}
        active: True
        #End of spinner
        
        #Bottom Navigation
        
        
        #End of bottom navigation
'''
class Tab(MDFloatLayout, MDTabsBase):
   # '''Class implementing content for a tab.'''
    icon = ObjectProperty()

    def build(self):
         self.add_widget(MDIconButton(
            id=self.icon,
            icon=self.icon,
            icon_size="48sp",
            theme_icon_color="Custom",
            icon_color="white",
            pos_hint={"center_x": .5, "center_y": .5}
        ))
class Test(MDApp):
    icons = list(md_icons.keys())[15:30]


    def build(self):
        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.accent_palette = "Red"

    def build (self):
        for name_tab in self.icons:
            tab = Tab(title="Cipher Vault " + name_tab, icon=name_tab)


        label = MDLabel(
            text='Hello, Kivy!',
            halign='center',
            theme_text_color='Custom',
            text_color=(236 / 255.0, 98 / 255.0, 81 / 255.0, 1),
            font_style='H2'
        )


        return Builder.load_string(kv)

    def pressed(self, instance):
        print("Button pressed")

if  __name__ == '__main__':
    Test().run()
