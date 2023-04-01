from odoo import api, fields, models


class balance_energetico(models.Model):
    _name = "balance.energetico"
    _description = "Balance Energético"
    _rec_name = "nombre"

    red_id = fields.Many2one("red", string="Red")

    nombre = fields.Char("Nombre")
    consumo_consumidores = fields.Float("Consumo Consumidores")
    consumo_totalizador = fields.Float("Consumo Totalizador")

    eficacia = fields.Float("Eficacia en Medición de Red (en %)")
    error = fields.Float("Error en Medición de Red (en %)")

    active = fields.Boolean('Esta activo', default=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)
    
    # red = fields.Char(string='Red', compute='_compute_red')

    # @api.depends('red_id')
    # def _compute_red(self):
    #     for record in self:
    #         if record.red_id.nombre:
    #             record.red_id = record.red_id.nombre
    #         else:
    #             record.red = False

    def name_get(self):

        result = []
        #print ("...Context...", self.env.context)
        
        for rec in self:
            name = f'[{rec.id:03d}] {rec.red_id.nombre} {rec.nombre}'
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
                    new_arg = '|', ('id', 'ilike', valor), ('red_id.nombre', 'ilike', valor), ('nombre', 'ilike', valor)
                    args[args.index(arg)] = new_arg
                    break
        return super(balance_energetico, self).search(args, offset=offset, limit=limit, order=order, count=count)
    

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        #print (self, name, args, operator, limit, name_get_uid)
        args = list(args or [])
        if name :
            args += ['|', '|' , ('nombre', operator, name), ('red_id', operator, name), ('id', operator, name)]
        #print (self, name, args, operator, limit, name_get_uid)
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)
    