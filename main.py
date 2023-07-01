from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (380, 700)


class FlyerManager(ScreenManager):
    pass
class SignIn(Screen):
    pass
class SignUp(Screen):
    pass



# Runs Application
class Flyer(App):
    def build(self):
        return FlyerManager()

if __name__ == '__main__':
    Flyer().run()