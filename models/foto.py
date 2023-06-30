from odoo import api, fields, models
import base64
import requests
import time
import random
import  io
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from google.auth.transport.requests import AuthorizedSession
import google.auth

import requests
from google.oauth2 import service_account



class foto(models.Model):
    _name = "foto"
    _description = "Fotografia"
    _rec_name = "nombre"

    id = fields.Integer("Id")
    fotografia = fields.Image("Fotografia")
    nombre = fields.Char("Nombre")
    
    vinculacion = fields.Many2one(comodel_name='vinculacion', string='Vinculacion de Consumidor')

    active = fields.Boolean('Esta activo', default=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)

    def name_get(self):
        result = []
        # print ("...Context...", self.env.context)

        for rec in self:
            name = f'[{rec.nombre}]-ID:{rec.id}'
            result.append((rec.id, name))

        return result
    
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        print (args)
        if args:
            for arg in args:
                if arg[0] == '&' and len(arg) == 3:
                    campo = arg[0][0]
                    valor = arg[2].lower()
                    new_arg = '|', ('id', 'ilike', valor), ('nombre', 'ilike', valor)
                    args[args.index(arg)] = new_arg
                    break
        return super(foto, self).search(args, offset=offset, limit=limit, order=order, count=count)
    

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        #print (self, name, args, operator, limit, name_get_uid)
        args = list(args or [])
        if name :
            args += ['|', ('nombre', operator, name), ('id', operator, name)]
        #print (self, name, args, operator, limit, name_get_uid)
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)
    
    

    @api.model
    def load(self, fields, data):
        
        SCOPES = ['https://www.googleapis.com/auth/drive']
        TOKEN = '/mnt/extra-addons/balancesEnergeticos/GoogleDriveApi/token.json'
        CREDENTIALS = "/mnt/extra-addons/balancesEnergeticos/GoogleDriveApi/credential_sample.json"
        #CREDENTIALS = '/var/lib/odoo/.config/gcloud/application_default_credentials.json' 

        id_tkn="ya29.a0Ael9sCPiOWT1z-xyMclyO8V4j0DpgqSOV60naInZ5UMT51uqerqewj5SSWg5-VlfLu8_HH-8IvDVvj96ObyF25bbyUWKi8J-DkitQAyP78XE67u4gSlg0Z0RWnv0o6Mu1K9tdgtnFYsLc4tboJZ_OTb3mcPnaCgYKAc4SARASFQF4udJhoYxACkWPL72gibw0Lyfp1Q0163"
        file_id = ''
        
        print('Datos de importación:', self, fields, data)
        
        data2 = []
        service = None
        for idx, row in enumerate(data):
            
            if 'fotografia' in fields:
                indice = fields.index('fotografia')
                indexMap = dict((x, i) for i, x in enumerate(fields))
                acc = 0
                for i, pic in enumerate(str(row[indice]).split(' *-* ')):
                    
                    if(pic):
                        tmprow = row.copy()
                        
                        if(indexMap.get('id', -1)>-1):
                            theId = int(tmprow[fields.index('id')])
                            theId+=acc
                            acc+=1
                            tmprow[fields.index('id')] = str(theId)
                            print(theId)
                            
                        for k in range (0, 10):
                            print("intento de obtencion de foto", k+1)
                            
                            #test_file = requests.get(str(pic)).content
                            file_id = (str(pic)).split('id=')[1]
                            
                            #flow = InstalledAppFlow.from_client_secrets_file('/mnt/extra-addons/balancesEnergeticos/models/credentials.json', SCOPES)
                            #creds = flow.run_local_server(port=0)
                            
                            if not service:


                                creds = None
                                # The file token.json stores the user's access and refresh tokens, and is
                                # created automatically when the authorization flow completes for the first
                                # time.
                                if os.path.exists(TOKEN):
                                    creds = Credentials.from_authorized_user_file(TOKEN, SCOPES)
                                # If there are no (valid) credentials available, let the user log in.
                                if not creds or not creds.valid:
                                    if creds and creds.expired and creds.refresh_token:
                                        creds.refresh(Request())
                                    else:
                                        flow = Flow.from_client_secrets_file(
                                            CREDENTIALS, scopes=SCOPES, redirect_uri='urn:ietf:wg:oauth:2.0:oob')
                                        # Tell the user to go to the authorization URL.
                                        auth_url, _ = flow.authorization_url(prompt='consent')

                                        print('Please go to this URL: {}'.format(auth_url))

                                        # The user will get an authorization code. This code is used to get the
                                        # access token.
                                        code = input('Enter the authorization code: ')
                                        
                                        flow.fetch_token(code=code)

                                        # You can use flow.credentials, or you can just get a requests session
                                        # using flow.authorized_session.
                                        session = flow.authorized_session()
                                        print (session)
                                        
                                        creds = flow.credentials
                                        
                                    
                                    # Save the credentials for the next run
                                    with open(TOKEN, 'w') as token:
                                        token.write(creds.to_json())
                                        
                                        
                            try:
                                service = build('drive', 'v3', credentials=creds, cache_discovery=False)
                                
                                if creds.id_token:
                                    id_tkn = creds.id_token
                                
                                print ("tkn",id_tkn)

                            except HttpError as error:
                                # TODO(developer) - Handle errors from drive API.
                                print(f'An error occurred: {error}')
                                build('drive', 'v3', developerKey="AIzaSyCZLhc66MM4DV7Mfz43uS8Wo9q1szOrYYE")
                                    
                                
                            test_file = download_photo_from_google_drive(service, file_id, id_tkn)
                            
                            #print(test_file)
                            if (not (test_file)):
                                time.sleep((8+k)*60)
                                continue
                            else: 
                                data_file = base64.b64encode(test_file)
                                break
                            
                        if(data_file):
                            print ("se obtubo la foto de:",pic)
                            tmprow[indice] = data_file
                            
                        else:
                            print ("No se pudo en todos los intentos conseguir la foto...")
                            return
                            
                        
                        tmprow[fields.index('nombre')] += (' ' + str(pic))
                        
                        data2.append(tmprow)
                        #time.sleep(random.randint(3, 6))
                        
                        if len(data2) == 10:
                            res = super(foto, self).load(fields, data2)
                            print('Proceso de carga temporal finalizado')
                            data2 = []
                        else:
                            print('temporal de subida :', len(data2))

                            
            else:
                print('El elemento no está en la lista')
                
        #print('Datos de importación:', self, fields, data)

        res = super(foto, self).load(fields, data2)
        print('Proceso de carga finalizado')
        return res 





