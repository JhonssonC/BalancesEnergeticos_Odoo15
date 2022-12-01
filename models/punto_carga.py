from odoo import fields, models


class punto_carga(models.Model):
    _name = "punto.carga"
    _description = "Punto de Carga"


    coord = fields.Many2one("coordenada", string="Punto Coordenada")

    active = fields.Boolean('Esta activo', default=True)


    def name_get(self):

        result = []
        #print ("...Context...", self.env.context)
        
        for rec in self:
            name = f'[ {rec.id:05d} ]-[ {rec.coord.coord_x:.3f}, {rec.coord.coord_y:.3f} ]'
            result.append((rec.id, name))
        
        return result