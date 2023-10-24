##Exercicio 1 - a
print ("\nExercio 1 - a\n")
def exe1a(n):
  if n==1:
    return 10
  else:
    return exe1a(n-1)+10
n =4
resultado=exe1a(n)
print(resultado)


## Exercicio 1 - b
print ("\nExercio 1 - b\n")
def exe1b(n):
  if n==1:
    return 2
  else:
    return exe1b(n-1)**-1
n = 5
resultado=exe1b(n)
print(resultado)


##Exercicios 1 c
print ("\nExercio 1 - c\n")
def exe1c(n):
  if n==1:
    return 1
  else:
    return exe1c(n-1)+n**2
n =3
resultado=exe1c(n)
print(resultado)


##Exercicio 1 d
print ("\nExercio 1 - d\n")
def exe1d(n):
  if n ==1:
    return 1
  else:
    return n**2 * exe1d(n-1) + (n-1)
n = 3
resultado=exe1d(n)
print(resultado)
    

## Exercicio 1 - e
print ("\nExercio 1 - e\n")
def exe1e(n):
  if n==1:
    return 3
  elif n==2:
    return 5
  else:
    return (n-1)*exe1e(n-1)+(n-2)*exe1e(n-2)
n =3
resultado=exe1e(n)
print(resultado)


##Exercicio 1 f
print ("\nExercio 1 - f\n")
def exe1f(n):
  if n==1:
    return 2
  elif n==2:
    return 5
  else:
    return exe1f(n-1)* exe1f(n-2)
n =3
resultado=exe1f(n)
print(resultado)


## Exercicio 1 - g
print ("\nExercio 1 - g\n")
def exe1g(n):
  if n==1:
    return 1
  elif n==2:
    return 2
  elif n==3:
    return 3
  else:
    return exe1g(n-1)+2*exe1g(n-2)+3*exe1g(n-3)
n =4
resultado=exe1g(n)
print(resultado)

##Exercicio 2
print ("\nExercio 2\n")
def exe2(r, i):
  return i*r
i = 2
r = 3
c = 0
while c<=3:
  print(i)
  i=exe2(r,i)
  c+=1


##Exercicio 3
print ("\nExercio 3\n")
def exe3(i):
  if i == 2:
    return True
  elif i < 2:
    return False
  elif (i - 3) % 2 == 0:
    return exe3((i - 3) / 2)
  elif (i % 2 == 0):
    return exe3(i / 2)
  else:
    return False
  
numeros = [6, 7, 19, 12]

for i in numeros:
  if exe3(i):
    print(f"{i} pertence a T.")
  else:
    print(f"{i} não pertence a T.")

    
##Exercicio 4
print ("\nExercio 4\n")
def exe4(i):
  if i == 2 or i == 3:
    return True
  elif i < 2:
    return False
  elif (i % 3 == 0):
    return exe4(i /3)
  elif (i % 2 == 0):
    return exe4(i / 2)
  else:
    return False

numeros = [6, 9, 16, 21, 26, 54, 72, 218]

for i in numeros:
  if exe4(i):
    print(f"{i} pertence a M.")
  else:
    print(f"{i} não pertence a M.")


##Exercicio 7
print ("\nExercio 7\n")




##Exercicio 8
print ("\nExercio 8 a\n")

def exe8a(r, i):
  return i*r
i = 1
r = 3
c = 0
while c<=3:
  print(i)
  i=exe8a(r,i)
  c+=1

print ("\nExercio 8 b\n")
def exe8b(r, i):
  return i/r
i = 2
r = 2
c = 0
while c<=3:
  print(i)
  i=exe8b(r,i)
  c+=1
##Exercicio 9
print ("\nExercio 9\n")
def numero_triangular(n):
  if n == 1:
      return 1
  else:
      return n + numero_triangular(n - 1)

n = 3  # Substitua 5 pelo valor de n que você deseja calcular

resultado = numero_triangular(n)
print(f"O {n}-ésimo número triangular é {resultado}")


##Exercicio 10

populacao = 50000  
leituras = 1  

while populacao < 200000:
    populacao = (3 * populacao) * leituras
    leituras += 1

print(f"A população excederá 200.000 em {leituras-1} leituras.")


##Exercicio 11
print ("\nExercio 11\n")

def Rotina(L, j, chamadas=0):
  if j == 1:
      return L, chamadas

  i_max = L.index(max(L[:j])) 
  L[i_max], L[j - 1] = L[j - 1], L[i_max] 

  return Rotina(L, j - 1, chamadas + 1)

L = [3, 7, 4, 2, 6]
L, total_chamadas = Rotina(L, 5)
print("Lista final L:", L)
print("Total de chamadas realizadas à Rotina:", total_chamadas)