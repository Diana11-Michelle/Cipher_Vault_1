from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp

class MyWidget(GridLayout):
    pass

class FileChooserWindow(MDApp):
    def build(self):


        return MyWidget()

if __name__ =="__main__":
    window = FileChooserWindow()
    window.run()
