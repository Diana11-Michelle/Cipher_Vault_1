# filechooser_screen.py

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.filemanager import MDFileManager

Builder.load_file("filechooser_screen.kv")

class FileChooserScreen(Screen):
    def open_file_chooser(self):
        filemanager = MDFileManager(exit_manager=self.exit_manager, select_path=self.select_path)
        filemanager.show('/')

    def exit_manager(self, *args):
        pass  # Handle the exit event here

    def select_path(self, path):
        selected_path_label = self.ids.selected_path_label
        selected_path_label.text = f"Selected Path: {path}"
