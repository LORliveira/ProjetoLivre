from rich.console import Console

console = Console()

class Sala_principal:

    def __init__(self, nome):
        self.nome = nome
        self.salas = []

    def list_salas(self):

        console.print("\n[blue]Você está na Sala Principal da Dungeon.[/blue]")

        print("[green]Salas disponíveis:[/green]")

        for i, sala in enumerate(self.salas, start=1):
            status = "matou_boss" if sala.matou_boss else "disponível"
            print(f"{i}. {sala.nome} - {status if not isinstance(sala, Sala_principal) or sala.desbloqueado() else 'bloqueado'}")

    def choose_salas(self):
        
        self.list_salas()
        escolha = input("\nEscolha uma sala para entrar (1 a {0}): ".format(len(self.salas))).strip()
        if not escolha.isdigit() or not (1 <= int(escolha) <= len(self.salas)):
            console.print("[red]Escolha inválida![/red]")
            return None
        return self.salas[int(escolha) - 1]
