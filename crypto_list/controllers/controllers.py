# -*- coding: utf-8 -*-
# from odoo import http


# class CryptoList(http.Controller):
#     @http.route('/crypto_list/crypto_list', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crypto_list/crypto_list/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('crypto_list.listing', {
#             'root': '/crypto_list/crypto_list',
#             'objects': http.request.env['crypto_list.crypto_list'].search([]),
#         })

#     @http.route('/crypto_list/crypto_list/objects/<model("crypto_list.crypto_list"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crypto_list.object', {
#             'object': obj
#         })
