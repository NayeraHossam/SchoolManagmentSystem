from odoo import models, fields, api


class Courses(models.Model):
    _name = 'courses'
    _description = 'Courses'

    name = fields.Char(string='Name')
    course_id = fields.Char(string='Course ID')
    credit_hours = fields.Float(string='Credit Hours')
    time = fields.Date(string='Time')

    grade_ids = fields.One2many(
        'student.grades',
        'course_id',
        string='Grades'
    )



    #student_ids = fields.One2many('student.profile', 'course_id', string='Student IDs')
    #teacher_id = fields.Many2one('teacher.profile', string='Teacher ID')


