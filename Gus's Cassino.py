# ----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------- GUS'S CASSINO -----------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

exec(open('back.py').read())

input("\nTecle ENTER para Começar")
nome = str(input(wyn)).title()


op = [(diamante, 1), (saco, 1), (banana, 1), (cadeado, 1), (remedio, 1)]
prize_list = [prize for prize, weight in op for i in range(weight)]
hist_CN = []
hist = []
z = 0
v = 0
n_sort = []
fichas = 0

def Random():
    global z
    mudou = False
    while mudou == False:
        try:
            r = (range(6))
            print(rolet)
            n = int(input("\nDigite um número de '0' à '5' para apostar: "))
            if n in r:
                rol = randint(0,5)
                n_sort.append(rol)
                if n == rol:
                    z += 1
                    hist.append(f'Na {z}ª partida você ' + UNDER + GREEN + 'Ganhou' + RESET + f' com o número: "{n}".')
                    print(ganh)
                    print('\nParabéns! ' + YELLOW + 'Você ganhou "5" fichas' + RESET)
                    return 4
                else:
                    z += 1
                    hist.append(f'Na {z}ª partida você ' + UNDER + RED + 'Perdeu' + RESET + f' com o número: "{n}". O número sorteado foi: "{rol}".')
                    print(nfdv + f'\nO número sorteado foi: "{rol}".\n')
                    return -1
                mudou = True
            else:
                print(erro1)
        except:
            print(erro2)



def CN():
    global v
    v += 1
    global hist_CN
    resul = []
    print(cn)
    input("\nTecle ENTER para puxar a alavanca\n\n")
    for i in range(3):
        resul.append(random.choice(prize_list))
    hist_CN.append(resul)
    for i in range(2):
        print(resul[i], end=" ")
        time.sleep(0.3)
        for j in range(3):
            print(". ", end=" ")
            time.sleep(0.3)
    print(resul[2])
    if resul.count(diamante) == 3 or resul.count(cadeado) == 3 or resul.count(banana) == 3 or resul.count(remedio) == 3 or resul.count(saco) == 3:
        print(ganh)
        if banana in resul:
            print('\nParabéns! ' + YELLOW + 'Você ganhou "1" fichas' + RESET)
            return 0
        elif diamante in resul:
            print('\nParabéns! ' + YELLOW + 'Você ganhou "5" fichas' + RESET)
            return 4
        elif remedio in resul:
            print('\nParabéns! ' + YELLOW + 'Você ganhou "2" fichas' + RESET)
            return 1
        elif cadeado in resul:
            print('\nParabéns! ' + YELLOW + 'Você ganhou "3" fichas' + RESET)
            return 2
        elif saco in resul:
            print('\nParabéns! ' + YELLOW + 'Você ganhou "4" fichas' + RESET)
            return 3
    else:
        print(nfdv)
        return -1


def Caixa():
    global fichas
    mudou = False
    while mudou == False:
        try:
            ficha = int(input(caixis + 'Quantas fichas você deseja comprar?: '))
            fichas += ficha
            r = input(BOLD + "\n             1 - Roleta               2 - Caça-Níquel\n\n" + RESET + "insira o Jogo desejado: ").title()
            if r == "1" or r == "Roleta":
                while fichas > 0:
                    aux = Random()
                    fichas += aux
                    if fichas > 0:
                        print('Você tem ' + BOLD + f'"{fichas}"' + RESET + ' ficha(s) restante(s).')
                        if input(tece) != "":
                            print(spc)
                            Menu()
                    else:
                        if input(YELLOW + UNDER_BOLD + "Suas fichas acabaram\n\n" + RESET + "               Tecle ENTER para voltar ao Menu").casefold() == "":
                            Menu()
                        else:
                            print(fimm)
                mudou = True
            else:
                while fichas > 0:
                    au = CN()
                    fichas += au
                    if fichas > 0:
                        print('Você tem ' + BOLD + f'"{fichas}"' + RESET + ' ficha(s) restante(s).')
                        if input(tece) != "":
                            print(spc)
                            Menu()
                    else:
                        if input(YELLOW + UNDER_BOLD + "Suas fichas acabaram\n\n" + RESET + "               Tecle ENTER para voltar ao Menu").casefold() == "":
                            Menu()
                        else:
                            print(fimm)
                mudou = True
        except:
            print(RED + "\nResposta inválida!\n" + RESET + "Tente novamente com um " + UNDER_BOLD + "valor numérico." + RESET)



# ---------------------------------------------------------------------------------------------------------------------



def Est():
    print("O número " + UNDER_BOLD + "mais sorteado" + RESET + ' durante as partidas foi o: "', round(statistics.mode(n_sort), 2), '".')
    print("A " + UNDER_BOLD + "Média" + RESET + ' dos números sorteados em partida foi de "', round(statistics.mean(n_sort), 2),'".')


# ---------------------------------------------------------------------------------------------------------------



def Menu():
    global z
    global hist
    global fichas
    global n_sort
    global nome
    global v
    global hist_CN
    opcoes = ["1", "2", "3", "4", "5", "Caixa", "Histórico de partidas", "Histórico", "Estatística", "Estatística de jogo", "Sair", "Saldo", "Saldo de fichas"]
    print(menu)
    escolha = str(input('\nOlá, ' + BOLD + f'{nome}!' + RESET + '\n\nSeja bem vindo ao menu.' + menus)).title()

    while escolha not in opcoes:
        print("\nPor favor, insira uma opção válida.")
        escolha = str(input(menus)).title()
    if escolha == "5" or escolha == "Sair":
        print(agrad)
        z = 0
        v = 0
        hist_CN = []
        hist = []
        fichas = 0
        n_sort = []
        input("\nTecle ENTER para Começar")
        nome = str(input(wyn)).title()
        Menu()
    elif escolha == "1" or escolha == "Caixa":
        Caixa()
    elif escolha == "3" or escolha == "Estatística" or escolha == "Estatística de Jogo":
        print(estat)
        if z == 0:
            print(YELLOW + BOLD + "Você não possui histórico de partidas para avaliação." + RESET)
            Menu()
        else:
            Est()
            Menu()
    elif escolha == "4" or escolha == "Saldo" or escolha == "Saldo de fichas":
        print('\n---------------------------------------------------------------------------------\n                            ' + LIGHT_GREEN + ' Você tem ' + BOLD + f'"{fichas}"' + RESET + LIGHT_GREEN + ' ficha(s).' + RESET + '\n---------------------------------------------------------------------------------\n')
        Menu()
    elif escolha == "2" or escolha == "Histórico de partida" or escolha == "Histórico":
        print(histo)
        cho = input(BOLD + "\n\n             1 - Roleta                 2 - Caça-Níquel\n\n" + RESET + "Qual o Histórico desejado: ").title()
        if cho == "Roleta" or cho == "1":
            if z == 0:
                print(YELLOW + BOLD + "Você não possui histórico." + RESET)
                Menu()
            else:
                print(hrol)
                for i in hist:
                    print(i)
                input("\n                 Tecle ENTER para Continuar: ")
                Menu()
        else:
            if v == 0:
                print(nhist)
                Menu()
            else:
                print(hcn)
                for i in range(v):
                    print(f'Na {i + 1}ª partida o conjunto sorteado foi:', end=" ")
                    for j in range(3):
                        print(hist_CN[i][j], end=" ")
                    print("")
                input("\n                  Tecle ENTER para Continuar: ")
                Menu()




print(Menu())
