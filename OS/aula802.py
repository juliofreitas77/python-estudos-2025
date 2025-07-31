"""
Vamos analisar o código Python fornecido passo a passo, explicando cada parte para entender sua funcionalidade.

### Passo 1: Importando o Módulo `os`
```python
import os
```
- Esta linha importa o módulo `os`, que fornece uma maneira de usar funcionalidades dependentes do sistema operacional, como ler ou escrever no sistema de arquivos, criar diretórios e mais.

### Passo 2: Definindo o Caminho do Diretório
```python
diretorio = os.path.join(os.getcwd(), 'teste_dir')
```
- Aqui, `os.getcwd()` recupera o diretório de trabalho atual (a pasta de onde o script está sendo executado).
- `os.path.join()` é usado para criar um caminho que seja compatível com o sistema operacional. Ele combina o diretório de trabalho atual com a string `'teste_dir'`, resultando em um caminho completo para um novo diretório chamado `teste_dir` dentro do diretório atual.

### Passo 3: Verificando se o Diretório Existe
```python
if not os.path.exists(diretorio):
```
- Esta linha verifica se o diretório especificado pela variável `diretorio` já existe. 
- `os.path.exists()` retorna `True` se o caminho existir e `False` caso contrário. O operador `not` nega isso, então a condição será `True` se o diretório não existir.

### Passo 4: Criando o Diretório
```python
    os.makedirs(diretorio)
    print(f'Diretório criado: {diretorio}')
```
- Se o diretório não existir, `os.makedirs(diretorio)` cria o diretório no caminho especificado. 
- A função `print()` exibe uma mensagem indicando que o diretório foi criado, incluindo o caminho do novo diretório.

### Passo 5: Tratando o Caso em Que o Diretório Já Existe
```python
else:
    print(f'O diretório já existe: {diretorio}')
```
- Se o diretório já existir, o bloco `else` é executado. 
- Ele imprime uma mensagem indicando que o diretório já existe, novamente incluindo o caminho.

### Resumo
Este trecho de código verifica efetivamente a existência de um diretório chamado `teste_dir` no diretório de trabalho atual. Se ele não existir, o código cria o diretório e informa o usuário. Se já existir, ele simplesmente informa que o diretório está presente.

### Cenário de Exemplo
- Se você executar este script em uma pasta onde `teste_dir` não existe, você verá:
  ```
  Diretório criado: /caminho/para/o/diretorio/atual/teste_dir
  ```
- Se você executá-lo novamente na mesma pasta, verá:
  ```
  O diretório já existe: /caminho/para/o/diretorio/atual/teste_dir
  ```

Esse código é útil para organizar arquivos e garantir que uma estrutura de diretórios específica esteja em vigor antes de realizar operações de arquivo.
"""

import os
# Cria um diretório chamado 'teste_dir' no diretório atual
diretorio = os.path.join(os.getcwd(), 'teste_dir')

if not os.path.exists(diretorio):
    os.makedirs(diretorio)
    print(f'Diretório criado: {diretorio}')
else:
    print(f'O diretório já existe: {diretorio}')