import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import customtkinter as ctk

# ------------------------------------------------------------
# TaskRose - Agenda de tarefas
# A imagem Logo TasKRose.png deve ficar na mesma pasta deste arquivo.
# ------------------------------------------------------------

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

PALETAS = {
    "light": {
        "janela": "#FFF3F8",
        "topo": "#FCE4EC",
        "painel": "#FFFFFF",
        "lista": "#FFF8FB",
        "texto": "#321B28",
        "texto_secundario": "#916F80",
        "rosa": "#F48FB1",
        "rosa_hover": "#EC6F9E",
        "rosa_borda": "#D85A91",
        "rosa_claro": "#FCE4EC",
        "verde": "#2E8B57",
        "verde_hover": "#267347",
        "vermelho": "#E57373",
        "vermelho_hover": "#D95757",
        "roxo": "#9575CD",
        "roxo_hover": "#7E57C2",
        "campo": "#FFFFFF",
        "linha": "#FCE4EC",
        "texto_marcado": "#8A7881",
        "botao_texto": "#211018",
    },
    "dark": {
        "janela": "#100D10",
        "topo": "#211820",
        "painel": "#171216",
        "lista": "#171216",
        "texto": "#FFF7FB",
        "texto_secundario": "#B99EAD",
        "rosa": "#F56DB2",
        "rosa_hover": "#E84D9D",
        "rosa_borda": "#F56DB2",
        "rosa_claro": "#241923",
        "verde": "#36A56B",
        "verde_hover": "#278653",
        "vermelho": "#E66D83",
        "vermelho_hover": "#CF526A",
        "roxo": "#A88AE8",
        "roxo_hover": "#8E70D0",
        "campo": "#211A20",
        "linha": "#F56DB2",
        "texto_marcado": "#B8A6B0",
        "botao_texto": "#160D13",
    }
}

tema_atual = "light"
tarefas = []


def cores():
    return PALETAS[tema_atual]


def atualizar_tarefa(tarefa):
    c = cores()
    if tarefa["marcada"].get():
        tarefa["caixa"].configure(
            text_color=c["texto_marcado"],
            hover_color=c["rosa_claro"]
        )
    else:
        tarefa["caixa"].configure(
            text_color=c["texto"],
            hover_color=c["rosa_claro"]
        )
    atualizar_botao_selecionar()


def adicionar_tarefa():
    nome = entrada.get().strip()

    if not nome:
        messagebox.showwarning("TaskRose", "Digite uma tarefa antes de cadastrar.")
        entrada.focus()
        return

    c = cores()
    marcada = tk.BooleanVar(value=False)

    linha = ctk.CTkFrame(
        area_tarefas,
        fg_color=c["painel"],
        corner_radius=12,
        border_width=1,
        border_color=c["rosa_borda"]
    )
    linha.pack(fill="x", padx=10, pady=6)

    caixa = ctk.CTkCheckBox(
        linha,
        text=nome,
        variable=marcada,
        font=("Arial", 17),
        text_color=c["texto"],
        fg_color=c["rosa"],
        hover_color=c["rosa_hover"],
        border_color=c["rosa_borda"],
        checkmark_color="#201018",
        corner_radius=5,
        command=lambda: atualizar_tarefa(item)
    )
    caixa.pack(side="left", padx=18, pady=14)

    item = {"linha": linha, "caixa": caixa, "marcada": marcada}
    tarefas.append(item)

    entrada.delete(0, "end")
    atualizar_botao_selecionar()


def selecionar_todos():
    if not tarefas:
        messagebox.showwarning("TaskRose", "Ainda não existem tarefas cadastradas.")
        return

    todas_marcadas = all(item["marcada"].get() for item in tarefas)
    novo_estado = not todas_marcadas

    for item in tarefas:
        item["marcada"].set(novo_estado)
        atualizar_tarefa(item)

    atualizar_botao_selecionar()


def atualizar_botao_selecionar():
    if tarefas and all(item["marcada"].get() for item in tarefas):
        botao_selecionar.configure(text="Desmarcar todas")
    else:
        botao_selecionar.configure(text="Selecionar todas")


