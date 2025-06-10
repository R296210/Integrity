#coding: utf-8
#__author__="RINGANG"
#====================================================
#================== www.ringang.com =================

#INICIA LA APP EN MODO QUE-NO-SE-INICIE-PANTALLA-COMPLETA & SE-VEA-EL-MOUSE-EN-SCREEN+DESKTOP
import kivy
kivy.require('2.3.0')

from kivy.config import Config 
Config.set('input', 'mouse', 'mouse, multitouch') 
Config.set("graphics", "fullscreen", "0") #FALSE 0 TRUE 1

from kivy.core.window import Window
Window.show_cursor = True

from kivy.app import App
class CalculadoraApp(App):
    def build(self):
        
        pass

CalculadoraApp().run()
