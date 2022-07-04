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
        # It is common for menu items to reference security groups, and so it 
        # is a good practice to add security definitions before menu and view definitions.
        "security/library_security.xml",
        'views/library_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
