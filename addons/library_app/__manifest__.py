# -*- coding: utf-8 -*-
{
    'name': "library_app",

    'summary': "Manage library catalog and book lending.",

    'description': """
        Long description of module's purpose
    """,

    'author': "Bernard Codjoe",
    'website': "http://www.ibit-soft.com",
    'category': "Services/Library",
    'version': '1.0',
    'application': "True",
    'licence': "AGPL-3", # LGPL-3, OPL-3(proprietary)

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
