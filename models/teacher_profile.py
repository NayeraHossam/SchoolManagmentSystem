from odoo import models, fields, api


class TeacherProfile(models.Model):
    _name = 'teacher.profile'
    _description = 'Teacher Profile'

    name = fields.Char(string='Name')
    department = fields.Char(string='Department')
    #courses = fields.Char(string='Courses')
    teacherid = fields.Char(string='Teacher ID',readonly=True)

    course_ids = fields.One2many('courses','teacher_id',string='Courses')

    @api.model
    def create(self, vals):
        last_teacher = self.search([], order='id desc', limit=1)

        if last_teacher and last_teacher.teacherid:
            last_num = int(last_teacher.teacherid.replace('TCH-', ''))
            vals['teacherid'] = f"TCH-{last_num + 1:05d}"
        else:
            vals['teacherid'] = "TCH-00001"

        return super().create(vals)


