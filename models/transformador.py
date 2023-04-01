from odoo import api, fields, models


class transformador(models.Model):
    _name = "transformador"
    _description = "Transformador"


    potencia = fields.Char("Potencia")
    codigo = fields.Char("Codigo")
    serie = fields.Char("Serie")
    coord = fields.Many2one("coordenada", string="Punto Coordenada")

    active = fields.Boolean('Esta activo', default=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)

    def name_get(self):

        result = []
        #print ("...Context...", self.env.context)
        
        for rec in self:
            name = f'[ {rec.codigo} ] {rec.serie} / {rec.potencia}'
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
                    new_arg = '|', ('potencia', 'ilike', valor), ('codigo', 'ilike', valor), ('serie', 'ilike', valor)
                    args[args.index(arg)] = new_arg
                    break
        return super(transformador, self).search(args, offset=offset, limit=limit, order=order, count=count)
    

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        #print (self, name, args, operator, limit, name_get_uid)
        args = list(args or [])
        if name :
            args += ['|', '|' , ('potencia', operator, name), ('codigo', operator, name), ('serie', operator, name)]
        #print (self, name, args, operator, limit, name_get_uid)
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)