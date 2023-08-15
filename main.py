tentativas = 0


def correta():
  print("\033[0;32mResposta correta!")


def incorreta():
  print("\033[1;31mResposta incorreta!")


def indisponivel():
  print("Essa questão não está mais disponível")


print("\033[0;7m---------------------------\033[0;0m")
print("\033[0;7m------- SUPER Quiz --------\033[0;0m")
print("\033[0;7m---------------------------\033[0;0m")
op1 = False
op2 = False
op3 = False
op4 = False

while True:
  if (op1 and op2 and op3 and op4) == True:
    break
  #Opções
  print("\033[;1m1) Esportes")
  print("2) Filmes")
  print("3) Jogos")
  print("4) Música")
  var = int(input("\033[0;0mInforme uma opção: "))
  #Inicio da primeira pergunta
  if var == 1 and op1 == False:
    print(
      "\033[0;35mQual é o terceiro país com o maior número de títulos de Copa do Mundo no Futebol?"
    )
    print("\033[1;34m1) Brasil")
    print("2) Alemanha")
    print("3) Portugal")
    print("4) Argentina")
    while True:
      rp1 = int(input("\033[0;0mInforme sua resposta: "))
      if rp1 != 4:
        incorreta()
        tentativas += 1
        tn = input("\033[0;0mDeseja tentar novamente? S/N: ")
        if tn.upper() == "N":
          break
        elif tn.upper() == "S":
          print("")
      elif rp1 == 4:
        correta()
        tentativas += 1
        op1 = True
        break
  #Fim da primeira pergunta
  elif var == 1 and op1 == True:
    indisponivel()
  #Inicio da segunda pergunta
  if var == 2 and op2 == False:
    print(
      "\033[0;35mQual é o nome do filme em que Leonardo DiCaprio interpreta um ladrão de alto nível que entra nos sonhos das pessoas?\033[0;0m"
    )
    print("\033[1;34m1) Titanic")
    print("2) A Origem")
    print("3) Foi Apenas um Sonho")
    print("4) Ilha do Medo")
    while True:
      rp2 = int(input("\033[0;0mInforme sua resposta: "))
      if rp2 != 2:
        incorreta()
        tentativas += 1
        tn = input("\033[0;0mDeseja tentar novamente? S/N: ")
        if tn.upper() == "N":
          break
        elif tn.upper() == "S":
          print("")
      elif rp2 == 2:
        correta()
        tentativas += 1
        op2 = True
        break
  #Fim da segunda pergunta
  elif var == 2 and op2 == True:
    indisponivel()
  #Inicio da terceira pergunta
  if var == 3 and op3 == False:
    print("\033[0;35mQual o nome do Ouriço Rosa nos jogos de Sonic?")
    print("\033[1;34m1) Charmy Bee")
    print("2) Knuckles")
    print("3) Amy Rose")
    print("4) Sticks")
    while True:
      rp3 = int(input("\033[0;0mInforme sua resposta: "))
      if rp3 != 3:
        incorreta()
        tentativas += 1
        tn = input("\033[0;0mDeseja tentar novamente? S/N: ")
        if tn.upper() == "N":
          break
        elif tn.upper() == "S":
          print("")
      elif rp3 == 3:
        correta()
        tentativas += 1
        op3 = True
        break
  #Fim da terceira pergunta
  elif var == 3 and op3 == True:
    indisponivel()
  #Inicio da quarta pergunta
  if var == 4 and op4 == False:
    print(
      "\033[0;35mQual é o nome do álbum lançado pela banda britânica The Beatles em 1969, que foi o último álbum de estúdio gravado pelos membros da banda?"
    )
    print("\033[1;34m1) Abbey Road")
    print("2) Revolver")
    print("3) Beatles for Sale")
    print("4) Rubber Soul")
    while True:
      rp4 = int(input("\033[0;0mInforme sua resposta: "))
      if rp4 != 1:
        incorreta()
        tentativas += 1
        tn = input("\033[0;0mDeseja tentar novamente? S/N: ")
        if tn.upper() == "N":
          break
        elif tn.upper() == "S":
          print("")
      elif rp4 == 1:
        correta()
        tentativas += 1
        op4 = True
        break
  #Fim da quarta pergunta
  elif var == 4 and op4 == True:
    indisponivel()

print(
  f"\033[0;33mVocê terminou o quiz com um total de {tentativas} tentativas")
print("Fim do Programa!")
print("\033[0;0m")
