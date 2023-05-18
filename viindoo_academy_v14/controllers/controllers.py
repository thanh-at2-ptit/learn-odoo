from odoo import http

class Academy(http.Controller):
    
    # @http.route('/academy/academy/', auth='public')
    # def index(self, **kw):
    #     return http.request.render('academy.index', {})
    #     return"Hello, world"
    
    # @http.route('/academy/academy/', auth='public')
    # def index(self, **kw):
    #     return http.request.render('viindoo_academy_v14.academy', {
    #         'class': ["Class1", "Class 2", "Class 3"],
    #         })

    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['academy.teacher']
        return http.request.render('viindoo_academy_v14.academy', {
            'teachers': Teachers.search([])
        })
        
    # Create automatic route
    # @http.route('/academy/<name>/', auth='public', website=True)
    # def teacher(self, name):
    #     return '<h1>{}</h1>'.format(name)