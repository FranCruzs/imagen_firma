{
    'name': 'Mi Módulo',
    'version': '1.0',
    'summary': 'Un módulo con imagen estática',
    'author': 'Tu Nombre',
    'category': 'Custom',
    'depends': ['base'],
    'data': [
        # Aquí irían tus vistas XML si las tienes
    ],
    'assets': {
        'web.assets_common': [
            'images/static/src/img/firma1.jpg',
        ],
    },
    'installable': True,
    'application': False,
}
