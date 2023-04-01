from odoo import api, fields, models


class consumidor(models.Model):
    _name = "consumidor"
    _description = "Consumidor en Red"
    _rec_name = "codigo"
    

    codigo = fields.Char("Codigo")
    medidor = fields.Char("Medidor")
    serie = fields.Char("Serie")
    nombre = fields.Char("Nombre")
    direccion = fields.Char("Dirección")
    geo = fields.Char("Geocódigo")

    tipo_consumidor_id = fields.Many2one("tipo.consumidor", string="Tipo de Consumidor")
    
    marca_medidor_id = fields.Many2one("marca.medidor", string="Marca")
    
    marca_oculta=fields.Char("Marca Buscada")
    
    potencia_id = fields.Many2one("potencia", string="Potencia", default=None, required=False)
    
    tipo_conexion = fields.Selection([('AE', 'Aerea'), ('SU','Subterranea')], string="Tipo de Conexion")


    compartido = fields.Boolean('Punto Compartido (Caja Distribuidora / Panel / Parte de Agrupacion de medidores, semaforos o camaras)', default=False)
    cantidad_compartido = fields.Integer("Cantidad de Agrupados", default='1')
    punto_carga_id = fields.Many2one("punto.carga", "Punto de Carga")
    

    active = fields.Boolean('Esta activo', default=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)
    


    def name_get(self):

        result = []
        #print ("...Context...", self.env.context)
        
        for rec in self:
            name = f'{rec.codigo}-ID({rec.id})-[{rec.tipo_consumidor_id.nombre}]'
            result.append((rec.id, name))
        
        return result
    
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if args:
            for arg in args:
                if arg[0] == '&' and len(arg) == 3:
                    campo = arg[0][0]
                    valor = arg[2].lower()
                    new_arg = '|', ('id', 'ilike', valor), ('tipo_consumidor_id', 'ilike', valor), ('codigo', 'ilike', valor), ('medidor', 'ilike', valor)
                    args[args.index(arg)] = new_arg
                    break
        return super(consumidor, self).search(args, offset=offset, limit=limit, order=order, count=count)
    
    
    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        #print (self, name, args, operator, limit, name_get_uid)
        args = list(args or [])
        if name :
            args += ['|', '|' , '|' , ('id', operator, name), ('tipo_consumidor_id', operator, name), ('codigo', operator, name), ('medidor', operator, name)]
        #print (self, name, args, operator, limit, name_get_uid)
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)
    
         
    
    @api.onchange('marca_oculta')
    def onchange_serie(self):
        print (self)
        if self.marca_oculta:
            # Cargar el modelo de la vista
            vista_obj = self.env['marca.medidor']
            
            # Buscar la vista de lista por ID
            vista_id = vista_obj.search([('nomenclatura', '=', str(self.marca_oculta))])
            print (vista_id)
            if(len(vista_id.ids)==1):
                self.marca_medidor_id=(vista_id.ids)[0]
            #     return{'default':{'marca_medidor_id': (vista_id.ids)[0]}}
            # else:
            #     return{'domain':{'marca_medidor_id': [('id', 'in', vista_id.ids)]}}
    
    # # @api.model
    # # def obtener_datos_cliente(self, codigo_cliente):
    # #     url = 'http://<tu_url_del_servicio_rest>/clientes/{}/'.format(codigo_cliente)
    # #     headers = {'Content-Type': 'application/json'}
    # #     response = requests.get(url, headers=headers)

    # #     if response.status_code == 200:
    # #         datos_cliente = json.loads(response.text)
    # #         return datos_cliente
    # #     else:
    # #         return None


    # def seleccionar_cliente(self):
    #     return {}
    
    
    # def search_data(self, id, medidor=None, codigo=None, m=None):
        
    #     # url = 'http://jhonssonc.servehttp.com/'
    #     # params = {'un':'EOR','uid':'CONBALEOR1','pwd':'balance','params':''}
        
    #     # if codigo:
    #     #     url+='queryclis'
    #     #     params['cli']=str(codigo)
            
    #     # elif medidor:
    #     #     url+='querymeds'
    #     #     params['med']=str(medidor)
            
    #     # # Realizar la consulta al servicio REST
    #     # response = requests.get(url, params=params)
        
    #     # if response.status_code == 200:
            
    #     #     customers = response.json()
    #     #     if customers:
    #     #         customers = customers[1]
    #     if True:
    #         customers = [
    #             [1190070.0,"12345","11-66204","DIR-DIR"],
    #             [5655122.0,"12345774","61-186843","FAE-FAE"],
    #             [5900781.0,"12345777","61-186833","FAE-FAE"],
    #             [6011500.0,"12345783","61-186840","FAE-FAE"],
    #             [8267007.0,"12345858","81-189403","FAE-FAE"]
    #             ]
                
    #         print(customers)
            
    #         registros = self.env['model.name']
            
    #         # Cargar el modelo de la vista
    #         vista_obj = self.env['ir.ui.view']
            
    #         # Buscar la vista de lista por ID
    #         vista_id = vista_obj.search([('name', '=', 'view_popup_tree')])

    #         # Obtener el ID de la vista de lista
    #         vista_id = vista_id.id
    #         i=1
    #         data=[]
    #         html = '<tree>'
    #         for dato in customers:
    #             # html += '<record id="%s" model="%s">' % (str(i), 'model.name')
    #             html += '<field name="field1">%s</field>' % str(dato[0])
    #             html += '<field name="field2">%s</field>' % str(dato[1])
    #             html += '<field name="field3">%s</field>' % str(dato[2])
    #             # html += '</record>'
    #             i=i+1
    #             data.append({
    #                 'field1':dato[0],
    #                 'field2':dato[1],
    #                 'field3':dato[2],
    #             })
    #         html += '</tree>'
            
    #         # Actualizar el atributo "datas" de la vista
    #         vista = vista_obj.browse(vista_id)
    #         vista.write({'arch': html})
            
    #         print (html)
            
    #         # cnt = self.env.context
    #         # cnt.update({
    #         #     'arch': html
    #         # })
            
    #         return {
    #             'name': 'Resultados de búsqueda',
    #             'type': 'ir.actions.act_window',
    #             'res_model': 'model.name',
    #             'view_mode': 'list',
    #             'flags': {'action_buttons': False, 'actions':False},
    #             'view_id': vista_id,
    #             'target': 'new',
    #             'context': {'data': data},
                
    #             'views': [(vista_id, 'list')]
    #         }
    #     else:
    #         pass
        


    # def action_search_medidor(self, context=None):
    #     print(self.env.context)
    #     print(self.env['coordenada'].search([]))
    #     return self.search_data(self.id, medidor = self.medidor)
        
    # def action_search_code(self, context=None):
    #     print(self.env.context)
    #     print(type(self.env['coordenada']))
    #     return self.search_data(self.id, codigo = self.codigo)
    
    # def show_cntx(self):
    #     print(self.env.context)
    #     print(self.env['model.name'])
    
    
        
