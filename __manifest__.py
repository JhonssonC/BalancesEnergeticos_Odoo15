{
    'name': 'Balances Energéticos EOR',
    'version': '1.0.0',
    'category': 'Productivity/Balances',
    'author': 'JhonssonC',
    'sequence': -101,
    'summary': 'Control de Energía en redes de Distribucion de Bajo Voltaje, EL Oro',
    'description': """Control de Energía en redes de Distribucion de Bajo Voltaje, EL Oro""",
    'depends': [
        'base',
    ],
    'data': [
        'security/be_security.xml',
        'security/ir.model.access.csv',

        'views/fotos_views.xml',
        'views/coordenadas_views.xml',
        'views/transformador_views.xml',
        'views/punto_carga_views.xml',
        'views/tipo_vinculacion_views.xml',
        'views/tipo_consumidor_views.xml',
        'views/marca_medidor_views.xml',
        'views/provincia_views.xml',
        'views/canton_views.xml',
        'views/red_views.xml',
        'views/balance_energetico_views.xml',
        'views/consumidor_views.xml',
        'views/vinculacion_views.xml',


        'views/balances_menu_views.xml',
    ],
    'assets': {
        # -----------------------------
        # MAIN BUNDLES
        # -----------------------------
        'web.assets_qweb': [
            # EXAMPLE: Add everyithing in the folder
            #'web/static/src/**/*.xml',
            # EXAMPLE: Remove every .xml file
            #('remove', 'web/static/src/legacy/**/*.xml'),
        ],
        'web.assets_common_minimal': [
            # EXAMPLE lib
            #'web/static/lib/es6-promise/es6-promise-polyfill.js',

            'balancesEnergeticos/static/lib/leaflet/leaflet.js',

        ],
        'web.assets_common': [
            # EXAMPLE Can include sub assets bundle
            #('include', 'web._assets_helpers'),
            #'web/static/lib/bootstrap/scss/_variables.scss',
            'balancesEnergeticos/static/src/css/leaflet.css',
        ],
        'web.assets_common_lazy': [
            # ...
        ],
        'web.assets_backend': [
            # EXAMPLE Any files
            #'balancesEnergeticos/static/src/js/utmLatLng.js',
            #'balancesEnergeticos/static/src/js/map.js',
            #'balancesEnergeticos/static/src/js/*',
        ],
        "web.assets_backend_legacy_lazy": [
            # ...
        ],
        'web.assets_frontend_minimal': [
            # ...
        ],
        'web.assets_frontend': [
            # ...
        ],
        'web.assets_frontend_lazy': [
            # ...
        ],
        'web.assets_backend_prod_only': [
            # ...
        ],
        'web.report_assets_common': [
            # ...
        ],
        'web.report_assets_pdf': [
            # ...
        ],

        # --------------------------------
        # SUB BUNDLES
        # --------------------------------
        # These bundles can be used by main bundles but are not supposed to be
        # called directly from XML templates.
        #
        # Their naming conventions are similar to those of the main bundles,
        # with the addition of a prefixed underscore to reflect the "private"
        # aspect.
        #
        # Exemples:
        #   > web._assets_helpers = define assets needed in most main bundles

        'web._assets_primary_variables': [
            # ...
        ],
        'web._assets_secondary_variables': [
            # ...
        ],
        'web._assets_helpers': [
            # ...
        ],
        'web._assets_bootstrap': [
            # ...
        ],
        'web._assets_backend_helpers': [
            # ...
        ],
        'web._assets_frontend_helpers': [
            # ...
        ],
        'web._assets_common_styles': [
            # ...
        ],
        'web._assets_common_scripts': [
            # ...
        ],

        # Used during the transition of the web architecture
        'web.frontend_legacy': [
            # ...
        ],

        # -----------------------------------
        # TESTS BUNDLES
        # -----------------------------------

        'web.assets_tests': [
            # ...
        ],
        'web.tests_assets': [
            # ...
        ],
        'web.qunit_suite_tests': [
            # ...
        ],
        'web.qunit_mobile_suite_tests': [
            # ...
        ],
        # Used during the transition of the web architecture
        'web.frontend_legacy_tests': [
            # ...
        ],
    },
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}