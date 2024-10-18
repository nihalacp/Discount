{
    'name': 'Sale Discount Approval Workflow',
    'author': "nin",
    'license': "LGPL-3",
    'version': '17.0.1.1',
    'summary': 'Require approval for discounts greater than 15%',
    'depends': ['sale'],
    'data': [
        'security/sale_discount_approval_security.xml',
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}