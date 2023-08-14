## Gerenciador de Conta Bancária

Este é um pequeno programa que simula um gerenciador de conta bancária simples. Ele permite que você realize operações básicas em sua conta, como depósitos, saques e visualização de extrato.

### Funcionalidades

O programa oferece as seguintes opções:

1. **Depositar**
   - Permite que você deposite dinheiro em sua conta.
   - Você precisará informar o valor que deseja depositar.
   - O saldo da conta será atualizado de acordo com o valor depositado.
   - O valor do depósito será registrado no extrato da conta.

2. **Sacar**
   - Permite que você faça saques da sua conta.
   - Você precisará informar o valor que deseja sacar.
   - O programa verifica se o valor do saque é menor ou igual ao saldo disponível e ao limite diário de saque.
   - Se a operação for válida, o saldo será reduzido e o valor do saque será registrado no extrato.

3. **Extrato**
   - Exibe o extrato da conta, mostrando todas as transações realizadas.
   - Se nenhuma transação tiver sido feita, exibirá uma mensagem informando que não houve movimentações.
   - O saldo atual da conta também é mostrado.

4. **Sair**
   - Encerra o programa.

### Uso

1. Execute o programa em um ambiente Python.
2. Escolha a opção desejada digitando o número correspondente ou a tecla "S" para sair.
3. Siga as instruções para realizar as operações desejadas.

### Observações

- O limite diário de saque é de R$ 500,00.
- O saldo inicial da conta é de R$ 0,00.
- Todas as operações (depósitos, saques) são registradas no extrato.
