from odoo import fields, models


class provincia(models.Model):
    _name = "provincia"
    _description = "Provincia"


    codigo = fields.Integer("Codigo")
    nombre = fields.Char("Nombre")

    active = fields.Boolean('Esta activo', default=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)

    def name_get(self):

        result = []
        #print ("...Context...", self.env.context)
        
        for rec in self:
            #print(rec)
            code = rec.codigo
            code = f'{code:02d}'
            name = '[ '+code+' ] '+rec.nombre
            result.append((rec.id, name))
        
        return result