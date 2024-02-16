# -*- coding: utf-8 -*-
from odoo import models, fields, api

class medicos(models.Model):
    _name = 'medicos_pacientes.medicos'
    _description = 'medicos_pacientes.medicos'
    _rec_name = 'nombreCompleto'


    nombre = fields.Text('Nombre')
    apellidos = fields.Text('Apellidos')
    numColegiado = fields.Integer('Nº Colegiado')

    nombreCompleto = fields.Text(compute="_nombre_completo")

    diagnostico = fields.One2many('medicos_pacientes.diagnostico','medico')
    
    @api.depends('nombre','apellidos')
    def _nombre_completo(self):
        for record in self:
            record.nombreCompleto = f"{record.nombre} {record.apellidos}"
    
    
