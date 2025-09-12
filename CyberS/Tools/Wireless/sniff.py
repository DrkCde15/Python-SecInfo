from scapy.all import sniff
import sqlite3
from collections import Counter

# BANCO DE DADOS
conn = sqlite3.connect("packets.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS packets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    src_ip TEXT,
    dst_ip TEXT,
    protocol TEXT,
    length INTEGER
)
""")
conn.commit()

# Contadores
protocol_counter = Counter()
src_counter = Counter()
dst_counter = Counter()
total_packets = 0

# FUNÇÃO DE CAPTURA
def process_packet(packet):
    global total_packets

    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        proto = packet["IP"].proto
        length = len(packet)

        # Atualizar estatísticas
        total_packets += 1
        protocol_counter[proto] += 1
        src_counter[src_ip] += 1
        dst_counter[dst_ip] += 1

        # Salvar no banco
        cursor.execute(
            "INSERT INTO packets (src_ip, dst_ip, protocol, length) VALUES (?, ?, ?, ?)",
            (src_ip, dst_ip, str(proto), length)
        )
        conn.commit()

# EXECUTAR CAPTURA
print("📡 Capturando pacotes... (Ctrl+C para parar)")
try:
    sniff(prn=process_packet, store=0)
except KeyboardInterrupt:
    pass
    conn.close()
