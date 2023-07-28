#Um supermercado está fazendo uma promoção de venda de refrigerantes. 
#Se um dia você comprar refrigerantes e levar os cascos vazios no dia seguinte,
#ela troca cada conjunto de K garrafas vazias  por uma garrafa cheia. 
#Um cliente quer aproveitar ao máximo essa oferta e por isso comprou várias garrafas no primeiro dia da promoção. 
#Agora ele quer saber quantas garrafas terá ao final do segundo dia da promoção, se usá-la ao máximo.

#A primeira linha de entrada contém inteiro T (1 ≤ T ≤ 10000) , que indica o número de casos de teste. 
#Em cada uma das T linhas a seguir vêm dois inteiros N e K (1 ≤ K, N ≤ 10000),  
#respectivamente o número de refrigerantes comprados e o número de garrafas vazias para ganhar uma cheia.

import math

T = int(input())

for i in range(T):

    i = input().split(" ")
    N = int(i[0])
    K = int(i[1])

    if 1 <= K and N<= 10000:

        retorno = math.ceil((N/K)+3)

        if K < retorno:

            resultado = retorno -1

            print(resultado)

        else:
            print(retorno)
T = T - 1