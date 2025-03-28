import random  # Importa a biblioteca para gerar números aleatórios
import time  # Importa a biblioteca para manipulação de tempo (usado para delays)
import sys  # Importa a biblioteca para controle da saída no terminal
from os import system  # Importa a função system para limpar a tela do terminal
from colorama import init, Fore  # Importa a biblioteca colorama para colorir o texto no terminal
import pygame  # Importa a biblioteca pygame para manipulação de áudio


pygame.init()  # Inicializa o pygame
init()

# Função para simular tempo de espera
def tempo(t):
    time.sleep(t)  # Faz o programa "dormir" por 't' segundos


# Função para exibir barras de vida
def exibir_barra_vida(nome, vida, vida_max):
    barra = int((vida / vida_max) * 20)  # Calcula a proporção da barra de vida
    if vida >= 40: 
        print(f"{nome}: [{Fore.GREEN + '#' * barra + Fore.RESET}{'-' * (20 - barra)}] {vida}/{vida_max} HP")  # Exibe a barra de vida no formato [####--------] 50/100 HP
    elif vida >= 21 and vida <= 39:
        print(f"{nome}: [{Fore.YELLOW + '#' * barra + Fore.RESET}{'-' * (20 - barra)}] {vida}/{vida_max} HP")
    else:
        print(f"{nome}: [{Fore.RED + '#' * barra + Fore.RESET}{'-' * (20 - barra)}] {vida}/{vida_max} HP")


# Função para exibir texto em estilo RPG (efeito de digitação)
def texto_rpg(texto):
    for letra in texto:
        sys.stdout.write(letra)  # Escreve cada letra na tela
        sys.stdout.flush()  # Garante que a letra seja exibida imediatamente
        time.sleep(0.05)  # Pausa entre cada letra para simular digitação
    print()  # Pula uma linha após o texto


# Função para exibir texto com formatação especial
def texto_massa(texto):
    print('\033[1;34m—\033[m' * 60)  # Exibe uma linha com traços azuis
    print('\033[1;34m<\033[m' * 60)  # Exibe uma linha com os caracteres '<' em azul
    print(texto)  # Exibe o texto centralizado
    print('\033[1;34m—\033[m' * 60)  # Exibe outra linha de traços azuis
    print('\033[1;34m<\033[m' * 60)  # Exibe outra linha de '<' em azul


def musica_batalha():
    pygame.mixer.music.load(r"music\batalha.mp3")  # Carrega a música
    pygame.mixer.music.play(-1)  # Toca a música em loop infinito
    pygame.mixer.music.set_volume(0.5)  # Define o volume da música


def musica_venceu():
    pygame.mixer.music.load(r"music\venceu.mp3")  # Carrega a música de vitória
    pygame.mixer.music.play(0)  # Toca a música uma vez
    pygame.mixer.music.set_volume(0.5)  # Define o volume da música


def musica_perdeu():
    pygame.mixer.music.load(r"music\game_over.mp3")  # Carrega a música de derrota
    pygame.mixer.music.play(0)  # Toca a música uma vez
    pygame.mixer.music.set_volume(0.5)  # Define o volume da música

