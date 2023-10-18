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
from kivymd.uix.toolbar import MDToolbar  # Add the import for MDToolbar

Config.set('graphics', 'window_backend', 'x11')  # Replace 'x11' with the desired backend
# Other Config settings (optional)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '300')

kv = '''
<Root>:
    # Bottom Navigation
    MDBottomNavigation:
        MDBottomNavigationItem:
            name: "screen 1"
            YourContent:
        MDBottomNavigationItem:
            name: "screen 2"
            YourContent:
        MDBottomNavigationItem:
            name: "screen 3"
            YourContent:

<YourContent>:
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Bottom navigation'
            md_bg_color: .2, .2, .2, 1
            specific_text_color: 1, 1, 1, 1
        MDBottomNavigation:
            panel_color: .2, .2, .2, 1

            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Python'
                icon: 'language-python'

                MDLabel:
                    text: 'Python'
                    align: 'center'

            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'C++'
                icon: 'language-cpp'

                MDLabel:
                    text: 'I programming of C++'
                    align: 'center'

            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'JS'
                icon: 'language-javascript'

                MDLabel:
                    text: 'JS'
                    align: 'center'
'''

class YourContent(Screen):
    pass

class Test(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_string(kv)

Test().run()
