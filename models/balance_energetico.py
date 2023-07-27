import json
from odoo import api, fields, models
from datetime import datetime


class balance_energetico(models.Model):
    _name = "balance.energetico"
    _description = "Balance Energético"
    #es preferida esta linea para vista kanban
    # _rec_name = "nombre"
    
    nombre = fields.Char("Nombre")
    costo_kwh = fields.Float("Costo Kw/H", default="0.10")




    red_id = fields.Many2one("red", string="Red")
    
    red_id_trafo_id = fields.Integer(compute="_red_id_trafo_id", string="Id Transformador")
    red_id_sector = fields.Char(compute="_red_id_sector", string="Sector de ubicacion del Transformador")
    red_id_id = fields.Integer(compute="_red_id_id", string="Id Red")
    red_id_trafo_codigo = fields.Char(compute="_red_id_trafo_codigo", string="Codigo de Transformador")
    red_id_trafo_capacidad = fields.Char(compute="_red_id_trafo_capacidad", string="Capacidad de Transformador")
    red_id_trafo_x = fields.Float(compute="_red_id_trafo_x", string="Coordenada X de Transformador")
    red_id_trafo_y = fields.Float(compute="_red_id_trafo_y", string="Coordenada Y de Transformador")

    
    
    
    detalle_vinculaciones = fields.One2many(comodel_name='vinculacion', inverse_name='balance_energetico_id', string='Detalle Total de Vinculaciones')
    
    consumidores_clientes = fields.One2many(comodel_name='vinculacion.medido', compute="_compute_o2m_field_cli")
    consumidores_totaliza = fields.One2many(comodel_name='vinculacion.medido', compute="_compute_o2m_field_tot")
    consumidores_no_medidos_lum_ini = fields.One2many(comodel_name='vinculacion.no.medido', compute="_compute_o2m_field_no_med_l_ini")
    consumidores_no_medidos_lum_fin = fields.One2many(comodel_name='vinculacion.no.medido', compute="_compute_o2m_field_no_med_l_ini")
    consumidores_no_medidos_sem_ini = fields.One2many(comodel_name='vinculacion.no.medido', compute="_compute_o2m_field_no_med_s_ini")
    consumidores_no_medidos_sem_fin = fields.One2many(comodel_name='vinculacion.no.medido', compute="_compute_o2m_field_no_med_s_ini")
    consumidores_no_medidos_cam_ini = fields.One2many(comodel_name='vinculacion.no.medido', compute="_compute_o2m_field_no_med_c_ini")
    consumidores_no_medidos_cam_fin = fields.One2many(comodel_name='vinculacion.no.medido', compute="_compute_o2m_field_no_med_c_ini")
    consumidores_no_medidos_otr_ini = fields.One2many(comodel_name='vinculacion.no.medido', compute="_compute_o2m_field_no_med_o_ini")
    consumidores_no_medidos_otr_fin = fields.One2many(comodel_name='vinculacion.no.medido', compute="_compute_o2m_field_no_med_o_ini")
    
    
    
    
    fecha_inicial = fields.Date("Fecha de Levantamiento Inicial")
    fecha_final = fields.Date("Fecha de Levantamiento Posterior")
    
    
    cant_clientes = fields.Integer(compute="_cant_clientes", string="Clientes")
    cant_luminarias =  fields.Integer(compute="_cant_luminarias", string="Lámparas")
    cant_semaforos = fields.Integer(compute="_cant_semaforos", string="Semáforos")
    cant_camaras = fields.Integer(compute="_cant_camaras", string="Cámaras")
    cant_otros = fields.Integer(compute="_cant_otros", string="Servicios Convenidos (Directos)")
    cant_consumidores =  fields.Integer(compute="_cant_consumidores", string="Total de Consumidores")
    
    
    consumo_consumidores = fields.Float("Consumo Consumidores")
    consumo_totalizador = fields.Float("Consumo Totalizador")
    consumo_diferencia = fields.Float("Consumo Diferencia")
    
    consumo_luminarias = fields.Float("Consumo Luminarias", default=0)
    consumo_semaforos = fields.Float("Consumo Semáforos", default=0)
    consumo_camaras = fields.Float("Consumo Cámaras", default=0)
    consumo_otros = fields.Float("Servicios Convenidos", default=0)
    consumo_clientes = fields.Float("Consumo Clientes", default=0)
    
    
    costo_clientes = fields.Float(compute="_costo_clientes")
    costo_luminarias =  fields.Float(compute="_costo_luminarias")
    costo_semaforos = fields.Float(compute="_costo_semaforos")
    costo_camaras = fields.Float(compute="_costo_camaras")
    costo_otros = fields.Float(compute="_costo_otros")
    costo_consumidores =  fields.Float(compute="_costo_consumidores")
    
    
    porce_clientes = fields.Float(compute="_porce_clientes")
    porce_luminarias =  fields.Float(compute="_porce_luminarias")
    porce_semaforos = fields.Float(compute="_porce_semaforos")
    porce_camaras = fields.Float(compute="_porce_camaras")
    porce_otros = fields.Float(compute="_porce_otros")
    porce_consumidores =  fields.Float(compute="_porce_consumidores")
    
    
    porce2_clientes = fields.Float(compute="_porce2_clientes")
    porce2_luminarias =  fields.Float(compute="_porce2_luminarias")
    porce2_semaforos = fields.Float(compute="_porce2_semaforos")
    porce2_camaras = fields.Float(compute="_porce2_camaras")
    porce2_otros = fields.Float(compute="_porce2_otros")
    porce2_consumidores =  fields.Float(compute="_porce2_consumidores")
    
    
    
    perdidas_comerciales_dias = fields.Float(compute="_perdidas_comerciales_dias", string="Pérdidas Comerciales")
    perdidas_comerciales_dias_costo = fields.Float(compute="_perdidas_comerciales_dias_costo", string="Pérdidas Comerciales Dias Costo")
    perdidas_comerciales_mes = fields.Float(compute="_perdidas_comerciales_mes", string="Pérdidas Comerciales Mes")
    perdidas_comerciales_mes_costo = fields.Float(compute="_perdidas_comerciales_mes_costo", string="Pérdidas Comerciales Mes Costo")
    perdidas_comerciales_porcentaje = fields.Float(compute="_perdidas_comerciales_porcentaje", string="Pérdidas Comerciales [%]")
    
    energia_entregada_dias = fields.Float(compute="_energia_entregada_dias", string="Energía Entregada")
    energia_entregada_dias_costo = fields.Float(compute="_energia_entregada_dias_costo", string="Energia Entregada Dias Costo")
    energia_entregada_mes = fields.Float(compute="_energia_entregada_mes", string="Energía Entregada Mes")
    energia_entregada_mes_costo = fields.Float(compute="_energia_entregada_mes_costo", string="Energía Entregada Mes Costo")
    energia_entregada_porcentaje = fields.Float(compute="_energia_entregada_porcentaje", string="Energía Entregada [%]")
    
    energia_registrada_dias = fields.Float(compute="_energia_registrada_dias", string="Energía Registrada")
    energia_registrada_dias_costo = fields.Float(compute="_energia_registrada_dias_costo", string="Energía Registrada Días Costo")
    energia_registrada_mes = fields.Float(compute="_energia_registrada_mes", string="Energía Registrada Mes")
    energia_registrada_mes_costo = fields.Float(compute="_energia_registrada_mes_costo", string="Energía Registrada Mes Costo")
    energia_registrada_porcentaje = fields.Float(compute="_energia_registrada_porcentaje", string="Energía Registrada [%]")



    eficacia = fields.Float("Eficacia en Medición de Red (en %)")
    error = fields.Float("Error en Medición de Red (en %)")
    
    color = fields.Char("color de fondo", compute="_color")

    active = fields.Boolean('Esta activo', default=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)
    
    
    
    
    
    def name_get(self):

        result = []
        #print ("...Context...", self.env.context)
        
        for rec in self:
            name = f'[{rec.id:03d}] {rec.red_id.nombre} {rec.nombre}'
            result.append((rec.id, name))
        
        return result
    
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        print ('search', args)
        if args:
            for arg in args:
                if arg[0] == '&' and len(arg) == 3:
                    campo = arg[0][0]
                    valor = arg[2].lower()
                    new_arg = '|', ('id', 'ilike', valor), ('red_id.nombre', 'ilike', valor), ('nombre', 'ilike', valor)
                    args[args.index(arg)] = new_arg
                    break
        return super(balance_energetico, self).search(args, offset=offset, limit=limit, order=order, count=count)
    

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        #print (self, name, args, operator, limit, name_get_uid)
        args = list(args or [])
        if name :
            args += ['|', '|' , ('nombre', operator, name), ('red_id', operator, name), ('id', operator, name)]
        #print (self, name, args, operator, limit, name_get_uid)
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)
    
    
    def calcular_balance(self):
        print ('llamada a calcular')
        
        
        
    ##############################################################################################################################################
        
    @api.depends('detalle_vinculaciones')
    def _compute_o2m_field_cli(self):
        
        #print ('_compute_o2m_field_cli',self)
        
        for balance in self:
            
            try:
                related_recordset = self.env["vinculacion"].search([("consumidor_id.tipo_consumidor_id.id", "<","5"), ("balance_energetico_id.id","=",str(balance.id))], order='fecha_hora asc')
                
                #fechas del balance
                fechas = list(set([cli.fecha_hora.date() for cli in related_recordset]))
                
                print("+++++++++++++++++++++++++")
                print ('FECHAS_MED', fechas)
                print("+++++++++++++++++++++++++")
            except Exception as err:
                print (err)
                related_recordset=[]
                fechas = []
            
            if len(related_recordset) > 0 and len(fechas) == 2:
            
                # print("+++++++++++++++++++++++++")
                # print ('_compute_o2m_field_cli(1)', list(related_recordset))
                # print("+++++++++++++++++++++++++")
            
                clientes=[]
                tmpCliBal = []
                tmpFotBal = []
                medido_ids = []
                
                
                for cli in related_recordset:
                    
                    #ids de fotos
                    fotos_ids = [f.id for f in cli.fotos]
                    
                    
                    #Clientes del Balance
                    current_tmp_serv = cli.consumidor_id.codigo
                    if not (current_tmp_serv in tmpCliBal):
                    
                        tmpCliBal.append(current_tmp_serv)
                        
                        clientes.append({
                            'ides_v': str(cli.id),
                            'tipo_vinculacion_id' : cli.tipo_vinculacion_id.id,
                            'consumidor_id' : cli.consumidor_id.id,
                            'consumidor_codigo':current_tmp_serv,
                            'consumidor_medidor':cli.consumidor_id.medidor,
                            'consumidor_cant': 1,
                            'balance_energetico_id' : cli.balance_energetico_id.id,
                            'lectura_inicial' : cli.lectura,
                            'fecha_hora_inicial' : cli.fecha_hora,
                            'voltaje' : cli.voltaje,
                            'carga_l1' : cli.carga_l1,
                            'carga_l2' : cli.carga_l2,
                            'horas_uso' : cli.horas_uso,
                            'potencia_id' : cli.potencia_id.id,
                            #'fotos' : [(6, 0, fotos_ids)],
                            'observacion' : 'INICIAL: '+str(cli.observacion),
                            'tipo_consumidor' : cli.consumidor_id.tipo_consumidor_id.id,
                        })
                        
                        tmpFotBal.append(fotos_ids)
                        # print (cli.id, tmpFotBal)
                        
                    else:
                        cli_id = tmpCliBal.index(current_tmp_serv)
                        
                        tmpFotBal[cli_id] = tmpFotBal[cli_id] + fotos_ids
                        
                        
                        clientes[cli_id]['ides_v']=clientes[cli_id]['ides_v']+" ;"+ str(cli.id)
                        clientes[cli_id]['consumidor_cant']+=1
                        clientes[cli_id]['lectura_final'] = cli.lectura
                        clientes[cli_id]['fecha_hora_final'] = cli.fecha_hora
                        clientes[cli_id]['consumo'] = cli.lectura - clientes[cli_id]['lectura_inicial']
        
                        clientes[cli_id]['fotos'] = [(6, 0, tmpFotBal[cli_id])]
                        
                        clientes[cli_id]['observacion'] +=('- POSTERIOR: '+str(cli.observacion))

                    
                # for c in clientes:
                #     obj_tmp = self.env['vinculacion.medido'].create(c)
                #     medido_ids.append((4, obj_tmp.id))
                    
                medido_ids = [(self.env['vinculacion.medido'].create(c)).id for c in clientes]
                
                balance.consumidores_clientes = medido_ids
                try:
                    balance.consumo_clientes = sum(c['consumo'] for c in clientes)
                except Exception as e:
                    balance.consumo_clientes=0
                    print("Error al calcular Consumo de Clientes",e)
                
                
            else:
                balance.consumidores_clientes = None
                balance.consumo_clientes = None
        
        
    #####################################################################################################################################################  

    @api.depends('detalle_vinculaciones')
    def _compute_o2m_field_tot(self):
        
        #print ('_compute_o2m_field_cli',self)
        
        for balance in self:
            
            try:
                fechas=[]
                
                related_recordset = self.env["vinculacion"].search([("consumidor_id.tipo_consumidor_id.id", "=","10"), ("balance_energetico_id.id","=",str(balance.id))], order='fecha_hora asc')
                
                #fechas del balance
                fechas = list(set([cli.fecha_hora.date() for cli in related_recordset]))
                
                print("+++++++++++++++++++++++++")
                print ('FECHAS_TOT', fechas)
                print("+++++++++++++++++++++++++")
            except Exception as err:
                print (err)
                related_recordset=[]
                fechas = []
            
            if len(related_recordset) > 0 and len(fechas) == 2:
            
                clientes=[]
                tmpCliBal = []
                tmpFotBal = []
                medido_ids = []
                
                for cli in related_recordset:
                    
                    #ids de fotos
                    fotos_ids = [f.id for f in cli.fotos]
                    
                    
                    #Clientes del Balance
                    current_tmp_serv = cli.consumidor_id.codigo
                    if not (current_tmp_serv in tmpCliBal):
                    
                        tmpCliBal.append(current_tmp_serv)
                        
                        clientes.append({
                            'ides_v': str(cli.id),
                            'tipo_vinculacion_id' : cli.tipo_vinculacion_id.id,
                            'consumidor_id' : cli.consumidor_id.id,
                            'consumidor_codigo':current_tmp_serv,
                            'consumidor_medidor':cli.consumidor_id.medidor,
                            'consumidor_cant': 1,
                            'balance_energetico_id' : cli.balance_energetico_id.id,
                            'lectura_inicial' : cli.lectura,
                            'fecha_hora_inicial' : cli.fecha_hora,
                            'voltaje' : cli.voltaje,
                            'carga_l1' : cli.carga_l1,
                            'carga_l2' : cli.carga_l2,
                            'horas_uso' : cli.horas_uso,
                            'potencia_id' : cli.potencia_id.id,
                            #'fotos' : [(6, 0, fotos_ids)],
                            'observacion' : 'INICIAL: '+str(cli.observacion),
                            'tipo_consumidor' : cli.consumidor_id.tipo_consumidor_id.id,
                        })
                        
                        tmpFotBal.append(fotos_ids)
                        # print (cli.id, tmpFotBal)
                        
                    else:
                        cli_id = tmpCliBal.index(current_tmp_serv)
                        
                        tmpFotBal[cli_id] = tmpFotBal[cli_id] + fotos_ids
                        
                        clientes[cli_id]['ides_v']=clientes[cli_id]['ides_v']+" ;"+ str(cli.id)
                        clientes[cli_id]['consumidor_cant']+=1
                        clientes[cli_id]['lectura_final'] = cli.lectura
                        clientes[cli_id]['fecha_hora_final'] = cli.fecha_hora
                        clientes[cli_id]['consumo'] = cli.lectura - clientes[cli_id]['lectura_inicial']
        
                        clientes[cli_id]['fotos'] = [(6, 0, tmpFotBal[cli_id])]
                        
                        clientes[cli_id]['observacion'] +=('- POSTERIOR: '+str(cli.observacion))

                    
                # for c in clientes:
                #     obj_tmp = self.env['vinculacion.medido'].create(c)
                #     medido_ids.append((4, obj_tmp.id))
                    
                medido_ids = [(self.env['vinculacion.medido'].create(c)).id for c in clientes]
                    
               
                
                balance.consumidores_totaliza = medido_ids
                try:
                    balance.consumo_totalizador = sum(c['consumo'] for c in clientes)    
                except Exception as e:
                    balance.consumo_totalizador=0
                    print("Error al calcular Consumo de Totalizadores",e)
            else:
                balance.consumidores_totaliza = None
                balance.consumo_totalizador = None






