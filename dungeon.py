import random
from mainsala import Sala_principal
from subsala import Subsala
from salafinal import SalaBossFinal
from mago import Maguinho
from chefe import boss
import os
import sys
from rich.console import Console
import pygame

#cor das letras
console = Console()#todos os consoles.print são para colorir as letras

#tocar a musica
pygame.mixer.init()
def ost(music):
    try:
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(0.3)  #volume
        pygame.mixer.music.play(-1)  # Loop da parada
    except pygame.error as e:
        print(f"Erro ao carregar música: {e}")

#aqui puxa as informações dos bosses e do boss final
def startar_dungeon():
    salas = [
        Subsala("Sala 1", boss("Goblins", 12), "[purple]Bixos grotescos que simplesmente são desleais por natureza, abata um por um para a sua sobrevivência[/purple]", ["agua", "gelo"], "\nHá algo que até átomos possam ficar parados? Acho que não... mas pode chegar perto disso"),
        Subsala("Sala 2", boss("Minotauro", 12), "[blue]Quando você entra na sala, uma criatura vem direto na tua direção querendo te furar(la ele), mas você desvia e quando olha em direção à criatura, simplesmente um monstro raro está à sua frente... um Minotauro.[/blue]", ["raio", "fogo"], "\nExploda tudo que há na sua frente que revelará o caminho."),
        Subsala("Sala 3", boss("Ciclope", 12), "[purple]O monstro à sua frente é simplesmente um Ciclope, aquilo que está em sua frente é pulverizado com seu único olho horroroso(diga-se de passagem) talvez haja algum jeito de distraí-lo.[/purple]", ["raio", "agua"], "\nHá algo tão forte quanto as correntezas em dias de chuva..."),
        Subsala("Sala 4", boss("Serpente Gigante", 12), "[blue]Parece um desafio impossível para você, que está tremendo por causa dessa cobra gigantesca, há algo que se possa fazer?[/blue]", ["agua", "raio"], "\nHá algo tão puro e belo que possa ficar instável?"),
        Subsala("Sala do Final Boss", boss("Hidra", 16), "[purple]Simplesmente um dragão com várias cabeças, você nunca viu algo tão asqueroso na sua vida, mas era necessário enfrentar essa desgraça para terminar o desafio.[/purple]", ["terra"], "\nDepois de tantas infusões falhas, você sente em seu coração um estrondo... mas será que é o suficiente?")
    ]
    return salas

def enigma(dica, debuffar, player, boss):
    limpar()
    console.print("\n[blue]A luta é intensa... mas com base nos ataques do monstro, você teve alguma ideia[/blue]")
    console.print(f"[yellow]Dica: {dica}[/yellow]")
    tentativa = input("Depois de vários ataques de elementos únicos, você decide infundir os elementos para ver se há alguma reação na criatura...(escreva: fogo + agua): ").strip().lower()
    if sorted([e.strip() for e in tentativa.split("+")]) == sorted(debuffar):
        limpar()
        console.print("\n[bold green]A infusão deu certo! Utilize para matá-lo[/bold green]")
        return True
    else:
        console.print("[red]Infelizmente a infusão não faz um arranhão na criatura... e você não consegue desviar a tempo...[/red]")
        boss.atacar()
        player.tomar_dano(2)
        return False

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')



