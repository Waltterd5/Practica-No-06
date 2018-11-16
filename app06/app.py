import web
        
urls = (
    '/', 'application.controllers.index.Index',
    '/agregar', 'application.controllers.agregar.Agregar',
    '/borrar', 'application.controllers.borrar.Borrar',
    '/actualizar', 'application.controllers.actualizar.Actualizar' 
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()