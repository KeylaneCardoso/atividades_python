import random

print("Bem vindo ao jogo da adivinhação!")
print("As regras são simples. Eu vou escolher um numero, e você terá que descobrir qual número é.")
number = random.randint(1,10)

isGuessRight = False
while isGuessRight != True:
    guess = input("Escolha um número entre 1 e 10: ")
    if int(guess) == number:
        print("Você chutou {}. Está correto! Você venceu!".format(guess))
        isGuessRight = True
    else:
        print("Você chutou {}. Que pena, o valor não é esse. Tente novamente.".format(guess))
        #è assim que se adiciona um comentario
        
