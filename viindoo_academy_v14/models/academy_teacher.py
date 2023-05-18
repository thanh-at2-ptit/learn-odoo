from odoo import models, fields, api


class Academy_Teacher(models.Model):
    _name = 'academy.teacher'
    _description = 'Academy Teacher'
    
    name = fields.Char(string='name')
    
