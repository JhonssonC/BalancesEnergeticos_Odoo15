from odoo import fields, models


class tipo_vinculacion(models.Model):
    _name = "tipo.vinculacion"
    _description = "Tipo de Vinculación"

   
    nombre = fields.Char("Nombre")
    
    active = fields.Boolean('Esta activo', default=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)

    def name_get(self):

        result = []
        #print ("...Context...", self.env.context)
        
        for rec in self:
            name = f'[ {rec.id:02d} ]  {rec.nombre}'
            result.append((rec.id, name))
        
        return result