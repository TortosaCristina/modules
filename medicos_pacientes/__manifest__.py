# -*- coding: utf-8 -*-
{
    'name': "Medicos/Pacientes",

    'summary': "Registro de medicos y pacientes",

    'description': """
Gestiona los pacientes y los medicos de un hospital
    """,

    'author': "Maria Cristina Rodriguez Tortosa",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',
    'application' : True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/paciente_view.xml',
        'views/medico_view.xml',
        'views/diagnostico_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

