from random import randint

# Repetir o teste diversas vezes
tests = 0
testsMax = int(input("Enter the number of times to repeat the test: "))

wins = 0

while tests != testsMax:
    # Gerar porta com o prêmio e escolher uma porta aleatoriamente
    prizedDoor = randint(1, 3)
    firstChoice = randint(1, 3)

    # Identificar a porta que não foi escolhida e não contém o prêmio
    openDoor = randint(1, 3)

    while openDoor == prizedDoor or openDoor == firstChoice:
        openDoor = randint(1, 3)

    # Mudar para a porta que não foi escolhida e não foi aberta
    secChoice = firstChoice

    while secChoice == firstChoice or secChoice == openDoor:
        secChoice = randint(1, 3)

    # Verificar se o prêmio foi ganho ou não
    if prizedDoor == secChoice:
        print('won prize')
        wins += 1

    else:
        print('lost prize')

    # Contar quantos testes aconteceram
    tests += 1

# Mostrar o resultado final em porcentagem
result = wins/tests
print(result*100, '%')
