from odoo import fields, models, api


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