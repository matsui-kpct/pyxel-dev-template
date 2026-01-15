import http.server
import socketserver
import sys
import subprocess

# PyxelアプリをHTML化
try:
    print("Packaging Pyxel app...")
    subprocess.run(["pyxel", "package", ".", "game.py"], check=True)
    print("Converting to HTML...")
    subprocess.run(["pyxel", "app2html", "pyxel-dev.pyxapp"], check=True)
    print("HTML conversion completed.")
except subprocess.CalledProcessError as e:
    print(f"Error during HTML conversion: {e}")
    sys.exit(1)

# カスタムハンドラを定義してルートパスをpyxel-dev.htmlにリダイレクト
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/pyxel-dev.html'
        return super().do_GET()

# サーバーを起動
socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(("", 8000), CustomHandler)

print("Serving at port 8000")
try:
    httpd.serve_forever() # サーバーを停止するまで実行
except KeyboardInterrupt:
    print("Shutting down server...")
    httpd.server_close() # サーバーを停止
    print("Server stopped.")
    sys.exit(0)