# -*- coding: utf-8 -*-
from odoo import models, fields, api

class medicos(models.Model):
    _rec_name = 'nombreCompleto'
    _name = 'medicos_pacientes.medicos'
    _description = 'medicos_pacientes.medicos'

    nombre = fields.Text('Nombre')
    apellidos = fields.Text('Apellidos')
    numColegiado = fields.Integer('Nº Colegiado')

    nombreCompleto = fields.Text(compute="_nombre_completo")
    
    @api.depends('nombre','apellidos')
    def _nombre_completo(self):
        for record in self:
            record.nombreCompleto = self.nombre + " " + self.apellidos
    
    