# Classe do personagem
class Character:
    def __init__(self, name, max_health, attack_power, heal_amount, sorte):
        self.name = name  # Nome do personagem
        self.max_health = max_health  # Vida máxima do personagem
        self.health = max_health  # Vida atual do personagem
        self.attack_power = attack_power  # Poder de ataque
        self.heal_amount = heal_amount  # Quantidade de cura
        self.frozen = False  # Indica se está congelado
        self.bonus_attack = False  # Indica se já usou trovão
        self.sorte = sorte  # Parâmetro para sorteios (probabilidades)


    def attack(self, opponent):
        """Ataca o oponente"""
        if not self.frozen:  # Só ataca se não estiver congelado
            sorteio = random.randint(0, self.sorte[1])  # Sorteia um número para determinar se o ataque acerta
            if sorteio == 0:
                tempo(1)  # Pausa de 1 segundo para efeito
                damage = random.randint(self.attack_power[1] - 2, self.attack_power[1] + 2)  # Cálculo do dano aleatório
                opponent.health -= damage  # Aplica o dano no oponente
                texto_rpg(f"{self.name} acertou o golpe {self.attack_power[0]}, causando {damage} de dano!")  # Exibe mensagem de ataque
            else:
                tempo(1)  # Pausa de 1 segundo para efeito
                texto_rpg(f"{self.name} errou o ataque!")  # Exibe mensagem de erro de ataque
        else:
            texto_rpg(f"{self.name} está congelado e não pode atacar neste turno!")  # Caso o personagem esteja congelado
            self.frozen = False  # No próximo turno poderá atacar novamente


    def rage(self, opponent):
        """Ataca o oponente com Rage"""
        if not self.frozen:  # Só ataca se não estiver congelado
            sorteio = random.randint(0, self.sorte[2])  # Sorteio para determinar sucesso do ataque
            if sorteio == 0:
                tempo(1)  # Pausa de 1 segundo para efeito
                damage = random.randint(self.attack_power[3] - 2, self.attack_power[3] + 2)  # Cálculo do dano aleatório
                opponent.health -= damage  # Aplica o dano no oponente
                texto_rpg(f"{self.name} acertou o golpe {self.attack_power[2]}, causando {damage} de dano!")  # Exibe mensagem de ataque
            else:
                tempo(1)  # Pausa de 1 segundo para efeito
                texto_rpg(f"{self.name} errou o ataque!")  # Exibe mensagem de erro de ataque
        else:
            texto_rpg(f"{self.name} está congelado e não pode atacar neste turno!")  # Caso o personagem esteja congelado
            self.frozen = False  # No próximo turno poderá atacar novamente


    def dimensao(self, opponent):
        if not self.frozen:  # Só ataca se não estiver congelado
            sorteio = random.randint(0, self.sorte[2])  # Sorteio para determinar sucesso do ataque
            if sorteio == 0:
                tempo(1)  # Pausa de 1 segundo para efeito
                damage = random.randint(self.attack_power[3] - 2, self.attack_power[3] + 2)  # Cálculo do dano aleatório
                opponent.health -= damage  # Aplica o dano no oponente
                texto_rpg(f"{self.name} acertou o golpe {self.attack_power[2]}, causando {damage} de dano!")  # Exibe mensagem de ataque
            else:
                tempo(1)  # Pausa de 1 segundo para efeito
                texto_rpg(f"{self.name} errou o ataque!")  # Exibe mensagem de erro de ataque
        else:
            texto_rpg(f"{self.name} está congelado e não pode atacar neste turno!")  # Caso o personagem esteja congelado
            self.frozen = False  # No próximo turno poderá atacar novamente


    def heal(self):
        """Cura a si mesmo"""
        heal_points = random.randint(self.heal_amount - 2, self.heal_amount + 2)  # Cálculo da cura aleatória
        self.health = min(self.health + heal_points, self.max_health)  # A vida não pode ultrapassar o máximo
        tempo(1)  # Pausa de 1 segundo para efeito
        texto_rpg(f"{self.name} se curou em {heal_points} pontos!")  # Exibe mensagem de cura


    def gelo(self, opponent):
        """Chance de congelar o inimigo"""
        sorteio = random.randint(0, 2)  # 1/3 de chance de erro
        if sorteio == 0:
            tempo(1)  # Pausa de 1 segundo para efeito
            damage = random.randint(self.attack_power[3] - 2, self.attack_power[3] + 2)  # Cálculo do dano
            opponent.health -= damage  # Aplica o dano
            opponent.frozen = True  # Congela o inimigo
            texto_rpg(f"{self.name} usou {self.attack_power[2]}! Dano {damage}. {opponent.name} está congelado e perdeu o turno!")  # Exibe mensagem de ataque
        else:
            tempo(1)  # Pausa de 1 segundo para efeito
            texto_rpg(f"{self.name} tentou usar {self.attack_power[2]}, mas errou!")  # Exibe mensagem de erro


    def buff(self):
        """Aumenta o poder de ataque"""
        self.attack_power[1] += 2  # Aumenta o poder de ataque
        texto_rpg("Ataque aumentou em 2")  # Exibe mensagem de aumento de ataque


    def trovao(self):
        """Aumenta a velocidade apenas uma vez por luta"""
        if not self.bonus_attack:
            qualbuffar = input(f"Qual ataque quer bufar?\n1 {self.attack_power[0]}\n2 {self.attack_power[2]}\n: ")  # Escolha do jogador
            if qualbuffar == "1":
                self.sorte[1] -= 1  # Diminui a chance de erro do primeiro ataque
                self.bonus_attack = True  # Marca que o bônus foi usado
                texto_rpg(f"{self.name} usou {self.sorte[0]}! Você está mais rápido!")  # Exibe mensagem de aumento
            elif qualbuffar == "2":
                self.sorte[2] -= 1  # Diminui a chance de erro do segundo ataque
                self.bonus_attack = True  # Marca que o bônus foi usado
                texto_rpg(f"{self.name} usou {self.sorte[0]}! Você está mais rápido!")  # Exibe mensagem de aumento
        else:
            texto_rpg("TROVÃO já foi usado nesta luta!")  # Caso o bônus já tenha sido usado