def download_photo_from_google_drive(service, file_id, id_tkn):
    """
    Descarga una foto desde Google Drive y la guarda en el disco.
    :param credentials: Credenciales para autenticarse en la API de Google.
    :param file_id: ID del archivo de Google Drive.
    :param save_as: Ruta donde se guardará la foto descargada.
    :return: True si la descarga fue exitosa, False en caso contrario.
    """

    try:
      
        print (service)


        file = service.files().get(fileId=file_id).execute()
        print(file)
        
        # mime_type='image/jpeg'
        # export_url = f'https://www.googleapis.com/drive/v3/files/{file_id}/export?mimeType={mime_type}'
        # response = requests.get(export_url, headers={'Authorization': f'Bearer {id_tkn}'}, stream=True)
        # print (response.content)
        # return response.content
        
        request = service.files().get_media(fileId=file_id)
        print(request)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(f'Download {int(status.progress() * 100)}.')
        return file.getvalue()

    except HttpError as error:
        print(F'An error occurred (2): {error}')
        file = None
        if service != build('drive', 'v3', developerKey="AIzaSyCZLhc66MM4DV7Mfz43uS8Wo9q1szOrYYE"):
            service = build('drive', 'v3', developerKey="AIzaSyCZLhc66MM4DV7Mfz43uS8Wo9q1szOrYYE")
            file = download_photo_from_google_drive(service, file_id)
        return file

    
def obtain_access_token():
    
    # Obtén el token de acceso
    access_token=''
    with open('/var/lib/odoo/.config/gcloud/access_tokens.db', 'r') as f:
        access_token = f.readline().strip()
        
    print('access token', access_token)
    return access_token
    ####################################################################################
    # Configuración de las credenciales de la API
    # api_key = 'AIzaSyCZLhc66MM4DV7Mfz43uS8Wo9q1szOrYYE'
    # client_secret = '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'

    # # Configuración de las credenciales de OAuth2
    # credentials = service_account.Credentials.from_service_account_info({
    #     'client_id': api_key,
    #     'client_secret': client_secret,
    #     'token_uri': 'https://oauth2.googleapis.com/token',
    #     'client_email': 'balances.ceor@gmail.com'
    # })

    # # Obtención del access_token
    # response = requests.post('https://oauth2.googleapis.com/token', data={
    #     'grant_type': 'client_credentials',
    #     'audience': 'https://www.googleapis.com/oauth2/v4/token',
    # }, auth=credentials)
    # access_token = response.json()['access_token']

    # print(f'El access_token es: {access_token}')
    # return access_token
    
    
    ###################################################################################################
    # import google.auth
    # import google.auth.transport.requests
    # import requests

    # # Configurar las credenciales
    # api_key = 'AIzaSyCZLhc66MM4DV7Mfz43uS8Wo9q1szOrYYE'
    # scopes = ['https://www.googleapis.com/auth/drive.readonly'] # agregar los scopes necesarios

    # # Obtener el access_token
    # auth_req_url = f'https://www.googleapis.com/oauth2/v1/tokeninfo?key={api_key}'
    # auth_req = requests.get(auth_req_url)
    # auth_info = auth_req.json()
    # print(auth_info)
    # auth_credentials = google.auth.credentials.Credentials.from_authorized_user_info(info=auth_info)

    # # Utilizar el access_token
    # access_token = auth_credentials.token
    # print(f"Access token: {access_token}")
    # return access_token
    ###################################################################################################
    
    
    # import subprocess

    # # Ejecutar el comando "gcloud auth print-access-token" y capturar la salida
    # process = subprocess.Popen(['gcloud', 'auth', 'print-access-token'], stdout=subprocess.PIPE)
    # output, error = process.communicate()

    # # Decodificar la salida como UTF-8 y eliminar cualquier espacio en blanco
    # access_token = output.decode('utf-8').strip()

    # print(f'El access_token es: {access_token}')