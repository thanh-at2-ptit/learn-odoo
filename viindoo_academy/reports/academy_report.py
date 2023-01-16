from odoo import models, fields, api


class AcademyReport(models.Model):
    _name = 'academy.report'
    _description = 'Academy Report'

    enrollment_id = fields.Many2one('education.enrollment', readonly=True)
    student_id = fields.Many2one('education.student', readonly=True)
    class_id = fields.Many2one('education.class', readonly=True)
    student_ethnic_id = fields.Many2one('res.ethnic', readonly=True)
    student_country_id = fields.Many2one('res.country')
    date = fields.Date(string='Enroll Date', readonly=True)
    start_date = fields.Date(string='Start Date', readonly=True)
    end_date = fields.Date(string='End Date', readonly=True)
    
    @property
    def _table_query(self):
        return "%s %s" % (self._select(), self._from())

    def _select(self):
        return """
        SELECT enrollment.id AS enrollment_id,
            student.id AS student_id,
            class.id AS class_id,
            enrollment.date AS date,
            class.start_date AS start_date,
            class.end_date AS end_date,
            eth.id AS student_ethnic_id,
            c.id AS student_country_id
        """
    
    def _from(self):
        return """
        FROM education_enrollment enrollment
            JOIN education_student student ON enrollment.student_id = student.id
            JOIN education_class class ON enrollment.class_id = class.id
            LEFT JOIN res_ethnic eth ON eth.id = student.ethnic_id
            LEFT JOIN res_country c ON c.id =  student.country_id
        """
        
        