import kivy
kivy.require('1.11.1') # Need this version of kivy to use

print("Kivy version" + kivy.__version__)

# KIVY APP LIFE CYCLE:
# INITIALIZING APP STUFF:
    # Kivy bootstrap initiates (loading essential software after the program is 'booted')
    # Python starts; the run() method is executed in the program
    # the build() function is executed, attemping to "build" the app (if code is present)
    # on_start() internal function is executed if no previous errors occur.
    # Stuff happens with the actual UI (button clicks, mouse clicks, etc.).

# STOPPING APP STUFF:
    # on_stop() is executed when process is terminated
    # The Kivy window is destroyed
    # Python stops running


from kivy.app import App # Make your app inherit from the App class.
from kivy.uix.label import Label # uix module holds UI elements (labels, widgets, etc.).

class MyApp(App): # Defining the class itself

    def build(self): #Self refers to class itself (In this instance: build upon the class)
        return Label(text='Hello World') # Initialize and return Root Widget


if __name__ == '__main__':
    MyApp().run()