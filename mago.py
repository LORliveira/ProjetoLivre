from rich.console import Console
console = Console()


class Maguinho:
    def __init__(self, nome):
        self.nome = nome
        self.life = 8
        self.dash = 2

    def infusao_elementos(self, combinacao, debuffar):
        elementos = [elem.strip() for elem in combinacao.split("+")]
        if sorted(elementos) == sorted(debuffar):
            return True
        else:
            return False   
    def dash_limite(self):
        if self.dash > 0:
            self.dash -= 1
            console.print(f"[green]Você desviou do ataque! Dash restantes: {self.dash}[/green]")
        else:
            console.print("[red]Você não tem mais dash disponíveis![/red]")
            self.tomar_dano(2) 
    def resetar_status(self):
        self.life = 8
        self.dash = 2
    def tomar_dano(self, dano):
        self.life -= dano
        console.print(f"[red]Você recebeu {dano} de dano, necessita recuar amigão, vida restante: {self.life}[/red]")
        if self.life <= 0:
            console.print("[red]Você é fraco! Lhe falta ódio. Game Over...[/red]")
    def defender(self):
        console.print("[yellow]Você conseguiu defender o ataque! Mas o ataque do chefe foi paia e te deu dano...[/yellow]")
        self.tomar_dano(2)




