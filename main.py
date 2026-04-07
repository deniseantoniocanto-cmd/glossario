glossario = {
    "bug": "Um erro no código que impede o programa de funcionar.",
    "python": "Uma linguagem de programação poderosa e fácil de ler.",
    "loop": "Uma estrutura que repete instruções várias vezes."
}

palavra = input(' qual a palavra? ').lower()

if palavra in glossario:
    print(' o significado é {glossario[termo]}')
else:
    print('Está palavra ainda não no meu glossario.')