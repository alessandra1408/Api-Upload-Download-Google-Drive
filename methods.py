from ast import Try
from pandas import get_option
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


class ApiDrive:    

    # def __init__(self, credentials, folder_id):
    #     self.credentials = credentials
    #     self.folder_id = folder_id


    def authentication():
        
        try:

            gauth = GoogleAuth()

            # reads file with credentials. If the credentials are null, it will ask to authorize and save them. If it has expired, it will refresh. Then, it will save the credentials in onde file.
            gauth.LoadCredentialsFile('my_credentials.json')
            if gauth.credentials is None:
                gauth.LocalWebserverAuth()
            elif gauth.access_token_expired:
                gauth.Refresh()
            else:
                gauth.Authorize()
            gauth.SaveCredentialsFile('my_credentials.json')

            drive = GoogleDrive(gauth)

            return drive
 
        
        except:
            print("\nErro a autenticar credencial.")

    def list_files(drive, folder_id):
        #todo: list all files inside a google drive folder

        try:
            def file_list():
                    
                f_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder_id)}).GetList()
                
                return f_list

            def show_file_list():

                f_list = file_list()
            
                for file in f_list:
                    print('Nome: %s, id: %s\n' % (file['title'], file['id']))

            try:
                file_list()

                try:
                    show_file_list()

                except:
                    print("\nErro ao imprimir lista de arquivos")            
    
            except:
                print("\nErro ao gerar lista de arquivos")            
                    
        except:
                print("\nErro ao listar arquivos.")

    def upload(drive, folder_id):
        #to do: to acess files into folder and send to drive
        
        try: 
            path = "./files_to_upload"
            file = input("Qual arquivo você quer enviar? ")
            upload_file = os.path.join(path, file)

            gfile = drive.CreateFile({'parents': [{'id': folder_id}], 'title' : file})
            # Read file and set it as the content of this instance.
            gfile.SetContentFile(upload_file)
            gfile.Upload() # Upload the file
            print("\n ---> Arquivo enviado.\n")

        except:
            print("\nErro ao fazer upload.")
    

    def download(drive, folder_id):
        #todo: download files from google drive
        try:

            file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder_id)}).GetList()
            
            for file in file_list:
                for i, file in enumerate(sorted(file_list, key = lambda x: x['title']), start=1):
                    print('Downloading {} file from GDrive ({}/{})'.format(file['title'], i, len(file_list)))
                    file.GetContentFile(file['title'])
        except:
            print("\nErro ao baixar arquivos.")
    
    def create_file(drive, folder_id):
        #todo: create a file into google drive
        
        try: 
            
            file = drive.CreateFile({'parents': [{'id': folder_id}], 'title': 'file.txt'})
            file.SetContentString("Olá, Mundo!")
            file.Upload()
            print("\n ---> Arquivo Criado.\n")

        
        except:
            print("\nErro ao criar arquivo. \n")