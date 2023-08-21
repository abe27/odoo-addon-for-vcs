# -*- coding: utf-8 -*-
from odoo import http
import json
from werkzeug.wrappers import Response

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


class VcsGroup(http.Controller):
    @http.route('/api/vcsgroup/hello', auth='public', csrf=False, website=False, type="json", methods=['GET'])
    def index(self, **kw):
        return "Hello, world"

    @http.route('/api/vcsgroup/accbook', auth='public', csrf=False, website=False, type="json", methods=['GET', 'POST'])
    def account_books(self, **kw):
        # if method is POST
        print(kw)
        if http.request.httprequest.method == 'POST':
            data = {
                "account_book_id":  kw["account_book_id"],
                "account_book_code": kw["account_book_code"],
                "name": kw["name"],
                "description": kw["description"],
                "is_active": kw["is_active"],
            }

            try:
                obj = http.request.env["vcsgroup.account_book"].sudo().create([data])
                return obj.id
            
            except Exception as e:
                print(e)
                pass

            return data

        # if method is GET
        if len(kw) > 0:
            print(kw['id'])

        # http.request.env["vcsgroup.account_book"].sudo().search([('id', '=', kw['id'])])
        accbook = http.request.env["vcsgroup.account_book"].sudo().search([])

        data = []
        for a in accbook:
            data.append({
                "account_book_id": a.account_book_id,
                "account_book_code": a.account_book_code,
                "name": a.name,
                "description": a.description,
                "is_active": a.is_active,
            })

        return data
