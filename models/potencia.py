from odoo import fields, models


class potencia(models.Model):
    _name = "potencia"
    _description = "Potencia"
    _rec_name = "nombre"


    nombre = fields.Float("Nombre", required=True)

    active = fields.Boolean('Esta activo', default=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)

    def name_get(self):

        result = []
        #print ("...Context...", self.env.context)
        
        for rec in self:
            #print(rec)
            code = rec.nombre
            code = f'{code:.00f}'
            name = ''+code+' KW'
            result.append((rec.id, name))
        
        return result