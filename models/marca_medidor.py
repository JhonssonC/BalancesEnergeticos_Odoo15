from odoo import fields, models


class marca_medidor(models.Model):
    _name = "marca.medidor"
    _description = "Marca de Medidor"

   
    nomenclatura = fields.Char("Nomenclatura")
    descripcion = fields.Char("Descripcion")
    
    active = fields.Boolean('Esta activo', default=True)
    