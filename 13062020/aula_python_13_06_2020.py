# -*- coding: utf-8 -*-
"""Aula Python 13_06_2020.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/rsucupira/Pythonzinho/blob/master/Aula%20Python%2013_06_2020.ipynb

# Aula 13/06/2020 - Python
### Prof. Rodrigo Sucupira / [sucupira.rodrigo@gmail.com](mailto:sucupira.rodrigo@gmail.com) 

## [GitHub Pythonzinho](https://github.com/rsucupira/Pythonzinho) / [www.pythonzinho.com.br](http://www.pythonzinho.com.br)

- Aluno:Nara / carlos.cf.batista@gmail.com
- [GitHub](https://github.com/)

### 01) Operações Básicas / Calculadora
#### 01.1) Adição              (+)
"""

1+2

"""**Ex 01:** Na celula abaixo insira uma **adição** e depois clique no botão "Run":"""

56+98

"""#### 01.2) Subtração           (-)"""

5-2

"""**Ex 02:** Na celula abaixo insira uma **subtração** e depois clique no botão "Run":"""

4-6

"""#### 01.3) Multiplicação       (*)"""

3*5

"""**Ex 03:** Na celula abaixo insira uma **multiplicação** e depois clique no botão "Run":"""

8*9

"""#### 01.4) Divisão             (/)"""

20/4

"""**Ex 04:** Na celula abaixo insira uma **divisão** e depois clique no botão "Run":"""

6/29

"""#### 01.5) Potência            (**)"""

2**3

"""**Ex 05:** Na celula abaixo insira uma operação **potência** e depois clique no botão "Run":"""

8**6

"""#### 01.6) Resto               (%)"""

10%3

"""**Ex 06:** Na celula abaixo insira uma operação **resto** e depois clique no botão "Run":"""

67%5

"""#### 01.7) Comentário          (#)"""

# Este é um comentário

"""Note que rodar este exemplo não retorna nenhum valor, por se tratar de um comentário

**Ex 07:** Na celula abaixo insira um **comentário** e depois clique no botão "Run":
"""

# eu gosto de gatos

"""## 02) Print
A função `print` é normalmente utilizada para amostrar uma *string* (cadeia de caracteres):
"""

print("Olá Mundo")

"""#### Função:
A ideia básica de uma função, é encapsular um código que poderá ser invocado/chamado por qualquer outro trecho do programa. Seu significado e uso é muito parecido com o de funções matemáticas, ou seja, existe um nome, uma definição e posterior invocação à função.

**Ex 08:** escreva um código que amostra o seu nome e depois clique no botão "Run":
"""

print('não sei o que escrever')

"""## 03) Variáveis
Variáveis são **"objetos"** que você cria e armazena informação 

Voçê pode definir variáveis usando o símbolo igual (=):
"""

x = 10
print(x)

"""a variável criada acima é conhecida como **integer** que quer dizer numero inteiro"""

x

"""reparem na celula acima que outra forma de amostrar alguma variável é colocar ela em uma celula e rodar"""

texto = "Olá mundo"
print(texto)

"""a variável criada acima é conhecida como **string** que significa texto ou cadeia de caracteres

**Ex 09:** escreva um código que armazena o seu nome em uma variável e depois amostra a variável criada.
"""

nome="lorena"
print(nome)

"""## 04) Tipos de variáveis
Vamos apresentar as quatro principais variáveis que utilizamos em um código:
- Integer
- Float
- String
- Boolean

### 04.1) Integer & Float
para trabalhar com numeros temos dois tipos de variáveis, os numeros inteiros ou **integer** e os numeros reais ou **float**,
"""

numero_01 = 1 # exemplo de inteiro
numero_01

numero_02 = 1.0 # exemplo de float
numero_02

"""reparem que ao colocar um ponto no final do numero automaticamente eu tranformo ele num número real."""

x = 10/3
x

"""### 04.2) Função int() e float()
para tranformar uma variável em inteiro utilizamos a função **int()** e para transformar em um numero real utilizamos a função **float()**
"""

int(2.3)

int("olá")

float(2)

"""reparem que observamos um erro ao tentar transformar uma cadeia de caracteres em um numero inteiro.

### 04.2) Função type()
para saber qual o tipo da variável utilizamos a função **type()**
"""

type(2)

type(1.2)

"""**Ex 10:** escreva um código que armazena um numero real em uma variável e depois amostra o tipo da variável criada."""

mew = 4.9
type(mew)

"""### 04.3) Strings
O tipo de variável que utilizamos para trabalhar com texto é conhecida como **string**.

**Ex 11:** escreva um código que armazena um texto em uma variável, depois amostra o tipo da variável criada.
"""

a = 'ori'
type(a)

"""### 04.4) Função str()
para converter uma variável em **string** utilizamos a função **str()**
"""

x = 1
type(x)

y = str(x)
type(y)
print(y)

"""**Ex 12:** escreva um código que armazena um **float** ou numero real em uma variável e depois converte em uma **string** ou texto."""

mew = 1.50
str(mew)

"""### 04.5) Trabalhando com strings
#### 04.5.1) Concatenar +
"""

'a' + 'b'

"""**Ex 13:** escreva um código que armazena o seu primeiro nome em uma variável e o seu sobrenome em outra variável e depois amostra o seu nome concatenado com o seu sobrenome, contendo um espaço entre eles, armazenando em uma terceira variável."""



"""#### 04.5.2) Tamanho len()"""

