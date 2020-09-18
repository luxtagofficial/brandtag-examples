import http.server
import socketserver

PORT = 8000

class Handler( http.server.SimpleHTTPRequestHandler ):
    def do_GET( self ):
      print(self.path)
      if self.path.startswith('/v'):
        self.path = 'redirect.html'
      if self.path.startswith('/certificate'):
        self.path = 'certificate.html'
      return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()