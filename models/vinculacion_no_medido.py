from odoo import models, fields, api


class vinculacion(models.TransientModel):
    _name = "vinculacion.no.medido"
    _transient = True
    _description = "Vinculacion de Consumidor a Balance Energético (No Medido)"

    ides_v=fields.Char("Ides")
    tipo_vinculacion_id = fields.Many2one("tipo.vinculacion", string="Tipo de Vinculacion")
    consumidor_id = fields.Many2one("consumidor", string="Consumidor")
 
    balance_energetico_id = fields.Many2one("balance.energetico", string="Balance de Energia")


    fecha_hora = fields.Datetime("Fecha")

    voltaje = fields.Integer("Voltaje", default=220)
    carga_l1 = fields.Float("Carga en Linea 1")
    carga_l2 = fields.Float("Carga en Linea 2")
    horas_uso = fields.Integer("Horas de uso aproximado en el dia", default=12)
    
    potencia_id = fields.Many2one("potencia", string="Potencia", default=None, required=False)
    
    fotos = fields.Many2many(comodel_name='foto', string='Fotos de Campo')
    
    observacion = fields.Char("Observaciones y Novedades")
    
    
    tipo_consumidor = fields.Integer(string='Tipo de Consumidor', compute='_compute_tipo_consumidor')
    
    consumo = fields.Float("Consumo Aproximado")
    
    @api.depends('consumidor_id')
    def _compute_tipo_consumidor(self):
        for record in self:
            if record.consumidor_id.tipo_consumidor_id:
                record.tipo_consumidor = record.consumidor_id.tipo_consumidor_id
            else:
                record.tipo_consumidor = -1