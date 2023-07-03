from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.mapview import MapMarkerPopup
from kivy.core.window import Window

Window.size = (380, 700)


class FlyerManager(ScreenManager):
    pass
class SignIn(Screen):
    def __init__(self, **kw):
        super(SignIn, self).__init__(**kw)
    pass

class SignUp(Screen):
    def __init__(self, **kw):
        super(SignUp, self).__init__(**kw)
    def on_pre_enter(self):
        Window.bind(on_keyboard = self.back)
    def back(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'sign_in_screen'
            return True
    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard = self.back)
    pass

class Validation(Screen):
    def __init__(self, **kw):
        super(Validation, self).__init__(**kw)

    def on_pre_enter(self):
        Window.bind(on_keyboard = self.back)

    def back(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'sign_up_screen'
            return True
    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard = self.back)
    pass

class FlyerIndex(Screen):
    def __init__(self, **kw):
        super(FlyerIndex, self).__init__(**kw)
    pass

# Runs Application
class Flyer(App):
    def build(self):
        return FlyerManager()

if __name__ == '__main__':
    Flyer().run()