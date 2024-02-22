from odoo import fields, models, api

class modulos(models.Model):
    _name = 'instituto.modulos'
    _description = 'instituto.modulos'

    _rec_name='modulo'
    
    modulo = fields.Text()
    alumnos = fields.Many2many(comodel_name='instituto.alumnos')
    ciclos = fields.Many2many(comodel_name='instituto.ciclos')
    profesor = fields.Many2one(comodel_name='instituto.profesores')