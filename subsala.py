from mainsala import Sala_principal
from rich.console import Console

console = Console()
class Subsala(Sala_principal):
    def __init__(self, nome, boss, descricao, debuffar, dica_infusao):
        super().__init__(nome)
        self.boss = boss
        self.descricao = descricao
        self.debuffar = debuffar
        self.dica_infusao = dica_infusao
        self.matou_boss = False
    def startar_sala(self):
        console.print(f"\n[green]Você conseguiu entrar na {self.nome}.[/green]")
        console.print(f"[red]O boss é {self.boss.nome}, cuidado![/red]")
        console.print(f"\n[orange]Descrição: {self.descricao}[/orange]")