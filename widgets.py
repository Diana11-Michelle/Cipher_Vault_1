from kivymd.app import MDApp
from kivy import app
from kivymd.uix.label import MDLabel
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

Config.set('graphics', 'window_backend', 'x11')
# Replace 'x11' with the desired backend
# Other Config settings (optional)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '300')


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols=1
        self.inside = GridLayout()
        self.inside.cols=2

        self.inside.add_widget(MDLabel(text=" First Name: ", halign ='center', theme_text_color='Secondary', text_color=(236/255.0,98/255.0,81/255.0,1), font_style='H3')) #for TTC we have "Primary,Secondary,hint,error
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)
        #another widget
        self.inside.add_widget(MDLabel(text="Last Name: ", halign='center', theme_text_color='Secondary',
                                text_color=(236 / 255.0, 98 / 255.0, 81 / 255.0, 1),
                                font_style='H3'))  # for TTC we have "Primary,Secondary,hint,error
        self.Lastname = TextInput(multiline=False)
        self.inside.add_widget(self.Lastname)
        #another widget
        self.inside.add_widget(MDLabel(text="Email: ", halign ='center', theme_text_color='Secondary', text_color=(236/255.0,98/255.0,81/255.0,1), font_style='H3')) #for TTC we have "Primary,Secondary,hint,error
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)
        # another widget
        self.inside.add_widget(MDLabel(text="Contact: ", halign='center', theme_text_color='Secondary',
                                text_color=(236 / 255.0, 98 / 255.0, 81 / 255.0, 1),
                                font_style='H3'))  # for TTC we have "Primary,Secondary,hint,error
        self.contact = TextInput(multiline=False)
        self.inside.add_widget(self.contact)

        self.add_widget(self.inside)
        #a button
        self.submit = Button(text='Submit', font_size='40',background_color=(1,0,0,1))
        self.submit.bind(on_press=self.pressed) #this line binds a fxn "pressed" to the button when pressed
        self.add_widget(self.submit)

        #a function for the button when pressed
    def pressed (self, instance):
        name = self.name.text
        lastname = self.Lastname.text
        email = self.email.text
        contact = self.contact.text
        print("Name:",name,"Last Name:",lastname,"Email:",email,"Conact:",contact) #prints the values in the grids
        #to clear what is in the box
        self.name.text=""
        self.Lastname.text=""
        self.email.text=""
        self.contact.text=""
class Test(MDApp):
    def build(self):
        # Add your GUI code here

        return MyGrid()


if __name__ == "__main__":
    Test().run()






