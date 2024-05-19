# -*- coding: utf-8 -*-

from odoo import models, fields, api,  _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'
        
    type_id = fields.Many2one('type.info', string='Customer Type', ondelete='cascade')
    
    @api.model
    def fields_get(self, fields=None):
        fields_to_hide = ['address_type']
        res = super(ResPartner, self).fields_get()
        for field in fields_to_hide:
            res[field]['selectable'] = False #To Hide Field From Filter
            res[field]['sortable'] = False #To Hide Field From Group by        
            res[field]['exportable'] = False #To Hide Field From Export List
        return res