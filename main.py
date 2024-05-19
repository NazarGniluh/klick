from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cli(self):
        self.ids.ball.size_hint = (0.5, 0.5)

    def cli1(self):
        self.ids.ball.size_hint = (1, 1)



class MiniScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def Click(self):
        self.manager.current = 'main'


class CkickApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MiniScreen(name='mini'))
        sm.add_widget(MainScreen(name='main'))
        return sm

app = CkickApp()
app.run()
