# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class formation_eu(models.Model):
#     _name = 'formation_eu.formation_eu'
#     _description = 'formation_eu.formation_eu'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
