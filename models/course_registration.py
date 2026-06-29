from odoo import models, fields, api


class CourseRegistration(models.Model):
    _name = 'course.registration'
    _description = 'Course Registration'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    course_num = fields.Char(related='course_id.course_id',string='Course ID')
    course_hour = fields.Float(related='course_id.credit_hours',string='Credit Hours')
    studentid = fields.Char(related='student_id.student_id', string='Student ID')

    course_id = fields.Many2one('courses',string='Course')
    student_id = fields.Many2one('student.profile', string='Student Name')
    #teacher_id = fields.Many2one('teacher.profile', string='Teacher ID')