len('abc')

"""**Ex 14:** escreva um código que amostra o tamanho do texto gerano no **Ex 13**."""



"""#### 04.5.3) Posição []"""

texto = 'AaBbCcDdEe'
texto[0]

texto[2:4]

"""**Ex 15:** escreva um código que amostra um intervalo qualquer de tamanho 3 do texto gerado no **Ex 13**."""



"""#### 04.5.4) Substituir .replace()"""

texto.replace('c','j')

"""**Ex 16:** escreva um código que utilize o texto gerado no **Ex 13**, substituindo o seu sobrenome por outro texto."""



"""#### 04.5.5) Encontrar .find()"""

texto.find('b')

"""**Ex 17:** escreva um código que utilize o texto gerado no **Ex 13**, buscando a localização do espaço " " ."""



"""#### 04.5.6) Contar .count()"""

texto.count('A')

"""**Ex 18:** escreva um código que utilize o texto gerado no **Ex 13**, contando quantos caracteres tem nele."""



"""#### 04.5.7) MAIÚSCULO .upper()"""

texto.upper()

"""**Ex 19:** escreva um código que utilize o texto gerado no **Ex 13**, transformando tudo em maiúculo."""



"""#### 04.5.8) minúsculo .lower()"""

texto.lower()

"""**Ex 20:** escreva um código que utilize o texto gerado no **Ex 13**, transformando tudo em minúsculo."""



"""#### 04.5.9) Capitalizar .capitalize()"""

texto.capitalize()

"""**Ex 21:** escreva um código que utilize o texto gerado no **Ex 13**, capitalizando."""



"""### 04.6) Booleano
Para trabalhar com lógicas, verdadeiro e falso, utilizamos as variáveis booleanas
"""

x = True
print(x)

"""**Ex 22:** Verifique qual é o tipo da variável **x**."""



1 > 2

x = 1
x == 2

x == 1

y = x == 1
print(y)

"""**Ex 23:** Escreva um código que verifica se um número é igual ao mesmo número somado com 1."""



"""#### 04.6.1) Contém  => in"""

'a' in texto

"""**Ex 24:** Escreva um código que verifica se a letra "j" contem no texto."""



"""## 05) Input
Muitas vezes um código precisa de informações externas, como uma calculadora que pode receber sempre numeros diferentes. Para criar esta flexibilidade, utilizamos a função **input**, que traduzindo significa **entrada**.
"""

texto_02 = input("insira um texto: ")
print(texto_02)



"""Atenção: todos os valores que a função **input** recebe são do tipo **string**, caso deseje trabalhar com numeros, deverá converter.
Utilize o código abaixo para testar uma entrada de um numero somado com 1.
"""

numero = input("insira um numero: ")
numero = numero + 1

"""O código acima irá apresentar um erro, pois não é possivel somar um **integer** com uma **string**

**Ex 25:** escreva um código que armazena um **input** em uma variável, converte ele em um numero real e por fim amostra ele.
"""



"""**Ex 26:** Ajude a sua mãe na feira, escreva um código que:
- recebe um input de quantidade de laranjas.
- recebe um input de preço da laranja.
- calcula o custo total.
obs: deve aceitar valores reais e não inteiros.
"""



"""## 06) Comparações -> IF / ELSE / ELIF

Muitas vezes precisamos realizar comparações e para isso utilizamos o recurso IF.

Para utilizar o **if** precisamos colocar um booleano e dois pontos (:)
"""

numero = 3
if numero > 2:
    print('o número é maior que 2')

"""Note que abaixo do **if** existe um espaço onde o código será rodado.

Para utilizar o **else** não colocamos booleano, somente dois pontos (:)
"""

numero = 2
if numero > 2:
    print('o número é maior que 2')
else:
    print('o número é menor ou igual a 2')

"""Para utilizar o **elif**  precisamos colocar um booleano e dois pontos (:)"""

numero = 1
if numero > 2:
    print('o número é maior que 2')
elif numero < 2:
    print('o número é menor que 2')

"""Ele irá entrar no primeiro que conseguir e não entrará nos demais."""

numero = 2
if numero > 2:
    print('o número é maior que 2')
elif numero < 2:
    print('o número é menor que 2')
else:
    print('o número não é maior nem menor que 2')

"""Exemplo para verificar se contem a letra 'a'"""

texto = input('Insira um texto: ')
if texto.count('a') > 0:
    print('Esse texto contêm a letra a')

"""Dois exemplos verificando se é inteiro."""

variavel = 1.    # exemplo de inteiro

if type(variavel) == int:
    print('é um inteiro')
else:
    print('não é um inteiro')

variavel = 'a'    # exemplo de string

if type(variavel) == int:
    print('é um inteiro')
else:
    print('não é um inteiro')

"""Exemplo verificando qual é o tipo da variável, faça o exercício de alterar a variável para atingir todas as possibilidades."""

variavel = True    # exemplo de booleano

if type(variavel) == str:
    print('é uma string')
elif type(variavel) == int:
    print('é um inteiro')
elif type(variavel) == float:
    print('é um numero real')
elif type(variavel) == bool:
    print('é um booleano')
else:
    print('não sei o que é')

"""**Ex 27:** Escreva um código que:
- Recebe um **input** de texto.
- Mede o tamanho do texto e armazena em uma outra variável
- Verifica se o tamanho é maior que 4, caso positivo amostra o tamanho dele.
- Caso negativo amostra o próprio texto.
"""

