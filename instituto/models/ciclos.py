# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ciclos(models.Model):
    _name = 'instituto.ciclos'
    _description = 'instituto.ciclos'

    _rec_name='ciclo'

    ciclo = fields.Text()
    modulos = fields.Many2many(comodel_name='instituto.modulos')
