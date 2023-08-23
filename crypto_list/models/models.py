# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class crypto_list(models.Model):
#     _name = 'crypto_list.crypto_list'
#     _description = 'crypto_list.crypto_list'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
