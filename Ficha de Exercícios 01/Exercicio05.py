def jogar_pedra_papel_tesoura(jogador1, jogador2):
    if jogador1 == jogador2:
        return "Empate!"
    elif jogador1 == "pedra":
        if jogador2 == "tesoura":
            return "Jogador 1 venceu!"
        else:
            return "Jogador 2 venceu!"
    elif jogador1 == "papel":
        if jogador2 == "pedra":
            return "Jogador 1 venceu!"
        else:
            return "Jogador 2 venceu!"
    elif jogador1 == "tesoura":
        if jogador2 == "papel":
            return "Jogador 1 venceu!"
        else:
            return "Jogador 2 venceu!"
    else:
        return "Opção inválida! Por favor, escolha entre pedra, papel ou tesoura."


escolha_jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ").lower()
escolha_jogador2 = input("Jogador 2, escolha pedra, papel ou tesoura: ").lower()


resultado = jogar_pedra_papel_tesoura(escolha_jogador1, escolha_jogador2)
print(resultado)
