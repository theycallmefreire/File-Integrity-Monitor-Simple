import time 
from hashing import calculando_file_hash

arquivo_original = 'senha.txt'
hash_original = calculando_file_hash(arquivo_original)
print(f"--- Baseline inicial coletada de '{arquivo_original}' ---")
print(f"--- Hash original: {hash_original} ---")


while True:
    print("\n#########################################")
    print("o que vc quer fazer?")
    print("1 - coletar uma nova baseline? (Opção ainda em desenvolvimento)")
    print("2 - monitorar 'senha.txt' AO VIVO?")
    print("3 - Sair") 
    resposta = input("Digite a opção desejada: ")

    caminho_arquivo = arquivo_original 

    if resposta == "1":
        print("Coletando nova baseline...")
        new_base = input("Digite o nome da nova baseline: ")
        conteudo_new_base = input("Digite o conteúdo da nova baseline: ")

        with open(new_base + '.txt', 'w') as f:
            f.write(f"{conteudo_new_base}\n")
        print(f"Baseline '{new_base}.txt' criada com sucesso.")
        print("Ainda monitorando 'senha.txt' como base.")
        
    
    elif resposta == "2":
        print(f"Iniciando monitoramento de '{arquivo_original}'...")
        print("Pressione CTRL+C para parar o monitoramento e voltar ao menu.")
        
        try:
            while True: 
                hash_atual = calculando_file_hash(arquivo_original)
                if hash_atual != hash_original:
                    print(f"\nALERTA! O arquivo '{arquivo_original}' FOI ALTERADO!")
                    print(f"Hash original: {hash_original}")
                    print(f"Hash novo:     {hash_atual}")
                    
                else:
                    print(f"Status: '{arquivo_original}' intacto... (CTRL+C para sair)", end="\r")
                time.sleep(1) 
        
        except KeyboardInterrupt:
            # 6. Permite que o usuário pressione CTRL+C para
            # sair do loop de monitoramento e voltar ao menu
            print("\n...Monitoramento parado. Voltando ao menu principal.")

    elif resposta == "3":
        print("Saindo...")
        break 

    else:
        print("Opção inválida, tente novamente.")