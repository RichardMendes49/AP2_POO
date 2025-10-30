# Sistema de Abastecimento em Python

Este projeto implementa um **sistema de controle de abastecimento de veículos** (carros e motos) utilizando **Python** e os princípios de **Programação Orientada a Objetos (POO)**.  

O sistema permite simular o abastecimento, consumo de combustível, verificação de tanque cheio, tentativa de ligar com tanque vazio e controle de tempo mínimo entre abastecimentos.

E

##  Estrutura do Projeto

- `sistema_abastecimento.py` → Código principal do sistema (classes e exceções)
- `test_sistema_abastecimento.py` → Testes automatizados com **pytest**
- `requirements.txt` → Lista de dependências do projeto

---

##  Pré-requisitos

- **Python 3.10** ou superior instalado  
- Criar um ambiente virtual (venv) para o projeto:

```bash
python -m venv Gasolina
```

Ativar o ambiente virtual:

- **Windows:**
```bash
venv\Scripts\activate
```


```bash
pip install -r requirements.txt
```
---

##  Executando o Sistema

Para rodar o exemplo interativo e visualizar o comportamento do sistema:

```bash
python sistema_abastecimento.py
```

Você poderá ver a simulação de:
- Abastecimento de carros e motos  
- Consumo de combustível ao percorrer distâncias  
- Tentativas de abastecimento acima da capacidade  
- Bloqueio de reabastecimento recente  

---

##  Testes 

O projeto possui testes unitários com **pytest** para validar:

- Abastecimento normal  
- Exceção de tanque cheio  
- Exceção de abastecimento muito recente  
- Tentativa de ligar com tanque vazio  
- Consumo de combustível em carros e motos  

### Rodando os testes

saída esperada:

```
carro.abastecido com 20.0 L. Nível atual: 20.0 L.
A moto MT-07 rodou 100 km. Combustível: 5.0 L.
```

---

##  Observações

- Motos consomem **0,05 L/km**  
- Carros consomem **0,12 L/km**  
- Tempo mínimo entre abastecimentos: **1 hora**
- Exceções personalizadas ajudam a tratar erros específicos:
  - `TanqueCheioError`
  - `TanqueVazioError`
  - `AbastecimentoRecenteError`

---

