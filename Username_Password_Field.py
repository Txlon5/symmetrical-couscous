from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.core.window import Window
from kivy.config import Config


    # Astericks mean a variable number of function parameters. One asterick will return
# all of the function parameters as a tuple (immutable list); Two astericks will return
# all of the keyword arguments (stored in a dictionary) which are passed into the function

# def foo (*args):                  def boo (**kargs):
    # for a in args:                    for a in args
        # print(a)                          print(a, kwargs[a]) get dictionary location

# foo (1, 2, 3)                     boo(name = 'one', age=27)
    # 1                                 age 27
    # 2                                 name one
    # 3

#"The LoginScreen class overwrites the init method of GridLayout, so,
#since you still want LoginScreen to be initialized like a normal GridLayout,
#you call super, which is a function that will call the init method of GridLayout
#for you, while still allowing you to make changes afterwards in the rest of the
#init method of LoginScreen".

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        self.cols = 2 # Set properties for the class itself
        self.add_widget(Label(text='Username'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()