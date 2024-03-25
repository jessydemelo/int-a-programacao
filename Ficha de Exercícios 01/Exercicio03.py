def verificar_par_impar(numero):
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')


num = int(input("Digite um número inteiro: "))


verificar_par_impar(num)
