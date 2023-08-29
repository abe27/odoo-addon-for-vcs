# -*- coding: utf-8 -*-
{
    'name': "Approve Order",
    'author': "Taweechai Yuenyang",
    "email": "taweechai.yuenyang@outlook.com",
    'website': 'https://abe27.github.io',
    # license คือ หมวดหมู่หน่วยงานของโมดูล
    'license': 'Other OSI approved licence',
    'summary': 'จัดการข้อมูล Order',  # summary คือ คำอธิบายสั้นๆ ของโมดูล
    # description คือ คำอธิบายยาวของโมดูล
    'description': 'ระบบจัดการข้อมูล Order พัฒนาขึ้มมาเพื่อบริษัทในเคลือของ VCS Group.',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',  # version คือ เวอร์ชันของโมดูล

    # any module necessary for this one to work correctly
    'depends': ['base', 'vcsgroup', 'web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/order_report.xml',
        'report/order_report_pdf_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # 'approve_orders/static/src/css/bulma.min.css',
            'approve_orders/static/src/css/approve_orders.css',
            'approve_orders/static/src/js/bootstrap.bundle.min.js.js',
            'approve_orders/static/src/js/tree_button.js',
        ],
        'web.assets_qweb': [
            'approve_orders/static/src/xml/tree_button.xml',
            # 'approve_orders/report/order_report_view.xml',
        ],
        # 'web.assets_frontend': [
        #     'approve_orders/static/src/css/bulma.min.css',
        # ],
    },
    "bootstrap": True,
    "application": True,
    'installable': True,  # installable คือ ระบุว่าโมดูลสามารถติดตั้งได้หรือไม่
    'auto_install': False,  # auto_install คือ ระบุว่าโมดูลจะติดตั้งโดยอัตโนมัติหรือไม่
}
