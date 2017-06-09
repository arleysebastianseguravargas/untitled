from archivos import Utilidades


class Generador:
    def generarTab(self, titulo):
        head = "<title>" + titulo + "</title>"
        return head

    def generarTitulo(self, tipoTitulo, titulo):
        head = "<"+tipoTitulo+ ">" + titulo + "</"+ tipoTitulo+ ">"
        return head

    def generarTabla(self):
        tabla ="<table> [1]</table>"
        utilidad = Utilidades()
        file = utilidad.cargarArchivo("datos.csv")
        filasColumnas = ""
        for i in file:
            x = i.split(",")
            filasColumnas += "<tr><td>"+ x[0] + "</td><td>"+ x[1] +"</td><td>"+ x[2]+\
                             "</td><td>"+ x[3]+"</td><td>"+ x[4]+"</td><td>"+ x[5]+"</td>"
        tabla = tabla.replace("[1]",filasColumnas)
        return tabla


    def generaLista(self, ListaItems):
        tabla = ""
        td = ""

        for i in ListaItems:
            tr = "<tr>"
            for j in i.split(","):
                td = td + "<td>" + j + "</td>"
            tr2 = "</tr>"

            tabla = tabla + tr + td + tr2
            td = ""
        return "<table>" + tabla + "</table>"
