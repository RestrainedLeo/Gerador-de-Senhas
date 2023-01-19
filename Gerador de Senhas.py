import random

print('Bem vindo ao gerado de senhas!')
name = input('Digite seu nome:')
print("Olá " + name + "!\n")

print('Vamos lá! 3 senhas irão ser geradas automaticamente. As 3 senhas irão conter 13 caracteres com letras minúsculas, maiúsculas, números e símbolos.\nObrigado por usar o gerador de senhas seguras!\n')
print('As senhas serão geradas logo a baixo!\n')

abcbig = 'QWERTYUIOPASDFGHJKLÇZXCVBNM'
abctiny = 'qwertyuiopasdfghjklçzxcvbnm'
number = '1234567890'
symbol = '!@#$%¨&*()'
soma = abcbig + abctiny + number + symbol
senha = 13

senha1 = ''.join(random.sample(soma, senha))
senha2 = ''.join(random.sample(soma, senha))
senha3 = ''.join(random.sample(soma, senha))

print("Primeira senha gerada:\n" + senha1)
print("Segunda senha gerada:\n" + senha2)
print("Terceira senha gerada:\n" + senha3)