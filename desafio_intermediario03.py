"""Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível
segundo o esquema abaixo, 
da esquerda para a direita.Em seguida conclua qual dos animais seguintes foi escolhido, 
através das três palavras fornecidas."""

a = input() # Entrada da variavel a
b = input() # Entrada da variavel b
c = input() # Entrada da variavel c

if a =="vertebrado": # Inicialização do bloco para verificação dos animais vertebrados

    if b== "ave" and c == "carnivoro":
        print("aguia")

    elif b =="ave" and c =="onivoro":
        print("pomba")

    elif b == "mamifero" and c == "onivero":
        print("homem")

    elif b== "mamifero" and c == "herbivoro":
        print("vaca")

elif a == "invertebrado": # Inicialização do bloco para a verificação dos animais invertebrados

    if b== "inseto" and c == "hamatofago":
        print("pulga")

    elif b=="inseto" and c == "herbivoro":
        print("largata")

    elif b == "anelidio" and c == "hematofago":
        print("sanguessuga")
    elif b == "anelideo" and c == "onivero":
        print("minhoca")

else:
    print("Não foi possivel identificar o animal descrito!")