# Função principal da batalha
def battle_boss_2(player, enemy):
    musica_batalha()  # Inicia a música de batalha
    turno = 0  # Contador de turnos
    while player.health > 0 and enemy.health > 0:  # A luta continua enquanto ambos os personagens estiverem vivos
        turno += 1  # Incrementa o turno
        tempo(0.7)  # Pausa antes de exibir o turno
        system('cls||clear')  # Limpa a tela do terminal (Windows ou Linux)

        tempo(1)  # Pausa de 1 segundo para efeito
        exibir_barra_vida(player.name, player.health, player.max_health)  # Exibe a barra de vida do jogador
        exibir_barra_vida(enemy.name, enemy.health, enemy.max_health)  # Exibe a barra de vida do inimigo

        # Verifica se o jogador está congelado
        if player.frozen:
            texto_rpg(f"{player.name} está congelado e não pode agir neste turno!")  # Exibe mensagem
            player.frozen = False  # No próximo turno ele poderá agir
        else:
            print(f"""
                turno {turno}
                (A) Atacar Dano {player.attack_power[1]}
                (G) RAGE
                (H) Curar
                (T) TROVÂO
            """)  # Exibe as opções de ação
            action = input("Sua escolha: ").upper()  # Recebe a ação do jogador

            if action == 'A':
                player.attack(enemy)  # Chama a função de ataque
            elif action == 'G':
                player.rage(enemy)  # Chama a função de rage
            elif action == 'H':
                player.heal()  # Chama a função de cura
            elif action == 'T':
                player.trovao()  # Chama a função de trovão
            else:
                texto_rpg("Opção inválida! Perdeu a vez.")  # Caso a opção seja inválida

        # Verifica se o inimigo foi derrotado
        if enemy.health <= 0:
            system('cls||clear')
            musica_venceu()
            exibir_barra_vida(player.name, player.health, player.max_health)  # Exibe a barra de vida do jogador
            exibir_barra_vida(enemy.name, enemy.health, enemy.max_health)  # Exibe a barra de vida do inimigo
            texto_rpg(f"\n{enemy.name} foi derrotado! {player.name} venceu!")
            tempo(2)  # Pausa de 2 segundos para efeito
            break  # Termina a batalha se o inimigo for derrotado

        # Turno do inimigo IA
        if enemy.frozen:
            texto_rpg(f"{enemy.name} ainda está congelado e perdeu o turno!")  # Exibe mensagem se o inimigo estiver congelado
            enemy.frozen = False  # No próximo turno o inimigo poderá agir
        else:
            player_health_percentage = (player.health / player.max_health) * 100  # Calcula a porcentagem de vida do jogador
            enemy_health_percentage = (enemy.health / enemy.max_health) * 100  # Calcula a porcentagem de vida do inimigo

        # Determina a ação do inimigo com base na porcentagem de vida do jogador
        if enemy_health_percentage <= 40:
            enemy_action = 'H'  # Prioriza a cura
        elif player_health_percentage > 80:
            enemy_action = "G"  # Pode usar gelo
        else:
            enemy_action = random.choice(['G', 'A'])  # Escolhe entre gelo ou ataque aleatoriamente

        # Realiza a ação do inimigo
        if enemy_action == 'A':
            enemy.attack(player)  # Inimigo ataca
        elif enemy_action == 'G':
            enemy.gelo(player)  # Inimigo usa gelo
        elif enemy_action == 'H':
            enemy.heal()  # Inimigo se cura

        # Verifica se o jogador foi derrotado
        if player.health <= 0:
            system('cls||clear')
            musica_perdeu()
            exibir_barra_vida(player.name, player.health, player.max_health)  # Exibe a barra de vida do jogador
            exibir_barra_vida(enemy.name, enemy.health, enemy.max_health)  # Exibe a barra de vida do inimigo
            texto_rpg(f"\n{player.name} foi derrotado! {enemy.name} venceu!")
            tempo(10)  # Pausa de 10 segundos para fim da música
            break  # Termina a batalha se o jogador for derrotado

# Criando personagens
jogador = Character("Herói", 50, ["Espada", 10, "Rage", 20], 8, ["Trovãoooo",1,3])  # Personagem do jogador
inimigo = Character("Monstro", 50, ["Garra", 10, "Geladinho", 13], 8, ["Fica Frio ae",1,2])  # Personagem do inimigo

# Iniciar batalha
battle_boss_2(jogador, inimigo)  # Inicia a batalha entre o jogador e o inimigo