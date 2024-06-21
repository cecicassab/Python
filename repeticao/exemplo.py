PALAVRAS_PROIBIDAS = ("futebol", "politica", "religiao")
textos = [
    "João gosta de futebol",
    "O dia está ensolarado"
]


for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print("Palavra proibida detectada ",palavra)
            break
    else:
        found = True
        print("Frase sem palavras probida ", texto)