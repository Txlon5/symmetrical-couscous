from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse
import random


Window.size=(800, 600)
ColourList = [0, 0, 0]


# TODO: Create random int list for color picker to choose from using 2D list
# TODO: Red, Green, Blue, Yellow, etc.


# Steps to creating a Kivy app
#sub-classing the App class
#implementing its build() method so it returns a Widget instance (the root of your widget tree)
#instantiating this class, and calling its run() method.


class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(255,0,0)
            d = 30
            Ellipse(pos=(touch.x - (d / 2), touch.y - (d / 2)) , size=(d, d))

class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()

if __name__=='__main__':
    MyPaintApp().run()