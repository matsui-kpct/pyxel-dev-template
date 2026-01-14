"""
ゲームの背景を管理するクラス。
タイルマップを描画する。
"""
import pyxel

def draw():
    """タイルマップ（レイヤ0）を画面全体に描画する。"""
    pyxel.bltm(0,0,0,0,0,pyxel.width, pyxel.height, 0)