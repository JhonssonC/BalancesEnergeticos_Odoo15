from odoo import fields, models


class vinculacion(models.Model):
    _name = "vinculacion"
    _description = "Vinculacion de Consumidor a Balance Energético"

    tipo_vinculacion_id = fields.Many2one("tipo_vinculacion", string="Tipo de Vinculacion")
    consumidor_id = fields.Many2one("consumidor", string="Consumidor")
    balance_energetico_id = fields.Many2one("balance_energetico", string="Balance de Energia")

    lectura = fields.Float("Lectura")
    fecha_hora = fields.Datetime("Momento de Reporte", default=lambda self: fields.Datetime.now())
    voltaje = fields.Integer("Voltaje")
    carga_l1 = fields.Float("Carga en Linea 1")
    carga_l2 = fields.Float("Carga en Linea 2")
    horas_uso = fields.Integer("Horas de uso aproximado en el dia")
    potencia = fields.Float("Potencia")
    observacion = fields.Char("Observaciones y Novedaades")
    

    active = fields.Boolean('Esta activo', default=True)