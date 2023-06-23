from kivy.app import App
from kivy_garden.mapview import MapView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

#Window.clearcolor = (.0, .0, .0, 1)
#Window.clearcolor = (1, 1, 1, 1)

Window.size = (380, 680)

# Runs Application
class FlyerView(App):
    def build(self):
        flyerMap = MapView(zoom=18, lat=-23.5489, lon=-46.6388)
        return flyerMap


if __name__ == '__main__':
    FlyerView().run()