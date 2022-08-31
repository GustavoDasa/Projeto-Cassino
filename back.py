# Style worlds:
# 0 - sem título
# 1 - negrito
# 4 - sublinhado
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
BLACK = "\033[0;30m"
YELLOW = "\033[0;93m"
MAGENTA = "\033[1;35m"
LIGHT_GREY = "\033[0;37m"
DARK_MAGENTA = "\033[1;95m"
DARK_GREY = "\033[0;90m"
LIGHT_RED = "\033[0;91m"
LIGHT_GREEN = "\033[0;92m"
LIGHT_BLUE = "\033[0;94m"
MARROM = "\033[0;3a"
BOLD = "\33[1:1m"
UNDER = "\33[:4m"
UNDER_BOLD = "\33[1:4m"

# EMOJIS ##
banana = YELLOW + "\U0001f34C" + RESET
remedio = RED + "\U0001f48a" + RESET

#cadeado = LIGHT_GREY + "\U0001f513" + RESET
cadeado = "\U0001f480"
saco = MAGENTA + "\U0001f381" + RESET
diamante = BLUE + "\U0001f48E" + RESET
from random import randint
import time
import random
import statistics

# TEXTOS

rolet = CYAN + "\n------------------------------------   ROLETA   -----------------------------------" + RESET

ganh = LIGHT_GREEN + "\n***********************************************************************************\n****************************|      Você ganhou!      |*****************************\n***********************************************************************************\n" + RESET

fimm = CYAN + "\n---------------------------------------------------------------\n -----------------------  Fim de jogo!  -----------------------\n---------------------------------------------------------------\n" + RESET

agrad = '\n-----------------------------------------------------------------------------------\n                              Obrigado pela presença!                              \n-----------------------------------------------------------------------------------'

hrol = CYAN + "\n------------------------------   Histórico da Roleta  -----------------------------\n" + RESET

estat = LIGHT_GREY + "\n----------------------------------  Estatística  ---------------------------------\n" + RESET

nhist = YELLOW + BOLD + "Você não possui histórico." + RESET

hcn = MAGENTA + "\n---------------------------   Histórico do Caça-Níquel   --------------------------\n" + RESET

erro1 = RED + "\nResposta inválida!\n" + RESET + "Tente novamente com um " + UNDER_BOLD + "valor numérico válido." + RESET

erro2 = RED + "\nResposta inválida!\n" + RESET + "Tente novamente com um " + UNDER_BOLD + "valor numérico." + RESET

histo = LIGHT_GREY + "\n-----------------------------------  Histórico  ----------------------------------\n" + RESET

cn = MAGENTA + "\n----------------------------------  Caça-Níquel  ---------------------------------\n" + RESET

menu = LIGHT_GREY + "\n-------------------------------------  Menu  -------------------------------------" + RESET

nfdv = RED + "\n|---------------------------|    Não foi desta vez    |---------------------------|\n" + RESET

tece = "Tecle ENTER para continuar ou digite 'SAIR' para voltar ao Menu incial: "

spc = BOLD + "__________________________________________________________________________________"

caixis = GREEN +'\n------------------------------------   Caixa   ------------------------------------\n\n' + RESET

menus = BOLD + '\n1 - Caixa;\n2 - Histórico de partida;\n3 - Estatística de jogo;\n4 - Saldo de fichas;\n5 - Sair; '+ RESET + '\n\nDigite uma das opções acima: '

wyn = BOLD + '\nQual o seu nome? : ' + RESET