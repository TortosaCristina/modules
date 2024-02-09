# -*- coding: utf-8 -*-
from odoo import models, fields, api

#Definimos el modelo de datos
class lista_tareas(models.Model):
    #Nombre y descripción del modelo de datos.
    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar son
    #https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields

    tarea = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute = "_value_urgente", store = True)
    realizada = fields.Boolean()
    imagenTarea = fields.Binary('Imagen de la tarea')
    fechaFin = fields.Datetime('Fecha límite')
    fechaInicio = fields.Datetime('Fecha de Inicio')
    duracion = fields.Integer()

    #Este apartado depende de la variable prioridad
    @api.depends('prioridad')
    #Funcion para calcular el valor de urgente
    def _value_urgente(self):
        #Para cada registro
        for record in self:
            #Si la prioridad es mayor que 10, se considera urgente, en otro caso no lo es
            if record.prioridad > 10:
                record.urgente = True
            else:
                record.urgente = False