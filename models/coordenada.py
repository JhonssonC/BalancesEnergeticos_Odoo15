from odoo import api, fields, models


class coordenada(models.Model):
    _name = "coordenada"
    _description = "Coordenada"
    _rec_name = "id"

    coord_x = fields.Float("Coordenada X")
    coord_y = fields.Float("Coordenada Y")
    latitud = fields.Float("Latitud")
    longitud = fields.Float("Longitud")
    precision = fields.Float("Precision")

    active = fields.Boolean('Esta activo', default=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)
    
    def name_get(self):

        result = []
        #print ("...Context...", self.env.context)
        
        for rec in self:
            name = f' {rec.id:05d} - [X:{rec.coord_x:.3f}, Y:{rec.coord_y:.3f} ] - Coordenada'
            result.append((rec.id, name))
        
        return result
    
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if args:
            for arg in args:
                if arg[0] == '&' and len(arg) == 3:
                    campo = arg[0][0]
                    valor = arg[2].lower()
                    new_arg = '|', ('id', 'ilike', valor), ('coord_x', 'ilike', valor), ('coord_y', 'ilike', valor)
                    args[args.index(arg)] = new_arg
                    break
        return super(coordenada, self).search(args, offset=offset, limit=limit, order=order, count=count)
    
    
    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        #print (self, name, args, operator, limit, name_get_uid)
        args = list(args or [])
        if name :
            args += ['|', '|', ('id', operator, name), ('coord_x', operator, name), ('coord_y', operator, name)]
        #print (self, name, args, operator, limit, name_get_uid)
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)