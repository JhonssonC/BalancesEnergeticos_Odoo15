import json
from odoo import http
from odoo.http import request, Response
import requests

class MyController(http.Controller):

    @http.route('/buscarCoincidencias',  type='http', auth='public', website=True)
    def index(self, **kwargs):
        
        # Hacer la petición GET a la API
        url = 'http://jhonssonc.servehttp.com/'
        params = {'un':'EOR','uid':'CONBALEOR1','pwd':'balance','params':''}
        
        if kwargs.get('codigo'):
            url+='queryclis'
            params['cli']=str(kwargs.get('codigo'))
            
        elif kwargs.get('medidor'):
            url+='querymeds'
            params['med']=str(kwargs.get('medidor'))
           
        # Realizar la consulta al servicio REST
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            customers = response.json()
        
        
        # if True:
        #     customers = [
        #         ["SERVICIO","MEDIDORFAB","NUMEROEMPRESA","MARCA"],
        #         [
        #         [1190070.0,"12345","11-66204","DIR-DIR"],
        #         [5655122.0,"12345774","61-186843","FAE-FAE"],
        #         [5900781.0,"12345777","61-186833","FAE-FAE"],
        #         [6011500.0,"12345783","61-186840","FAE-FAE"],
        #         [8267007.0,"12345858","81-189403","FAE-FAE"]
        #         ]]
            
            

            # Obtener el resultado de la petición
            result = customers

            # Devolver el resultado
            # return result
            return Response(json.dumps(result), content_type='application/json;charset=utf-8',status=200)
        else:
            return Response(json.dumps([['Error'],[['No se ejecutó busqueda...']]]), content_type='application/json;charset=utf-8',status=200)
        
    @http.route('/buscarCliente',  type='http', auth='public', website=True)
    def datosSicoCliente(self, **kwargs):
        
        # Hacer la petición GET a la API
        url = 'http://conielcialtda.servehttp.com:8008/queryalldatacli'
        params = {'un':'EOR','uid':'CONBALEOR1','pwd':'balance','params':''}
        

        params['cli']=str(kwargs.get('codigo'))
            
           
        # Realizar la consulta al servicio REST
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            customers = response.json()           

            # Obtener el resultado de la petición
            result = customers

            # Devolver el resultado
            # return result
            return Response(json.dumps(result), content_type='application/json;charset=utf-8',status=200)
        else:
            return Response(json.dumps([['Error'],[['No se ejecutó busqueda...']]]), content_type='application/json;charset=utf-8',status=200)
        
    @http.route('/marca/create', type='json', auth='user')
    def create(self, **kwargs):
        my_model = request.env['marca.medidor']
        modelList = my_model.search([('descripcion', '=',str(kwargs['descripcion']))])
        print('lista de modelo', modelList)
        if(len(modelList)<=0):
            new_record = my_model.create(kwargs)
        else:
            #new_record = my_model.browse([modelList[0]])
            new_record = modelList[0]
            
        print(new_record)
        return new_record.id