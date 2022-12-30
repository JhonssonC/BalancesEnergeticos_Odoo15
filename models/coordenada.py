from odoo import fields, models


class coordenada(models.Model):
    _name = "coordenada"
    _description = "Coordenada"

    coord_x = fields.Float("Coordenada X")
    coord_y = fields.Float("Coordenada Y")
    latitud = fields.Float("Latitud")
    longitud = fields.Float("Longitud")
    precision = fields.Float("Precision")

    active = fields.Boolean('Esta activo', default=True)


    def name_get(self):

        result = []
        #print ("...Context...", self.env.context)
        
        for rec in self:
            name = f'[ {rec.coord_x:.3f}, {rec.coord_y:.3f} ] '
            result.append((rec.id, name))
        
        return result