# -*- coding: utf-8 -*-
{
    "name": "Remember Resized Tree Column Width",
    "version": "17.0.0.1",
    "license": "LGPL-3",
    "summary": """
        Resize Column Width, Remember the tree view column's width each and every session.""",
    "category": "Sales/Sales",
    "sequence": 1,
    "description": "This module is used to Auto save when the user resizes the tree view column's widths or one2many fields column's width.",
    # "author": "Caret IT Solutions Pvt. Ltd.",
    "depends": [
        "web",
    ],
    "data": [],
    "assets": {
        "web.assets_backend": [
            "remember_resized_tree_column_width/static/src/js/list_renderer.js",
            "remember_resized_tree_column_width/static/src/scss/main.scss",
        ],
    },
    # 'images': ['static/description/banner.gif'],
    'price': 46.04,
    'currency': 'EUR',
}
