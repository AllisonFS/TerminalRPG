import random
import time
import sys

class Personagem:
    # Passar no parametro --> 1 - nome | 2 - Três listas com 3 golpes contendo["Nome do golpe", "Dano", "Soteio 1", "Sorteio 2"] | 3 - Passar a vida | 4 - Vezes de cura
    # !!IMPORTANTE!! --> Primeiro move é o mais forte, Segundo move é a cura, Terceiro move é o mais fraco

    # a = Personagem("Allison", ["Flechada", 20, 0, 3], ["Cura", 20], ["Magia", 10, 0, 2], 40, 3)
    # b = Personagem("Maquina", ["Espadada", 30, 0, 2], ["Cura", 20], ["Investida", 10, 0, 2], 40, 3)

    # Função para a batalha
    # a.lutar(b)
    def __init__(self, name, move1, move2, move3, life, qnt_cura):
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.life = life
        self.name = name
        self.qnt_cura = qnt_cura

    def lutar(self, p2):
        # importaçoes
        import random
        import time
        import sys

        def texto_rpg(texto):
            for letra in texto:
                sys.stdout.write(letra)
                sys.stdout.flush()
                time.sleep(0.06)

        # Texto de inicio
        texto_rpg("Preparare-se para lutar...\n")

        # Loopdabatalha
        while (self.life > 0) and (p2.life > 0):
            qb1 = self.life
            qb2 = p2.life
            barras1 = qb1 * "\033[32m=\033[m"
            barras2 = qb2 * "\033[32m=\033[m"
            if qb1 == 30:
                barras1 = qb1 * "\033[1;33m=\033[m"
            if qb1 < 30:
                barras1 = qb1 * "\033[1;31m=\033[m"
            if qb2 <= 20:
                barras2 = qb2 * "\033[1;33m=\033[m"
            if qb2 < 20:
                barras2 = qb2 * "\033[1;31m=\033[m"

            print(f"""
            YOUR LIFE: {self.life}HP : {barras1}
            RIVAL'S LIFE: {p2.life}HP : {barras2}\n""")
            print("-----YOUR MOVES-----")
            print(f"""
        [1]: {self.move1[0]}
        [2]: {self.move2[0]}
        [3]: {self.move3[0]}
                """)

            # Entrada do jogador
            texto_rpg("Escolha...\n")
            entrada = input("?: ")

            # move1(Mais forte)
            if entrada == '1':
                texto_rpg(f"{self.name} escolheu {self.move1[0]}\n")
                sor = random.randint(self.move1[2], self.move1[3])
                if sor == 1:
                    texto_rpg("Você acertou...\n")
                    p2.life -= self.move1[1]
                    qb1 = self.life
                    qb2 = p2.life
                    barras1 = qb1 * "\033[32m=\033[m"
                    if qb2 <= 20:
                        barras2 = qb2 * "\033[1;33m=\033[m"
                else:
                    texto_rpg("Você errou...\n")

            # Move2(cura)
            if entrada == '2':
                texto_rpg(f"{self.name} escolheu {self.move2[0]}\n")
                self.qnt_cura -= 1
                cod = True
                while self.qnt_cura <= 0 and cod:
                    texto_rpg("Você usou toda sua cura... Escolha outro Move\n")
                    entrada = input("?: ")
                    if entrada == '3':
                        texto_rpg(f"{self.name} escolheu {self.move3[0]}\n")
                        sor = random.randint(self.move3[2], self.move3[3])
                        if sor == 1:
                            texto_rpg("Você acertou..\n")
                            p2.life -= self.move3[1]
                            qb1 = self.life
                            qb2 = p2.life
                            barras1 = qb1 * "\033[32m=\033[m"
                            barras2 = qb2 * "\033[32m=\033[m"
                            cod = False
                        else:
                            texto_rpg("Você errou...\n")
                            cod = False

                    if entrada == '1':
                        texto_rpg(f"{self.name} escolheu {self.move1[0]}\n")
                        sor = random.randint(self.move1[2], self.move1[3])
                        cod = False
                        if sor == 1:
                            texto_rpg("Você acertou...\n")
                            p2.life -= self.move1[1]
                            qb1 = self.life
                            qb2 = p2.life
                            barras1 = qb1 * "\033[32m=\033[m"
                            barras2 = qb2 * "\033[32m=\033[m"
                            cod = False
                        else:
                            texto_rpg("Você errou...\n")
                            cod = False

                if self.qnt_cura > 0:
                    self.life += self.move2[1]
                    qb1 = self.life
                    qb2 = p2.life
                    barras1 = qb1 * "\033[32m=\033[m"
                    barras2 = qb2 * "\033[32m=\033[m"
                    texto_rpg(f"Você curou {self.move2[1]}HP")

            # Move3(Mais fraco)
            if entrada == '3':
                texto_rpg(f"{self.name} escolheu {self.move3[0]}\n")
                sor = random.randint(self.move3[2], self.move3[3])
                if sor == 1:
                    texto_rpg("Você acertou..\n")
                    p2.life -= self.move3[1]
                    qb1 = self.life
                    qb2 = p2.life
                    barras1 = qb1 * "\033[32m=\033[m"
                    barras2 = qb2 * "\033[32m=\033[m"
                else:
                    texto_rpg("Você errou...\n")

            # Verificar se alguém está sem HP
            if p2.life <= 0:
                print(f"""
            YOUR LIFE: {self.life}HP : {barras1}
            RIVAL'S LIFE: {p2.life}HP : {barras2}\n""")
                texto_rpg(f"{p2.name} desmaiou")
                break

            # Maquina
            Sor = random.randint(0, 2)
            print(f"""
            YOUR LIFE: {self.life}HP : {barras1}
            RIVAL'S LIFE: {p2.life}HP : {barras2}\n""")

            texto_rpg(f"Vez de {p2.name}...\n")

            # Move1(Mais forte)
            if Sor == 0:
                texto_rpg(f"{p2.name} escolheu {p2.move1[0]}\n")
                sor = random.randint(p2.move1[2], p2.move1[3])
                if sor == 1:
                    texto_rpg(f"{p2.name} acertou...\n")
                    self.life -= p2.move1[1]
                    qb1 = self.life
                    qb2 = p2.life
                    barras1 = qb1 * "\033[32m=\033[m"
                    barras2 = qb2 * "\033[32m=\033[m"
                    if qb1 == 30:
                        barras1 = qb1 * "\033[1;33m=\033[m"
                    if qb1 < 30:
                        barras1 = qb1 * "\033[1;31m=\033[m"
                    if qb2 <= 20:
                        barras2 = qb2 * "\033[1;33m=\033[m"
                    if qb2 < 20:
                        barras2 = qb2 * "\033[1;31m=\033[m"

                else:
                    texto_rpg(f"{p2.name} errou...\n")

            # Move2(Cura)
            if Sor == 1:
                p2.qnt_cura -= 1
                if p2.qnt_cura > 0:
                    texto_rpg(f"{p2.name} escolheu {p2.move2[0]}\n Curou {p2.move2[1]}HP")
                    p2.life += p2.move2[1]
                    qb1 = self.life
                    qb2 = p2.life
                    barras1 = qb1 * "\033[32m=\033[m"
                    barras2 = qb2 * "\033[32m=\033[m"

                elif p2.qnt_cura <= 0:
                    sor2 = random.randint(0, 1)
                    if sor2 == 0:
                        texto_rpg(f"{p2.name} escolheu {p2.move1[0]}\n")
                        sor = random.randint(p2.move1[2], p2.move1[3])
                        if sor == 1:
                            texto_rpg(f"{p2.name} acertou...\n")
                            self.life -= p2.move1[1]
                            qb1 = self.life
                            qb2 = p2.life
                            barras1 = qb1 * "\033[32m=\033[m"
                            barras2 = qb2 * "\033[32m=\033[m"
                        else:
                            texto_rpg(f"{p2.name} errou...\n")

                    if sor2 == 1:
                        texto_rpg(f"{p2.name} escolheu {p2.move3[0]}\n")
                        sor = random.randint(p2.move3[2], p2.move3[3])
                        if sor == 1:
                            texto_rpg(f"{p2.name} acertou...\n")
                            self.life -= p2.move3[1]
                            qb1 = self.life
                            qb2 = p2.life
                            barras1 = qb1 * "\033[32m=\033[m"
                            barras2 = qb2 * "\033[32m=\033[m"
                        else:
                            texto_rpg(f"{p2.name} errou...\n")

            # Move3(Mais fraco)
            if Sor == 2:

                texto_rpg(f"{p2.name} escolheu {p2.move3[0]}\n")
                sor = random.randint(p2.move3[2], p2.move3[3])
                if sor == 1:
                    texto_rpg(f"{p2.name} acertou...\n")
                    self.life -= p2.move3[1]
                    qb1 = self.life
                    qb2 = p2.life
                    barras1 = qb1 * "\033[32m=\033[m"
                    barras2 = qb2 * "\033[32m=\033[m"
                else:
                    texto_rpg(f"{p2.name} errou...\n")

            # Verificar se alguém está sem HP
            if self.life <= 0:
                print(f"""
            YOUR LIFE: {self.life}HP : {barras1}
            RIVAL'S LIFE:  {p2.life}HP : {barras2}\n""")
                texto_rpg(f"{self.name} desmaiou")
                break
        
        return self.life, p2.life
   
