from odoo import fields, models


class provincia(models.Model):
    _name = "provincia"
    _description = "Provincia"


    codigo = fields.Integer("Codigo")
    nombre = fields.Char("Nombre")

    active = fields.Boolean('Esta activo', default=True)

    def name_get(self):

        result = []
        print ("...Context...", self.env.context)
        
        for rec in self:
            #print(rec)
            pass