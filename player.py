"""
プレイヤーキャラクターを管理するクラス。
左右移動と描画を担当する。
"""
import pyxel

class Player():
    def __init__(self):
        """プレイヤーを初期位置（画面下寄せ）で生成する。"""
        self.x = 80
        self.y = 128 - 24
    
    def update(self):
        """左右キー入力を受けてプレイヤーを水平方向に移動する。"""
        
    
    def draw(self):
        """現在の位置にプレイヤーのスプライトを描画する。"""
        pyxel.blt(self.x, self.y-8, 0, 16, 0, 16, 16, 0)
