"""
Vamos analisar o código Python que você forneceu, explicando cada parte e seu funcionamento detalhadamente.

### Importação do Módulo `datetime`
```python
from datetime import datetime
```
- Aqui, você está importando a classe `datetime` do módulo `datetime`, que fornece funcionalidades para manipulação de datas e horas.

### Entrada do Usuário
```python
nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
```
- Esta linha solicita ao usuário que insira sua data de nascimento no formato `DD/MM/AAAA`. O valor digitado é armazenado na variável `nascimento` como uma string.

### Tentativa de Conversão da Data
```python
try:
    data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
```
- O bloco `try` é usado para tentar executar um código que pode gerar uma exceção.
- **`datetime.strptime(nascimento, "%d/%m/%Y")`**: Esta função tenta converter a string `nascimento` em um objeto `datetime`. O formato especificado (`"%d/%m/%Y"`) indica que a string deve estar no formato dia/mês/ano. Se a string não estiver nesse formato ou contiver valores inválidos (como 32 para o dia ou 13 para o mês), uma exceção `ValueError` será levantada.

### Cálculo da Idade
```python
    idade = datetime.now().year - data_nascimento.year
```
- Aqui, a idade é calculada subtraindo o ano de nascimento (`data_nascimento.year`) do ano atual (`datetime.now().year`).

### Ajuste da Idade
```python
    if (datetime.now().month, datetime.now().day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
```
- Este bloco verifica se o aniversário do usuário já ocorreu no ano atual. 
- **`(datetime.now().month, datetime.now().day) < (data_nascimento.month, data_nascimento.day)`**: Se a data atual (mês e dia) for anterior à data de nascimento (mês e dia), significa que o usuário ainda não fez aniversário neste ano, então a idade é decrementada em 1.

### Impressão da Idade
```python
    print(f"Sua idade é: {idade} anos.")
```
- Se a conversão da data e o cálculo da idade forem bem-sucedidos, a idade do usuário é impressa no console.

### Tratamento de Erros
```python
except ValueError:
    print("Data inválida. Por favor, use o formato DD/MM/AAAA.")
```
- Se ocorrer uma exceção `ValueError` durante a conversão da data, o código dentro do bloco `except` será executado. Ele informa ao usuário que a data inserida é inválida e solicita que ele use o formato correto.

### Resumo do Funcionamento
1. O usuário é solicitado a inserir sua data de nascimento.
2. O código tenta converter a entrada em um objeto `datetime`.
3. Se a conversão for bem-sucedida, a idade é calculada e ajustada conforme necessário.
4. A idade é impressa. Se a entrada for inválida, uma mensagem de erro é exibida.

### Considerações
- **Validação de Entrada**: O uso do bloco `try-except` é uma boa prática para lidar com entradas inválidas e evitar que o programa falhe.
- **Formato da Data**: É importante que o usuário siga o formato especificado para que a conversão funcione corretamente.

Esse código é um exemplo prático de como manipular datas e calcular idades em Python, utilizando o módulo `datetime`.
"""
from datetime import datetime
nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
try:
    data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
    idade = datetime.now().year - data_nascimento.year
    if (datetime.now().month, datetime.now().day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    print(f"Sua idade é: {idade} anos.")
except ValueError:
    print("Data inválida. Por favor, use o formato DD/MM/AAAA.")
