from odoo import fields, models


class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"


    name = fields.Char(required=True)

    _sql_contraints = [
        ("unique_tag_name", "UNIQUE(name)", "Tag name must be unique")
    ]
