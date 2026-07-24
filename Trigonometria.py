
def seno(angulo):
    pi = 0
    for i in range(1000000):
        pi += ((-1) ** i) / (2 * i + 1)
    pi*=4
    radiano = angulo * pi / 180
    x = radiano
    resultado = x
    j = 3
    f = 3*2*1
    f2 = 3
    for i in range(84):
        if i % 2 == 1:
            resultado+=(x**j)/f
        else:
            resultado-=(x**j)/f
        j+=2
        f2+=1
        f*=f2
        f2+=1
        f*=f2
    return resultado
    
def cos(angulo):
    pi = 0
    for i in range(1000000):
        pi += ((-1) ** i) / (2 * i + 1)
    pi*=4
    radiano = angulo * pi / 180
    x = radiano
    num =1
    j = 2
    f = 2*1
    f2 = 2
    for i in range(84):
        if i % 2 == 1:
            num+=(x**j)/f
        else:
            num-=(x**j)/f
        j+=2
        f2+=1
        f*=f2
        f2+=1
        f*=f2
    return num

def tan(angulo):
    sen = seno(angulo)
    coss = cos(angulo)
    tangente = sen / coss
    print("A tangente de {}° é {:.2f}" .format(angulo,tangente))

angulo = float(input("Digite um ângulo:"))
sen = seno(angulo)
coss = cos(angulo)
print("O seno de {}° é {:.2f}" .format(angulo,sen))
print("O cosseno de {}° é {:.2f}" .format(angulo,coss))
tan(angulo)