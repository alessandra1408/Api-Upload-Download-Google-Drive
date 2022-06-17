from time import sleep
from methods import ApiDrive


def menu():
    print("\n[a] Listar Arquivos no Google Drive")
    print("[b] Upload de Arquivo para o Google Drive")
    print("[c] Download de Arquivo da pasta do Google Drive")
    print("[d] Criar arquivo de texto no Google Drive")
    print("[s] Para Sair ")
    

def ending(text):
    sleep(1)
    print(f"\n {text}")
    sleep(1)
    print("\n")
    

menu()
option = input("\nDigite sua opção: ")


while option != 's':
    
    drive = ApiDrive.authentication()
    folder_id = '1O421lpvoVYrzlm8xCa_HT0-x_zVMXy7z'

    if option == 'b':
        ApiDrive.upload(drive, folder_id)
    elif option == 'a':
        print("--------------------------")
        print("\n")
        ApiDrive.list_files(drive, folder_id)
        print("--------------------------")
    elif option == 'c':
        ApiDrive.download(drive, folder_id)
    elif option == 'd':
        ApiDrive.create_file(drive, folder_id) 
    else:
        print("\nOpção inválida.\n")
    
    menu()
    option = input("\nDigite sua opção: ")

ending("Saindo...")





