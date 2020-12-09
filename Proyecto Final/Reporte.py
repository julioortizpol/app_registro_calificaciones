import webbrowser
from datetime import date
import folium
import os
import matplotlib.pyplot as plt
from Data import Data
from Calculo import Calculo
from Notas import Notas
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

class Reporte:
    def __init__(self, matricula):
        self._database = Data()
        self._estudiante = self._database.consultarById('ESTUDIANTE','ID_ESTUDIANTE',matricula)
        self._calificaiones = self._database.calificacionByEstudiante(matricula)
        self._date = date.today()
        
        self._fig, self._ax = plt.subplots()
        
    #end method

    def get_Date(self):
        today = self._date.today()
        return today.strftime("%m/%d/%Y")
    #end methd

    def literalhtml(self, literal):
        htmlLiteral = self.html_literalColor("A","#0070c0")
        if(literal == "B"):
            htmlLiteral = self.html_literalColor("B","#00b050")
        if(literal == "C"):
            htmlLiteral = self.html_literalColor("C","#ffc000")
        if(literal == "D"):
            htmlLiteral = self.html_literalColor("D","#fa62ef")
        if(literal == "F"):
            htmlLiteral = self.html_literalColor("F","#ff0000")
        return htmlLiteral
    #end method
    def literalMapa(self,literal):
        mapaLiteral='cadetblue'
        if(literal == "B"):
            mapaLiteral="darkgreen"
        if(literal == "C"):
            mapaLiteral="orange"
        if(literal == "D"):
            mapaLiteral="pink"
        if(literal == "F"):
            mapaLiteral="red"
        return mapaLiteral

    #end method

    def html_literalColor(self, literal, color):
        return f'''<td rowspan = 5 style="text-align:center; font-size:200px; color:{color};">{literal}</td>'''
    #end method

    def generateCalificationsRow(self, n):
        nota= Notas([n[3],n[4],n[5],n[6],n[7],n[8],n[9]])
        calc = Calculo(nota) 
        materia = self._database.consultarById('MATERIA', 'CODIGO', n[2])
        print(self._estudiante)
        # promedioPractica = calcular_promedio(calificaciones[0],calificaciones[1])
        # promedioForo = calcular_promedio(calificaciones[2],calificaciones[3])
        # promedioParcial = calcular_promedio(calificaciones[4],calificaciones[5])
        # promedioFinal = calcular_promedio(calificaciones[6],promedioParcial,promedioForo,promedioPractica,False)
        htmlLiteral = self.literalhtml(calc.get_literal())
        return f'''<tr>
        <td style="text-align:center; font-size:25px;"><img src="{self._estudiante[5]}" alt="foto de perfil" /></td>
        <td style="text-align:center; font-size:25px;"><b>{self._estudiante[1]}</b></td>
        <td style="text-align:center; font-size:25px;"><b>{self._estudiante[2]}</b></td>
        <td style="text-align:center; font-size:25px;"><b>{materia[0]}</b></td>
        <td style="text-align:center; font-size:20px;">Practica1 {nota.get_ppractica()}</td>
        <td style="text-align:center; font-size:20px;">Practica2 {nota.get_spractica()}</td>
        {htmlLiteral}
      </tr>
      <tr>
        <td style="text-align:center; font-size:20px;"></td>
        <td style="text-align:center; font-size:20px;"></td>
        <td style="text-align:center; font-size:20px;"></td>
        <td style="text-align:center; font-size:20px;">Foro1 {nota.get_pforo()}</td>
        <td style="text-align:center; font-size:20px;">Foro2 {nota.get_sforo()}</td>
      </tr>
      <tr>
        <td style="text-align:center; font-size:20px;"></td>
        <td style="text-align:center; font-size:20px;"></td>
        <td style="text-align:center; font-size:20px;"></td>
        <td style="text-align:center; font-size:20px;">P. Parcial {nota.get_pparcial()}</td>
        <td style="text-align:center; font-size:20px;">S. Parcial {nota.get_sparcial()}</td>
      </tr>
      <tr>
        <td style="text-align:center; font-size:20px;"></td>
        <td style="text-align:center; font-size:20px;"></td>
        <td style="text-align:center; font-size:20px;"></td>
        <td style="text-align:center; font-size:20px;">Ex. Final {nota.get_final()}</td>
        <td style="text-align:center; font-size:20px;"></td> 
      </tr>
      <tr>
        <td style="text-align:center; font-size:20px;"></td>
        <td style="text-align:center; font-size:20px;"></td>
        <td style="text-align:center; font-size:20px;"></td>
        <td style="text-align:center; font-size:20px;">Promedio {calc.get_pr_final()}</td>
        <td style="text-align:center; font-size:20px;"></td> 
      </tr>'''
    #end method

    # def generateDataGrafico(self,tipo):
    #     self._
    #end method

    def get_report(self):
        actualDate = self.get_Date()
        calificacion = ""
        for cal in self._calificaiones:
            calificacion = calificacion + self.generateCalificationsRow(cal)
        #end for
        mensaje = f'''
        <html>
        <head></head>
        <body>
        
        <center>
        <h2>Sistema de Estudiantes</h2>
        </center>
        <div style="overflow: hidden;">
        <p style="float: left;
        width:33.33333%;
        text-align:left;"></p>
        <p style="float: left;
        width:33.33333%;
        text-align:center; font-size:25px;">Listado de Calificaciones de un Estudiante</p>
        <p style="float: left;
        width:33.33333%;
        text-align:right; font-size:25px;">Fecha: {actualDate}</p>
        </div>
        
        <table style="width:100%">
        <tr>
            <th><div style="color: #0070c0; font-size:30px; font-family: Calibri">Perfil</div></th>
            <th><div style="color: #0070c0; font-size:30px; font-family: Calibri">Matrícula</div></th>
            <th><div style="color: #0070c0; font-size:30px; font-family: Calibri">Nombre</h3></th>
            <th><div style="color: #0070c0; font-size:30px; font-family: Calibri">Materia</div></th>
            <th colspan="2"><div style="color:#0070c0 ; font-size:30px; font-family: Calibri">Calificaciones</div></th>
            <th><div style="color:#0070c0; font-size:30px;font-family: Calibri">Literal</div></th>
        </tr>
        {calificacion}
        
        </table>
        </body>
        </html>
        
        '''
        file = open("Calificaciones.html","w")
        file.write(mensaje)
        file.close()
        webbrowser.open_new_tab('Calificaciones.html')
    #end method
    
    def get_reportM(self,values):
        #0 materia 1 provincia 2 literal
        self._mapaData = self._database.mapaData(values)
        if len(self._mapaData)>0:
            melbourne = (18.8269076, -70.2872627)
            map = folium.Map(location = melbourne, zoom_start=8, titles='literal')
            if values[2]=="TODOS":
                for item in self._mapaData:
                    nota= Notas([item[16],item[17],item[18],item[19],item[20],item[21],item[22]])
                    calc = Calculo(nota)
                    folium.Marker(location = (item[2],item[3]), tooltip=(item[1]), popup=(item[6]),icon=folium.Icon(self.literalMapa(calc.get_literal()))).add_to(map)
                #end loop
                map.save("MateriProvincia.html")
                os.system("MateriProvincia.html")
            else:
                for item in self._mapaData:
                    nota= Notas([item[16],item[17],item[18],item[19],item[20],item[21],item[22]])
                    calc = Calculo(nota)
                    if calc.get_literal()==values[2]:
                        folium.Marker(location = (item[2],item[3]), tooltip=(item[1]), popup=(item[6]),icon=folium.Icon(self.literalMapa(calc.get_literal()))).add_to(map)
                #end loop
                map.save("MapaPorLiteral.html")
                os.system("MapaPorLiteral.html")
            #end condition
        #end condition
    #end method

    def get_reportG(self, values):
        # values=['tipo',[0,2,4],['juan','pedro'],'title','colum','values']
        self._ax.set_title(values[3])
        if values[0]=='barra':
            self._ax.set_xlabel(values[4])
            self._ax.set_ylabel(values[5])
            self._ax.bar(values[1],values[2],color=['blue','green', 'yellow','pink','red',])
            plt.savefig('barra.png')
            # plt.show()
        elif values[0]=='barra3D':
            self._ax = plt.subplot(111,projection= "3d")
            self._ax.set_xlabel(values[4])
            self._ax.set_ylabel(values[5])
            x = np.arange(len(values[1]))
            y = [0,0,0,0,0]
            z = [0,0,0,0,0]
            dx = [1,1,1,1,1]
            dy = [1,1,1,1,1]
            dz = values[2]
            self._ax.bar3d(x,y,z,dx,dy,dz,color=['blue','green', 'yellow','pink','red',])
            self._ax.set_xticks(range(0,5,1))
            self._ax.set_xticklabels(values[1][::1])
            plt.savefig('barra3D.png')
            # plt.show()
        elif values[0]=="pastel":
            self._ax.pie(values[1],autopct="%1.1f%%",)
            self._ax.legend(labels=values[2])
            plt.savefig('pastel.png')
            plt.show()
        elif values[0]=="Comparativo":
            graph1 = values[1]
            graph2 = values[2]
            fig = plt.gcf()
            fig.suptitle(values[3], fontsize=14)
            plt.subplot(1,2,1)
            plt.pie(graph1[1],autopct="%1.1f%%",)
            plt.title(values[4][0])
            plt.legend(labels=graph1[0])
            plt.subplot(1,2,2)
            plt.title(values[4][1])
            plt.pie(graph2[1],autopct="%1.1f%%",)
            plt.legend(labels=graph2[0])
            plt.savefig('Comparativo.png')
            # plt.show()
    #end method
#end class