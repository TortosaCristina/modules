# -*- coding: utf-8 -*-
from odoo import models, fields, api


# class medicos_pacientes(models.Model):
#     _name = 'medicos_pacientes.medicos_pacientes'
#     _description = 'medicos_pacientes.medicos_pacientes'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class pacientes(models.Model):
    _rec_name = 'nombreCompleto'
    _name = 'medicos_pacientes.pacientes'
    _description = 'medicos_pacientes.pacientes'

    nombre = fields.Text('Nombre')
    apellidos = fields.Text('Apellidos')

    nombreCompleto = fields.Text(compute="_nombre_completo")

    @api.depends('nombre','apellidos')
    def _nombre_completo(self):
        for record in self:
            record.nombreCompleto = self.nombre + " " + self.apellidos
    
    

    
    """diagnostico = fields.Many2many(comodel_name='medicos',
                              relation='diagnostico_medicos',
                              column1='pacientes_id',
                              column2='medicos_id')"""