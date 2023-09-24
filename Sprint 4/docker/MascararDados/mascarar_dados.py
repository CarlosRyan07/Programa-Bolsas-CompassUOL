import hashlib

isStop = False
while isStop == False:
    # 1 - Recebe uma string via input
    input_string = input("Digite uma string para mascaramento (ou 'exit' para sair): ")
    
    if input_string.lower() == 'exit':
        isStop = True
    
    # 2 - Gera o hash SHA-1 da string
    sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()
    
    # 3 - Imprime o hash em tela
    print(f"Hash SHA-1 da string: {sha1_hash}")
