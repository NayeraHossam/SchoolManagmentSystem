from odoo import models, fields, api


class TeacherProfile(models.Model):
    _name = 'teacher.profile'
    _description = 'Teacher Profile'

    name = fields.Char(string='Name')
    department = fields.Char(string='Department')
    courses = fields.Char(string='Courses')
    teacher_id = fields.Integer(string='Teacher ID')

    #course_ids = fields.One2many('courses','teacher_id',string='Courses')


