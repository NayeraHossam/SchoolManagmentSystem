from odoo import http
from odoo.http import request


class SchoolPortal(http.Controller):

    @http.route('/student', auth='public', website=True)
    def open_student(self, **kw):
        return request.redirect('/web/login')
        #action = request.env.ref(
        #    'school_system.student_profile_action'
        #).read()[0]

        #return request.redirect(
        #    '/web#action=%s&model=student.profile&view_type=list'
        #    % action['id']
        #)

    @http.route('/teacher', auth='public', website=True)
    def open_teacher(self, **kw):
        return request.redirect('/web/login')
        #action = request.env.ref(
        #    'school_system.teacher_profile_action'
        #).read()[0]

        #return request.redirect(
        #    'web#action=202&model=courses&view_type=list'
        #    % action['id']
        #)





    @http.route('/choose-role', auth='public', website=True)
    def choose_role(self, **kw):
        request.session.logout()
        return request.render(
            'school_system.role_selection_page'
        )