def texto_rpg(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.01)

def tempo():
    time.sleep(0.5)


def texto_rpg(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.06)


def texto_massa(texto):
    print('\033[1;34m—\033[m' * 60)
    print('\033[1;34m<\033[m' * 60)
    print(texto)
    print('\033[1;34m—\033[m' * 60)
    print('\033[1;34m<\033[m' * 60)

put = input("Let's to play now!! [S/N]: ").upper()
if put == "S":
    texto_massa("O jogador escolheu (MODO HISTORIA)")
    time.sleep(2)

    texto_rpg("...\n")
    texto_rpg("....\n")
    texto_rpg("......\n")

    texto_rpg("(?): Olá!")
    tempo()
    texto_rpg("(?): Nossa... Quando tempo não converso assim...\n")
    time.sleep(1)
    texto_rpg("(?): Aaah, antes de tudo, permita-me apresentar-me.\n")
    time.sleep(1)
    texto_rpg("(?): Meu nome é Gubeter e sou um cavaleiro...\n")
    tempo()
    texto_rpg("(Guteber): Bom... Vou te contar uma história, gostaria de ouvir? (S/N)\n")
    entrada_1 = input("<Digite a opçao>: ").upper()

    while entrada_1 != "S":
        texto_rpg("(Guteber): Uau, vai ser interesante. Vamos nessa!!")
        texto_rpg("(Guteber): Bom... Vamos? (S/N)")
        entrada_1 = input("<Digite a opçao>: ").upper()

    texto_rpg("(Guteber): Let's go!!\n")
    tempo()
    texto_rpg("(Gubeter): Nosso mundo é habitado por criaturas estralhas... mas...\n")
    texto_rpg(
        "(Guteber): Existia uma familía muito inteligente\n Frix e Lauriem. Eles tinham um filho\n e dominavam uma arte exclusiva e misteriosa...\n")
    texto_rpg("(Guteber): Adivinha?\n")
    entrada_2 = input("<Digite a opçao>: ").upper()

    if entrada_2 == "MAGIA":
        texto_rpg("(Guteber): Sim!!!\n")
    else:
        texto_rpg("(Guteber): Não, vou te falar o que é\n ")

    texto_rpg("(Guteber): Magia não é para todos, poucos sabiam dominá-la\n")
    tempo()
    texto_rpg("(Guteber): Bom... O filho deles??... eles o ensinaram a tal arte\n")
    tempo()
    texto_rpg("(Guteber): Ok, eu queria aprender... mas eles não estão mais aqui...\n")
    tempo()
    texto_rpg("(Guteber): Mas você...\n")
    tempo()
    texto_rpg("(Guteber): ... perdoe-me(risos), não deixei você apresentar-se. Mas então, como posso te chamar?\n")
    nome_do_jg = input("<DIGITE A OPÇAO>: ")
    texto_rpg("...")
    tempo()
    texto_rpg(f"(Guteber): Sinto muito {nome_do_jg}... Seus pais morreram salvando-te de um MORFO\n")
    tempo()
    texto_rpg("(Guteber): Nossa, essa criatura é muito poderosa... A magia não foi suficiente\n")
    tempo()
    texto_rpg("(Guteber): Eu estava lá... eles deram a vida por você...\n")
    tempo()
    texto_rpg("(Guteber): Eu me sinto horrível....\n")
    tempo()
    texto_rpg("(Guteber): Apenas salvei você....\n")
    tempo()
    texto_rpg("(Guteber): Você me perdoa?...\n")

    entrada_3 = input("<DIGITE A OPÇAO>(S/N): ").upper()
    if entrada_3 == "S":
        texto_rpg(f"(Guteber): Obrigado, {nome_do_jg}\n")
    elif entrada_3 == "N":
        texto_rpg(f"(Guteber): Eu entendo, {nome_do_jg}\n")
    elif entrada_3 != "N" or "S":
        texto_rpg("(Guteber): Não entendi\n")

    tempo()
    texto_rpg("(Guteber): ... ok... vamos dá uma saida?\n")
    entrada_4 = input("<DIGITE A OPÇAO>(S/N): ").upper()
    while entrada_4 != "S":
        texto_rpg("(Guteber): Vamos lá Rapaz... conheça o mundo, siga em frente\n")
        texto_rpg("(Guteber): ... ok... vamos dá uma saida?\n")
        entrada_4 = input("<DIGITE A OPÇAO>(S/N): ").upper()

    texto_rpg("(Guteber): Vamos nessa!\n")
    texto_rpg("...\n")
    tempo()
    texto_rpg('...\n')
    tempo()
    texto_rpg("(Guteber): Eae... quando tempo, não?...\n")
    tempo()
    texto_rpg("(info): Você vê o mundo após muito tempo.....\n")
    tempo()
    texto_rpg("(info): Você ainda sabe um pouco de magia...\n")
    tempo()
    texto_massa("Sua vida: 30\nSeus ataques: Pó Mágico\nSoco")
    tempo()
    texto_rpg("...\n ....\n")

    texto_rpg(f"(Guteber): Ei {nome_do_jg} vamos ao local que seus pais moravam?\n")
    entrada_5 = input("<DIGITE A OPÇAO>(S/N): ").upper()
    while entrada_5 != "S":
        texto_rpg("(Guteber): Eu sei como se sente, mas devemos ir. Você não lembra mais deles\n vamos...\n")
        entrada_5 = input("<DIGITE A OPÇAO>(S/N): ").upper()

    texto_rpg("...\n ... \n .... \n")
    tempo()
    texto_rpg("(info): Chegaram...\n")
    tempo()
    texto_rpg("(info): Você está perto de um quadro\n")
    tempo()
    texto_rpg("É seus pais?\n")
    entrada_6 = input("<DIGITE A OPÇAO>(S/N): ").upper()
    if entrada_6 == "S":
        texto_rpg("Você se emociona\n")
        tempo()
    else:
        texto_rpg("Você o joga fora")
        tempo()

    texto_rpg(f"(Guteber): {nome_do_jg} há algo atras de você\n")
    tempo()
    texto_rpg("(info): Você viu um kondo!!\n")
    tempo()
    kondo = Personagem("Kondo", ["cuspi", 10, 0, 3], ["Cura", 5], ["Morder", 5, 0, 2], 15, 2)
    jgn1 = Personagem(nome_do_jg, ["Pó Mágico", 20, 0, 3], ["Cura", 20], ["Soco", 10, 0, 2], 30, 3)
    jgn1.lutar(kondo)
    while jgn1.life <= 0:
        texto_rpg('Lutar novamente')
        kondo.life += 5
        jgn1.life += 10
        jgn1.lutar(kondo)
        
    time.sleep(2)
    texto_rpg("(Guteber): Eu nao acredido...\n")
    tempo()
    texto_rpg("(Guteber): Você usou magia...\n")
    texto_rpg("(Guteber): Como você sabe disso?\n")
    print("""
    [a] = NÃO SEI
    [b] = MEUS PAIS ME ENSINARAM
    [c] = FOI INSTINTO
    """)
    entrada_7 = input("<DIGITE A OPÇAO>(S/N): ").upper()

    if entrada_7 == "A" or "C":
        texto_rpg("Bom, suponho que você herdou dos seus pais\n")
        tempo()
    elif entrada_7 == "C" or "B":
        texto_rpg("(Guteber): Foi o que imaginei\n")
        tempo()
    else:
        texto_rpg("(Guteber): Bom... Fique calmo\n")
        tempo()

    texto_rpg("(Guteber): Você tem dom rapaz, vou leva-lo a um lugar que voce vai gostar\n")
    tempo()
    texto_rpg("(Guteber): Fica um pouco perto de onde eu moro, vamos lá\n")
    tempo()
    texto_massa("Carregando Dados...")
    tempo()
    texto_massa("Você irá para o centro da cidade, há um Bar por perto...")
    tempo()
    texto_massa("Há uma garota chamada LANA, ela é garçonete")
    tempo()
    texto_rpg("Info: Você entra com Guteber...\n")
    tempo()
    texto_rpg("Info: Guteber sauda seus amigos\n")
    tempo()
    texto_rpg(f"(Guteber): Olha {nome_do_jg}, aquela é LANA... Ela é lind... ...digo... ugr... faz armamentos\n")
    tempo()
    texto_massa("(Guteber): LANAAA!!!!!\n")
    tempo()
    texto_rpg("(info): Lana não gosta do barulho...\n")
    tempo()
    texto_rpg("(Lana): Ei, cala boca por favor, vai espantar a crientela....\n")
    tempo()
    texto_rpg("(info: Lana lhe diz (quem é você)\n")
    tempo()
    print(f"""
    [a] = Prazer, sou o {nome_do_jg}
    [b] = Nossa, você é gata... sou o {nome_do_jg}
    """)
    entrada_8 = input("Digite a opçao>: ").upper()
    if entrada_8 == "A":
        texto_rpg(f"(Lana): .... Bem-vindo {nome_do_jg}\n")
        tempo()
    else:
        texto_rpg(f"(Lana): ....UGR...Não gosto de caras folgados\n")
        tempo()
    texto_rpg(
        f"(Guteber): Olha, Lana, {nome_do_jg} precisa de um armamento... nesse mundo...  Cheio dessas criaturas...\n")
    tempo()
    texto_rpg('(Lana): Venha para sala de armamentos...\n')
    tempo()
    texto_rpg("................\n")
    tempo()
    texto_massa("No bar, há uma sala de armamentos\n")
    tempo()
    texto_massa("Por sorte há um arco pronto\n")
    tempo()
    texto_rpg("...\n")
    tempo()
    texto_rpg("(Lana): Olha, só tenho esse arco...\n Deve ajudá-lo para se defender\n")
    tempo()
    texto_rpg("(info): Você se questiona sobre esse mundo misterioso...\n")
    texto_rpg("(Lana): Você nāo sabe sobre as criaturas?\n")
    tempo()
    print("""
    [a] = Só sei que mataram meus pais
    [b] = Tenho muitas dúvidas
    """)
    entrada_9 = input("<Digite a opçao>: ").upper()
    if entrada_9 == 'A':
        texto_rpg(f"(Lana): Sinto Muito {nome_do_jg}\n")
        tempo()
    elif entrada_9 == 'B':
        texto_rpg("(Lana): Bom... \n")
        tempo()

    else:
        texto_rpg("(Lana): Está gagejando de medo? haha....\n")
        tempo()

    texto_rpg("(Lana): Bom... Há muito tempo... os humanos viviam em paz, multiplicando-se pelo mundo\n")
    tempo()
    texto_rpg("(Lana): Todos viviam livre, podiam viver, trabalhar, se divetir...\n")
    tempo()
    texto_rpg("(Lana): Mas... numa época pra cá, as coisas mudaram...\n")
    tempo()
    texto_rpg("(Lana): Mas os Kaibutsu reinaram aqui no planeta...\n")
    tempo()
    texto_rpg(
        "(Lana): Bom... eles estavam sob controle.... por algum motivo eles estão aparencendo com mais frequencia...\n")
    tempo()
    texto_rpg("(Guteber): Lana... os pais deles eram...\n")
    tempo()
    texto_rpg("(Lana: )Não me diga que você é filho de Frix e Lauriem?")
    tempo()
    print("""
    [a] = Sim... sou o único mago
    [b] = Sim... eles morreram me salvando
    """)
    entrada_10 = input("<Digite a opçao>: ").upper()
    if entrada_10 == 'A':
        texto_rpg("(Lana): Por isso, Eles mantian os Kaibutsus neutros")
        tempo()
    elif entrada_10 == 'B':
        texto_rpg("(Lana): Agora entendo, Eles mantian os Kaibutsus neutros")
        tempo()
    texto_massa("KABOMMMMM")
    tempo()
    texto_massa("Um morfo está quebrando tudo...")
    tempo()
    texto_rpg("Guteber salva Lana\n")
    tempo()
    texto_rpg('(info): Prepare-se para a luta...')
    tempo()
    texto_massa("Sua vida: 30\nSeus ataques: Magia pura\nFlechada\nCura(3vezes)")
    tempo()
    morfo = Personagem("Morfo", ["Ataque Furacão", 30, 0, 4], ["Cura sombria", 30], ["Morder", 20, 0, 2], 80, 4)
    jgn2 = Personagem(nome_do_jg, ["Magia Pura", 30, 0, 2], ["Cura", 20], ["Flechada", 35, 0, 3], 40, 3)
    jgn2.lutar(morfo)
    
    while jgn2.life <= 0:
        texto_rpg(f'{morfo.name} te derrotou\n preparece para lutar novamente\n')
        kondo.life += 30
        jgn2.life += 20
        jgn2.lutar(morfo)
    
    tempo()
    texto_rpg("(Guteber): Ei... voce está legal?\n")
    tempo()
    print("""
    [a] = Sim, estou...
    [b] = Estou machucado, mas o derrotei
    """)
    entrada_11 = input("<Digite a opçao>: ").upper()
    if entrada_11 == "A":
        texto_rpg("(Guteber): Você precisa de cuidados médicos...\n")
        tempo()
    elif entrada_11 == "B":
        texto_rpg("(Guteber): Uau, Você derrotou a criatura que tirou seus pais......\n")  
    else:
        texto_rpg("(Guteber): Você está tão machucado que não fala corretamente\n")
        tempo()
    texto_rpg(f"(Guteber): Perdoe-me {nome_do_jg}\nEu estava salvando Lana...\n")
    tempo()
    texto_rpg("(info): Você diz: \n")
    tempo()
    print(""""
    [a] = Ela está bem?
    [b] = Onde elá está?
    """)
    entrada_12 = input("<Digite a opçao>: ").upper()
    if entrada_12 == 'A':
        texto_rpg("(Guteber): Uh... sim... Rapaz...\n Vejo que tem mais alguém interessado\n")
        tempo()
    elif entrada_11 == 'B':
        texto_rpg("(Guteber): Está na minha casa...\n")
        tempo()
    else:
        texto_rpg("(Guteber): Ok.....\n")
        tempo()
    
    texto_rpg("(Guteber): Vou levá-lo até ela\n")
    tempo()
    texto_massa("Carregando dados...")
    time.sleep(2.5)
    texto_rpg("(Info): Você vê lana bem...\n")
    tempo()
    texto_rpg("(Lana): Eu estou bem...\nMelhor eu voltar para meu trabalho...\n")
    tempo()
    texto_rpg("(Lana): Nossa... Aquele Morfo deatruiu tudo...")
    tempo()
    texto_rpg(f"(Guteber): Desde que os pais de {nome_do_jg} morreram, esses monstros Kaibutsu estão aparecendo com mais frequencia...\n")
    tempo()
    texto_rpg("(Lana): Bom... eles os controlavam\n")
    tempo()
    texto_rpg("(Guteber): Sim... A porção controladora...\n")
    tempo()
    texto_rpg("(Guteber): Já sei...\n")
    tempo()
    texto_rpg("(Lana): Não Guteber...\n")
    tempo()
    texto_rpg("(Guteber): Sim, existe uma pessoa que era muito amigo de seus pais, ele mora próximo onde está sugindo os Kaibtsu...\n")
    tempo()