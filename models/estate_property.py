from jsonschema import ValidationError
from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta



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

    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    salesman_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)
    total_area = fields.Integer(string='Total Area (sqm)', compute='_compute_total_area')
    best_offer = fields.Float(string='Best Offer', compute='_compute_best_offer')

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for record in self:
            record.best_offer = max(record.offer_ids.mapped('price')) if record.offer_ids else 0.0


    # compute field
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    # onchange function
    @api.onchange('garden')
    def _onchange_garden(self):
        for estate in self:
            if not estate.garden:
                estate.garden_area = 0
                estate.garden_orientation = False

    
    @api.constrains('selling_price')
    def _check_selling_price(self):
        for rec in self:
            if rec.selling_price < 50000:
                raise ValidationError(_("Selling price must be greater than 50000")))