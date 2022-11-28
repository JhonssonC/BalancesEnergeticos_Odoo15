from odoo import fields, models


class tipo_consumidor(models.Model):
    _name = "tipo.consumidor"
    _description = "Tipo de Consumidor"

   
    nombre = fields.Char("Nombre")
    
    active = fields.Boolean('Esta activo', default=True)
    