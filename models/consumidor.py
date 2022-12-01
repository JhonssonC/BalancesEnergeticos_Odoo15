from odoo import fields, models


class consumidor(models.Model):
    _name = "consumidor"
    _description = "Consumidor en Red"

    tipo_consumidor_id = fields.Many2one("tipo_consumidor", string="Tipo de Consumidor")
    codigo = fields.Char("Codigo")
    medidor = fields.Char("Medidor")
    marca_medidor_id = fields.Many2one("marca_medidor", string="Marca")
    tipo_conexion = fields.Selection([('AE', 'Aerea'), ('SU','Subterranea')])


    compartido = fields.Boolean('Punto Compartido (Caja Distribuidora / Panel / Parte de Agrupacion de medidores)', default=False)
    cantidad_compartido = fields.Integer("Cantidad de Medidores Agrupados")
    punto_carga_id = fields.Many2one("punto_carga", "Punto de Carga")
    

    active = fields.Boolean('Esta activo', default=True)


    def name_get(self):

        result = []
        #print ("...Context...", self.env.context)
        
        for rec in self:
            name = f'[ {rec.tipo_consumidor_id.nombre} ]  {rec.codigo}'
            result.append((rec.id, name))
        
        return result