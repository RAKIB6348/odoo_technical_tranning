{
    'name' : 'Real Estate',
    'version' : '1.0.0',
    'description' : 'This is a real estate module',
    'summary' : 'This is a real estate module',
    'license' : 'LGPL-3',
    'depends' : ['contacts'],
    'data' : [
        #SECURITY
        'security/ir.model.access.csv',

        #VIEWS
        'views/menu.xml',
        'views/estate_property.xml',
        'views/estate_property_type.xml',
        'views/estate_property_tag.xml',
        'views/estate_property_offer.xml',



    ],
    'installable' : True,
    'auto_install' : False,
    'application' : True,
}