###############################################################################################
        
    @api.depends('detalle_vinculaciones')
    def _compute_o2m_field_no_med_l_ini(self):
        
        #print ('_compute_o2m_field_no_med', self)
        
        
        for balance in self:
            
            try:
                related_recordset = self.env["vinculacion"].search([("consumidor_id.tipo_consumidor_id.id", "=","5"), ("balance_energetico_id.id","=",str(self.id))])
                
                #fechas del balance
                fechas = list(set([cli.fecha_hora.date() for cli in related_recordset]))
                
                print("+++++++++++++++++++++++++")
                print ('FECHAS_LUM', fechas)
                print("+++++++++++++++++++++++++")
            except Exception as err:
                print (err)
                related_recordset=[]
                fechas = []
            
            if len(related_recordset) > 0 and len(fechas) == 2:
            
                luminarias = []
                luminarias2 = []
                    
                dias = 1
                if (fechas[0] > fechas[1]):
                    dias = fechas[0]-fechas[1]
                    balance.fecha_inicial=fechas[1]
                    balance.fecha_final=fechas[0]
                else:
                    dias = fechas[1]-fechas[0]
                    balance.fecha_inicial=fechas[0]
                    balance.fecha_final=fechas[1]
                    
                dias = dias.days    
                
                    
                for cli in related_recordset:
                    
                    #ids de fotos
                    fotos_ids = [f.id for f in cli.fotos]
                    
                    
                    #Luminarias del Balance
                    
                    if cli.fecha_hora.date() == fechas[0]:
                        
                        luminarias.append({
                            'ides_v': str(cli.id),
                            'tipo_vinculacion_id' : cli.tipo_vinculacion_id.id,
                            'consumidor_id' : cli.consumidor_id.id,

                            'balance_energetico_id' : cli.balance_energetico_id.id,
                            'fecha_hora' : cli.fecha_hora,
                            
                            'voltaje' : cli.voltaje,
                            'carga_l1' : cli.carga_l1,
                            'carga_l2' : cli.carga_l2,
                            'horas_uso' : cli.horas_uso,
                            'potencia_id' : cli.potencia_id.id,
                            'fotos' : [(6, 0, fotos_ids)],
                            'observacion' : cli.observacion,
                            'tipo_consumidor' : cli.consumidor_id.tipo_consumidor_id.id,
                            'consumo' : ((((cli.potencia_id.nombre) / 1000) * cli.horas_uso) * dias),
                        })
                        
                    elif cli.fecha_hora.date() == fechas[1]:
                        
                        luminarias2.append({
                            'ides_v': str(cli.id),
                            'tipo_vinculacion_id' : cli.tipo_vinculacion_id.id,
                            'consumidor_id' : cli.consumidor_id.id,

                            'balance_energetico_id' : cli.balance_energetico_id.id,
                            'fecha_hora' : cli.fecha_hora,
                            
                            'voltaje' : cli.voltaje,
                            'carga_l1' : cli.carga_l1,
                            'carga_l2' : cli.carga_l2,
                            'horas_uso' : cli.horas_uso,
                            'potencia_id' : cli.potencia_id.id,
                            'fotos' : [(6, 0, fotos_ids)],
                            'observacion' : cli.observacion,
                            'tipo_consumidor' : cli.consumidor_id.tipo_consumidor_id.id,
                            'consumo' : ((((cli.potencia_id.nombre) / 1000) * cli.horas_uso) * dias),
                        })
                        
                    
                no_medido_ids = [(self.env['vinculacion.no.medido'].create(c)).id for c in luminarias]
                
                no_medido2_ids = [(self.env['vinculacion.no.medido'].create(c)).id for c in luminarias2]    
                
                balance.consumidores_no_medidos_lum_ini = no_medido_ids
                ini = sum(c['consumo'] for c in luminarias)
                
                balance.consumidores_no_medidos_lum_fin = no_medido2_ids
                fin = sum(c['consumo'] for c in luminarias2)
                
                balance.consumo_luminarias = max([ini, fin])
            
            else:
                balance.consumidores_no_medidos_lum_ini = None                
                balance.consumidores_no_medidos_lum_fin = None
                balance.consumo_luminarias = 0
            
            
    ###############################################################################################
        
    @api.depends('detalle_vinculaciones')
    def _compute_o2m_field_no_med_s_ini(self):
        
        #print ('_compute_o2m_field_no_med', self)
        
        
        for balance in self:
            
            try:
                related_recordset = self.env["vinculacion"].search([("consumidor_id.tipo_consumidor_id.id", "in", [6,7,8]), ("balance_energetico_id.id","=",str(self.id))])
                
                #fechas del balance    
                fechas = list(set([cli.fecha_hora.date() for cli in related_recordset]))
                
                print("+++++++++++++++++++++++++")
                print ('FECHAS_SEM', fechas)
                print("+++++++++++++++++++++++++")
            except Exception as err:
                print (err)
                related_recordset=[]
                fechas = []
            
            if len(related_recordset) > 0 and len(fechas) == 2:
            
                semaforos = []
                semaforos2 = []
                    
                dias = 1
                if (fechas[0] > fechas[1]):
                    dias = fechas[0]-fechas[1]

                else:
                    dias = fechas[1]-fechas[0]
                    
                dias = dias.days    
                
                    
                for cli in related_recordset:
                    
                    #ids de fotos
                    fotos_ids = [f.id for f in cli.fotos]
                    
                    current_consumo=0
                    if cli.potencia_id.nombre:
                        current_consumo = ((((cli.potencia_id.nombre) / 1000) * cli.horas_uso) * dias)
                    if current_consumo==0:
                        p1 = cli.carga_l1*120
                        p2 = cli.carga_l2*120
                        current_consumo = ((((p1+p2) / 1000) * cli.horas_uso) * dias)
                        
                    
                    if cli.fecha_hora.date() == fechas[0]:
                        
                        semaforos.append({
                            'ides_v': str(cli.id),
                            'tipo_vinculacion_id' : cli.tipo_vinculacion_id.id,
                            'consumidor_id' : cli.consumidor_id.id,

                            'balance_energetico_id' : cli.balance_energetico_id.id,
                            'fecha_hora' : cli.fecha_hora,
                            
                            'voltaje' : cli.voltaje,
                            'carga_l1' : cli.carga_l1,
                            'carga_l2' : cli.carga_l2,
                            'horas_uso' : cli.horas_uso,
                            'potencia_id' : cli.potencia_id.id,
                            'fotos' : [(6, 0, fotos_ids)],
                            'observacion' : cli.observacion,
                            'tipo_consumidor' : cli.consumidor_id.tipo_consumidor_id.id,
                            'consumo' : current_consumo,
                        })
                        
                    elif cli.fecha_hora.date() == fechas[1]:
                        
                        semaforos2.append({
                            'ides_v': str(cli.id),
                            'tipo_vinculacion_id' : cli.tipo_vinculacion_id.id,
                            'consumidor_id' : cli.consumidor_id.id,

                            'balance_energetico_id' : cli.balance_energetico_id.id,
                            'fecha_hora' : cli.fecha_hora,
                            
                            'voltaje' : cli.voltaje,
                            'carga_l1' : cli.carga_l1,
                            'carga_l2' : cli.carga_l2,
                            'horas_uso' : cli.horas_uso,
                            'potencia_id' : cli.potencia_id.id,
                            'fotos' : [(6, 0, fotos_ids)],
                            'observacion' : cli.observacion,
                            'tipo_consumidor' : cli.consumidor_id.tipo_consumidor_id.id,
                            'consumo' : current_consumo,
                        })
                        
                    
                no_medido_ids = [(self.env['vinculacion.no.medido'].create(c)).id for c in semaforos]
                
                no_medido2_ids = [(self.env['vinculacion.no.medido'].create(c)).id for c in semaforos2]    
                
                
                balance.consumidores_no_medidos_sem_ini = no_medido_ids
                ini = sum(c['consumo'] for c in semaforos)
                
                balance.consumidores_no_medidos_sem_fin = no_medido2_ids
                fin = sum(c['consumo'] for c in semaforos2)
                
                balance.consumo_semaforos = max([ini, fin])
            else:
                
                balance.consumidores_no_medidos_sem_ini = None
                balance.consumidores_no_medidos_sem_fin = None
                
                balance.consumo_semaforos = 0
            
            
        
    
    ###############################################################################################
        
    @api.depends('detalle_vinculaciones')
    def _compute_o2m_field_no_med_c_ini(self):
        
        print ('_compute_o2m_field_no_med', self)
        
        
        for balance in self:
            
            try:
                related_recordset = self.env["vinculacion"].search([("consumidor_id.tipo_consumidor_id.id", "=","9"), ("balance_energetico_id.id","=",str(self.id))])
                
                #fechas del balance
                fechas = list(set([cli.fecha_hora.date() for cli in related_recordset]))
                
                print("+++++++++++++++++++++++++")
                print ('FECHAS_CAM', fechas)
                print("+++++++++++++++++++++++++")
            except Exception as err:
                print (err)
                related_recordset=[]
                fechas = []
            
            if len(related_recordset) > 0 and len(fechas) == 2:
            
                camaras = []
                camaras2 = []
                    
                dias = 1
                if (fechas[0] > fechas[1]):
                    dias = fechas[0]-fechas[1]

                else:
                    dias = fechas[1]-fechas[0]
                    
                dias = dias.days    
                
                    
                for cli in related_recordset:
                    
                    #ids de fotos
                    fotos_ids = [f.id for f in cli.fotos]
                    
                    
                    current_consumo=0
                    if cli.potencia_id.nombre:
                        current_consumo = ((((cli.potencia_id.nombre) / 1000) * cli.horas_uso) * dias)
                    if current_consumo==0:
                        p1 = cli.carga_l1*120
                        p2 = cli.carga_l2*120
                        current_consumo = ((((p1+p2) / 1000) * cli.horas_uso) * dias)
                        
                    
                    if cli.fecha_hora.date() == fechas[0]:
                        
                        camaras.append({
                            'ides_v': str(cli.id),
                            'tipo_vinculacion_id' : cli.tipo_vinculacion_id.id,
                            'consumidor_id' : cli.consumidor_id.id,

                            'balance_energetico_id' : cli.balance_energetico_id.id,
                            'fecha_hora' : cli.fecha_hora,
                            
                            'voltaje' : cli.voltaje,
                            'carga_l1' : cli.carga_l1,
                            'carga_l2' : cli.carga_l2,
                            'horas_uso' : cli.horas_uso,
                            'potencia_id' : cli.potencia_id.id,
                            'fotos' : [(6, 0, fotos_ids)],
                            'observacion' : cli.observacion,
                            'tipo_consumidor' : cli.consumidor_id.tipo_consumidor_id.id,
                            'consumo' : current_consumo,
                        })
                        
                    elif cli.fecha_hora.date() == fechas[1]:
                        
                        camaras2.append({
                            'ides_v': str(cli.id),
                            'tipo_vinculacion_id' : cli.tipo_vinculacion_id.id,
                            'consumidor_id' : cli.consumidor_id.id,

                            'balance_energetico_id' : cli.balance_energetico_id.id,
                            'fecha_hora' : cli.fecha_hora,
                            
                            'voltaje' : cli.voltaje,
                            'carga_l1' : cli.carga_l1,
                            'carga_l2' : cli.carga_l2,
                            'horas_uso' : cli.horas_uso,
                            'potencia_id' : cli.potencia_id.id,
                            'fotos' : [(6, 0, fotos_ids)],
                            'observacion' : cli.observacion,
                            'tipo_consumidor' : cli.consumidor_id.tipo_consumidor_id.id,
                            'consumo' : current_consumo,
                        })
                        
                    
                no_medido_ids = [(self.env['vinculacion.no.medido'].create(c)).id for c in camaras]
                
                no_medido2_ids = [(self.env['vinculacion.no.medido'].create(c)).id for c in camaras2]    
                
                balance.consumidores_no_medidos_cam_ini = no_medido_ids
                ini = sum(c['consumo'] for c in camaras)
                
                balance.consumidores_no_medidos_cam_fin = no_medido2_ids
                fin = sum(c['consumo'] for c in camaras2)
                
                balance.consumo_camaras = max([ini, fin])
            else:
                
                balance.consumidores_no_medidos_cam_ini = None
                balance.consumidores_no_medidos_cam_fin = None
                
                balance.consumo_camaras = 0
        
        
        ###############################################################################################
        
    @api.depends('detalle_vinculaciones')
    def _compute_o2m_field_no_med_o_ini(self):
        
        
        for balance in self:
            
            try:
                related_recordset = self.env["vinculacion"].search([("consumidor_id.tipo_consumidor_id.id", "=","11"), ("balance_energetico_id.id","=",str(self.id))])
                
                #fechas del balance
                fechas = list(set([cli.fecha_hora.date() for cli in related_recordset]))
                
                print("+++++++++++++++++++++++++")
                print ('FECHAS_OTR', fechas)
                print("+++++++++++++++++++++++++")
            except Exception as err:
                print (err)
                related_recordset=[]
                fechas = []
            
            if len(related_recordset) > 0 and len(fechas) == 2:
                
            
                otros = []
                otros2 = []
                    
                dias = 1
                if (fechas[0] > fechas[1]):
                    dias = fechas[0]-fechas[1]

                else:
                    dias = fechas[1]-fechas[0]
                    
                dias = dias.days    
                
                    
                for cli in related_recordset:
                    
                    #ids de fotos
                    fotos_ids = [f.id for f in cli.fotos]
                    
                    current_consumo=0
                    if cli.potencia_id.nombre:
                        current_consumo = ((((cli.potencia_id.nombre) / 1000) * cli.horas_uso) * dias)
                    if current_consumo==0:
                        p1 = cli.carga_l1*120
                        p2 = cli.carga_l2*120
                        current_consumo = ((((p1+p2) / 1000) * cli.horas_uso) * dias)
                        
                    
                    if cli.fecha_hora.date() == fechas[0]:
                        
                        otros.append({
                            'ides_v': str(cli.id),
                            'tipo_vinculacion_id' : cli.tipo_vinculacion_id.id,
                            'consumidor_id' : cli.consumidor_id.id,

                            'balance_energetico_id' : cli.balance_energetico_id.id,
                            'fecha_hora' : cli.fecha_hora,
                            
                            'voltaje' : cli.voltaje,
                            'carga_l1' : cli.carga_l1,
                            'carga_l2' : cli.carga_l2,
                            'horas_uso' : cli.horas_uso,
                            'potencia_id' : cli.potencia_id.id,
                            'fotos' : [(6, 0, fotos_ids)],
                            'observacion' : cli.observacion,
                            'tipo_consumidor' : cli.consumidor_id.tipo_consumidor_id.id,
                            'consumo' : current_consumo,
                        })
                        
                    elif cli.fecha_hora.date() == fechas[1]:
                        
                        otros2.append({
                            'ides_v': str(cli.id),
                            'tipo_vinculacion_id' : cli.tipo_vinculacion_id.id,
                            'consumidor_id' : cli.consumidor_id.id,

                            'balance_energetico_id' : cli.balance_energetico_id.id,
                            'fecha_hora' : cli.fecha_hora,
                            
                            'voltaje' : cli.voltaje,
                            'carga_l1' : cli.carga_l1,
                            'carga_l2' : cli.carga_l2,
                            'horas_uso' : cli.horas_uso,
                            'potencia_id' : cli.potencia_id.id,
                            'fotos' : [(6, 0, fotos_ids)],
                            'observacion' : cli.observacion,
                            'tipo_consumidor' : cli.consumidor_id.tipo_consumidor_id.id,
                            'consumo' : current_consumo,
                        })
                        
                    
                no_medido_ids = [(self.env['vinculacion.no.medido'].create(c)).id for c in otros]
                
                no_medido2_ids = [(self.env['vinculacion.no.medido'].create(c)).id for c in otros2]    
                
                
                balance.consumidores_no_medidos_otr_ini = no_medido_ids
                ini = sum(c['consumo'] for c in otros)
                
                balance.consumidores_no_medidos_otr_fin = no_medido2_ids
                fin = sum(c['consumo'] for c in otros2)
                
                balance.consumo_otros = max([ini, fin])
        
            else:
                
                balance.consumidores_no_medidos_otr_ini = None
                balance.consumidores_no_medidos_otr_fin = None
                
                balance.consumo_otros = 0
                
                

