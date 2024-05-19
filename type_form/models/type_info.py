# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class TypeInfo(models.Model):
    _name = 'type.info'
    _description = 'Type'
    _order = 'name'

    name = fields.Char('Name', required=True)
    active = fields.Boolean('Active', default=True,
                            help="If the active field is set to false, it will allow you to hide the type without removing it.")
                            