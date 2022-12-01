from odoo import fields, models


class transformador(models.Model):
    _name = "transformador"
    _description = "Transformador"


    potencia = fields.Char("Potencia")
    codigo = fields.Char("Codigo")
    serie = fields.Char("Serie")
    coord = fields.Many2one("coordenada", string="Punto Coordenada")

    active = fields.Boolean('Esta activo', default=True)


    def name_get(self):

        result = []
        #print ("...Context...", self.env.context)
        
        for rec in self:
            name = f'[ {rec.codigo} ] {rec.serie} / {rec.potencia}'
            result.append((rec.id, name))
        
        return result