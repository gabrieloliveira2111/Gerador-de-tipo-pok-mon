novamente = "S"
while novamente == "S":
    mes = str(input("Digite o mês do seu aniversário: " )).lower()
    tipo = ""
    tipo2 = ""

    while tipo == "":

        if "jan" in mes or mes == "1":
            tipo = "Ground"
        elif "fev" in mes or mes == "2":
            tipo = "Fighting"
        elif "mar" in mes or mes == "3":
            tipo = "Normal"
        elif "abr" in mes or mes == "4":
            tipo = "Steel"  
        elif "mai" in mes or mes == "5":
            tipo = "Flying"
        elif "jun" in mes or mes == "6":
            tipo = "Psychic"
        elif "jul" in mes or mes == "7":
            tipo = "Normal"
        elif "ago" in mes or mes == "8":
            tipo = "Ground"
        elif "set" in mes or mes == "9":
            tipo = "Flying"
        elif "out" in mes or mes == "10":
            tipo = "Psychic"
        elif "nov" in mes or mes == "11":
            tipo = "Fighting"
        elif "dez" in mes or mes == "12":
            tipo = "Steel"
        else:
            print("Escolha Inválida")
            mes = (input("Digite o mês do seu aniversário novamente: " )).lower()

    dia = int(input("Digite o dia do seu aniversário: "))

    while tipo2 == "":

        if dia == 1 or dia == 9 or dia == 17:
            tipo2 = tipo + " Eletric"                                                  
        elif dia == 2 or dia == 10 or dia == 21:
            tipo2 = tipo + " Fairy"
        elif dia == 3 or dia == 24:
            tipo2 = tipo + " Normal"
        elif dia == 4 or dia == 12 or dia == 23:
            tipo2 = tipo + " Dark"
        elif dia == 5 or dia == 22 or dia == 27:
            tipo2 = tipo + " Dragon"
        elif dia == 6 or dia == 16 or dia == 29:
            tipo2 = tipo + " Ice"
        elif dia == 7 or dia == 18:
            tipo2 = tipo + " Bug"
        elif dia == 8 or dia == 19 or dia == 30:
            tipo2 = tipo + " Poison"
        elif dia == 11 or dia == 22:
            tipo2 = tipo + " Ghost"
        elif dia == 13 or dia == 26:
            tipo2 = tipo + " Fire"
        elif dia == 14 or dia == 25:
            tipo2 = tipo + " Grass"
        elif dia == 15 or dia == 28:
            tipo2 = tipo + " Water"
        elif dia == 20 or dia == 31:
            tipo2 = tipo + " Rock"
        else:
            print("Escolha inválida")
            dia = int(input("Digite o dia do seu aniversário novamente: "))

    print(f"Seu tipo é: {tipo2}")
    novamente = str(input("Gostaria de ver o seu tipo Pokémon novamente? S/N : ")).upper()
    