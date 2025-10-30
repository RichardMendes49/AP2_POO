from datetime import datetime, timedelta

class AbastecimentoError(Exception):
    pass

class TanqueCheioError(AbastecimentoError):
    pass

class TanqueVazioError(AbastecimentoError):
    pass

class AbastecimentoRecenteError(AbastecimentoError):
    pass


class Veiculo:
    def __init__(self, marca, modelo, ano, capacidade_tanque):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.capacidade_tanque = capacidade_tanque
        self.nivel_combustivel = 0
        self.data_ultimo_abastecimento = None
        self.ligado = False

    def ligar(self):
        if self.nivel_combustivel <= 0:
            raise TanqueVazioError(f"{self.modelo} não pode ligar: tanque vazio.")
        self.ligado = True
        return f"{self.modelo} foi ligado."

    def desligar(self):
        self.ligado = False
        return f"{self.modelo} foi desligado."

    def mover(self, km):
        if not self.ligado:
            return f"{self.modelo} não pode se mover, pois está desligado."
        if self.nivel_combustivel <= 0:
            raise TanqueVazioError(f"{self.modelo} não pode se mover: tanque vazio.")
        consumo = km * 0.1
        self.nivel_combustivel = max(self.nivel_combustivel - consumo, 0)
        return f"{self.modelo} percorreu {km} km. Combustível restante: {self.nivel_combustivel:.1f} L."

    def abastecer(self, litros):
        agora = datetime.now()

        if self.data_ultimo_abastecimento:
            intervalo = agora - self.data_ultimo_abastecimento
            if intervalo < timedelta(hours=1):
                raise AbastecimentoRecenteError(
                    f"{self.modelo} abasteceu há pouco tempo ({intervalo.seconds // 60} min atrás)."
                )

        if self.nivel_combustivel + litros > self.capacidade_tanque:
            raise TanqueCheioError(f"Tanque de {self.modelo} já está cheio ou ultrapassaria a capacidade.")

        self.nivel_combustivel += litros
        self.data_ultimo_abastecimento = agora
        return f"{self.modelo} abastecido com {litros:.1f} L. Nível atual: {self.nivel_combustivel:.1f} L."

    def __str__(self):
        status = "Ligado" if self.ligado else "Desligado"
        return f"{self.marca} {self.modelo} ({self.ano}) - {status} - Tanque: {self.nivel_combustivel:.1f}/{self.capacidade_tanque} L"


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, capacidade_tanque, portas):
        super().__init__(marca, modelo, ano, capacidade_tanque)
        self.portas = portas

    def mover(self, km):
        if not self.ligado:
            return f"O carro {self.modelo} está desligado e não pode rodar."
        if self.nivel_combustivel <= 0:
            raise TanqueVazioError(f"O carro {self.modelo} está sem combustível!")
        consumo = km * 0.12
        self.nivel_combustivel = max(self.nivel_combustivel - consumo, 0)
        return f"O carro {self.modelo} percorreu {km} km. Combustível: {self.nivel_combustivel:.1f} L."

    def __str__(self):
        return f"{super().__str__()} - {self.portas} portas"


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, capacidade_tanque, cilindradas):
        super().__init__(marca, modelo, ano, capacidade_tanque)
        self.cilindradas = cilindradas

    def mover(self, km):
        if not self.ligado:
            return f"A moto {self.modelo} está desligada."
        if self.nivel_combustivel <= 0:
            raise TanqueVazioError(f"A moto {self.modelo} está sem combustível!")
        consumo = km * 0.05
        self.nivel_combustivel = max(self.nivel_combustivel - consumo, 0)
        return f"A moto {self.modelo} rodou {km} km. Combustível: {self.nivel_combustivel:.1f} L."

    def __str__(self):
        return f"{super().__str__()} - {self.cilindradas}cc"


if __name__ == "__main__":
    carro = Carro("Toyota", "Corolla", 2020, 50, 4)
    moto = Moto("Honda", "CB 500", 2022, 18, 500)
    print(carro.abastecer(20))
    print(moto.abastecer(10))
    print(carro.ligar())
    print(carro.mover(50))
    print(carro.desligar())
