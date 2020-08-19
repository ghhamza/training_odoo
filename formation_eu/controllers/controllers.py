# -*- coding: utf-8 -*-
# from odoo import http


# class FormationEu(http.Controller):
#     @http.route('/formation_eu/formation_eu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/formation_eu/formation_eu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('formation_eu.listing', {
#             'root': '/formation_eu/formation_eu',
#             'objects': http.request.env['formation_eu.formation_eu'].search([]),
#         })

#     @http.route('/formation_eu/formation_eu/objects/<model("formation_eu.formation_eu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('formation_eu.object', {
#             'object': obj
#         })
