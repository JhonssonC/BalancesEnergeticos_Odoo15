from odoo import fields, models


class coordenada(models.Model):
    _name = "coordenada"
    _description = "Coordenada"

    coord_x = fields.Float("Coordenada X")
    coord_y = fields.Float("Coordenada Y")
    latitud = fields.Float("Latitud")
    longitud = fields.Float("Longitud")

    active = fields.Boolean('Esta activo', default=True)


    def name_get(self):

        result = []
        #print ("...Context...", self.env.context)
        
        for rec in self:
            name = f'[ {rec.coord_x:03d}, {rec.coord_y:03d} ] '
            result.append((rec.id, name))
        
        return result