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


from odoo import models, fields, api, exceptions
from datetime import date

class incidencia(models.Model):
    _name = 'incidencias.incidencia'
    _description = 'Define los atributos de una incidencia'
    
    motivoIncidencia = fields.Selection(string='Motivo de la incidencia', selection=[('a','Funcionamiento'),('b','Jugabilidad'),('c','Online'),('d','Multijugador')], required=True)
    descripcionIncidencia = fields.Text(string='descripcion de la incidencia', required=True, help='Escribe una descripcion detallada')
    fechaIncidencia = fields.Date(string='Fecha de la incidencia', required=True, default=fields.Date.today())

    #Relacion entre tablas
    devolucion_id = fields.Many2many('incidencias.devoluciones', 'incidencia_id')


class devoluciones(models.Model):
    _name = 'incidencias.devoluciones'
    _description = 'Define los atributos de una devolucion'
    
    motivoDevolucion = fields.Selection(string='Motivo de la devolucion', selection=[('a','Funcionamiento'),('b','Jugabilidad'),('c','Online'),('d','Multijugador')], required=True)
    prioridadDevolucion = fields.Selection(string='Prioridad de la devolucion', selection=[('a','Urgente'),('b','Media'),('c','Baja')])
    descripcionDevolucion = fields.Text(string='descripcion de la devolucion', required=True, help='Escribe una descripcion detallada')
    fechaDevolucion = fields.Date(string='Fecha de la devolucion', required=True, default=fields.Date.today())

    #Relacion entre tablas
    incidencia_id = fields.Many2one('incidencias.incidencia', string='incidencia')
    devoluciones = fields.Many2one('alquileres.cliente', string='Cliente')
    cliente_id = fields.Many2one('alquileres.cliente', string='Cliente')