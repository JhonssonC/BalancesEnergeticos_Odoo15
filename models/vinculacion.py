from odoo import fields, models, api


class vinculacion(models.Model):
    _name = "vinculacion"
    _description = "Vinculacion de Consumidor a Balance Energético"

    tipo_vinculacion_id = fields.Many2one("tipo.vinculacion", string="Tipo de Vinculacion")
    consumidor_id = fields.Many2one("consumidor", string="Consumidor")
    balance_energetico_id = fields.Many2one("balance.energetico", string="Balance de Energia")

    lectura = fields.Float("Lectura")
    fecha_hora = fields.Datetime("Momento de Reporte", default=lambda self: fields.Datetime.now())
    voltaje = fields.Integer("Voltaje", default=220)
    carga_l1 = fields.Float("Carga en Linea 1")
    carga_l2 = fields.Float("Carga en Linea 2")
    horas_uso = fields.Integer("Horas de uso aproximado en el dia", default=12)
    
    potencia_id = fields.Many2one("potencia", string="Potencia", default=None, required=False)
    #potencia = fields.Float("Potencia")
    
    fotos = fields.One2many(comodel_name='foto', inverse_name='vinculacion', string='Fotos de Campo')
    
    observacion = fields.Char("Observaciones y Novedades")
    
    

    active = fields.Boolean('Esta activo', default=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)
    
    tipo_consumidor = fields.Integer(string='Tipo de Consumidor', compute='_compute_tipo_consumidor')

    @api.depends('consumidor_id')
    def _compute_tipo_consumidor(self):
        for record in self:
            if record.consumidor_id.tipo_consumidor_id:
                record.tipo_consumidor = record.consumidor_id.tipo_consumidor_id
            else:
                record.tipo_consumidor = -1
                
                
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        print (args)
        if args:
            for arg in args:
                if arg[0] == '&' and len(arg) == 3:
                    campo = arg[0][0]
                    valor = arg[2].lower()
                    new_arg = '|', ('tipo_vinculacion_id', 'ilike', valor), ('consumidor_id', 'ilike', valor), ('balance_energetico_id', 'ilike', valor)
                    args[args.index(arg)] = new_arg
                    break
        return super(vinculacion, self).search(args, offset=offset, limit=limit, order=order, count=count)
    

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        #print (self, name, args, operator, limit, name_get_uid)
        args = list(args or [])
        if name :
            args += ['|', '|' , ('tipo_vinculacion_id', operator, name), ('consumidor_id', operator, name), ('balance_energetico_id', operator, name)]
        #print (self, name, args, operator, limit, name_get_uid)
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)