import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class UI(GridLayout):
    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.add_widget(Button(text='hey'))
        self.add_widget(Label(text='your mom gay'))

class MyApp(App):

    def build(self):
        return UI()

if __name__ == '__main__':
    MyApp().run()