from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy_garden.mapview import MapView
from kivy.core.window import Window

Window.size = (380, 700)

#   Main Screen Manager
class FlyerManager(ScreenManager):
    pass

#   Sign-in Screen
class SignIn(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

#   Sign-up Screen
class SignUp(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_pre_enter(self): # bind ESC for previous screen
        Window.bind(on_keyboard = self.back)

    def back(self, window, key, *args):
        if key == 27: # When ESC is pressed
            App.get_running_app().root.current = 'sign_in_screen'
            return True
    def on_pre_leave(self, *args): # unbind ESC for previous screen
        Window.unbind(on_keyboard = self.back)

#   Validation Screen 
class Validation(Screen):
    def __init__(self, **kw):
        super(Validation, self).__init__(**kw)

    def on_pre_enter(self): # bind ESC for previous screen
        Window.bind(on_keyboard = self.back)

    def back(self, window, key, *args):
        if key == 27: # When ESC is pressed
            App.get_running_app().root.current = 'sign_up_screen'
            return True
    def on_pre_leave(self, *args): # unbind ESC for previous screen
        Window.unbind(on_keyboard = self.back)

class FlyerMap(MapView):
    pass
#   Main Screen

class FlyerIndex(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def changeLayout(self):
        self.ids.main.add_widget(FlyerMap)
        print('TESTE')
        pass
        

# Runs Application
class Flyer(App):
    def build(self):
        return FlyerManager()

if __name__ == '__main__':
    Flyer().run()