##############################################################################################################################
    
    # red_id_trafo_id = fields.Integer(compute="_red_id_trafo_id")
    # red_id_sector = fields.Char(compute="_red_id_sector")
    # red_id_id = fields.Integer(compute="_red_id_id")
    # red_id_trafo_codigo = fields.Char(compute="_red_id_trafo_codigo")
    # red_id_trafo_capacidad = fields.Char(compute="_red_id_trafo_capacidad")
    # red_id_trafo_x = fields.Float(compute="_red_id_trafo_x")
    # red_id_trafo_y = fields.Float(compute="_red_id_trafo_y")

    
    @api.depends('red_id')
    def _red_id_trafo_id(self):
        for record in self:
            record.red_id_trafo_id = record.red_id.transformador_id.id
    
    @api.depends('red_id')
    def _red_id_sector(self):
        for record in self:
            record.red_id_sector = str(record.red_id.canton_id.nombre) + " / " +str(record.red_id.provincia_id.nombre)
    
    @api.depends('red_id')
    def _red_id_id(self):
        for record in self:
            record.red_id_id = record.red_id.id
            
    @api.depends('red_id')
    def _red_id_trafo_codigo(self):
        for record in self:
            record.red_id_trafo_codigo = record.red_id.transformador_id.codigo
   
    @api.depends('red_id')
    def _red_id_trafo_capacidad(self):
        for record in self:
            record.red_id_trafo_capacidad = record.red_id.transformador_id.potencia
    
    @api.depends('red_id')
    def _red_id_trafo_x(self):
        for record in self:
            record.red_id_trafo_x = record.red_id.transformador_id.coord.coord_x
            
    @api.depends('red_id')
    def _red_id_trafo_y(self):
        for record in self:
            record.red_id_trafo_y = record.red_id.transformador_id.coord.coord_y
    
