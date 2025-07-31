"""
Vamos analisar o código Python que você forneceu, explicando cada parte em detalhes.

### Código Explicado

```python
with open("frutas.txt", "w") as arquivo:
    while True:
        fruta = input("Digite uma fruta: ")
        if fruta == 'sair':
            break
        else:
            arquivo.write(fruta)
            arquivo.write('\n')
```

#### 1. **Abrindo um Arquivo**

```python
with open("frutas.txt", "w") as arquivo:
```

- **`with open(...)`**: Este comando abre um arquivo chamado `frutas.txt` para escrita (`"w"`). O uso do `with` é uma prática recomendada em Python, pois garante que o arquivo será fechado automaticamente após o bloco de código ser executado, mesmo que ocorra um erro.
- **`"w"`**: O modo de abertura `"w"` significa que o arquivo será criado se não existir, ou será truncado (apagado) se já existir. Isso significa que qualquer conteúdo anterior no arquivo será perdido.
- **`as arquivo`**: A variável `arquivo` é um objeto que representa o arquivo aberto e será usado para realizar operações de leitura e escrita.

#### 2. **Loop Infinito**

```python
while True:
```

- **`while True:`**: Este é um loop infinito que continuará a executar até que uma condição de parada seja encontrada (neste caso, quando o usuário digitar 'sair').

#### 3. **Entrada do Usuário**

```python
fruta = input("Digite uma fruta: ")
```

- **`input(...)`**: Esta função exibe uma mensagem ao usuário ("Digite uma fruta: ") e aguarda que o usuário insira um valor. O valor inserido é armazenado na variável `fruta`.

#### 4. **Verificação da Condição de Saída**

```python
if fruta == 'sair':
    break
```

- **`if fruta == 'sair':`**: Esta linha verifica se o valor inserido pelo usuário é igual a `'sair'`.
- **`break`**: Se a condição for verdadeira (ou seja, o usuário digitou 'sair'), o comando `break` é executado, o que interrompe o loop `while`, saindo do bloco de repetição.

#### 5. **Escrevendo no Arquivo**

```python
else:
    arquivo.write(fruta)
    arquivo.write('\n')
```

- **`else:`**: Se o usuário não digitou 'sair', o código dentro do bloco `else` será executado.
- **`arquivo.write(fruta)`**: Esta linha escreve o valor da variável `fruta` no arquivo `frutas.txt`.
- **`arquivo.write('\n')`**: Esta linha escreve uma nova linha no arquivo, garantindo que cada fruta digitada pelo usuário fique em uma linha separada.

### Resumo do Funcionamento

1. O programa abre (ou cria) um arquivo chamado `frutas.txt` para escrita.
2. Ele entra em um loop onde solicita ao usuário que digite o nome de uma fruta.
3. Se o usuário digitar 'sair', o loop é interrompido e o arquivo é fechado.
4. Se o usuário digitar o nome de uma fruta, essa fruta é escrita no arquivo, seguida de uma nova linha.
5. O processo se repete até que o usuário decida sair.

### Conclusão

Esse código é um exemplo simples de como interagir com o usuário para coletar dados e armazená-los em um arquivo de texto. É uma maneira eficaz de registrar informações de forma persistente. Se você tiver mais perguntas ou precisar de mais detalhes sobre algum aspecto específico do código, sinta-se à vontade para perguntar!
"""


with open("frutas.txt", "w") as arquivo:
    while True:
        fruta = input("Digite uma fruta: ")
        if fruta == 'sair':
            break
        else:
            arquivo.write(fruta)
            arquivo.write('\n')