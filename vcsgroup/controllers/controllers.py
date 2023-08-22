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
        # print(kw)
        if http.request.httprequest.method == 'POST':
            data = {
                "account_book_id":  kw["account_book_id"],
                "account_book_code": kw["account_book_code"],
                "name": kw["name"],
                "description": kw["description"],
                "is_active": kw["is_active"],
            }

            try:
                id = http.request.env["vcsgroup.account_book"].sudo().search([('account_book_id', '=', kw["account_book_id"])])
                if len(id) == 0:
                    obj = http.request.env["vcsgroup.account_book"].sudo().create([data])
                    return obj.id
                
                return id
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

    @http.route('/api/vcsgroup/whs', auth='public', csrf=False, website=False, type="json", methods=['GET', 'POST'])
    def whs(self, **kw):
        # if method is POST
        # print(kw)
        if http.request.httprequest.method == 'POST':
            data = {
                "whs_id":  kw["whs_id"],
                "whs_code": kw["whs_code"],
                "name": kw["name"],
                "description": kw["description"],
                "is_active": kw["is_active"],
            }

            try:
                id = http.request.env["vcsgroup.whs"].sudo().search([('whs_id', '=', kw["whs_id"])])
                if len(id) == 0:
                    obj = http.request.env["vcsgroup.whs"].sudo().create([data])
                    return obj.id
                
                return id
            except Exception as e:
                print(e)
                pass

            return data

        # if method is GET
        if len(kw) > 0:
            print(kw['id'])

        # http.request.env["vcsgroup.account_book"].sudo().search([('id', '=', kw['id'])])
        accbook = http.request.env["vcsgroup.whs"].sudo().search([])

        data = []
        for a in accbook:
            data.append({
                "whs_id": a.whs_id,
                "whs_code": a.whs_code,
                "name": a.name,
                "description": a.description,
                "is_active": a.is_active,
            })

        return data
    
    @http.route('/api/vcsgroup/unit', auth='public', csrf=False, website=False, type="json", methods=['GET', 'POST'])
    def unit(self, **kw):
        # if method is POST
        # print(kw)
        if http.request.httprequest.method == 'POST':
            data = {
                "unit_id":  kw["unit_id"],
                "unit_code": kw["unit_code"],
                "name": kw["name"],
                "description": kw["description"],
                "is_active": kw["is_active"],
            }

            try:
                id = http.request.env["vcsgroup.unit"].sudo().search([('unit_id', '=', kw["unit_id"])])
                if len(id) == 0:
                    obj = http.request.env["vcsgroup.unit"].sudo().create([data])
                    return obj.id
                
                return id
            except Exception as e:
                print(e)
                pass

            return data

        # if method is GET
        if len(kw) > 0:
            print(kw['id'])

        # http.request.env["vcsgroup.account_book"].sudo().search([('id', '=', kw['id'])])
        accbook = http.request.env["vcsgroup.unit"].sudo().search([])

        data = []
        for a in accbook:
            data.append({
                "unit_id": a.unit_id,
                "unit_code": a.unit_code,
                "name": a.name,
                "description": a.description,
                "is_active": a.is_active,
            })

        return data
    
    @http.route('/api/vcsgroup/ordertype', auth='public', csrf=False, website=False, type="json", methods=['GET', 'POST'])
    def order_type(self, **kw):
        # if method is POST
        # print(kw)
        if http.request.httprequest.method == 'POST':
            data = {
                "order_type_id": kw["code"],
                "name": kw["name"],
                "description": kw["description"],
                "is_active": kw["is_active"],
            }

            try:
                id = http.request.env["vcsgroup.order_type"].sudo().search([('order_type_id', '=', kw["code"])])
                if len(id) == 0:
                    obj = http.request.env["vcsgroup.order_type"].sudo().create([data])
                    return obj.id
                
                return id
            except Exception as e:
                print(e)
                pass

            return data

        # if method is GET
        if len(kw) > 0:
            print(kw['id'])

        # http.request.env["vcsgroup.account_book"].sudo().search([('id', '=', kw['id'])])
        obj = http.request.env["vcsgroup.order_type"].sudo().search([])

        data = []
        for a in obj:
            data.append({
                "code": a.order_type_id,
                "name": a.name,
                "description": a.description,
                "is_active": a.is_active,
            })

        return data
    
    @http.route('/api/vcsgroup/parttype', auth='public', csrf=False, website=False, type="json", methods=['GET', 'POST'])
    def part_type(self, **kw):
        # if method is POST
        # print(kw)
        if http.request.httprequest.method == 'POST':
            data = {
                "product_type_id": kw["code"],
                "name": kw["name"],
                "description": kw["description"],
                "is_active": kw["is_active"],
            }

            try:
                id = http.request.env["vcsgroup.product_type"].sudo().search([('product_type_id', '=', kw["code"])])
                if len(id) == 0:
                    obj = http.request.env["vcsgroup.product_type"].sudo().create([data])
                    return obj.id
                
                return id
            except Exception as e:
                print(e)
                pass

            return data

        # if method is GET
        if len(kw) > 0:
            print(kw['id'])

        # http.request.env["vcsgroup.account_book"].sudo().search([('id', '=', kw['id'])])
        obj = http.request.env["vcsgroup.product_type"].sudo().search([])

        data = []
        for a in obj:
            data.append({
                "code": a.product_type_id,
                "name": a.name,
                "description": a.description,
                "is_active": a.is_active,
            })

        return data
    
    @http.route('/api/vcsgroup/product', auth='public', csrf=False, website=False, type="json", methods=['GET', 'POST'])
    def product(self, **kw):
        # if method is POST
        # print(kw)
        if http.request.httprequest.method == 'POST':
            data = {
                "product_id": kw["code"],
                "name": kw["name"],
                "description": kw["description"],
                "is_active": kw["is_active"],
            }

            try:
                id = http.request.env["vcsgroup.product"].sudo().search([('product_id', '=', kw["code"])])
                if len(id) == 0:
                    obj = http.request.env["vcsgroup.product"].sudo().create([data])
                    return obj.id
                
                return id
            except Exception as e:
                print(e)
                pass

            return data

        # if method is GET
        if len(kw) > 0:
            print(kw['id'])

        # http.request.env["vcsgroup.account_book"].sudo().search([('id', '=', kw['id'])])
        obj = http.request.env["vcsgroup.product"].sudo().search([])

        data = []
        for a in obj:
            data.append({
                "code": a.product_id,
                "name": a.name,
                "description": a.description,
                "is_active": a.is_active,
            })

        return data
    
    @http.route('/api/vcsgroup/productlist', auth='public', csrf=False, website=False, type="json", methods=['GET', 'POST'])
    def product_list(self, **kw):
        # if method is POST
        # print(kw)
        if http.request.httprequest.method == 'POST':
            data = {
                "type": kw["type"],
                "product": kw["product"],
                "unit": kw["unit"],
                "whs": kw["whs"],
                "price": kw["price"],
                "is_active": kw["is_active"],
            }

            product_type = http.request.env["vcsgroup.product_type"].sudo().search([('product_type_id', '=', kw["type"])])
            product = http.request.env["vcsgroup.product"].sudo().search([('product_id', '=', kw["product"])])
            unit = http.request.env["vcsgroup.unit"].sudo().search([('unit_id', '=', kw["unit"])])
            whs = http.request.env["vcsgroup.whs"].sudo().search([('whs_code', '=', kw["whs"])])

            
            try:
                id = http.request.env["vcsgroup.product_group"].sudo().search([('product_type_id', '=', product_type.id),('product_id', '=', product.id)])
                if len(id) == 0:
                    obj = http.request.env["vcsgroup.product_group"].sudo().create([{
                        "product_type_id": product_type.id,
                        "product_id": product.id,
                        "unit_id": unit.id,
                        "whs_id": whs.id,
                        "price": kw["price"],
                        "is_active": kw["is_active"],
                    }])
                    return obj.id
                
                return id
            except Exception as e:
                print(e)
                pass

            return data

        # if method is GET
        if len(kw) > 0:
            print(kw['id'])

        # http.request.env["vcsgroup.account_book"].sudo().search([('id', '=', kw['id'])])
        obj = http.request.env["vcsgroup.product_group"].sudo().search([])

        data = []
        for a in obj:
            data.append(a)

        return data
    
    @http.route('/api/vcsgroup/booking', auth='public', csrf=False, website=False, type="json", methods=['GET', 'POST'])
    def booking(self, **kw):
        # if method is POST
        # print(kw)
        if http.request.httprequest.method == 'POST':
            data = {
                "ref_type_id": "AJ",
                "booking_id": "Eu4OM30K",
                "booking_code": "0001",
                "prefix": "AJ0001/",
                "name": "1",
                "description": "Adjust 1",
                "from_whs_id": "Eu4OBY05",
                "to_whs_id": "",
                "is_active": "true"
            }

            product_type = http.request.env["vcsgroup.product_type"].sudo().search([('product_type_id', '=', kw["ref_type_id"])])
            from_whs = http.request.env["vcsgroup.whs"].sudo().search([('whs_id', '=', kw["from_whs_id"])])
            to_whs = http.request.env["vcsgroup.whs"].sudo().search([('whs_id', '=', kw["to_whs_id"])])

            
            try:
                id = http.request.env["vcsgroup.booking"].sudo().search([('booking_id', '=', kw['booking_id']),('booking_code', '=', kw['booking_code'])])
                if len(id) == 0:
                    obj = http.request.env["vcsgroup.booking"].sudo().create([{
                        "ref_type_id": product_type.id,
                        "booking_id": kw['booking_id'],
                        "booking_code": kw['booking_code'],
                        "prefix": kw['prefix'],
                        "name": kw['name'],
                        "description": kw['description'],
                        "from_whs_id": from_whs.id,
                        "to_whs_id": to_whs.id,
                        "is_active": kw['is_active'],
                    }])
                    return obj.id
                
                return id
            except Exception as e:
                print(e)
                pass

            return data

        # if method is GET
        if len(kw) > 0:
            print(kw['id'])

        # http.request.env["vcsgroup.account_book"].sudo().search([('id', '=', kw['id'])])
        obj = http.request.env["vcsgroup.booking"].sudo().search([])

        data = []
        for a in obj:
            data.append(a)

        return data