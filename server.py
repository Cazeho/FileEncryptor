import http.server

port = 9000
address = ("",port)

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(address, handler)

print("Server demarre", port)
httpd.serve_forever()