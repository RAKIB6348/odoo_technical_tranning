from odoo import fields, models, api


class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"


    price = fields.Float(string="Price")
    state = fields.Selection(
        [
            ('accepted', 'Accepted'),
            ('refused', 'Refused'),
        ],
        copy=False
    )
    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("property.property", string="Property")