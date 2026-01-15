import http.server
import socketserver
import sys
import subprocess

# 入力チェック
if len(sys.argv) < 2:
    print("Usage: python server.py <python_file>")
    sys.exit(1)

py_file = sys.argv[1]
if not py_file.endswith('.py'):
    print("Please provide a .py file")
    sys.exit(1)

# ベース名を取得
base_name = py_file[:-3]  # .pyを除く
pyxapp_file = f"{base_name}.pyxapp"
html_file = f"{base_name}.html"

# PyxelアプリをHTML化
try:
    print(f"Packaging Pyxel app from {py_file}...")
    subprocess.run(["pyxel", "package", ".", py_file], check=True)
    print(f"Renaming pyxapp to {pyxapp_file}...")
    subprocess.run(["mv", "pyxel-dev.pyxapp", pyxapp_file], check=True)
    print(f"Converting to HTML: {html_file}...")
    subprocess.run(["pyxel", "app2html", pyxapp_file], check=True)
    print("HTML conversion completed.")
except subprocess.CalledProcessError as e:
    print(f"Error during HTML conversion: {e}")
    sys.exit(1)

# カスタムハンドラを定義してルートパスを指定したHTMLファイルにリダイレクト
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = f'/{html_file}'
        return super().do_GET()

# サーバーを起動
socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(("", 8000), CustomHandler)

print(f"Serving {html_file} at port 8000")
try:
    httpd.serve_forever()  # サーバーを停止するまで実行
except KeyboardInterrupt:
    print("Shutting down server...")
    httpd.server_close()  # サーバーを停止
    print("Server stopped.")
    sys.exit(0)