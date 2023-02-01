from odoo import fields, models


class marca_medidor(models.Model):
    _name = "marca.medidor"
    _description = "Marca de Medidor"

   
    nomenclatura = fields.Char("Nomenclatura")
    descripcion = fields.Char("Descripcion")
    
    active = fields.Boolean('Esta activo', default=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)

    def name_get(self):

        result = []
        #print ("...Context...", self.env.context)
        
        for rec in self:
            name = f'[ {rec.nomenclatura} ] {rec.descripcion}'
            result.append((rec.id, name))
        
        return result