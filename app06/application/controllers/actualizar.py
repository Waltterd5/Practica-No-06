import web

render = web.template.render('application/views/', base='master')

class Actualizar:        
    def __init__(self):
        pass

    def GET(self):
        return render.actualizar()