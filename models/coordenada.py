from odoo import fields, models


class coordenada(models.Model):
    _name = "coordenada"
    _description = "Coordenada"

    coord_x = fields.Float("Coordenada X")
    coord_y = fields.Float("Coordenada Y")
    latitud = fields.Float("Latitud")
    longitud = fields.Float("Longitud")

    active = fields.Boolean('Esta activo', default=True)