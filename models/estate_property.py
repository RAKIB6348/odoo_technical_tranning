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
        copy=False
    )


    def default_date_availability(self):
        return fields.Date.today()


    date_availability = fields.Date(string='Available From', copy=False, default=default_date_availability)
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', copy=False)
    best_offer = fields.Float(string='Best Offer', copy=False)
    bedrooms = fields.Integer(string='Bedrooms', default=2)
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