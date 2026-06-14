from odoo import models, fields, api


class StudentGrades(models.Model):
    _name = 'student.grades'
    _description = 'Student Grades'

    percentage = fields.Float(string='percentage')


    student_id = fields.Many2one(
        'student.profile',
        required=True
    )
    course_id = fields.Many2one(
        'courses'
    )












