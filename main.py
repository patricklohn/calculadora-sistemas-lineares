import tkinter as tk
from tkinter import messagebox
from src.solver import resolver_sistema_linear

# Cores e fontes para a interface
FONTE_PADRAO = ("Segoe UI", 12)
FONTE_TITULO = ("Segoe UI", 18, "bold")
COR_FUNDO = "#f3eafd"
COR_BOTAO = "#7c3aed"
COR_BOTAO_HOVER = "#5b21b6"
COR_TEXTO_BOTAO = "#ffffff"
COR_INPUT = "#ede9fe"
COR_TEXTO_INPUT = "#4b006e"
COR_TEXTO_LABEL = "#4b006e"
COR_FUNDO_RESULTADO = "#ede9fe"

VARIAVEIS = "abcdefghijklmnopqrstuvwxyz"

class SistemaLinearApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Resolvedor de Sistemas Lineares")
        self.janela.configure(bg=COR_FUNDO)
        self.campos_coeficientes = []
        self.campos_constantes = []
        self.quantidade_equacoes = tk.IntVar()

        # Título
        tk.Label(
            janela, text="Resolvedor de Sistemas Lineares", font=FONTE_TITULO,
            bg=COR_FUNDO, fg=COR_TEXTO_LABEL
        ).pack(pady=(16, 8))

        # Campo para número de equações
        tk.Label(
            janela, text="Número de equações:", font=FONTE_PADRAO,
            bg=COR_FUNDO, fg=COR_TEXTO_LABEL
        ).pack()
        tk.Entry(
            janela, textvariable=self.quantidade_equacoes, font=FONTE_PADRAO,
            width=15, justify="center", bg=COR_INPUT, fg=COR_TEXTO_INPUT,
            relief="solid", highlightthickness=1, highlightbackground=COR_BOTAO
        ).pack(pady=(0, 14))

        # Botão para confirmar número de equações
        self.botao_confirmar = tk.Button(
            janela, text="Confirmar", font=FONTE_PADRAO, bg=COR_BOTAO, fg=COR_TEXTO_BOTAO,
            activebackground=COR_BOTAO_HOVER, activeforeground=COR_TEXTO_BOTAO, bd=0, relief="flat",
            command=self.criar_campos, cursor="hand2"
        )
        self.botao_confirmar.pack(pady=(0, 14))
        self.botao_confirmar.bind("<Enter>", lambda e: self.botao_confirmar.config(bg=COR_BOTAO_HOVER))
        self.botao_confirmar.bind("<Leave>", lambda e: self.botao_confirmar.config(bg=COR_BOTAO))

        # Frame para os campos das equações
        self.frame_campos = tk.Frame(janela, bg=COR_FUNDO)
        self.frame_campos.pack()

        # Botão para resolver o sistema
        self.botao_resolver = tk.Button(
            janela, text="Resolver", font=FONTE_PADRAO, bg=COR_BOTAO, fg=COR_TEXTO_BOTAO,
            activebackground=COR_BOTAO_HOVER, activeforeground=COR_TEXTO_BOTAO, bd=0, relief="flat",
            highlightbackground=COR_BOTAO, command=self.resolver_sistema, cursor="hand2"
        )
        self.botao_resolver.pack(pady=(14, 8))
        self.botao_resolver.config(state=tk.DISABLED)
        self.botao_resolver.bind("<Enter>", lambda e: self.botao_resolver.config(bg=COR_BOTAO_HOVER))
        self.botao_resolver.bind("<Leave>", lambda e: self.botao_resolver.config(bg=COR_BOTAO))

        # Label para mostrar o resultado
        self.label_resultado = tk.Label(
            janela, text="", font=FONTE_PADRAO, bg=COR_FUNDO_RESULTADO, fg=COR_TEXTO_LABEL,
            bd=2, relief="groove", width=60, height=6, anchor="center", justify="center"
        )
        self.label_resultado.pack(pady=(15, 12))

    def criar_campos(self):
        # Limpa campos antigos
        for widget in self.frame_campos.winfo_children():
            widget.destroy()
        self.campos_coeficientes.clear()
        self.campos_constantes.clear()
        n = self.quantidade_equacoes.get()
        if n <= 0 or n > len(VARIAVEIS):
            messagebox.showerror("Erro", f"Insira um número válido de equações (1 a {len(VARIAVEIS)}).")
            return

        # Cria campos para coeficientes com rótulos e constantes
        for linha in range(n):
            entradas_linha = []
            for coluna in range(n):
                # Campo para o coeficiente
                campo = tk.Entry(
                    self.frame_campos, width=5, font=FONTE_PADRAO, justify="center",
                    bg=COR_INPUT, fg=COR_TEXTO_INPUT, relief="solid",
                    highlightthickness=1, highlightbackground=COR_BOTAO
                )
                campo.grid(row=linha, column=coluna * 2, padx=(2, 0), pady=5)
                entradas_linha.append(campo)

                # Rótulo da variável
                var_label = tk.Label(
                    self.frame_campos, text=VARIAVEIS[coluna], font=FONTE_PADRAO,
                    bg=COR_FUNDO, fg=COR_TEXTO_LABEL
                )
                var_label.grid(row=linha, column=coluna * 2 + 1, padx=(0, 5), pady=5)

            self.campos_coeficientes.append(entradas_linha)

            # Sinal de igual
            igual_label = tk.Label(
                self.frame_campos, text="=", font=FONTE_PADRAO,
                bg=COR_FUNDO, fg=COR_TEXTO_LABEL
            )
            igual_label.grid(row=linha, column=n * 2, padx=(8, 4))

            # Campo para constante
            campo_constante = tk.Entry(
                self.frame_campos, width=7, font=FONTE_PADRAO, justify="center",
                bg=COR_INPUT, fg=COR_TEXTO_INPUT, relief="solid",
                highlightthickness=1, highlightbackground=COR_BOTAO
            )
            campo_constante.grid(row=linha, column=n * 2 + 1, padx=(0, 5), pady=5)
            self.campos_constantes.append(campo_constante)

        self.botao_resolver.config(state=tk.NORMAL)

    def resolver_sistema(self):
        try:
            n = self.quantidade_equacoes.get()
            matriz_coeficientes = []
            vetor_constantes = []

            for i in range(n):
                linha = []
                for j in range(n):
                    entrada = self.campos_coeficientes[i][j].get().strip()
                    if entrada == "-":
                        valor = -1.0
                    elif entrada == "":
                        valor = 1.0  # ou 0.0, depende da lógica que deseja
                    else:
                        valor = float(entrada)
                    linha.append(valor)
                matriz_coeficientes.append(linha)  # <- ESSA LINHA FALTAVA
                vetor_constantes.append(float(self.campos_constantes[i].get()))

            solucao = resolver_sistema_linear(matriz_coeficientes, vetor_constantes)
            resultado = "\n".join([f"{VARIAVEIS[i]} = {valor:.4f}" for i, valor in enumerate(solucao)])
            self.label_resultado.config(text="Solução encontrada:\n\n" + resultado)
        except Exception as erro:
            messagebox.showerror("Erro", f"Verifique os dados inseridos.\n{erro}")


if __name__ == "__main__":
    janela = tk.Tk()
    app = SistemaLinearApp(janela)
    janela.mainloop()
