# -*- coding: utf-8 -*-
{
    'name': 'Chess Academy',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage chess academy students, lessons, coaches, and tournaments',
    'description': """
Chess Academy Management
========================
Complete solution for managing a chess academy including:
* Student enrollment and progress tracking
* Lesson scheduling and booking
* Coach management
* Tournament organization
* Parent portal access
* Billing and invoicing
    """,
    'author': 'Chess Academy',
    'website': 'https://www.chessacademy.com',
    'depends': [
        'base',
        'mail',
        'crm',
        'contacts',
        'sale',
        'account',
        'calendar',
        'project',
        'website',
        'portal',
        'event',
        'mass_mailing',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/lesson_views.xml',
        'views/coach_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
