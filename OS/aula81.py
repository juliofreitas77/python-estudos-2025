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