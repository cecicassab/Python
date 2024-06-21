PALAVRAS_PROIBIDAS = {"futebol", "politica", "religiao"}
textos = [
    "João gosta de futebol",
    "O dia está ensolarado"
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print("Palavra proibida detectada ",intersecao)
    else:
        print("Frase sem palavras proibidas", texto)