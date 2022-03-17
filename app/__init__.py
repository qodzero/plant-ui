
from kivy.app import App
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

from .view import MainWindow

class MainApp(App):
    colors = QueryDict()
    colors.primary = rgba("#9E7EED")
    colors.secondary = rgba("#1B0B42")
    colors.warning = rgba("#F4D73C")
    colors.danger = rgba("#E86767")
    colors.success = rgba("#88D7CF")
    colors.white = rgba("#FFFFFF")
    colors.grey = rgba("#C4C4C4")
    colors.grey_light = rgba("#F5F5F5")

    fonts = QueryDict()
    fonts.heading = 'assets/fonts/Roboto/Roboto-Bold.ttf'
    fonts.subheading = 'assets/fonts/Roboto/Roboto-Regular.ttf'
    fonts.body = 'assets/fonts/Roboto/Roboto-Light.ttf'
    
    fonts.size = QueryDict()
    fonts.size.h1 = sp(24)
    fonts.size.h2 = sp(22)
    fonts.size.h3 = sp(18)
    fonts.size.h4 = sp(16)
    fonts.size.h5 = sp(14)
    fonts.size.h6 = sp(12)
    def build(self):
        return MainWindow()
