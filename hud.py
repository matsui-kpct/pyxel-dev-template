"""
ゲームの HUD（ヘッドアップディスプレイ）を描画する関数。
ハートとスコアを表示する。
"""
import pyxel

def draw(score: int = 0, lives: int = 3):
    """ HUD として左上にハートを、右上にスコア（数字のみ）を表示する。"""
    max_hearts = 3
    count = min(max(0, lives), max_hearts)
    start_x = 4
    y = 4
    gap = 4
    for i in range(count):
        x = start_x + i * (8 + gap)
        pyxel.blt(x, y, 0, 0, 8, 8, 8, 0)

    s = str(score)
    x = pyxel.width - len(s) * 4 - 4
    pyxel.text(x, y+2, s, 7)
