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
class diagnostico(models.Model):
    _name = 'medicos_pacientes.diagnostico'
    _description = 'medicos_pacientes.diagnostico'

    numDiagnostico = fields.Integer()
    medico = fields.Many2one('medicos_pacientes.medicos')
    paciente = fields.Many2one('medicos_pacientes.pacientes')
    sintomas = fields.Text('Sintomas')
    diagnostico = fields.Text()