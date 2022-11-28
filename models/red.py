from odoo import fields, models


class red(models.Model):
    _name = "red"
    _description = "Identificador de Red"


    nombre = fields.Char("Nombre de Red")

    transformador_id = fields.Many2one("transformador", string="Transformador")
    provincia_id = fields.Many2one("provincia", "Provincia")
    canton_id = fields.Many2one("canton", "Canton")

    active = fields.Boolean('Esta activo', default=True)