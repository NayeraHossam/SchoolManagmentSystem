from odoo import models, fields, api


class Courses(models.Model):
    _name = 'courses'
    _description = 'Courses'

    name = fields.Char(string='Name')
    course_id = fields.Char(
        string='Course ID',
        readonly=True)
    credit_hours = fields.Float(string='Credit Hours')
    time = fields.Date(string='Time')
    teacher = fields.Char(related='teacher_id.name',string='Teacher')

    grade_ids = fields.One2many(
        'student.grades',
        'course_id',
        string='Grades'
    )
    teacher_id = fields.Many2one('teacher.profile', string='Teacher ID')

    _sql_constraints = [
        ('unique_course_id', 'unique(course_id)', 'Course ID must be unique!')
    ]

    @api.model
    def create(self, vals):
        last_course = self.search([], order='id desc', limit=1)

        if last_course and last_course.course_id:
            last_num = int(last_course.course_id.replace('CRS-', ''))
            vals['course_id'] = f"CRS-{last_num + 1:05d}"
        else:
            vals['course_id'] = "CRS-00001"

        return super().create(vals)









    #student_ids = fields.One2many('student.profile', 'course_id', string='Student IDs')


