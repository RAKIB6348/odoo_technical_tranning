from odoo import fields, models, api
from dateutil.relativedelta import relativedelta




class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"


    price = fields.Float(string="Price")
    status = fields.Selection(
        [
            ('accepted', 'Accepted'),
            ('refused', 'Refused'),
        ],
        copy=False
    )
    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("estate.property", string="Property")
    property_type_id = fields.Many2one(related="property_id.property_type_id", string="Property Type", store=True)

    # inverse compute function
    validity = fields.Integer(string='Validity (days)', default=7)
    date_deadline = fields.Date(string='Deadline', compute='_compute_date_deadline', inverse='_inverse_date_deadline')

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = fields.Date.today() + relativedelta(days=record.validity)


    # inverse function
    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - fields.Date.today()).days

