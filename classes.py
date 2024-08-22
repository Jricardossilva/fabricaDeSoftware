class Carro:
    def __init__(self, modelo, marca, cor) -> None:
        self.modelo = modelo
        self.marca = marca
        self.cor = cor

    def acelerar(self):
        print(f"{self.modelo} acelerou 10Km")
    
    def freiar(self):
        print(f"{self.modelo} freiou")
    
class Caminhao(Carro):
    def buzinou(self):
        print (f"{self.modelo} buzinou!")

onix = Carro(marca='GM', modelo='Onix', cor='Branco')
chain = Caminhao(marca='Volkswagem', modelo='T-Cross', cor='Preto')

onix.acelerar()
chain.buzinou()