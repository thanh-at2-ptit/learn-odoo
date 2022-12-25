from odoo import models, fields, api, _
from odoo.exceptions import UserError


class WizardEnrollmentSingle(models.TransientModel):
    _name = 'wizard.enrollment.single'
    _description = 'Single Enrollment Wizard'
    
    registration_number = fields.Char(required=True)
    class_id = fields.Many2one('education.class', string='Class', required=True)
    student_id = fields.Many2one('education.student', string='Student', required=True)
    date = fields.Date(
        help="The date on which the student enrolls"
        )
    
    active_model = fields.Char()
    
    wizard_multipe_id = fields.Many2one('wizard.enrollment.multi')
    
    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        
        active_model = self._context.get('active_model')
        active_id = self._context.get('active_id')

        if not 'class_id' not in fields_list and active_model == 'education.class':
            res['class_id'] = active_id
        elif active_model == 'education.student':
            res['student_id'] = active_id
        res['active_model'] = self._context.get('active_model')
        res['date'] = fields.Date.today()
        return res
    
    def enroll(self):
        if not self.class_id or not self.student_id:
            raise UserError(_("You must specify both class and student fist."))

        self.env['education.enrollment'].create({
            'name': self.registration_number,
            'class_id': self.class_id.id,
            'student_id': self.student_id.id,
            'date': self.date or fields.Date.today()
            })

        
class WizardEnrollmentMulti(models.TransientModel):
    _name = 'wizard.enrollment.multi'
    
    line_ids = fields.One2many('wizard.enrollment.single', 'wizard_multipe_id')
    
    def enroll(self):
        for l in self.line_ids:
            WizardEnrollmentSingle.enroll(l)

