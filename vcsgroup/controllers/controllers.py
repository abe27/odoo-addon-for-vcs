# -*- coding: utf-8 -*-
# from odoo import http


# class Vcsgroup(http.Controller):
#     @http.route('/vcsgroup/vcsgroup', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vcsgroup/vcsgroup/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vcsgroup.listing', {
#             'root': '/vcsgroup/vcsgroup',
#             'objects': http.request.env['vcsgroup.vcsgroup'].search([]),
#         })

#     @http.route('/vcsgroup/vcsgroup/objects/<model("vcsgroup.vcsgroup"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vcsgroup.object', {
#             'object': obj
#         })
