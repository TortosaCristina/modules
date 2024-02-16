# -*- coding: utf-8 -*-
from odoo import models, fields, api

class diagnostico(models.Model):
    _name = 'medicos_pacientes.diagnostico'
    _description = 'medicos_pacientes.diagnostico'

    numDiagnostico = fields.Integer()
    medico = fields.Many2one('medicos_pacientes.medicos')
    paciente = fields.Many2one('medicos_pacientes.pacientes')
    sintomas = fields.Text('Sintomas')
    diagnostico = fields.Text()