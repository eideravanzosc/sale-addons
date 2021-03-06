# Copyright 2017 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Sale Contract Specification',
    'version': '11.0.1.0.1',
    'category': 'Sale Management',
    'author': 'AvanzOSC',
    'license': 'AGPL-3',
    'summary': 'Define conditions and specifications in sale orders',
    'depends': [
        'sale',
        'sales_team',
        'contract_specification',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_condition_views.xml',
        'views/sale_order_views.xml',
        'views/sale_contract_specification_menu.xml',
        'views/sale_portal_templates.xml',
    ],
    'installable': True,
}
