# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class TypeInfo(models.Model):
    _name = 'type.info'
    _description = 'Type'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(default=True,
                            help="The active field is allow you to hide the type without removing it.")
                            