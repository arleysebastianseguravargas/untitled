import cherrypy,os
from generador import Generador
from template import Template


class goodAndDevil(object):
    @cherrypy.expose
    def index(self):



        miGenerador = Generador()
        pagina =""
        template = Template()
        pagina = template.TEMPLATE.replace("[1]",miGenerador.generarTab("Destroyer"))
        pagina = pagina.replace("[2]",miGenerador.generarTitulo("h1","Game Score"))
        pagina = pagina.replace("[3]",miGenerador.generarTabla())
        return pagina





if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.config.update({'server.socket_host': '127.0.0.1', })
    cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')), })
    cherrypy.quickstart(goodAndDevil(), '/', conf)

