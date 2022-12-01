from odoo import fields, models


class balance_energetico(models.Model):
    _name = "balance.energetico"
    _description = "Balance Energético"

    red_id = fields.Many2one("red", string="Red")

    nombre = fields.Char("Nombre")
    consumo_consumidores = fields.Float("Consumo Consumidores")
    consumo_totalizador = fields.Float("Consumo Totalizador")

    eficacia = fields.Float("Eficacia en Medición de Red (en %)")
    error = fields.Float("Error en Medición de Red (en %)")

    active = fields.Boolean('Esta activo', default=True)


    def name_get(self):

        result = []
        #print ("...Context...", self.env.context)
        
        for rec in self:
            name = f'[ {rec.id:03d} ]  {rec.red_id} {rec.nombre}'
            result.append((rec.id, name))
        
        return result