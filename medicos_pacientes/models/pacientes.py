# -*- coding: utf-8 -*-
from odoo import models, fields, api

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