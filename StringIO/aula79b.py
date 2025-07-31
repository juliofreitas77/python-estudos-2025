"""
Análise Detalhada do CódigoEste código tem como objetivo coletar nomes de frutas digitados pelo usuário e salvá-los em um arquivo chamado frutas.txt. A parte interessante é que ele não escreve diretamente no arquivo físico. Em vez disso, ele usa um "arquivo virtual" em memória para armazenar os dados temporariamente.1. Preparando o "Arquivo Virtual"from io import StringIO

frutas = ""
arquivo = StringIO(frutas)
from io import StringIO: Importa a classe StringIO do módulo io. A classe StringIO permite que você trate uma string como se fosse um arquivo de texto. Isso é útil para ler e escrever dados na memória sem a necessidade de interagir com o sistema de arquivos real.frutas = "": Inicializa uma string vazia. Embora esta string não seja usada diretamente para armazenar as frutas, ela é passada para StringIO para criar o objeto arquivo.arquivo = StringIO(frutas): Cria um objeto StringIO chamado arquivo. Pense nele como um arquivo em branco que existe apenas na memória do seu computador. Você pode ler, escrever e fazer buscas nele, assim como faria com um arquivo de verdade.2. Coletando a Entrada do Usuáriowhile True:
    fruta = input("Dgite um fruta: ")
    if fruta == "sair":
        break
    else:
        arquivo.write(fruta)
        arquivo.write('\n')
while True:: Inicia um loop infinito. Isso significa que o programa continuará pedindo uma fruta até que uma condição específica seja atendida para encerrar o loop.fruta = input("Dgite um fruta: "): Pede ao usuário para digitar uma fruta e armazena a entrada na variável fruta.if fruta == "sair": break: Esta é a condição de saída do loop. Se o usuário digitar "sair", a instrução break interrompe o loop, e a execução do programa continua após ele.else: arquivo.write(fruta) / arquivo.write('\n'): Se o usuário digitou uma fruta válida (ou qualquer outra coisa que não seja "sair"), o código escreve o nome da fruta no nosso "arquivo virtual" (arquivo) e depois adiciona um caractere de nova linha (\n) para que cada fruta seja salva em uma linha separada.3. Escrevendo os Dados no Arquivo Físicoarquivo.seek(0)

with open('frutas.txt', 'w') as arq_fisico:
    for fruta in arquivo.readlines():
        arq_fisico.write(fruta)
arquivo.seek(0): Esta é uma linha crucial! O objeto StringIO (assim como arquivos físicos) tem um "cursor" que se move à medida que você escreve nele. Após o loop, o cursor está no final do texto. O método seek(0) move o cursor de volta para a posição zero, ou seja, o início do arquivo. Isso é necessário para que você possa começar a ler o conteúdo a partir do começo.with open('frutas.txt', 'w') as arq_fisico:: Abre um arquivo físico chamado frutas.txt no modo de escrita ('w'). O comando with garante que o arquivo será fechado automaticamente, mesmo se ocorrer um erro.for fruta in arquivo.readlines():: Lê todas as linhas do nosso "arquivo virtual" arquivo e itera sobre cada uma delas.arq_fisico.write(fruta): Dentro do loop, cada linha (cada fruta) é lida do StringIO e escrita no arquivo físico frutas.txt.Em ResumoO código cria uma área de armazenamento temporário na memória, coleta as entradas do usuário nessa área e, somente após o usuário terminar, copia todo o conteúdo de uma vez para um arquivo de texto no seu computador.
"""

from io import StringIO

frutas = ""
arquivo = StringIO(frutas)

while True:
    fruta = input("Dgite um fruta: ")
    if fruta == "sair":
        break
    else:
        arquivo.write(fruta)
        arquivo.write('\n')

arquivo.seek(0)

with open('frutas.txt', 'w') as arq_fisico:
    for fruta in arquivo.readlines():
        arq_fisico.write(fruta)