def remover_tarefa():
    selecionadas = [item for item in tarefas if item["marcada"].get()]

    if not selecionadas:
        messagebox.showwarning("TaskRose", "Marque as tarefas que deseja remover.")
        return

    for item in selecionadas:
        item["linha"].destroy()
        tarefas.remove(item)

    atualizar_botao_selecionar()


def alternar_tema():
    global tema_atual
    tema_atual = "dark" if tema_atual == "light" else "light"
    aplicar_tema()


def aplicar_tema():
    c = cores()

    janela.configure(fg_color=c["janela"])
    barra_topo.configure(fg_color=c["topo"])
    titulo_janela.configure(text_color=c["texto"])
    titulo_principal.configure(text_color=c["rosa"])
    subtitulo.configure(text_color=c["texto"])

    entrada.configure(
        fg_color=c["campo"],
        text_color=c["texto"],
        placeholder_text_color=c["texto_secundario"],
        border_color=c["rosa_borda"]
    )

    container.configure(fg_color=c["painel"], border_color=c["rosa_borda"])
    area_tarefas.configure(fg_color=c["lista"])
    area_botoes.configure(fg_color="transparent")

    botao_adicionar.configure(
        fg_color=c["rosa"], hover_color=c["rosa_hover"],
        text_color=c["botao_texto"]
    )
    botao_selecionar.configure(
        fg_color=c["rosa"], hover_color=c["rosa_hover"],
        text_color=c["botao_texto"]
    )
    botao_remover.configure(
        fg_color=c["rosa"], hover_color=c["rosa_hover"],
        text_color=c["botao_texto"]
    )

    # Atualiza também os itens já cadastrados.
    for item in tarefas:
        item["linha"].configure(
            fg_color=c["painel"],
            border_color=c["rosa_borda"]
        )
        item["caixa"].configure(
            text_color=c["texto_marcado"] if item["marcada"].get() else c["texto"],
            fg_color=c["rosa"],
            hover_color=c["rosa_hover"],
            border_color=c["rosa_borda"]
        )

    botao_tema.configure(
        text="☀  Claro" if tema_atual == "dark" else "☾  Escuro",
        fg_color=c["rosa"],
        hover_color=c["rosa_hover"],
        text_color=c["botao_texto"],
        border_color=c["rosa_borda"]
    )


# ----------------------- Janela principal -----------------------

janela = ctk.CTk()
janela.title("TaskRose")
janela.geometry("1100x850")
janela.minsize(760, 650)
janela.configure(fg_color=cores()["janela"])

# Caminho da logo usada em toda a interface (verifique se o 'k' é minúsculo).
pasta_programa = Path(__file__).resolve().parent
caminho_logo = pasta_programa / "TaskRose1.png"



