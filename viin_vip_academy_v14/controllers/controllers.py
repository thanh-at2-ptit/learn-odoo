# -*- coding: utf-8 -*-
# from odoo import http


# class ViinVipAcademy(http.Controller):
#     @http.route('/viin_vip_academy_v14/viin_vip_academy_v14', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/viin_vip_academy_v14/viin_vip_academy_v14/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('viin_vip_academy_v14.listing', {
#             'root': '/viin_vip_academy_v14/viin_vip_academy_v14',
#             'objects': http.request.env['viin_vip_academy_v14.viin_vip_academy_v14'].search([]),
#         })

#     @http.route('/viin_vip_academy_v14/viin_vip_academy_v14/objects/<model("viin_vip_academy_v14.viin_vip_academy_v14"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('viin_vip_academy_v14.object', {
#             'object': obj
#         })