###############################################################################################################

# consumo_consumidores = fields.Float("Consumo Consumidores")
# consumo_luminarias = fields.Float("Consumo Luminarias", default=0)
# consumo_semaforos = fields.Float("Consumo Semáforos", default=0)
# consumo_camaras = fields.Float("Consumo Cámaras", default=0)
# consumo_otros = fields.Float("Consumo Otros", default=0)
# consumo_clientes = fields.Float("Consumo Clientes", default=0)


            
###############################################################################################################
    # perdidas_comerciales_dias = fields.Integer(compute="_perdidas_comerciales_dias", string="Pérdidas Comerciales")
    # perdidas_comerciales_dias_costo = fields.Integer(compute="_perdidas_comerciales_dias_costo", string="Pérdidas Comerciales Dias Costo")
    # perdidas_comerciales_mes = fields.Integer(compute="_perdidas_comerciales_mes", string="Pérdidas Comerciales Mes")
    # perdidas_comerciales_mes_costo = fields.Integer(compute="_perdidas_comerciales_mes_costo", string="Pérdidas Comerciales Mes Costo")
    # perdidas_comerciales_porcentaje = fields.Integer(compute="_perdidas_comerciales_porcentaje", string="Pérdidas Comerciales Porcentaje")
    
    # energia_entregada_dias = fields.Integer(compute="_energia_entregada_dias", string="Energía Entregada")
    # energia_entregada_dias_costo = fields.Integer(compute="_energia_entregada_dias_costo", string="Energia Entregada Dias Costo")
    # energia_entregada_mes = fields.Integer(compute="_energia_entregada_mes", string="Energía Entregada Mes")
    # energia_entregada_mes_costo = fields.Integer(compute="_energia_entregada_mes_costo", string="Energía Entregada Mes Costo")
    # energia_entregada_porcentaje = fields.Integer(compute="_energia_entregada_porcentaje", string="Energía Entregada Porcentaje")
    
    # energia_registrada_dias = fields.Integer(compute="_energia_registrada_dias", string="Energía Registrada")
    # energia_registrada_dias_costo = fields.Integer(compute="_energia_registrada_dias_costo", string="Energía Registrada Días Costo")
    # energia_registrada_mes = fields.Integer(compute="_energia_registrada_mes", string="Energía Registrada Mes")
    # energia_registrada_mes_costo = fields.Integer(compute="_energia_registrada_mes_costo", string="Energía Registrada Mes Costo")
    # energia_registrada_porcentaje = fields.Integer(compute="_energia_registrada_porcentaje", string="Energía Registrada Porcentaje")

    @api.depends('consumo_totalizador', 'consumo_clientes', 'consumo_luminarias', 'consumo_semaforos', 'consumo_camaras', 'consumo_otros')
    def _perdidas_comerciales_dias(self):
        for record in self:
            consum = sum([record.consumo_clientes, record.consumo_luminarias, record.consumo_semaforos, record.consumo_camaras, record.consumo_otros])
            dife = record.consumo_totalizador - consum
            if dife >0:
                record.consumo_diferencia = dife
                record.perdidas_comerciales_dias = dife
            else:
                record.consumo_diferencia = 0
                record.perdidas_comerciales_dias = 0
                
            record.consumo_consumidores = consum
            
    @api.depends('perdidas_comerciales_dias', 'costo_kwh')
    def _perdidas_comerciales_dias_costo(self):
        for record in self:
            record.perdidas_comerciales_dias_costo = record.perdidas_comerciales_dias * record.costo_kwh
            
    @api.depends('fecha_inicial', 'fecha_final', 'perdidas_comerciales_dias')
    def _perdidas_comerciales_mes(self):
        for record in self:
            try:
                dias = (record.fecha_final - record.fecha_inicial).days
                kwh_dia = (record.perdidas_comerciales_dias / dias)
            except:
                kwh_dia = 0
            record.perdidas_comerciales_mes = kwh_dia * 30
            
    @api.depends('perdidas_comerciales_mes', 'costo_kwh')
    def _perdidas_comerciales_mes_costo(self):
        for record in self:
            record.perdidas_comerciales_mes_costo = record.perdidas_comerciales_mes * record.costo_kwh
            
    @api.depends('perdidas_comerciales_dias', 'consumo_totalizador')
    def _perdidas_comerciales_porcentaje(self):
        for record in self:
            try:
                er =  (record.perdidas_comerciales_dias / record.consumo_totalizador)*100
            except:
                er = None
            record.perdidas_comerciales_porcentaje = er
            if er:
                er=er/100
            record.color = self.determinarColor(er)
            record.error = er
    
    
    
    @api.depends('consumo_totalizador')
    def _energia_entregada_dias(self):
        for record in self:     
            record.energia_entregada_dias=record.consumo_totalizador
            
    @api.depends('energia_entregada_dias', 'costo_kwh')
    def _energia_entregada_dias_costo(self):
        for record in self:     
            record.energia_entregada_dias_costo=record.costo_kwh * record.energia_entregada_dias
            
    @api.depends('fecha_inicial', 'fecha_final', 'energia_entregada_dias')
    def _energia_entregada_mes(self):
        for record in self:
            try:
                dias = (record.fecha_final - record.fecha_inicial).days
                kwh_dia = (record.energia_entregada_dias / dias)
            except:
                kwh_dia = 0
            record.energia_entregada_mes = kwh_dia * 30
            
    @api.depends('energia_entregada_mes', 'costo_kwh')
    def _energia_entregada_mes_costo(self):
        for record in self:
            record.energia_entregada_mes_costo = record.energia_entregada_mes * record.costo_kwh
            
    @api.depends('energia_entregada_dias', 'consumo_totalizador')
    def _energia_entregada_porcentaje(self):
        for record in self:
            try:
                record.energia_entregada_porcentaje = (record.energia_entregada_dias / record.consumo_totalizador)*100
            except:
                record.energia_entregada_porcentaje = None
            
            
    
    @api.depends('consumo_consumidores')
    def _energia_registrada_dias(self):
        for record in self:
            record.energia_registrada_dias = record.consumo_consumidores
            
    @api.depends('energia_registrada_dias', 'costo_kwh')
    def _energia_registrada_dias_costo(self):
        for record in self:
            record.energia_registrada_dias_costo=record.costo_kwh * record.energia_registrada_dias
            
    @api.depends('fecha_inicial', 'fecha_final', 'energia_registrada_dias')
    def _energia_registrada_mes(self):
        for record in self:
            try:
                dias = (record.fecha_final - record.fecha_inicial).days
                kwh_dia = (record.energia_registrada_dias / dias)
            except:
                kwh_dia = 0
            record.energia_registrada_mes = kwh_dia * 30
            
    @api.depends('energia_registrada_mes', 'costo_kwh')
    def _energia_registrada_mes_costo(self):
        for record in self:
            record.energia_registrada_mes_costo = record.energia_registrada_mes * record.costo_kwh
            
    @api.depends('energia_registrada_dias', 'energia_entregada_dias')
    def _energia_registrada_porcentaje(self):
        for record in self:
            try:
                ef = (record.energia_registrada_dias / record.energia_entregada_dias)*100
            except:
                ef = None
            record.energia_registrada_porcentaje = ef
            if ef:
                ef=ef/100
            record.color = self.determinarColor(None,ef)
            record.eficacia = ef
            
    def determinarColor(self, er = None, ef= None):
        color = 'green'
        if er:
            if er>0.30:
                color = 'red'
            elif er>0.20:
                color = 'yellow'     
        elif ef:
            if ef<0.70:
                color = 'red'
            elif ef<0.80:
                color = 'yellow'
        print('color', color)
        return color
    
    @api.depends('eficacia', 'error')
    def _color(self):
        for record in self:
            record.color = self.determinarColor(record.error)
            

