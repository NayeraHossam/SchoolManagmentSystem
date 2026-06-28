from odoo import models,fields,api

class StudentProfile(models.Model):
    _name = 'student.profile'
    _description = 'Student Profile'

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    department = fields.Char(string='Department')
    student_id = fields.Char(string='Student ID',readonly=True)
    total_hours = fields.Float(compute='_compute_total_hours', store=True,string='Total Hours')
    gpa = fields.Float(compute='_compute_gpa',string='GPA')

    grade_ids = fields.One2many('student.grades','student_id',string='Grades')
    course_id = fields.Many2one('courses')
    course_ids = fields.One2many('course.registration','student_id',string='Course IDs')

    #create unique ID
    @api.model
    def create(self, vals):
        last_student = self.search([], order='id desc', limit=1)

        if last_student and last_student.student_id:
            last_num = int(last_student.student_id.replace('STU-', ''))
            vals['student_id'] = f"STU-{last_num + 1:05d}"
        else:
            vals['student_id'] = "STU-00001"

        return super().create(vals)


    #calculate the total credit hours
    @api.depends('course_ids.course_hour', 'grade_ids.percentage')
    def _compute_total_hours(self):
        for rec in self:
            total = 0.0

            for grade in rec.grade_ids:
                if grade.percentage >= 50:
                    total += grade.course_id.credit_hours

            rec.total_hours = total


    #calculate the gpa
    @api.depends(
        'grade_ids.percentage',
        'grade_ids.course_id.credit_hours'
    )
    def _compute_gpa(self):
        for student in self:
            total_points = 0.0
            total_credits = 0.0

            for grade in student.grade_ids:
                credits = grade.course_id.credit_hours

                # Convert percentage to GPA points (example 4.0 scale)
                if grade.percentage >= 90:
                    points = 4.0
                elif grade.percentage >= 80:
                    points = 3.0
                elif grade.percentage >= 70:
                    points = 2.0
                elif grade.percentage >= 60:
                    points = 1.0
                else:
                    points = 0.0

                total_points += points * credits
                total_credits += credits

            student.gpa = (
                total_points / total_credits
                if total_credits else 0.0
            )

    # @api.depends('grade_ids.grade')
    # def _compute_gpa(self):
    #    for rec in self:
    #        rec.c_gpa = sum(rec.grade_ids.mapped('grade'))/4.00
    # def update_student_ids(self):
    #    students = self.search([], order='id')

    #    for index, student in enumerate(students, start=1):
    #        student.student_id = f"STU-{index:05d}"

    # def action_update_student_ids(self):
    #    self.update_student_ids()








