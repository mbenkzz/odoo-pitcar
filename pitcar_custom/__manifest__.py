{
    'name':'Pitcar\'s Customization',
    'author':'Pitcar',
    'website':'https://www.pitcar.co.id',
    'summary':'Pitcar\'s Customization for Odoo 2024',
    'maintainer': 'Ahmad Husein Hambali, Teddinata Kusuma',
    'sequence': 1,
    'depends': [
        'base',
        'mail',
        'sale',
        'stock',
        'sale_stock',
        'account',
        'crm',
        'sale_management',
        'purchase',
        'project',
        'product',
        # 'stock_quant',
    ],
    'assets': {
        'web.assets_backend': [
            'pitcar_custom/static/src/js/product_template_list.js',
            'pitcar_custom/static/src/js/product_template_kanban.js',
            'pitcar_custom/static/src/js/lead_time_widget.js',
            'pitcar_custom/static/src/css/custom_button.css',
            'pitcar_custom/static/src/css/lead_time.css',
        ],
    },
    'qweb': ['static/src/xml/lead_time_widget.xml'],
    'data': [
        'data/res_partner_data.xml',
        'data/res_partner_car_data.xml',
        'data/lead_time_data.xml',
        # 'data/cron_jobs.xml',

        'report/ir_actions_report_templates.xml',
        'report/ir_actions_report.xml',
        'report/report_invoice.xml',

        'security/lead_time_security.xml',
        'security/ir.model.access.csv',

        'views/account_move.xml',
        'views/pitcar_mechanic_views.xml',
        'views/pitcar_service_advisor_views.xml',  # View untuk Service Advisor
        'views/res_partner_car_brand.xml',
        'views/res_partner_car_type.xml',
        'views/res_partner_category.xml',
        'views/res_partner_car.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',
        'views/stock_picking.xml',
        'views/product_views.xml',
        'views/product_tag_views.xml',
        'views/crm_tag_views.xml',
        'views/project_task_views.xml',
        'views/menu.xml',
        'views/product_template_views.xml',
        'views/user_views.xml',
        # 'views/product_actions.xml', 
        # 'views/stock_quant_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'version':'16.0.19'
}