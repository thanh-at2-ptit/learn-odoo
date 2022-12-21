from odoo import models, fields, api


class EducationEnrollment(models.Model):
    _name = 'education.enrollment'
    _description = 'Education Enrollment'
    
    name = fields.Char(
        string='Ref.',
        required=True
        )

    class_id = fields.Many2one('education.class', string='Class')
    student_id = fields.Many2one('education.student', string='Student')
    date = fields.Date(help="The date on which the student enrolls")
