from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.properties import StringProperty, NumericProperty, ColorProperty, ListProperty

Builder.load_file('views/plant/plant.kv')
class PlantView(BoxLayout):
    name = StringProperty("")
    source = StringProperty("")
    subtitle = StringProperty("Juicy and delicious")
    bcolor = ColorProperty([1,1,1,1])
    price = NumericProperty(0.0)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
