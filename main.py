import json

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen



player = {
    "score": 0,
    "power": 1
}

def read_dat():
    global player
    try:
        with open("play.json", "r", encoding="utf-8") as file:
            player = json.load(file)
    except:
        print("НЕВДАЧА")



def save_dat():
    global player
    try:
        with open("play.json", "w", encoding="utf-8") as file:
           json.dump(player, file, indent=4, ensure_ascii=True)
    except:
        print("Unlucky")


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def on_enter(self, *args):
        read_dat()
        self.ids.score_lbl.text = " рахунок: " + str(player["score"])

    def cli(self):
        self.ids.ball.size_hint = (0.5, 0.5)

        read_dat()
        player["score"] += player["power"]
        self.ids.score_lbl.text = " рахунок: " + str(player["score"])
        save_dat()

    def cli1(self):
        self.ids.ball.size_hint = (1, 1)


    def shop_switch(self):
        self.manager.current = "shop"

class ShopScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def shop_switch(self):
        self.manager.current = "main"
    def buy(self, price, power):
        read_dat()
        if price <= player["score"]:
            player["score"] -= price
            player["power"] += power
            save_dat()





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
        sm.add_widget(ShopScreen(name='shop'))
        return sm

app = CkickApp()
app.run()
