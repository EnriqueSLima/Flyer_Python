from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (380, 700)

#   Main Screen
class FlyerIndex(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
    pass

#   Main Screen Manager
class FlyerManager(ScreenManager):
    pass

#   Option Screens
class FlyerMap(Screen):
    pass
class FlyerList(Screen):
    pass
class FlyerSearch(Screen):
    pass
class FlyerHome(Screen):
    pass
class FlyerPromo(Screen):
    pass
class FlyerFav(Screen):
    pass
class FlyerSettings(Screen):
    pass

# Runs Application
class Flyer(App):
    def build(self):
        return FlyerIndex()

if __name__ == '__main__':
    Flyer().run()