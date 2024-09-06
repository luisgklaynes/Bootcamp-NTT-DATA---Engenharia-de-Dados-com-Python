# Sistema de Operações Bancárias

## Descrição

Este projeto simula um sistema simples de operações bancárias, que permite realizar depósitos, saques e consultar extratos. Ele é baseado em interações através do terminal, onde o usuário pode navegar pelas opções de menu para realizar as operações desejadas.

## Funcionalidades

1. **Depósito**: O usuário pode depositar valores positivos na conta. Não é permitido depositar valores iguais ou inferiores a R$ 0,00.
2. **Saque**: O sistema permite saques limitados a R$ 500,00 por transação, com um máximo de três saques por dia. O valor sacado não pode ser superior ao saldo da conta.
3. **Extrato**: O usuário pode visualizar o histórico de operações (depósitos e saques), além do saldo atual da conta.
4. **Sair**: O sistema pode ser encerrado pelo usuário a qualquer momento.

## Regras do Sistema

- O saldo inicial da conta é de **R$ 1.500,00**.
- O limite de saque é de **3 saques por dia**.
- Cada saque tem um valor máximo de **R$ 500,00**.
- Depósitos e saques são registrados com a data e hora da operação no extrato.
- O saldo é atualizado a cada operação de depósito ou saque.

## Como Usar

1. Ao iniciar o sistema, o menu será exibido com as seguintes opções:
   - `[1] Depósito`
   - `[2] Extrato`
   - `[3] Saque`
   - `[4] Sair`

2. Selecione a operação desejada digitando o número correspondente.

### Depósito
- Escolha a opção `[1] Depósito`.
- Informe o valor que deseja depositar. O sistema só aceitará valores positivos.

### Saque
- Escolha a opção `[3] Saque`.
- Informe o valor que deseja sacar. O sistema validará se o valor é inferior ou igual ao saldo disponível e ao limite de **R$ 500,00** por saque.
- Caso tenha realizado 3 saques no dia, o sistema bloqueará novos saques até o próximo dia.

### Extrato
- Escolha a opção `[2] Extrato`.
- O sistema exibirá o histórico de transações e o saldo atual da conta.

### Sair
- Escolha a opção `[4] Sair` para encerrar o sistema.

## Estrutura do Código

- `saldo_conta`: Saldo atual da conta.
- `saque_diario`: Contador de saques realizados no dia.
- `LIMITE_SAQUE`: Número máximo de saques por dia.
- `LIMITE_VALOR_SAQUE`: Valor máximo permitido por saque.
- `menu`: Lista de opções do menu principal.
- `navegacao`: Lista de opções de navegação para confirmação.
- `extrato`: Lista que armazena o histórico de transações, incluindo depósitos e saques, com data e hora.

## Requisitos

- Python 3.x instalado.

## Como Executar

1. Clone o repositório ou copie o código para o seu ambiente local.
2. Execute o script em um terminal ou prompt de comando:
   ```bash
   python sistema_bancario.py
