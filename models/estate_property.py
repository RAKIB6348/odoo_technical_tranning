from odoo import models, fields, api


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), 
                   ('offer_received', 'Offer Received'), 
                   ('offer_accepted', 'Offer Accepted'), 
                   ('sold', 'Sold'), 
                   ('canceled', 'Canceled')],
        default='new',
        copy=False,
        required=True
    )


    def default_date_availability(self):
        return fields.Date.today()


    date_availability = fields.Date(string='Available From', copy=False, default=default_date_availability)
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', copy=False)
    best_offer = fields.Float(string='Best Offer', copy=False)
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), 
                   ('south', 'South'), 
                   ('east', 'East'), 
                   ('west', 'West')],
        default="north",
        copy=False
    )
    active = fields.Boolean(string='Active', default=True, invisible=True)

    #many2one relation
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    # one2many relation
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')
    # many2many relation
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')