# o core do jogo
def gameplay():
    limpar()
    ost("musga.mp3")
    console.print("""[bold red]
  ____                                      __        ___                  _ 
 |  _ \ _   _ _ __   __ _  ___  ___  _ __   \ \      / (_)______ _ _ __ __| |
 | | | | | | | '_ \ / _` |/ _ \/ _ \| '_ \   \ \ /\ / /| |_  / _` | '__/ _` |
 | |_| | |_| | | | | (_| |  __/ (_) | | | |   \ V  V / | |/ / (_| | | | (_| |
 |____/ \__,_|_| |_|\__, |\___|\___/|_| |_|    \_/\_/  |_/___\__,_|_|  \__,_|
                    |___/                                                    
          [/bold red]""")
    nome = input("\n Diga o seu nome... meu jovem mago... ")
    player = Maguinho(nome)
    salas = startar_dungeon()

    while player.life > 0:
        limpar()
        console.print("\nVocê entrou nessa Dungeon pensando que iria ganhar tesouros facilmente... mal sabe você o que irá enfrentar para conseguir sair novamente...", style="#8B4513")
        console.print("\n [blue]Você está na Sala Principal. Selecione a sala que gostaria de enfrentar...[/blue]")
        console.print("\n Salas disponíveis para acesso:", style="#8B4513")

        for i, sala in enumerate(salas[:-1], start=1):
            status = "[orange]Derrotado...[/orange]" if sala.matou_boss else "[green]Pode adentrar[/green]"
            console.print(f"[blue]{i}. {sala.nome} - {status}[/blue]")
        console.print(f"{len(salas)}. {salas[-1].nome} - {'[red]Bloqueada, você ainda é FRACO![/red]' if not all(s.matou_boss for s in salas[:-1]) else '[green]Pode adentrar...[/green]'}")

        escolha = input("\nEscolha alguma sala... ").strip()
        if not escolha.isdigit() or not (1 <= int(escolha) <= len(salas)):
            console.print("[bold red]Escolha inválida![/bold red]")
            continue

        sala_escolhida = salas[int(escolha) - 1]

        if sala_escolhida.nome == "[bold red]Sala do boss Final[/bold red]" and not all(s.matou_boss for s in salas[:-1]):
            console.print("[bold red]Você ainda é fraco para enfrentar o que vem nessa sala, lute com mais chefes para obter xp meu caro[/bold red]")
            continue

        if sala_escolhida.matou_boss:
            console.print("[bold green]Esse boss foi de base.[/bold green]")
            continue

        #isso faz com que resete os status do player
        player.resetar_status()
        sala_escolhida.startar_sala()
        boss = sala_escolhida.boss
        enigma_resolvido = False

        #essa é a parte do loop que faz o player batalhar com o boss
        while boss.esta_vivo() and player.life > 0:
            console.print("\n[blue]Escolha uma ação:[/blue]")
            console.print("[yellow]1. Resolver o enigma[/yellow]")
            console.print("[purple]2. Atacar o boss[/purple]")
            acao = input("Digite o número da ação: ")

            if acao == "1":
                enigma_resolvido = enigma(sala_escolhida.dica_infusao, sala_escolhida.debuffar, player, boss)
            elif acao == "2":
                if enigma_resolvido:
                    combinacao = input("Digite a combinação de elementos para atacar (exemplo: fogo + agua): ").strip().lower()
                    if player.infusao_elementos(combinacao, sala_escolhida.debuffar):
                        boss.levar_dano(4)
                    else:
                        console.print("[red]A combinação não surtiu efeito![/red]")
                    
                    if boss.bloquear == 1:
                        boss.atacar()
                        console.print("\n[blue]Escolha uma ação:[/blue]")
                        console.print("[green]1. Desviar[/green]")
                        console.print("[yellow]2. Bloquear o ataque[/yellow]")
                        resposta = input("Digite sua escolha: ")
                        if resposta == "1":
                            player.dash_limite()
                        else:
                            boss.atacar()
                            player.defender()
                else:
                    console.print("[red]Você não resolveu o enigma! Não sabe qual infusão usar.[/red]")
            else:
                console.print("[red]Ação inválida.[/red]")

        if not boss.esta_vivo():
            limpar()
            console.print(f"[bold green]Você derrotou o {boss.nome} e completou a sala![/bold green]")
            sala_escolhida.matou_boss = True

        if player.life <= 0:
            limpar()
            console.print("[bold red]Game over. Você é fraco, lhe falta ódio.[/bold red]")
            return

    console.print("\n[bold blue]Você conseguiu sair da dungeon com vida! Você sai da Dungeon e vê a luz do sol e se sente livre daquele sofrimento...[/bold blue]")
