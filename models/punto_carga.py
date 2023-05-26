from odoo import fields, models, api


class punto_carga(models.Model):
    _name = "punto.carga"
    _description = "Punto de Carga"
    _rec_name = "id"


    coord = fields.Many2one("coordenada", string="Punto Coordenada")

    active = fields.Boolean('Esta activo', default=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)

    def name_get(self):

        result = []
        #print ("...Context...", self.env.context)
        
        for rec in self:
            name = f'{rec.id:05d} - [X:{rec.coord.coord_x:.3f}, Y:{rec.coord.coord_y:.3f}] - Punto de Carga'
            result.append((rec.id, name))
        
        return result
    

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        print ('search', args)
        if args:
            for arg in args:
                if arg[0] == '&' and len(arg) == 3:
                    campo = arg[0][0]
                    valor = arg[2].lower()
                    new_arg = '|', ('id', 'ilike', valor), ('coord.id', 'ilike', valor)
                    args[args.index(arg)] = new_arg
                    break
        return super(punto_carga, self).search(args, offset=offset, limit=limit, order=order, count=count)