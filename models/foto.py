from odoo import api, fields, models
import base64


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
        
        print('Datos de importación:', self, fields, data)
        
        for idx, row in enumerate(data):
            if 'fotografia' in fields:
                indice = fields.index('fotografia')
                print(indice)
                test_file = open(str(row[indice]),'rb')
                data_file = base64.b64encode(test_file.read())
                data[idx][indice] = data_file
            else:
                print('El elemento no está en la lista')
                
        print('Datos de importación:', self, fields, data)

        res = super(foto, self).load(fields, data)
        print('Proceso de carga finalizado')
        return res 