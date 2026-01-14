"""
ちくわゲームのメインアプリケーションクラス。
Pyxel を使用してゲームループを管理する。
"""
import pyxel
from player import Player
from chikuwa import Chikuwa
import background
import hud
import collision

class App:
    def __init__(self):
        """Pyxel を初期化し、リソースを読み込んでゲームオブジェクトを生成する。"""
        pyxel.init(128, 128)
        pyxel.load("assets/game.pyxres")
        self.player = Player()
        self.chikuwa = Chikuwa()
        self.music = pyxel.playm(0, loop=True)
        self.score = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        """各フレームでゲームオブジェクトの状態を更新する（Pyxel から呼ばれる）。"""
        self.player.update()
        self.chikuwa.update()

        # あたり判定: プレイヤーとちくわが衝突したらスコア加算して、ちくわをリスポーン
        player_rect = (self.player.x, self.player.y-8, 16, 16)
        chikuwa_rect = (self.chikuwa.x, self.chikuwa.y, 8, 8)
        if collision.check_collision(player_rect, chikuwa_rect):
            self.score += 100
            self.chikuwa.exits = False  


    def draw(self):
        """各フレームで画面を描画する（背景→オブジェクト→HUD の順）。"""
        pyxel.cls(0)
        background.draw()
        self.player.draw()
        self.chikuwa.draw()
        hud.draw(self.score, lives=3)

App()
