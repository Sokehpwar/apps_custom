# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'
        
    type_id = fields.Many2one('type.info', string='Customer Type', ondelete='cascade')
    
    