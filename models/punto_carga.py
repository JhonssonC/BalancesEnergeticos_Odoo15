from odoo import fields, models


class punto_carga(models.Model):
    _name = "punto.carga"
    _description = "Punto de Carga"


    coord = fields.Many2one("coordenada", string="Punto Coordenada")

    active = fields.Boolean('Esta activo', default=True)