try:
    from PIL import Image

    # 1. Converte o PNG para .ico automaticamente e aplica na barra superior (remove o quadrado azul)
    caminho_ico = pasta_programa / "TaskRose1.ico"
    img_pil = Image.open(caminho_logo)
    img_pil.save(caminho_ico, format="ICO", sizes=[(32, 32), (64, 64)])
    janela.after(250, lambda: janela.iconbitmap(str(caminho_ico)))

    # 2. Carrega as imagens para a barra interna e o cabeçalho
    logo_original = tk.PhotoImage(file=str(caminho_logo))

    fator_barra = max(1, logo_original.width() // 30)
    imagem_logo_barra = logo_original.subsample(fator_barra, fator_barra)

    fator_cabecalho = max(1, logo_original.width() // 105)
    imagem_logo = logo_original.subsample(fator_cabecalho, fator_cabecalho)
except Exception as erro:
    print("Erro ao carregar a logo:", erro)
    logo_original = None
    imagem_logo_barra = None
    imagem_logo = None

# Barra superior
barra_topo = ctk.CTkFrame(janela, height=62, corner_radius=0, fg_color=cores()["topo"])
barra_topo.pack(fill="x")
barra_topo.pack_propagate(False)

# A logo substitui o símbolo de verificado ao lado do nome.
titulo_janela = ctk.CTkLabel(
    barra_topo, text="TaskRose", image=imagem_logo_barra,
    compound="left", padx=8,
    font=("Arial", 19, "bold"), text_color=cores()["texto"]
)
titulo_janela.pack(side="left", padx=18)

# Cabeçalho principal
cabecalho = ctk.CTkFrame(janela, fg_color="transparent")
cabecalho.pack(fill="x", padx=38, pady=(22, 12))
cabecalho.grid_columnconfigure(1, weight=1)

# A mesma logo enviada aparece no cabeçalho principal.
logo_label = ctk.CTkLabel(cabecalho, text="", image=imagem_logo)
logo_label.grid(row=0, column=0, padx=(0, 18), sticky="w")

titulo_principal = ctk.CTkLabel(
    cabecalho, text="TaskRose",
    font=("Arial", 42, "bold"), text_color=cores()["rosa"],
    anchor="w"
)
titulo_principal.grid(row=0, column=1, sticky="w")

botao_tema = ctk.CTkButton(
    cabecalho, text="☾  Escuro", command=alternar_tema,
    width=145, height=48, corner_radius=22,
    border_width=2, border_color=cores()["rosa_borda"],
    fg_color=cores()["rosa"], hover_color=cores()["rosa_hover"],
    text_color=cores()["botao_texto"],
    font=("Arial", 15, "bold")
)
botao_tema.grid(row=0, column=2, sticky="e")

divisoria = ctk.CTkFrame(janela, height=3, corner_radius=5, fg_color=cores()["rosa"])
divisoria.pack(fill="x", padx=38, pady=(0, 22))

# Campo de cadastro e botão
area_cadastro = ctk.CTkFrame(janela, fg_color="transparent")
area_cadastro.pack(fill="x", padx=38, pady=(0, 20))
area_cadastro.grid_columnconfigure(0, weight=1)

entrada = ctk.CTkEntry(
    area_cadastro,
    placeholder_text="Digite sua tarefa...",
    height=62, corner_radius=17, border_width=2,
    border_color=cores()["rosa_borda"],
    fg_color=cores()["campo"], text_color=cores()["texto"],
    placeholder_text_color=cores()["texto_secundario"],
    font=("Arial", 19)
)
entrada.grid(row=0, column=0, sticky="ew", padx=(0, 14))

botao_adicionar = ctk.CTkButton(
    area_cadastro, text="Cadastrar", command=adicionar_tarefa,
    width=190, height=62, corner_radius=17,
    fg_color=cores()["rosa"], hover_color=cores()["rosa_hover"],
    text_color=cores()["botao_texto"], font=("Arial", 19, "bold")
)
botao_adicionar.grid(row=0, column=1)

entrada.bind("<Return>", lambda evento: adicionar_tarefa())

subtitulo = ctk.CTkLabel(
    janela, text="Suas tarefas",
    font=("Arial", 22, "bold"), text_color=cores()["texto"]
)
subtitulo.pack(anchor="w", padx=42, pady=(0, 10))

# Lista de tarefas
container = ctk.CTkFrame(
    janela, fg_color=cores()["painel"], corner_radius=20,
    border_width=2, border_color=cores()["rosa_borda"]
)
container.pack(fill="both", expand=True, padx=38, pady=(0, 20))

area_tarefas = ctk.CTkScrollableFrame(
    container, fg_color=cores()["lista"], corner_radius=15
)
area_tarefas.pack(fill="both", expand=True, padx=10, pady=10)

# Botões inferiores
area_botoes = ctk.CTkFrame(janela, fg_color="transparent")
area_botoes.pack(fill="x", padx=38, pady=(0, 28))
area_botoes.grid_columnconfigure((0, 1), weight=1)

botao_selecionar = ctk.CTkButton(
    area_botoes, text="Selecionar todas", command=selecionar_todos,
    height=62, corner_radius=17,
    fg_color=cores()["rosa"], hover_color=cores()["rosa_hover"],
    text_color=cores()["botao_texto"], font=("Arial", 17, "bold")
)
botao_selecionar.grid(row=0, column=0, sticky="ew", padx=(0, 12))

botao_remover = ctk.CTkButton(
    area_botoes, text="Remover selecionadas", command=remover_tarefa,
    height=62, corner_radius=17,
    fg_color=cores()["rosa"], hover_color=cores()["rosa_hover"],
    text_color=cores()["botao_texto"], font=("Arial", 17, "bold")
)
botao_remover.grid(row=0, column=1, sticky="ew", padx=(12, 0))

janela.mainloop()
