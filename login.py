from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.graphics import *

# App Window Options
#Window.clearcolor = (1, 1, 1, 1)
Window.clearcolor = (.0, .0, .0, 1)
Window.size = (360, 640)

#Logotype Declaration
class FlyerLogo(Image):
    pass

# Inputs Declaration
class UserMail(TextInput):
    pass
class UserPass(TextInput):
    pass
class RegisterMail(TextInput):
    pass
class RegisterPass(TextInput):
    pass
class ConfirmPass(TextInput):
    pass
class ValidateMail(TextInput):
    pass

# Buttons Declaration
class LogIn_Btn(Button):
    pass
class Register_Btn(Button):
    pass
class SignUp_Btn(Button):
    pass
class Validate_Btn(Button):
    pass

# Log In screen
class FlyerLogin(Screen):
    pass
# Register Screen
class FlyerSignUp(Screen):
    pass
# Validation Mail Screen
class FlyerValidation(Screen):
    pass
# Log In screen
class FlyerIndex(Screen):
    pass
# Root Layout
class LoginLayout(BoxLayout):
    def build(self):
        my_layout = BoxLayout()
        self = my_layout
        return my_layout

# Root Screen
class FlyerRootScreen(Screen):
    sm = ScreenManager()
    sm.add_widget(FlyerLogin(name ='screen_login'))
    sm.add_widget(FlyerSignUp(name ='screen_signup'))
    sm.add_widget(FlyerSignUp(name ='screen_validation'))


# Runs Application
class FlyerApp(App):
    def build(self):
        return FlyerRootScreen()

if __name__ == '__main__':
    FlyerApp().run()