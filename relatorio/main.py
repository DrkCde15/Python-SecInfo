import tkinter as tk
from tkinter import ttk, messagebox
import json
from utils import gerar_relatorio, salvar_relatorio

class AvaliacaoApp(tk.Tk):
    def __init__(self, perguntas, segmentos, tipos_servicos):
        super().__init__()
        self.title("Consciência Segura")
        self.geometry("600x500")

        self.perguntas = perguntas
        self.segmentos = segmentos
        self.tipos_servicos = tipos_servicos
        self.respostas = [tk.StringVar(value="Não") for _ in perguntas]  # "Sim" ou "Não"

        self.segmento_var = tk.StringVar(value=segmentos[0])
        self.tipo_servico_var = tk.StringVar(value=tipos_servicos[0])

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.criar_aba_segmento_servico()
        self.criar_abas_perguntas()

        # Esconder todas as abas do Notebook
        for i in range(len(self.notebook.tabs())):
            self.notebook.hide(i)

        # Mostrar só a primeira aba (segmento e serviço)
        self.notebook.add(self.aba_segmento_servico)
        self.notebook.select(0)

    def criar_aba_segmento_servico(self):
        self.aba_segmento_servico = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_segmento_servico, text="Segmento e Serviço")

        ttk.Label(self.aba_segmento_servico, text="Selecione o Segmento da Empresa:", font=("Helvetica", 12, "bold")).pack(pady=10)
        segmento_menu = ttk.OptionMenu(self.aba_segmento_servico, self.segmento_var, self.segmentos[0], *self.segmentos)
        segmento_menu.pack(pady=5)

        ttk.Label(self.aba_segmento_servico, text="Selecione o Tipo de Serviço:", font=("Helvetica", 12, "bold")).pack(pady=10)
        tipo_menu = ttk.OptionMenu(self.aba_segmento_servico, self.tipo_servico_var, self.tipos_servicos[0], *self.tipos_servicos)
        tipo_menu.pack(pady=5)

        btn_proximo = ttk.Button(self.aba_segmento_servico, text="Próximo", command=lambda: self.ir_para_aba(1))
        btn_proximo.pack(pady=20)

    def criar_abas_perguntas(self):
        self.abas_perguntas = []
        for i, pergunta in enumerate(self.perguntas):
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=f"Pergunta {i+1}")
            self.abas_perguntas.append(frame)

            ttk.Label(frame, text=pergunta["pergunta"], wraplength=550, font=("Helvetica", 11)).pack(pady=20)

            radio_sim = ttk.Radiobutton(frame, text="Sim", variable=self.respostas[i], value="Sim")
            radio_nao = ttk.Radiobutton(frame, text="Não", variable=self.respostas[i], value="Não")
            radio_sim.pack(anchor="w", padx=20)
            radio_nao.pack(anchor="w", padx=20)

            nav_frame = ttk.Frame(frame)
            nav_frame.pack(pady=30)

            if i > 0:
                btn_anterior = ttk.Button(nav_frame, text="Anterior", command=lambda idx=i-1: self.ir_para_aba(idx+1))
                btn_anterior.pack(side="left", padx=10)
            else:
                btn_anterior = ttk.Button(nav_frame, text="Anterior", state="disabled")
                btn_anterior.pack(side="left", padx=10)

            if i < len(self.perguntas) - 1:
                btn_proximo = ttk.Button(nav_frame, text="Próximo", command=lambda idx=i+1: self.ir_para_aba(idx+1))
                btn_proximo.pack(side="left", padx=10)
            else:
                btn_finalizar = ttk.Button(nav_frame, text="Finalizar Avaliação", command=self.finalizar)
                btn_finalizar.pack(side="left", padx=10)

    def ir_para_aba(self, index):
        # Esconde todas as abas
        for i in range(len(self.notebook.tabs())):
            self.notebook.hide(i)
        # Mostra só a aba selecionada
        self.notebook.add(self.notebook.tabs()[index])
        self.notebook.select(index)

    def finalizar(self):
        respostas_bool = [r.get() == "Sim" for r in self.respostas]
        segmento = self.segmento_var.get()
        relatorio = gerar_relatorio(respostas_bool, self.perguntas, segmento)
        caminho = salvar_relatorio(relatorio)
        msg = (f"Segmento: {relatorio['segmento']}\n"
               f"Multiplicador: {relatorio['multiplicador']}\n"
               f"Score de Segurança: {relatorio['score_percentual']}%\n"
               f"Nível: {relatorio['nível']}\n\nRecomendações:\n")
        msg += "\n".join(f"- {rec}" for rec in relatorio["recomendações"])
        msg += f"\n\nRelatório salvo em:\n{caminho}"
        messagebox.showinfo("Resultado da Avaliação", msg)
        self.destroy()

if __name__ == "__main__":
    with open("perguntas.json", "r", encoding="utf-8") as f:
        perguntas = json.load(f)

    with open("segmentos.json", "r", encoding="utf-8") as f:
        segmentos = json.load(f)

    tipos_servicos = ["Consultoria", "Auditoria", "Treinamento", "Outros"]

    app = AvaliacaoApp(perguntas, segmentos, tipos_servicos)
    app.mainloop()
