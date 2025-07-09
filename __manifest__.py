{
    'name': "supplier",
    'version': "18.0.1.1",
    'license': 'LGPL-3',
    'summary': """Manage Supplier ERP Data""",
    'description': """suply module descp""",
    'author': "eman",
    'category':"Service Provider ,Materials Supplier, Service&Materials Supplier",
'depends': ['base', 'account'],
    'data': [
        'views/supplier_views.xml',
    ],
    'website':"www.service.com",
    'sequence':1,
    'aplication':True,
    'auto_install':True,
    'installable':True,
}