from random import randint
#Adicionar ASCII arte em cima para poder decorar o programa
#Fazer tipo uma UI meio ASCII, com link, arte, github, link do itch.io.
#Pra isso pesquisar como fazer no python.
print("Bem vindo ao criador de personagem do TTRPG Walden!")

print("Deseja criar seu nome ou utilizar um aleatório?")
while True:
    print("1 - Criar nome")
    print("2 - Utilizar nome aleatório")
    x = int(input())
    if x == 1:
        nome = input('Digite seu nome: ')
        break
    elif x == 2:
        print("Nome aleatório: PlaceHolder-chan")
        break
    else:
        print("Opcao invalida")

print("Pressione 1 para gerar seu personagem aleatoriamente ou 2 para criar manualmente com ajuda")
x = int(input()) #Pesquisar como fazer com que o programa não crashe se o usuario digitar um valor invalido

#x = int(input("Pressione 1 para gerar seu personagem aleatoriamente ou 2 para criar manualmente com ajuda"))
if x == 1:
#A lógica por trás desse bloco gigante é utilizar ter os valores aleatórios, por conseguinte, as strings que representam, geradas em suas respectivas classes.
    n = randint(1, 6)
    class fisico:
        if n == 1 or n == 2 or n == 3:
            print('entrou em corpo1')

            def corpo1(numero):

                match numero:
                    case 1:
                        return "Alto"
                    case 2:
                        return "Atlético"
                    case 3:
                        return "Baixo"
                    case 4:
                        return "Delicado"
                    case 5:
                        return "Esguio"
                    case 6:
                        return "Escultural"

        elif n == 4 or n == 5 or n == 6:
            def corpo2(numero):
                print('entrou em corpo2')

                match numero:
                    case 1:
                        return "Franzino"
                    case 2:
                        return "Molenga"
                    case 3:
                        return "Musculoso"
                    case 4:
                        return "Parrudo"
                    case 5:
                        return "Pesado"
                    case 6:
                        return "Robusto"
    m = randint(1, 6)
    class rosto:
        if m == 1 or m == 2 or m == 3:

            def rosto1(numero):
                """
                docstring
                """
                match numero:
                    case 1:
                        return "Afiado"
                    case 2:
                        return "Alongado"
                    case 3:
                        return "Delicado"
                    case 4:
                        return "Esculpido"
                    case 5:
                        return "Estreito"
                    case 6:
                        return "Inchado"
        elif m == 4 or m == 5 or m == 6:

            def rosto2(numero):
                """
                docstring
                """
                match numero:
                    case 1:
                        return "Largo"
                    case 2:
                        return "Magro"
                    case 3:
                        return "Nobre"
                    case 4:
                        return "Quadrado"
                    case 5:
                        return "Quebrado"
                    case 6:
                        return "Redondo"
    b = randint(1,6)         
    class pele:
        if b == 1 or b == 2 or b == 3:

            def pele1(numero):
                """
                docstring
                """
                match numero:
                    case 1:
                        return "Amarelada"
                    case 2:
                        return "Áspera"
                    case 3:
                        return "Cicatrizada"
                    case 4:
                        return "Escura"
                    case 5:
                        return "Macia"
                    case 6:
                        return "Morena"
        elif b == 4 or b == 5 or b == 6:

            def pele2(numero):
                """
                docstring
                """
                match numero:
                    case 1:
                        return "Oleosa"
                    case 2:
                        return "Pálida"
                    case 3:
                        return "Pintada"
                    case 4:
                        return "Rosada"
                    case 5:
                        return "Sardenta"
                    case 6:
                        return "Tatuada"
    c = randint(1,6)
    class cabelo:
        if c == 1 or c == 2 or c == 3:

            def cabelo1(numero):
                """
                docstring
                """
                match numero:
                    case 1:
                        return "Careca"
                    case 2:
                        return "Crespo"
                    case 3:
                        return "Curto"
                    case 4:
                        return "Desgranhado"
                    case 5:
                        return "Encaracolado"
                    case 6:
                        return "Frizado"
        elif c == 4 or c == 5 or c == 6:

            def cabelo2(numero):
                """
                docstring
                """
                match numero:
                    case 1:
                        return "Longo"
                    case 2:
                        return "Luxuoso"
                    case 3:
                        return "Oleoso"
                    case 4:
                        return "Ondulado"
                    case 5:
                        return "Sedoso"
                    case 6:
                        return "Trançado"
    d = randint(1,6)
    class vestimenta:
        if d == 1 or d == 2 or d == 3:

            def vestimenta1(numero):
                """
                docstring
                """
                match numero:
                    case 1:
                        return "Antiga"
                    case 2:
                        return "Brega"
                    case 3:
                        return "Cerimonial"
                    case 4:
                        return "Decorada"
                    case 5:
                        return "Elegante"
                    case 6:
                        return "Estrangeira"
        elif d == 4 or d == 5 or d == 6:

            def vestimenta2(numero):
                """
                docstring
                """
                match numero:
                    case 1:
                        return "Extravagante"
                    case 2:
                        return "Folgada"
                    case 3:
                        return "Imunda"
                    case 4:
                        return "Manchada"
                    case 5:
                        return "Rasgada"
                    case 6:
                        return "Remendada"
    k = randint(1,6)
    class fala:
        if k == 1 or k == 2 or k == 3:

            def fala1(numero):
                """
                docstring
                """
                match numero:
                    case 1:
                        return "Arrastada"
                    case 2:
                        return "Contundente"
                    case 3:
                        return "Enigmática"
                    case 4:
                        return "Estridente"
                    case 5:
                        return "Formal"
                    case 6:
                        return "Gaguejante"
        elif k == 4 or k == 5 or k == 6:

            def fala2(numero):
                """
                docstring
                """
                match numero:
                    case 1:
                        return "Ligeira"
                    case 2:
                        return "Monótona"
                    case 3:
                        return "Murmurante"
                    case 4:
                        return "Precisa"
                    case 5:
                        return "Rouca"
                    case 6:
                        return "Sussurrada"
    e = randint(1,6)
    class virtude:
        if e == 1 or e == 2 or e == 3:

            def virtude1(numero):
                """
                docstring
                """
                match numero:
                    case 1:
                        return "Ambição"
                    case 2:
                        return "Coragem"
                    case 3:
                        return "Curiosidade"
                    case 4:
                        return "Disciplina"
                    case 5:
                        return "Generosidade"
                    case 6:
                        return "Gentileza"
        elif e == 4 or e == 5 or e == 6:

            def virtude2(numero):
                """
                docstring
                """
                match numero:
                    case 1:
                        return "Honestidade"
                    case 2:
                        return "Humildade"
                    case 3:
                        return "Idealismo"
                    case 4:
                        return "Lealdade"
                    case 5:
                        return "Prudência"
                    case 6:
                        return "Tolerância"
    f = randint(1,6)
    class vicio:
        if f == 1 or f == 2 or f == 3:

            def vicio1(numero):
                """
                docstring
                """
                match numero:
                    case 1:
                        return "Agressão"
                    case 2:
                        return "Arrogância"
                    case 3:
                        return "Covardia"
                    case 4:
                        return "Falsidade"
                    case 5:
                        return "Ganância"
                    case 6:
                        return "Imprudência"
        elif f == 4 or f == 5 or f == 6:

            def vicio2(numero):
                """
                docstring
                """
                match numero:
                    case 1:
                        return "Irreverência"
                    case 2:
                        return "Nervosismo"
                    case 3:
                        return "Preguiça"
                    case 4:
                        return "Rancor"
                    case 5:
                        return "Resguardo"
                    case 6:
                        return "Vaidade"
