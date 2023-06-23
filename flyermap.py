from kivy.app import App
from kivy_garden.mapview import MapView
from kivy_garden.mapview import MapMarkerPopup
from kivy.core.window import Window

#Window.clearcolor = (.0, .0, .0, 1)
#Window.clearcolor = (1, 1, 1, 1)

#Window.size = (380, 680)

# Runs Application
class FlyerView(App):
    def build(self):
        flyerMap = MapView(zoom=16, lat=-23.55044830669224, lon=-46.6387767566324)
        return flyerMap
    def on_start(self):
        marker = MapMarkerPopup(lat=23.55044830669224, lon=-46.6387767566324)
        self.root.add_widget(marker)
        #return super().on_start()

if __name__ == '__main__':
    FlyerView().run()