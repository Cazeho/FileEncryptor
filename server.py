import http.server
import webbrowser
from threading import Timer
import os

def open_browser():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open_new('http://localhost:9000/inter.py')

port = 9000
address = ("",port)

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(address, handler)

print("Server demarre", port)
if __name__ == "__main__":
    Timer(1, open_browser).start()

httpd.serve_forever()