##########################################################################################################


    @api.depends('consumidores_clientes')
    def _cant_clientes(self):
        for record in self:
            record.cant_clientes = len(record.consumidores_clientes)
    
    @api.depends('consumo_clientes', 'costo_kwh')
    def _costo_clientes(self):
        for record in self:
            record.costo_clientes = record.consumo_clientes * record.costo_kwh
            
    @api.depends('consumo_clientes', 'consumo_consumidores')
    def _porce_clientes(self):
        for record in self:
            record.porce_clientes = (record.consumo_clientes / (record.consumo_consumidores if record.consumo_consumidores>0 else 1)) * 100

    @api.depends('consumo_clientes', 'consumo_consumidores')
    def _porce2_clientes(self):
        for record in self:
            record.porce2_clientes = (record.consumo_clientes / (record.consumo_consumidores if record.consumo_consumidores>0 else 1))

            
            
            
    @api.depends('consumidores_no_medidos_lum_ini', 'consumidores_no_medidos_lum_fin')
    def _cant_luminarias(self):
        for record in self:
            record.cant_luminarias = max([len(record.consumidores_no_medidos_lum_ini), len(record.consumidores_no_medidos_lum_fin)])
    
    @api.depends('consumo_luminarias', 'costo_kwh')
    def _costo_luminarias(self):
        for record in self:
            record.costo_luminarias = record.consumo_luminarias * record.costo_kwh
            
    @api.depends('consumo_luminarias', 'consumo_consumidores')
    def _porce_luminarias(self):
        for record in self:
            
            record.porce_luminarias = (record.consumo_luminarias / (record.consumo_consumidores if record.consumo_consumidores>0 else 1)) * 100
        
    @api.depends('consumo_luminarias', 'consumo_consumidores')
    def _porce2_luminarias(self):
        for record in self:
            record.porce2_luminarias = (record.consumo_luminarias / (record.consumo_consumidores if record.consumo_consumidores>0 else 1))

    
    
    
    @api.depends('consumidores_no_medidos_sem_ini', 'consumidores_no_medidos_sem_fin')
    def _cant_semaforos(self):
        for record in self:
            record.cant_semaforos = max([len(record.consumidores_no_medidos_sem_ini), len(record.consumidores_no_medidos_sem_fin)])
    
    @api.depends('consumo_semaforos', 'costo_kwh')
    def _costo_semaforos(self):
        for record in self:
            record.costo_semaforos = record.consumo_semaforos * record.costo_kwh
            
    @api.depends('consumo_semaforos', 'consumo_consumidores')
    def _porce_semaforos(self):
        for record in self:
            record.porce_semaforos = (record.consumo_semaforos / (record.consumo_consumidores if record.consumo_consumidores>0 else 1)) * 100
        
    @api.depends('consumo_semaforos', 'consumo_consumidores')
    def _porce2_semaforos(self):
        for record in self:
            record.porce2_semaforos = (record.consumo_semaforos / (record.consumo_consumidores if record.consumo_consumidores>0 else 1))
            


    @api.depends('consumidores_no_medidos_cam_ini', 'consumidores_no_medidos_cam_fin')
    def _cant_camaras(self):
        for record in self:
            record.cant_camaras = max([len(record.consumidores_no_medidos_cam_ini), len(record.consumidores_no_medidos_cam_fin)])
    
    @api.depends('consumo_camaras', 'costo_kwh')
    def _costo_camaras(self):
        for record in self:
            record.costo_camaras = record.consumo_camaras * record.costo_kwh
            
    @api.depends('consumo_camaras', 'consumo_consumidores')
    def _porce_camaras(self):
        for record in self:
            record.porce_camaras = (record.consumo_camaras / (record.consumo_consumidores if record.consumo_consumidores>0 else 1)) * 100
            
    @api.depends('consumo_camaras', 'consumo_consumidores')
    def _porce2_camaras(self):
        for record in self:
            record.porce2_camaras = (record.consumo_camaras / (record.consumo_consumidores if record.consumo_consumidores>0 else 1))
            
            
            
    @api.depends('consumidores_no_medidos_otr_ini', 'consumidores_no_medidos_otr_fin')
    def _cant_otros(self):
        for record in self:
            record.cant_otros = max([len(record.consumidores_no_medidos_otr_ini), len(record.consumidores_no_medidos_otr_fin)])
    
    @api.depends('consumo_otros', 'costo_kwh')
    def _costo_otros(self):
        for record in self:
            record.costo_otros = record.consumo_otros * record.costo_kwh
            
    @api.depends('consumo_otros', 'consumo_consumidores')
    def _porce_otros(self):
        for record in self:
            record.porce_otros = (record.consumo_otros / (record.consumo_consumidores if record.consumo_consumidores>0 else 1)) * 100
            
    @api.depends('consumo_otros', 'consumo_consumidores')
    def _porce2_otros(self):
        for record in self:
            record.porce2_otros = (record.consumo_otros / (record.consumo_consumidores if record.consumo_consumidores>0 else 1))
    
    

    @api.depends('cant_clientes', 'cant_luminarias', 'cant_semaforos', 'cant_camaras', 'cant_otros')
    def _cant_consumidores(self):
        for record in self:
            record.cant_consumidores = sum([record.cant_clientes, record.cant_luminarias, record.cant_semaforos, record.cant_camaras, record.cant_otros])
    
    @api.depends('consumo_consumidores', 'costo_kwh')
    def _costo_consumidores(self):
        for record in self:
            record.costo_consumidores = record.consumo_consumidores * record.costo_kwh
            
    @api.depends('consumo_consumidores')
    def _porce_consumidores(self):
        for record in self:
            record.porce_consumidores = 100
            
    @api.depends('consumo_consumidores')
    def _porce2_consumidores(self):
        for record in self:
            record.porce2_consumidores = 1
            
    
    def chart_img_general(self):                                                                                              
                                                                                           
        data = {                                                                               
            'type': 'doughnut',                                                                     
            'data': {                                                                          
                'labels': [
                    'Eficacia ('+str(round(self.eficacia*100,2))+'%25)', 
                    'Error ('+str(round(self.error*100,2))+'%25)'
                    ],                                                              
                'datasets': [                                                                  
                    {                                                                          
                        'label': "%25",
                        'data': [round(self.eficacia*100,2), round(self.error*100,2)],
                        'backgroundColor': [
                            'rgba(82, 190, 128, 1)',
                            'rgba(250, 219, 216, 1)'
                        ],
                        'borderWidth': 1                                                   
                    },
                ]
            },
            'options': {
                'title': {
                    'display': True,
                    'text': 'Analisis de Consumos Generales de Red en Porcentajes'
                }
            }                                                                                    
        }                 
        print(f"https://quickchart.io/chart?c={json.dumps(data)}")                                                                     
        return f"https://quickchart.io/chart?c={json.dumps(data)}"
    
    def chart_img_general2(self):                                                                                              
                                                                                           
        data = {                                                                               
            'type': 'doughnut',                                                                     
            'data': {                                                                          
                'labels': [
                    'Energía Registrada ('+str(round(self.energia_registrada_dias,2))+'Kw)', 
                    'Perdidas ('+str(round(self.perdidas_comerciales_dias,2))+'Kw)'
                    ],                                                              
                'datasets': [                                                                  
                    {                                                                          
                        'label': "Kw",
                        'data': [round(self.energia_registrada_dias,2), round(self.perdidas_comerciales_dias,2)],
                        'backgroundColor': [
                            'rgba(82, 190, 128, 1)',
                            'rgba(250, 219, 216, 1)'
                        ],
                        'borderWidth': 1                                                   
                    },
                ]
            },
            'options': {
                'title': {
                    'display': True,
                    'text': 'Analisis de Consumos Generales de Red en Kw'
                }
            }                                                                                    
        }                 
        print(f"https://quickchart.io/chart?c={json.dumps(data)}")                                                   
        return f"https://quickchart.io/chart?c={json.dumps(data)}"
    
    def chart_img_especifico(self):                                                                                              
                                                                                           
        data = {                                                                               
            'type': 'doughnut',                                                                     
            'data': {                                                                          
                'labels': [
                    'Clientes ('+str(round(self.consumo_clientes,2))+'Kw)', 
                    'Luminarias ('+str(round(self.consumo_luminarias,2))+'Kw)', 
                    'Semáforos ('+str(round(self.consumo_semaforos,2))+'Kw)', 
                    'Cámaras ('+str(round(self.consumo_camaras,2))+'Kw)', 
                    'Servicios Convenidos ('+str(round(self.consumo_otros,2))+'Kw)', 
                    'Perdida ('+str(round(self.perdidas_comerciales_dias,2))+'Kw)'
                    ],                                                              
                'datasets': [                                                                  
                    {                                                                          
                        'label': "%25",
                        'data': [
                            round(self.consumo_clientes,2), 
                            round(self.consumo_luminarias,2),
                            round(self.consumo_semaforos,2),
                            round(self.consumo_camaras,2),
                            round(self.consumo_otros,2),
                            round(self.perdidas_comerciales_dias,2)
                            ],
                        'backgroundColor': [
                            'rgba(118, 215, 196, 1)',
                            'rgba(187, 143, 206, 1)',
                            'rgba(248, 196, 113, 1)',
                            'rgba(133, 193, 233, 1)',
                            'rgba(215, 219, 221, 1)',
                            'rgba(250, 219, 216, 1)'
                        ],
                        'borderWidth': 1                                                   
                    },
                ]
            },
            'options': {
                'title': {
                    'display': True,
                    'text': 'Analisis de Consumos Específicos de Red por Tipo de Consumidor'
                }
            }                                                                                    
        }                 
        print(f"https://quickchart.io/chart?c={json.dumps(data)}")                                                                              
        return f"https://quickchart.io/chart?c={json.dumps(data)}"
    
    
    def chart_img_especifico2(self):                                                                                              
                                                                                           
        data = {                                                                               
            'type': 'doughnut',                                                                     
            'data': {                                                                          
                'labels': [
                    'Clientes ('+str(self.cant_clientes)+')', 
                    'Luminarias ('+str(self.cant_luminarias)+')', 
                    'Semáforos ('+str(self.cant_semaforos)+')', 
                    'Cámaras ('+str(self.cant_camaras)+')', 
                    'Servicios Convenidos ('+str(self.cant_otros)+')'
                    ],                                                              
                'datasets': [                                                                  
                    {                                                                          
                        'label': "%25",
                        'data': [
                            self.cant_clientes, 
                            self.cant_luminarias,
                            self.cant_semaforos,
                            self.cant_camaras,
                            self.cant_otros,
                            ],
                        'backgroundColor': [
                            'rgba(118, 215, 196, 1)',
                            'rgba(187, 143, 206, 1)',
                            'rgba(248, 196, 113, 1)',
                            'rgba(133, 193, 233, 1)',
                            'rgba(215, 219, 221, 1)'
                        ],
                        'borderWidth': 1                                                   
                    },
                ]
            },
            'options': {
                'title': {
                    'display': True,
                    'text': 'Cantidades de Tipos de Consumidores en la Red'
                }
            }                                                                                    
        }                 
        print(f"https://quickchart.io/chart?c={json.dumps(data)}")                                                                              
        return f"https://quickchart.io/chart?c={json.dumps(data)}" 