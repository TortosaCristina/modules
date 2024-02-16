# -*- coding: utf-8 -*-
# from odoo import http


# class MedicosPacientes(http.Controller):
#     @http.route('/medicos_pacientes/medicos_pacientes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/medicos_pacientes/medicos_pacientes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('medicos_pacientes.listing', {
#             'root': '/medicos_pacientes/medicos_pacientes',
#             'objects': http.request.env['medicos_pacientes.medicos_pacientes'].search([]),
#         })

#     @http.route('/medicos_pacientes/medicos_pacientes/objects/<model("medicos_pacientes.medicos_pacientes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('medicos_pacientes.object', {
#             'object': obj
#         })

