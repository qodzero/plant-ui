from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp
from kivy.clock import Clock
from kivy.utils import rgba, QueryDict
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import SwapTransition
from kivy.properties import StringProperty, NumericProperty, ColorProperty, ListProperty

Builder.load_file('views/home/home.kv')
class Home(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        colors = App.get_running_app().colors
        products = [
            {
                'name': 'Pineapple',
                'source': 'assets/imgs/pineapple.png',
                'avatar': 'assets/imgs/pineapple-square.png',
                'price': 25,
                'color': colors.success, # any kivy color will do
                'categories': ['popular', 'discounts']
            },
            {
                'name': 'Blackberry',
                'source': 'assets/imgs/berry.png',
                'avatar': 'assets/imgs/berry-square.png',
                'price': 32,
                'color': colors.primary, # any kivy color will do
                'categories': ['popular', 'sun-kissed berries']
            },
            {
                'name': 'Apples',
                'source': 'assets/imgs/apple.png',
                'avatar': 'assets/imgs/apple-square.png',
                'price': 25,
                'color': colors.danger, # any kivy color will do
                'categories': ['popular', 'gold apples']
            },
            {
                'name': 'Avocado',
                'source': 'assets/imgs/avocado.png',
                'avatar': 'assets/imgs/avocado-square.png',
                'price': 28.45,
                'color': colors.success, # any kivy color will do
                'categories': ['popular']
            },
            {
                'name': 'Tomatoes',
                'source': 'assets/imgs/tomato.png',
                'avatar': 'assets/imgs/tomato-square.png',
                'price': 4.5,
                'color': colors.danger, # any kivy color will do
                'categories': ['popular', 'discount']
            },
            {
                'name': 'Mangoes',
                'source': 'assets/imgs/mango.png',
                'avatar': 'assets/imgs/mango-square.png',
                'price': 32.5,
                'color': colors.warning, # any kivy color will do
                'categories': ['popular', 'discounts']
            }
        ]

        specials = [{
                'name': 'Avocado',
                'source': 'assets/imgs/avocado.png',
                'avatar': 'assets/imgs/avocado-square.png',
                'price': 28.45,
                'color': colors.success, # any kivy color will do
                'categories': ['popular']
            },
            {
                'name': 'Tomatoes',
                'source': 'assets/imgs/tomato.png',
                'avatar': 'assets/imgs/tomato-square.png',
                'price': 4.5,
                'color': colors.danger, # any kivy color will do
                'categories': ['popular', 'discount']
            },
            {
                'name': 'Mangoes',
                'source': 'assets/imgs/mango.png',
                'avatar': 'assets/imgs/mango-square.png',
                'price': 32.5,
                'color': colors.warning, # any kivy color will do
                'categories': ['popular', 'discounts']
            },
            ]

        prods = self.ids.products
        prods.clear_widgets()
        for product in products:
            p = Product()
            p.name = product['name']
            p.price = product['price']
            p.bcolor = product['color']
            p.source = product['avatar']
            p.back = product['source']
            p.bind(on_release=self.view_product)

            prods.add_widget(p)

        spec = self.ids.specials
        spec.clear_widgets()
        for product in reversed(specials):
            p = Special()
            p.name = product['name']
            p.price = product['price']
            p.bcolor = product['color']
            p.source = product['avatar']
            p.back = product['source']
            p.bind(on_release=self.view_product)

            spec.add_widget(p)

    def view_product(self, product):
        view = App.get_running_app().root.ids.plant_view
        mngr = App.get_running_app().root.ids.scrn_mngr

        view.name = product.name
        view.price = product.price
        view.source = product.back
        view.bcolor = product.bcolor

        mngr.transition = SwapTransition()
        mngr.current = 'scrn_plant'

class Product(ButtonBehavior, BoxLayout):
    name = StringProperty("")
    source = StringProperty("")
    back = StringProperty("")
    bcolor = ColorProperty([1,1,1,1])
    price = NumericProperty(0.0)
    radius = NumericProperty(dp(18))
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

class Special(ButtonBehavior, BoxLayout):
    name = StringProperty("")
    source = StringProperty("")
    bcolor = ColorProperty([1,1,1,1])
    price = NumericProperty(0.0)
    extras = ListProperty([])
    radius = NumericProperty(dp(18))
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
