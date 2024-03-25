def validar_casamento(idade, pais, sexo):
    if pais.lower() == 'brasil':
        if idade >= 18:
            return True
        else:
            return False
    elif pais.lower() == 'japão':
        if sexo.lower() == 'masculino':
            if idade >= 18:
                return True
            else:
                return False
        elif sexo.lower() == 'feminino':
            if idade >= 16:
                return True
            else:
                return False
        else:
            return False
    elif pais.lower() == 'alemanha':
        if idade >= 18:
            return True
        else:
            return False
    else:
        return False

def main():
    idade = int(input("Qual é a sua idade? "))
    pais_origem = input("Qual é o seu país de origem? ")
    sexo = input("Qual é o seu sexo? (Masculino/Feminino) ")

    if validar_casamento(idade, pais_origem, sexo):
        print("Você pode se casar!")
    else:
        print("Você não pode se casar!")

if __name__ == "__main__":
    main()
