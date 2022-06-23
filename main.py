from time import sleep
from methods import ApiDrive
import os
from dotenv import load_dotenv

load_dotenv()

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
    folder_id = os.getenv('folder_id')
    drive = ApiDrive.authentication()
    
    if option == 'a':
        print("--------------------------")
        print("\n")
        ApiDrive.list_files(drive, folder_id)
        print("--------------------------")
    elif option == 'b':
        ApiDrive.upload(drive, folder_id)
    
    elif option == 'c':
        ApiDrive.download(drive, folder_id)
    elif option == 'd':
        ApiDrive.create_file(drive, folder_id) 
    else:
        print("\nOpção inválida.\n")
    
    menu()
    option = input("\nDigite sua opção: ")

ending("Saindo...")





