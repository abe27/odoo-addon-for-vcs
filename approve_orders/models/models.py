# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class approve_orders(models.Model):
#     _name = 'approve_orders.approve_orders'
#     _description = 'approve_orders.approve_orders'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class OrderHeader(models.Model):
    _name = 'approve_orders.order_header'
    _description = 'approve_orders.order_header'

    order_type_id = fields.Many2one(
        'vcsgroup.order_type', string="Order Type", required=True)
    order_date = fields.Date(
        string="Date", default=lambda self: fields.Date.today())
    name = fields.Char(size=15, string="Order No.", required=True)
    partner_id = fields.Many2one("res.partner", string="Partner")
    item_count = fields.Integer(string="Item", default="0")
    vat_total = fields.Float(string="Vat.", default="0.0")
    order_step = fields.Many2one('vcsgroup.order_step', string="Step")
    remark = fields.Text(string="Remark", default="-")
    is_approve = fields.Selection([("0", "Open"), ("1", "In Process"), (
        "2", "Approved"), ("3", "Completed"), ("4", "Cancel")], string="Status")
    is_sync = fields.Boolean(string="Is Sync", default=False)
    line_ids = fields.One2many("approve_orders.order_detail", "order_id", string="Order Detail")

class OrderDetail(models.Model):
    _name = 'approve_orders.order_detail'
    _description = 'approve_orders.order_detail'

    order_id = fields.Many2one('approve_orders.order_header', string="Order", required=True)
    product_id = fields.Many2one( 'vcsgroup.product_group', string="Product", required=True)
    quantity = fields.Float(string="Quantity", default="0.0")
    unit_id = fields.Many2one( 'vcsgroup.unit', string="Unit", required=True)