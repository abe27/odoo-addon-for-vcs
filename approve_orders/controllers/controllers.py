# -*- coding: utf-8 -*-
# from odoo import http


# class ApproveOrders(http.Controller):
#     @http.route('/approve_orders/approve_orders', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/approve_orders/approve_orders/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('approve_orders.listing', {
#             'root': '/approve_orders/approve_orders',
#             'objects': http.request.env['approve_orders.approve_orders'].search([]),
#         })

#     @http.route('/approve_orders/approve_orders/objects/<model("approve_orders.approve_orders"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('approve_orders.object', {
#             'object': obj
#         })
