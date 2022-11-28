from odoo import fields, models


class canton(models.Model):
    _name = "canton"
    _description = "Canton"


    codigo = fields.Integer("Codigo")
    provincia_id = fields.Many2one("provincia", string="Provincia")
    nombre = fields.Char("Nombre")

    active = fields.Boolean('Esta activo', default=True)