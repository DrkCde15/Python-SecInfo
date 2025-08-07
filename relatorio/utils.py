import json
from datetime import datetime
import os

def obter_multiplicador(segmento):
    segmento = segmento.lower()
    if "tecnologia da informação" in segmento or "serviços financeiros" in segmento:
        return 1.2
    elif "educação" in segmento or "saúde" in segmento:
        return 1.1
    else:
        return 1.0

def calcular_score(respostas, perguntas):
    score = 0
    for resp, pergunta in zip(respostas, perguntas):
        if resp:
            score += pergunta["peso"]
    return score

def obter_nivel_descritivo(percentual):
    if percentual < 40:
        return "1 - Inexistente"
    elif percentual < 60:
        return "2 - Inicial"
    elif percentual < 75:
        return "3 - Parcial"
    elif percentual < 90:
        return "4 - Consistente"
    else:
        return "5 - Otimizado"

def gerar_relatorio(respostas, perguntas, segmento):
    score_base = calcular_score(respostas, perguntas)
    multiplicador = obter_multiplicador(segmento)
    score_final = score_base * multiplicador

    max_score = sum(p["peso"] for p in perguntas) * multiplicador
    percentual = round((score_final / max_score) * 100)

    nivel_descritivo = obter_nivel_descritivo(percentual)

    # Recomendação baseada na escala 1 a 5
    recomendacoes = {
        "1 - Inexistente": [
            "Implementar do zero todas as práticas de segurança.",
            "Desenvolver política formal de segurança.",
            "Sensibilizar liderança sobre riscos cibernéticos."
        ],
        "2 - Inicial": [
            "Formalizar os processos de segurança existentes.",
            "Treinar a equipe regularmente.",
            "Contratar apoio externo para estruturar segurança."
        ],
        "3 - Parcial": [
            "Padronizar e documentar processos.",
            "Realizar auditorias internas.",
            "Implementar ferramentas de monitoramento."
        ],
        "4 - Consistente": [
            "Buscar certificações como ISO 27001.",
            "Realizar testes de intrusão regulares.",
            "Automatizar processos críticos de segurança."
        ],
        "5 - Otimizado": [
            "Manter melhoria contínua com base em métricas.",
            "Realizar auditorias externas periódicas.",
            "Investir em inovação e segurança proativa."
        ]
    }

    return {
        "score_percentual": percentual,
        "nível": nivel_descritivo,
        "segmento": segmento,
        "multiplicador": multiplicador,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "recomendações": recomendacoes[nivel_descritivo]
    }

def salvar_relatorio(relatorio):
    if not os.path.exists("relatorios"):
        os.makedirs("relatorios")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = f"relatorios/relatorio_{timestamp}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(relatorio, f, indent=4, ensure_ascii=False)
    return path