
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup



KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True

MDScreen:

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager

            #1st screen

            MDScreen:
                name: "scr 1" 
                id:scr1


                MDTopAppBar:
                    title: "Cipher Vault"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]
                MDLabel:
                    text: "Screen 1"
                    halign: "center"
                MDFloatLayout:
                    MDRoundFlatIconButton:
                        text:"Choose File"
                        icon:"file"
                        md_bg_color: "#e7e4c0"
                        text_color: "#4a4939"
                        #creates the file chooser
                        pos_hint:{"center_x": .7, "center_y":.7}
                        on_release: app.open_file_chooser()
                    MDRoundFlatButton:
                        id:selected_path_label
                        text:"Selected Path:"
                        md_bg_color: "#e7e4c0"
                        text_color: "#4a4939"
                        pos_hint:{"center_x": .7, "center_y":.6}
               

                    MDRoundFlatButton:
                        text:"File size"
                        md_bg_color: "#e7e4c0"
                        text_color: "#4a4939"
                        pos_hint:{"center_x": .7, "center_y":.5}
                    MDRoundFlatIconButton:
                        text:"Open File"
                        icon: "mailbox-open"
                        md_bg_color: "#e7e4c0"
                        text_color: "#4a4939"
                        pos_hint:{"center_x": .7, "center_y":.4}
                    MDLabel:
                        id:selected_path_label
                        text: "This is the file path"
                        theme_text_color: "Hint"
                        pos_hint:{"center_x": .6, "center_y":.6}

                    MDLabel:
                        id:selected_file_size
                        text: "This is the file size"
                        theme_text_color: "Hint"
                        pos_hint:{"center_x": .6, "center_y":.5}
                    MDTextField:
                        id: txt
                        multiline: True
                        hint_text: "This is the text display area "
                        halign: "left"
                        pos_hint: {"center_x": .5, "center_y": .3}
                        theme_text_color: "Hint"
                        line_color_focus: "#e7e4c0"
                        icon_left: "email"
                        text_color: app.theme_cls.primary_color

                    MDRectangleFlatButton:
                        text:"Next"
                         # green color with full opacity
                        text_color: "#4a4939"
                        pos_hint:{"center_x": .8, "center_y":.1} 
                        on_press: root.manager.current = 'scr 2'         



            #2nd screen

            MDScreen:
                name: "scr 2"

                MDTopAppBar:
                    title: "Ciper Vault Message extract"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]

                MDLabel:
                    text: "Screen 2"
                    halign: "center"
                MDLabel:
                    id:opened_file
                    text: "Opened File"
                    theme_text_color: "Primary"
                    pos_hint:{"center_x": .5, "center_y":.8}
                MDTextField:
                    id: txt
                    multiline: True
                    hint_text: "This is the opened file with the hidden message "
                    halign: "left"
                    pos_hint: {"center_x": .5, "center_y": .7}
                    theme_text_color: "Hint"
                    line_color_focus: "#e7e4c0"
                    icon_left: "email"
                    text_color: app.theme_cls.primary_color
                MDRoundFlatButton:
                    text:"Extract Secret Message"
                    md_bg_color: "#e7e4c0"
                    text_color: "#4a4939"
                    pos_hint:{"center_x": .2, "center_y":.6}
                MDTextField:
                    id: scrtxt
                    multiline: True
                    hint_text: "Secret message "
                    halign: "left"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    theme_text_color: "Hint"
                    line_color_focus: "#e7e4c0"
                    icon_left: "email"
                    text_color: app.theme_cls.primary_color
                MDRectangleFlatButton:
                    text:"Reply"
                    # color with full opacity
                    text_color: "#4a4939"
                    pos_hint:{"center_x": .8, "center_y":.1} 
                    on_press: root.manager.current = 'scr 2'
                MDRectangleFlatButton:
                    text:"Back"
                    # color with full opacity
                    text_color: "#4a4939"
                    pos_hint:{"center_x": .6, "center_y":.1} 
                    on_press: root.manager.current = 'scr 2'

            #3rd screen
            MDScreen:
                name: "scr 3"

                MDTopAppBar:
                    title: "Ciper Vault Message "
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]

                MDLabel:
                    text: "Screen 3"
                    halign: "center"
                MDFloatLayout:
                    MDRoundFlatIconButton:
                        text:"Choose File"
                        icon:"file"
                        md_bg_color: "#e7e4c0"
                        text_color: "#4a4939"
                        pos_hint:{"center_x": .7, "center_y":.7}
                       
                    MDRoundFlatButton:
                        text:"File Path"
                        md_bg_color: "#e7e4c0"
                        text_color: "#4a4939"
                        pos_hint:{"center_x": .7, "center_y":.6}
                    MDRoundFlatButton:
                        text:"File size"
                        md_bg_color: "#e7e4c0"
                        text_color: "#4a4939"
                        pos_hint:{"center_x": .7, "center_y":.5}
                    MDRoundFlatIconButton:
                        text:"Open File"
                        icon: "mailbox-open"
                        md_bg_color: "#e7e4c0"
                        text_color: "#4a4939"
                        pos_hint:{"center_x": .7, "center_y":.4}
                    MDLabel:
                        id:selected_path
                        text: "This is the file path"
                        theme_text_color: "Hint"
                        pos_hint:{"center_x": .6, "center_y":.6}
                    MDLabel:
                        id:file_size
                        text: "This is the file size"
                        theme_text_color: "Hint"
                        pos_hint:{"center_x": .6, "center_y":.5}
                    MDTextField:
                        id: txt
                        multiline: True
                        hint_text: "This is the text display area "
                        halign: "left"
                        pos_hint: {"center_x": .5, "center_y": .3}
                        theme_text_color: "Hint"
                        line_color_focus: "#e7e4c0"
                        icon_left: "email"
                        text_color: app.theme_cls.primary_color

                    MDRectangleFlatButton:
                        text:"Next"
                        # green color with full opacity
                        text_color: "#4a4939"
                        pos_hint:{"center_x": .8, "center_y":.1} 
                        on_press: root.manager.current = 'scr 2'        
            #4th screen
            MDScreen:
                name: "scr 4"

                MDTopAppBar:
                    title: "Ciper Vault"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]

                MDLabel:
                    text: "Screen 4"
                    halign: "center"
                MDLabel:
                    id:opened_file
                    text: "Opened File"
                    theme_text_color: "Primary"
                    pos_hint:{"center_x": .5, "center_y":.8}
                MDTextField:
                    id: txt
                    multiline: True
                    hint_text: "This is the opened file that will hide the message "
                    halign: "left"
                    pos_hint: {"center_x": .5, "center_y": .7}
                    theme_text_color: "Hint"
                    line_color_focus: "#e7e4c0"
                    icon_left: "email"
                    text_color: app.theme_cls.primary_color
                MDLabel:
                    id:write_msg
                    text: "Write Secret Message"
                    theme_text_color: "Primary"
                    pos_hint:{"center_x": .5, "center_y":.6} 
                MDTextField:
                    id: scrtxt
                    multiline: True
                    hint_text: "Secret message "
                    halign: "left"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    theme_text_color: "Hint"
                    line_color_focus: "#e7e4c0"
                    icon_left: "email"
                    text_color: app.theme_cls.primary_color

                MDRoundFlatButton:
                    text:"Embed Secret Message"
                    md_bg_color: "#e7e4c0"
                    text_color: "#4a4939"
                    pos_hint:{"center_x": .2, "center_y":.4}

                MDLabel:
                    id:output_msg
                    text: "Output"
                    theme_text_color: "Primary"
                    pos_hint:{"center_x": .5, "center_y":.3}
                MDTextField:
                    id: outputscrtxt
                    multiline: True
                    hint_text: "Output message "
                    halign: "left"
                    pos_hint: {"center_x": .5, "center_y": .2}
                    theme_text_color: "Hint"
                    line_color_focus: "#e7e4c0"
                    icon_left: "email"
                    text_color: app.theme_cls.primary_color
                MDRectangleFlatButton:
                    text:"Save File"
                    # color 
                    text_color: "#4a4939"
                    pos_hint:{"center_x": .5, "center_y":.3} 

                MDRectangleFlatButton:
                    text:"Finish"
                    # color with full opacity
                    text_color: "#4a4939"
                    pos_hint:{"center_x": .8, "center_y":.1} 
                    on_press: root.manager.current = 'scr 2'
                MDRectangleFlatButton:
                    text:"Back"
                    # color with full opacity
                    text_color: "#4a4939"
                    pos_hint:{"center_x": .6, "center_y":.1} 
                    on_press: root.manager.current = 'scr 2'

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)
            type:"standard"
            close_on_click:True


            #added but needs adjusting
            #ContentNavigationDrawer:
             #   screen_manager: screen_manager
              #  nav_drawer: nav_drawer



            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Cryptosteg"
                    title_color: "#e7e4c0"
                    source: "logo1.png"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"
                    #title_font_style:""
                    #title_font_size:""

                MDNavigationDrawerLabel:
                    text: "Select Action" 
                    text_halign:"center"

                MDNavigationDrawerDivider:   

                MDNavigationDrawerLabel:
                    text: "Extract"

                DrawerClickableItem:
                    icon: "file"
                    right_text: "+99"
                    text_right_color: "#4a4939"
                    text: "Select file"
                    on_release:
                        root.ids.screen_manager.current = "scr 1"



                DrawerClickableItem:
                    icon: "message-reply-text"
                    text: "Extract message"
                    on_release:
                        root.ids.screen_manager.current = "scr 2"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Hide"

                DrawerClickableItem:
                    icon: "file-document"
                    right_text: "+99"
                    text_right_color: "#4a4939"
                    text: "Select file"
                    on_release:
                        root.ids.screen_manager.current = "scr 3"

                DrawerClickableItem:
                    icon: "message-draw"
                    text: "Embed message"
                    on_release:
                        root.ids.screen_manager.current = "scr 4"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Labels"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Rate App"

                DrawerLabelItem:
                    icon: "account-settings"
                    text: "Settings"
                DrawerLabelItem:
                    icon: "help-circle"
                    text: "Help & Feedback"


'''

class Example(MDApp):


    def build(self):
        self.theme_cls.theme_style = "Dark"  # The name of the color scheme that the application will use"Purple", "Red""Teal"
        return Builder.load_string(KV)


    def open_file_chooser(self):
        # Create a FileChooserListView instance
        file_chooser = FileChooserListView()

        # Define the callback function when a file is selected
        file_chooser.bind(on_submit=self.on_file_selected)

        # Create a popup to contain the file chooser
        popup = Popup(
            title='Select a File',
            content=file_chooser,
            size_hint=(0.8, 0.8),
        )

        # Open the popup
        popup.open()

    def on_file_selected(self, selection):
        if selection:
            selected_file = selection[0]
            self.root.ids.selected_path_label.text = f"Selected path: {selected_file}"
        #prints the selected file path



Example().run()



