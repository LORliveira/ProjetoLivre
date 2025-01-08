from rich.console import Console

console = Console()

class boss:
    def __init__(self, nome, life):
        self.nome = nome
        self.life = life
        self.bloquear = 0


    def levar_dano(self, dano):
        self.bloquear += 1
        if self.bloquear == 3:
            self.life -= dano
            self.bloquear = 0
            console.print(f"[blue]O {self.nome} recebeu {dano} de dano! life restante: {self.life}[/blue]")
        else:
            console.print(f"[red]O {self.nome} bloqueou o ataque![red]")


    def atacar(self):
        console.print(f"[bold red]O {self.nome} ataca![/bold red]")


    def esta_vivo(self):
        return self.life > 0