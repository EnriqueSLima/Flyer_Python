from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (380, 700)

#   Main Screen
class MainLogin(BoxLayout):
    pass
#   Main Screen Manager
class LoginManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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
            App.get_running_app().root.ids.main_manager.current = 'sign_in_screen'
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
            App.get_running_app().root.ids.main_manager.current = 'sign_up_screen'
            return True
    def on_pre_leave(self, *args): # unbind ESC for previous screen
        Window.unbind(on_keyboard = self.back)

# Runs Application
class Login(App):
    def build(self):
        return MainLogin()
if __name__ == '__main__':
    Login().run()