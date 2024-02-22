from odoo import fields, models, api 

class profesores(models.Model):
    _name = 'instituto.profesores'
    _description = 'instituto.profesores'

    _rec_name='nombre'

    nombre = fields.Text()
    apellidos = fields.Text()
    dni = fields.Text()
    modulos = fields.One2many('instituto.modulos','profesor')