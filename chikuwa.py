"""
落下するちくわオブジェクトを管理するクラス。
ランダムな位置と種類で生成され、落下とリスポーンを行う。
"""
import pyxel
import random

class Chikuwa:
    def __init__(self):
        """ランダムな横位置と種類で落下するちくわを初期化する。"""
        self.x = random.randint(0+4, 128-4)
        self.y = 0
        self.speed = 2
        self.type = random.choice([0, 1]) # 0: normal, 1: rotten
        self.sprite_v = 0 # 0: normal, 8: rotten
        self.exits = True
    
    def update(self):
        """下方向に移動し、画面下端を越えたら上部へリスポーンする。"""
        self.y += self.speed
        if self.y > 128-20 or self.exits == False:
            self.create()
            

    def _apply_type(self):
        """種類に応じてスプライトの縦オフセットを設定する。"""


    def create(self):
        """ちくわオブジェクトを生成する。"""
        self.y = 0
        self.x = random.randint(0, 128-8)
        self.type = random.choice([0, 1])
        self.exits = True
        

    def draw(self):
        """種類を適用してちくわのスプライトを描画する。"""
        self._apply_type()
        pyxel.blt(self.x, self.y, 0, 8, self.sprite_v, 8, 8, 0)