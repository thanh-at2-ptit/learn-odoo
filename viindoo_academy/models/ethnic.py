from odoo import models, fields, api


class ResEthnic(models.Model):
    _name = 'res.ethnic'
    _description = 'Ethnic'
    
    name = fields.Char(
        string='Name',
        help="The name of nation",
        required=True)

    code = fields.Char(
        string='Code',
        required=True,
        # groups='base.group_user,base.group_portal'
        )
    
    @api.model
    def name_create(self, name):
        code = name.lower().replace(" ", "")
        return self.create({'code': code, 'name': name}).name_get()[0]

