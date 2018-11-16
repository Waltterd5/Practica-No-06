import web

render = web.template.render('application/views/', base='master')

class Borrar:        
    def __init__(self):
        pass

    def GET(self):
        return render.borrar()
        