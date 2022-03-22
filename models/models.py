# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class incidencias(models.Model):
#     _name = 'incidencias.incidencias'
#     _description = 'incidencias.incidencias'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


from odoo import models, fields, api
from datetime import date

class incidencia(models.Model):
    _name = 'incidencias.incidencia'
    _description = 'Define los atributos de una incidencia'
    
    motivoIncidencia = fields.Selection(string='Motivo de la incidencia', selection=[('a','Funcionamiento'),('b','Jugabilidad'),('c','Online'),('d','Multijugador')], required=True)
    descripcionIncidencia = fields.Text(string='descripcion de la incidencia', required=True, help='Escribe una descripcion detallada')
    fechaIncidencia = fields.Date(string='Fecha de la incidencia', required=True, default=fields.Date.today())

    #Relacion entre tablas
    cliente_id = fields.One2many('alquileres.cliente', 'cliente.incidencia_id')