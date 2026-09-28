# SISTEMA DE RESERVA DE HOTEL

## 1. DESCRIÇÃO DO PROJETO E OBJETIVO
O projeto consiste no desenvolvimento de um sistema de reserva de hotel utilizando Python e os conceitos de Programação Orientada a Objetos (POO).O sistema terá como objetivo permitir o gerenciamento de quartos, hóspedes, reservas, pagamentos, adicionais, cancelamentos e operações de check-in e check-out.Também serão implementados cálculos de tarifas, regras de disponibilidade, controle de capacidade, períodos de temporada, tarifas diferenciadas para finais de semana e relatórios administrativos.

## 2. ESTRUTURA PLANEJADA DAS CLASSES

### Pessoa: (Classe base para representar pessoas no sistema.)

#### Atributos principais:

- nome
- documento
- email
- telefone
- Hospede

##### Herda da classe Pessoa e representa os hóspedes do hotel.

#### Atributos adicionais:
- Reservas

#### Métodos principais:

- adicionar_reserva()
- historico_reservas()
- Quarto

### Representa um quarto do hotel.

#### Atributos principais:

- numero
- tipo
- capacidade
- tarifa_base
- status

#### Métodos principais:

- bloquear()
- desbloquear()
- verificar_disponibilidade()

### Subclasse de Quarto para representar quartos do tipo simples.
- QuartoSimples

### Subclasse de Quarto para representar quartos do tipo duplo.
- QuartoDuplo

### Subclasse de Quarto para representar quartos do tipo luxo.
- QuartoLuxo

### Reserva (Representa uma reserva realizada por um hóspede.)

#### Atributos principais:

- hospede
- quarto
- data_entrada
- data_saida
- quantidade_hospedes
- origem
- status
- pagamentos
- adicionais

#### Métodos principais:

- calcular_diarias()
- calcular_total()
- confirmar()
- checkin()
- checkout()
- cancelar()
- marcar_no_show()

### Pagamento: (Representa um pagamento realizado pelo hóspede.)

#### Atributos:
- data
- forma
- valor

### Adicional: (Representa serviços ou consumos adicionais vinculados a uma reserva.)

#### Atributos:

- descricao
- valor

### Heranças

- A classe Hospede herda de Pessoa.
- As classes QuartoSimples, QuartoDuplo e QuartoLuxo herdam de Quarto.
- Uma Reserva está relacionada a um Hospede e a um Quarto.
- Uma Reserva pode possuir vários Pagamentos e vários Adicionais.

#### Status da reserva

- PENDENTE
- CONFIRMADA
- CHECKIN
- CHECKOUT
- CANCELADA
- NO_SHOW

As principais transições previstas são:

PENDENTE → CONFIRMADA → CHECKIN → CHECKOUT

PENDENTE → CANCELADA

CONFIRMADA → CANCELADA

CONFIRMADA → NO_SHOW
