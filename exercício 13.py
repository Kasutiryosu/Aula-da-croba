print ('--- Primeira dupla ---')
p1 = int(input('Diga uma idade:'))
p2 = int(input('Diga outra idade'))
print ('--- Segunda dupla ---')
p3 = int(input('Diga uma idade:'))
p4 = int(input('Diga outra idade'))

a = p1+p2
b = p3+p4
print('--- Resultado ---')
print('A primeira dupla tem',a,'anos.')
print('A Segunda dupla tem',b,'anos.')

if(a>b):
    print('Logo, a primeira dupla é mais velha.')
elif(a<b):
    print('Logo, a segunda dupla é mais velha.')
else:
    print('logo, deu empate')