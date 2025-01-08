from subsala import Subsala

class SalaBossFinal(Subsala):
    def __init__(self, nome, boss, enigma, debuffar, dica_infusao):
        super().__init__(nome, boss, enigma, debuffar, dica_infusao)
        self.salas = []
    def desbloqueado(self):
        return all(s.matou_boss for s in self.salas if s is not self)
