import re
        
def operadores(lista):
        if lista[-1] in [".", "+", "-", "*", "/", "**"]:
                      print("Não pode pontuação ou operador no final do cálculo!")
                      return
        while "." in  lista:
            for i in range(len(lista)):
                  if lista[i] == "." and lista[i+1] == ".":
                    print("Não é aceito 2 ou mais pontuações!")
                    return
                  elif lista[i] == ".":
                    num1 = lista[i - 1]
                    num2 = lista[i + 1]
                    resultado = num1+"."+num2
                    lista[i - 1] = str(resultado)
                    del lista[i]
                    del lista[i]
                    break      
        while "-" in  lista:
            mudou = False
            for i in range(len(lista)):
                if lista[i] == "-" and i == 0:
                    lista[1] = "-" + lista[1]
                    del lista[0]
                    mudou = True
                    break
                elif lista[i] =="-" and lista[i - 1] in ["**", "*", "/"]:
                    lista[i+1] = "-" + lista[i+1]
                    del lista[i]
                    mudou = True
                    break
            if not mudou:
                break
        while "**" in  lista:
            for i in range(len(lista)):
                if lista[i] == "**" and (lista[i + 1] == "*" or lista[i+1] == "**"):
                    print("Não é aceito 3 ou mais operadores!")
                    return
                elif lista[i] == "**":
                    num1 = float(lista[i - 1])
                    num2 = float(lista[i + 1])
                    if num1 == 0.0 and num2 == 0.0:
                        print("Não é possível elevar 0 ao numero 0!")
                        return
                    else:
                        resultado = num1 ** num2
                        lista[i - 1] = str(resultado)
                        del lista[i]
                        del lista[i]
                        break
        while "/" in  lista:
            for i in range(len(lista)):
                if lista[i] == "/" and lista[i+1] == "/":
                    print("Não é aceito 2 ou mais operadores!")
                    return
                elif lista[i] == "/":
                    num1 = float(lista[i - 1])
                    num2 = float(lista[i + 1])
                    if num2 == 0.0:
                        print('Não é possível dividir algo por 0!')
                        return
                    else:
                        resultado = num1 / num2
                        lista[i - 1] = str(resultado)
                        del lista[i]
                        del lista[i]                                     
                        break
        while "*" in  lista:
            for i in range(len(lista)):
                if lista[i] == "*":
                    num1 = float(lista[i - 1])
                    num2 = float(lista[i+1])
                    resultado = num1 * num2
                    lista[i - 1] = str(resultado)
                    del lista[i]
                    del lista[i]
                    break
        while "-" in lista:
              for i in range(len(lista)):
                  if lista[i] == "-" and (lista[i+1] == "-" or lista[i+1] =="+"):
                    print("Não é aceito 2 ou mais operadores!")
                    return
                  elif lista[i] == "-":
                        num1 = float(lista[i - 1])
                        num2 = float(lista[i + 1])
                        resultado = num1 - num2
                        lista[i - 1] = str(resultado)
                        del lista[i]
                        del lista[i]
                        break                
        while "+" in  lista:
            for i in range(len(lista)):
                if lista[i] == "+" and (lista[i+1] == "+" or lista[i+1] == "-"):
                    print("Não é aceito 2 ou mais operadores!")
                    return
                elif lista[i] == "+":
                    num1 = float(lista[i - 1])
                    num2 = float(lista[i + 1])
                    resultado = num1 + num2
                    lista[i - 1] = str(resultado)
                    del lista[i]
                    del lista[i]
                    break
        return float(lista[0])
        
def parenteses(valores):
        lista = re.findall(r"\d+|\*\*|[+\-*/().]", valores)
        if lista.count("(") != lista.count(")"):
            print("Parênteses inválidos!")
            return
        else:
            while "(" in lista and ")" in lista:
                for i in range(len(lista) -1, -1, -1):
                    if lista[i] == "(":
                        break
                for j in range(i+1,len(lista)):
                    if lista[j] == ")":
                        break
                exp = "".join(lista[i+1:j])
                sublista = re.findall(r"\d+|\*\*|[+\-*/().]", exp)
                result = operadores(sublista)
                del lista[i:j+1]
                lista.insert(i, str(result))
            resultado = operadores(lista)
            return(resultado)
            
print("*CALCULADORA*")
texto = '#Digite \"1\" para acessar ou exit para sair a qualquer momento#'
print(texto.upper())
while True:
    comando = input("\nOpção:").lower()
    if comando == "1":
        while True:
            calculo = input("Digite seu cálculo: ")
            if calculo.lower() == "exit":
                exit()
            elif calculo == "":
                print("Digite uma expressão!")
                continue
            elif any(c.isalpha() for c in calculo):
                print("Erro, letras não são permitidas!")
            try:
                resultado = parenteses(calculo)
                if resultado is not None:
                    print("Resultado =",resultado)
            except Exception as erro:
                print("Erro:", erro)
                continue
    elif comando == "exit":
            exit()
    else:
            print("Ocorreu um erro!")   
            continue    