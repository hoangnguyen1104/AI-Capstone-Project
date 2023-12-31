# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hanger AI',
    'version': '1.0',
    'category': 'Virtual Fitting Room',
    'sequence': 15,
    'summary': 'virtual fitting room',
    'website': 'https://www.odoo.com/app/crm',
    'depends': ['product', 'website'],
    'data': [
        'data/data.xml',
        'views/fpt_product_template_view.xml',
        'views/templates.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_frontend': [
            'hangerAI/static/src/scss/dashboard.scss'
        ],
        'mail.assets_messaging': [],
        'web.assets_backend': [],
        'web.assets_tests': [],
        'web.qunit_suite_tests': [],
    },
    'license': 'LGPL-3',
}
