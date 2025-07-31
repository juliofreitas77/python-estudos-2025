"""
Vamos analisar o código Python que você forneceu, explicando cada parte e seu funcionamento detalhadamente.

### Importação de Módulos
```python
import shutil
import os
```
- **`import shutil`**: O módulo `shutil` fornece uma interface para operações de alto nível em arquivos e coleções de arquivos, como copiar e remover diretórios.
- **`import os`**: O módulo `os` permite interagir com o sistema operacional, incluindo a manipulação de arquivos e diretórios.

### Verificação da Existência de Arquivos e Diretórios
```python
print(os.path.exists('frutas.txt'))
print(os.path.exists('teste_dir'))
```
- **`os.path.exists('frutas.txt')`**: Verifica se o arquivo `frutas.txt` existe no diretório atual. O resultado (True ou False) será impresso no console.
- **`os.path.exists('teste_dir')`**: Verifica se o diretório `teste_dir` existe. O resultado também será impresso.

### Renomeando um Diretório (Comentado)
```python
# os.rename('teste_dir', 'novo_diretorio')
# print(os.path.exists('novo_diretorio'))
```
- Essas linhas estão comentadas, mas se fossem executadas, `os.rename('teste_dir', 'novo_diretorio')` renomearia o diretório `teste_dir` para `novo_diretorio`. A linha seguinte verificaria se o novo diretório existe após a renomeação.

### Condicional para Criar ou Remover o Diretório
```python
if os.path.exists('novo_diretorio'):
    shutil.rmtree('novo_diretorio')
    print('Diretório já existe, removendo...')
else:
    os.mkdir('novo_diretorio')
    print('Diretório criado com sucesso!')
```
- **Verificação da Existência do Diretório**: O código verifica se o diretório `novo_diretorio` já existe.
  - **Se existir (`True`)**:
    - **`shutil.rmtree('novo_diretorio')`**: Remove o diretório `novo_diretorio` e todo o seu conteúdo, incluindo arquivos e subdiretórios.
    - **`print('Diretório já existe, removendo...')`**: Informa que o diretório foi removido.
  - **Se não existir (`False`)**:
    - **`os.mkdir('novo_diretorio')`**: Cria um novo diretório chamado `novo_diretorio`.
    - **`print('Diretório criado com sucesso!')`**: Informa que o diretório foi criado.

### Resumo do Funcionamento
1. O código começa verificando a existência de um arquivo (`frutas.txt`) e um diretório (`teste_dir`).
2. Se o diretório `novo_diretorio` já existir, ele será removido junto com todo o seu conteúdo.
3. Se o diretório não existir, ele será criado.

### Considerações
- **Cuidado ao usar `shutil.rmtree()`**: Essa operação é irreversível, então tenha certeza de que você realmente deseja remover o diretório e seu conteúdo.
- **Verificações de Erros**: Para um código mais robusto, você pode querer adicionar tratamento de exceções para lidar com possíveis erros, como permissões insuficientes ou diretórios que não podem ser removidos.

Esse código é útil para gerenciar a criação e remoção de diretórios em um projeto, permitindo que você mantenha sua estrutura de arquivos organizada.
"""
import shutil
import os

print(os.path.exists('frutas.txt'))
print(os.path.exists('teste_dir'))
#os.rename('teste_dir', 'novo_diretorio')
#print(os.path.exists('novo_diretorio'))
if os.path.exists('novo_diretorio'):
    shutil.rmtree('novo_diretorio')
    print('Diretório já existe, removendo...')
else:
    os.mkdir('novo_diretorio')
    print('Diretório criado com sucesso!')