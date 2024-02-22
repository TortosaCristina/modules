from odoo import fields, models, api

class alumnos(models.Model):
    _name = 'instituto.alumnos'
    _description = 'instituto.alumnos'

    _rec_name='nombre'
    
    nombre = fields.Text()
    apellidos = fields.Text()
    dni = fields.Text()
    modulos = fields.Many2many(comodel_name='instituto.modulos')