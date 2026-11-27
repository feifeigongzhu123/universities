import http.server
import os
import socketserver
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8017

Handler = http.server.SimpleHTTPRequestHandler


class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True


with Server(("", PORT), Handler) as httpd:
    print("我的大学：http://127.0.0.1:%d/" % PORT)
    print("同一 Wi-Fi 下手机可访问：http://<本机局域网 IP>:%d/" % PORT)
    print("按 Ctrl+C 停止")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n已停止")
