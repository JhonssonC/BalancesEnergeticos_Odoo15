from odoo import fields, models


class tipo_vinculacion(models.Model):
    _name = "tipo.vinculacion"
    _description = "Tipo de Vinculación"

   
    nombre = fields.Char("Nombre")
    
    active = fields.Boolean('Esta activo', default=True)