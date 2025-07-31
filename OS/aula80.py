import os
print(os.getcwd())
print(os.listdir('.'))
print(os.listdir('..'))
print(os.listdir('/'))  # List files in the root directory
os.chdir('..')  # Change to parent directory
print(os.getcwd())  # Print current working directory after changing
print(os.name)