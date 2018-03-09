# -*- coding: utf-8 -*-
{
    'name': "stock_goods_express",

    'summary': """
           物流管理--快递鸟平台应用
           """,

    'description': """
          单号识别
          即时查询
          预约取件
          电子面单
          物流跟踪
       """,

    'author': "Gavin GU",
    'website': "http://www.bankcall.net",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Stock',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock_logistics'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
