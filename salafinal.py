from subsala import Subsala

class SalaBossFinal(Subsala):
    def __init__(self, nome, boss, enigma, debuffar, dica_infusao):
        super().__init__(nome, boss, enigma, debuffar, dica_infusao)

    def desbloqueado(self):
        return all(sala.matou_boss for sala in self.salas)