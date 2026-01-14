"""
当たり判定を管理するモジュール。
矩形同士の衝突を判定する。
"""

def check_collision(rect1, rect2):
    """
    2つの矩形の衝突を判定する。
    rect: (x, y, width, height) のタプル。
    """
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    return x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2