#Guardar os dados coletados a partir dos randints acima! O que vem em player_**, sendo player_corpo ou player_rosto é para armazenar
#E mostrar os resultados ao final do código.
if n == 1 or n == 2 or n == 3:
    physic = fisico
    player_corpo = physic.corpo1(randint(1,6))
    print(player_corpo)

elif n == 4 or n == 5 or n == 6:
    physic = fisico
    player_corpo = physic.corpo2(randint(1,6))
    print(player_corpo)

if m == 1 or m == 2 or m == 3:
    face = rosto
    player_rosto = face.rosto1(randint(1,6))
    print(player_rosto)

elif m == 4 or m == 5 or m == 6:
    face = rosto
    player_rosto = rosto.rosto2(randint(1,6))
    print(player_rosto)

if b == 1 or b == 2 or b == 3:
    skin = pele
    player_pele = skin.pele1(randint(1,6))
    print(player_pele)

elif b == 4 or b == 5 or b == 6:
    skin = pele
    player_pele = skin.pele2(randint(1,6))
    print(player_pele)

if c == 1 or c == 2 or c == 3:
    hair = cabelo
    player_cabelo = hair.cabelo1(randint(1,6))
    print(player_cabelo)

elif c == 4 or c == 5 or c == 6:
    hair = cabelo
    player_cabelo = hair.cabelo2(randint(1,6))
    print(player_cabelo)

if d == 1 or d == 2 or d == 3:
    clothes = vestimenta
    player_vestimenta = clothes.vestimenta1(randint(1,6))
    print(player_vestimenta)

elif d == 4 or d == 5 or d == 6:
    clothes = vestimenta
    player_vestimenta = clothes.vestimenta2(randint(1,6))
    print(player_vestimenta)

if k == 1 or k == 2 or k == 3:
    speech = fala
    player_fala = speech.fala1(randint(1,6))
    print(player_fala)

elif k == 4 or k == 5 or k == 6:
    speech = fala
    player_fala = speech.fala2(randint(1,6))
    print(player_fala)

if e == 1 or e == 2 or e == 3:
    virtue = virtude
    player_virtude = virtue.virtude1(randint(1,6))
    print(player_virtude)

elif e == 4 or e == 5 or e == 6:
    virtue = virtude
    player_virtude = virtue.virtude2(randint(1,6))
    print(player_virtude)

if f == 1 or f == 2 or f == 3:
    vice = vicio
    player_vicio = vice.vicio1(randint(1,6))
    print(player_vicio)

elif f == 4 or f == 5 or f == 6:
    vice = vicio
    player_vicio = vice.vicio2(randint(1,6))
    print(player_vicio)

#Gerador de personagem com auxílio!!!(Textos direto do livro)


elif x == 2:
    print("digite seu nome")
    nome = input()
    print("digite seus pronomes")
    pronome = input()
    print("digite seu arquétipo")
    arquetipo = input()
    print("digite sua ocupação")
    ocup = input()
    print("digite sua raca")
    raca = input()
    print("digite sua origem")
    origem = input()
else:
    print("digite um valor valido")


