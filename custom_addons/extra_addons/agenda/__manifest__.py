# -*- coding: utf-8 -*-
{
    'name': "Agenda Escolar",

    'summary': "Aqui realizaremos las funcionalidades para la agenda escolar",

    'description': """Este modulo es para gestionar a los usuarios, gestionar las materias, 
    gestionar los cursos""",

    'author': "Alejandra Villarreal and Ricardo",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/tarea_views.xml',
        'views/alumno_views.xml',
        'views/padre_views.xml',
        'views/profesor_views.xml',
        'views/administrativo_views.xml',
        'views/comunicado_views.xml',
        # 'views/comunicado_enviado_views.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

