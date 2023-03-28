from odoo import api, fields, models


class foto(models.Model):
    _name = "foto"
    _description = "Fotografia"
    _rec_name = "nombre"

    id = fields.Integer("Id")
    fotografia = fields.Image("Fotografia")
    nombre = fields.Char("Nombre")

    active = fields.Boolean('Esta activo', default=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)

    def name_get(self):
        result = []
        # print ("...Context...", self.env.context)

        for rec in self:
            name = f'[ {rec.nombre} ] '
            result.append((rec.id, name))

        return result