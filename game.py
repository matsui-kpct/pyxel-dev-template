import pyxel


class Game:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("assets/game.pyxres")
        self.x = 75
        self.y = 60
        pyxel.run(self.update, self.draw)

    def update(self):
        # 矢印キーの入力処理
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2
        
        # 画面の境界内に留める
        self.x = max(0, min(self.x, pyxel.width - 8))
        self.y = max(0, min(self.y, pyxel.height - 8))

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.x, self.y, 0, 0, 0, 8, 8, 2)
        pyxel.text(0, 0, "Zonbi game", 7)


Game()
