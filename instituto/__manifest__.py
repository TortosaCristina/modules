# -*- coding: utf-8 -*-
{
    'name': "instituto",

    'summary': "Gestionar ciclos formativos de un instituto",

    'description': """
Gestiona los ciclos formativos de un instituto junto con sus modulos, alumnos y profesores
    """,

    'author': "Cristina Tortosa",
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
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/ciclos.xml',
        'views/modulos.xml',
        'views/alumnos.xml',
        'views/profesores.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

