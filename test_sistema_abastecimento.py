import pytest
from datetime import datetime, timedelta
from sistema_abastecimento import (
    Carro,
    Moto,
    TanqueCheioError,
    TanqueVazioError,
    AbastecimentoRecenteError,
)

class TestSistemaAbastecimento:

    def test_abastecimento_normal(self):
        carro = Carro("Ford", "Fiesta", 2020, 50, 4)
        msg = carro.abastecer(20)
        assert "abastecido" in msg
        assert carro.nivel_combustivel == 20

    def test_abastecimento_excede_tanque(self):
        carro = Carro("Toyota", "Corolla", 2022, 50, 4)
        carro.abastecer(40)
        with pytest.raises(TanqueCheioError):
            carro.abastecer(20)

    def test_abastecimento_muito_recente(self):
        moto = Moto("Honda", "CB 500", 2022, 18, 500)
        moto.abastecer(10)
        moto.data_ultimo_abastecimento = datetime.now() - timedelta(minutes=30)
        with pytest.raises(AbastecimentoRecenteError):
            moto.abastecer(5)

    def test_tentar_ligar_sem_combustivel(self):
        carro = Carro("Ford", "Ka", 2018, 45, 4)
        with pytest.raises(TanqueVazioError):
            carro.ligar()

    def test_mover_consumo_combustivel_carro(self):
        carro = Carro("Chevrolet", "Onix", 2021, 50, 4)
        carro.abastecer(20)
        carro.ligar()
        carro.mover(50)
        assert pytest.approx(carro.nivel_combustivel, 0.1) == 14.0

    def test_mover_consumo_combustivel_moto(self):
        moto = Moto("Yamaha", "MT-07", 2022, 18, 689)
        moto.abastecer(10)
        moto.ligar()
        moto.mover(100)
        assert pytest.approx(moto.nivel_combustivel, 0.1) == 5.0
