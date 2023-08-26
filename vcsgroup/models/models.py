# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# class vcsgroup(models.Model):
#     _name = 'vcsgroup.vcsgroup'
#     _description = 'vcsgroup.vcsgroup'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class AccountBook(models.Model):
    _name = 'vcsgroup.account_book'
    _description = 'vcsgroup.account_book'

    account_book_id = fields.Char(size=8, required=True, string="ID")
    account_book_code = fields.Char(size=2, required=True, string="Code")
    name = fields.Char(size=250, string="Name", required=True)
    description = fields.Text(string="Description")
    is_active = fields.Boolean(string="Active", default=False)

    @api.constrains('account_book_id')
    def _check_registration_no(self):
        for rec in self:
            domain = [('account_book_id', '=', rec.account_book_id)]
            count = self.sudo().search_count(domain)

            if count > 0:
                raise ValidationError(("The ID should be unique"))
            
    def send_mail_template(self):
        print("Sending mail Click")


class Corporation(models.Model):
    _name = 'vcsgroup.corporation'
    _description = 'vcsgroup.corporation'

    corporation_id = fields.Char(size=8, required=True, string="ID")
    corporation_code = fields.Char(size=15, required=True, string="Code")
    name = fields.Char(size=250, string="Name", required=True)
    description = fields.Text(string="Description")
    tax_id = fields.Char(size=25, string="Tax ID")
    address = fields.Text(string="Address")
    tel_no = fields.Char(size=50, string="Tel. No.")
    fax_no = fields.Char(size=50, string="Fax No.")
    is_active = fields.Boolean(string="Active", default=False)

    @api.constrains('corporation_id')
    def _check_registration_no(self):
        for rec in self:
            domain = [('corporation_id', '=', rec.corporation_id)]
            count = self.sudo().search_count(domain)

            if count > 0:
                raise ValidationError(("The ID should be unique"))


class Customer(models.Model):
    _name = 'vcsgroup.customer'
    _description = 'vcsgroup.customer'

    customer_id = fields.Char(size=15,
                              required=True, string="ID")
    name = fields.Char(size=250, string="Name", required=True)
    description = fields.Text(string="Description")
    tax_id = fields.Char(size=25, string="Tax ID")
    address = fields.Text(string="Address")
    tel_no = fields.Char(size=50, string="Tel. No.")
    fax_no = fields.Char(size=50, string="Fax No.")
    is_active = fields.Boolean(string="Active", default=False)


class Whs(models.Model):
    _name = 'vcsgroup.whs'
    _description = 'vcsgroup.whs'

    whs_id = fields.Char(size=8,
                         required=True, string="ID")
    whs_code = fields.Char(size=15,
                           required=True, string="Code")
    name = fields.Char(size=250, string="Name", required=True)
    description = fields.Text(string="Description")
    is_active = fields.Boolean(string="Active", default=False)

    @api.constrains('whs_id')
    def _check_registration_no(self):
        for rec in self:
            domain = [('whs_id', '=', rec.whs_id)]
            count = self.sudo().search_count(domain)

            if count > 0:
                raise ValidationError(("The ID should be unique"))

class Unit(models.Model):
    _name = 'vcsgroup.unit'
    _description = 'vcsgroup.unit'

    unit_id = fields.Char(size=8,
                          required=True, string="ID")
    unit_code = fields.Char(size=15,
                            required=True, string="CODE")
    name = fields.Char(size=250, string="Name", required=True)
    description = fields.Text(string="Description")
    is_active = fields.Boolean(string="Active", default=False)

class OrderType(models.Model):
    # RefType
    _name = 'vcsgroup.order_type'
    _description = 'vcsgroup.order_type'

    order_type_id = fields.Char(size=15,
                                required=True, string="ID")
    name = fields.Char(size=250, string="Name", required=True)
    description = fields.Text(string="Description")
    is_active = fields.Boolean(string="Active", default=False)


class ProductType(models.Model):
    _name = 'vcsgroup.product_type'
    _description = 'vcsgroup.product_type'

    product_type_id = fields.Char(size=1,
                                  required=True, string="ID")
    name = fields.Char(size=250, string="Name", required=True)
    description = fields.Text(string="Description")
    is_active = fields.Boolean(string="Active", default=False)


class Product(models.Model):
    _name = 'vcsgroup.product'
    _description = 'vcsgroup.product'

    product_id = fields.Char(size=25,
                             required=True, string="ID")
    name = fields.Char(size=250, string="Name", required=True)
    description = fields.Text(string="Description")
    is_active = fields.Boolean(string="Active", default=False)


class ProductGroup(models.Model):
    _name = 'vcsgroup.product_group'
    _description = 'vcsgroup.product_group'

    product_type_id = fields.Many2one(
        'vcsgroup.product_type', string="Product Type ID")
    product_id = fields.Many2one('vcsgroup.product', string="Product ID")
    name = fields.Char(size=250, string="Name", required=True)
    unit_id = fields.Many2one('vcsgroup.unit', string="Unit ID")
    whs_id = fields.Many2one('vcsgroup.whs', string="WHS ID")
    price = fields.Float(string="Price", default="0.0")
    is_active = fields.Boolean(string="Active", default=False)

    # def name_get(self):
    #     result = None
    #     for record in self:
    #         result = record.id
            
    #     return result


class Booking(models.Model):
    _name = 'vcsgroup.booking'
    _description = 'vcsgroup.booking'

    ref_type_id = fields.Many2one(
        'vcsgroup.order_type', string="Order Type ID")
    booking_id = fields.Char(size=8,  required=True, string="ID")
    booking_code = fields.Char(size=15, required=True, string="CODE")
    prefix = fields.Char(size=15, string="Prefix")
    name = fields.Char(size=250,string="Name", required=True)
    description = fields.Text(string="Description")
    from_whs_id = fields.Many2one('vcsgroup.whs', string="From WHS ID")
    to_whs_id = fields.Many2one('vcsgroup.whs', string="To WHS ID")
    is_active = fields.Boolean(string="Active", default=False)
