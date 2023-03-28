from odoo import fields, models


class marca_medidor(models.Model):
    _name = "marca.medidor"
    _description = "Marca de Medidor"
    _rec_name = "descripcion"
   
    nomenclatura = fields.Char("Nomenclatura", required=True, index=True)
    descripcion = fields.Char("Descripcion", required=True)
    
    active = fields.Boolean('Esta activo', default=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)

    def name_get(self):

        result = []
        #print ("...Context...", self.env.context)
        
        for rec in self:
            name = f'{rec.nomenclatura}-{rec.descripcion}'
            result.append((rec.id, name))
        
        return result