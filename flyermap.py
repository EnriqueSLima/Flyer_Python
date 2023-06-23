import folium
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import *

#Window.clearcolor = (.0, .0, .0, 1)
#Window.clearcolor = (1, 1, 1, 1)

Window.size = (360, 640)

# Root Screen
class MapRootScreen(Screen):
    flyerMap = folium.Map(location = [-23.5489, -46.6388])
    print(flyerMap)

# Runs Application
class FlyerMap(App):
    def build(self):
        return MapRootScreen()

if __name__ == '__main__':
    FlyerMap().run()