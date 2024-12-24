from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import os
from os import path
import sys
import pickle as p
import pandas as pd
import math

form_class,_ = loadUiType(path.join(path.dirname(__file__),'m.ui'))

class MainApp(QWidget,form_class):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QWidget.__init__(self)
        self.setFixedSize(740,540)
        self.setupUi(self)
        self.handl_button()

    def handl_button(self):
        self.button.clicked.connect(self.handle_predicate)

    def handle_predicate(self):
        lis=[]
        #################################
        c_1 = self.com1.currentText()
        if(c_1 == "Resediential"):
            A=2
        if(c_1 == "School extension"):
                A=3
        if(c_1 == "Schools"):
                A=4
        lis.append(A)
        #################################
        c_2 = self.com2.currentText()
        if(c_2 == "60 – 100"):
            B=1
        if(c_2 == "100 – 200"):
            B=2
        if(c_2 == "200 – 300"):
            B=3
        if(c_2 == "300 – 400"):
            B=4
        if(c_2 == "400 – 500"):
            B=5
        if(c_2 == "500 – 600"):
            B=6
        if(c_2 == "600 – 700"):
            B=7
        if(c_2 == "700 – 800"):
            B=8
        if(c_2 == "800 – 900"):
            B=9
        if(c_2 == "900 – 1000"):
            B=10
        if(c_2 == "1000 – 1100"):
            B=11
        if(c_2 == "1100 – 1200"):
            B=12    
        lis.append(B)                        
        #################################
        c_3 = self.com3.currentText()
        if(c_3 == "1"):
            C=1
        if(c_3 == "2"):
            C=2
        if(c_3 == "3"):
            C=3
        if(c_3 == "4"):
            C=4 
        if(c_3 == "5"):
            C=5
        if(c_3 == "6"):
            C=6
        if(c_3 == "7"):
            C=7
        if(c_3 == "8"):
            C=8
        lis.append(C)
        #################################
        c_4 = self.com4.currentText()
        if(c_4 == "None"):
            D=0
        if(c_4 == "Isolated"):
            D=1
        if(c_4 == "Strap"):
            D=2
        if(c_4 == "Piles"):
            D=3
        if(c_4 == "Mat"):
            D=4
        lis.append(D)
        #################################
        c_5 = self.com5.currentText()
        if(c_5 == "Solid"):
            E=1
        c_5 = self.com5.currentText()
        if(c_5 == "Ribbed"):
            E=2
        c_5 = self.com5.currentText()
        if(c_5 == "Drop beams"):
            E=3
        lis.append(E)
        #################################
        c_6 = self.com6.currentText()
        if(c_6 == "0"):
            F=0
        if(c_6 == "1"):
            F=1
        if(c_6 == "2"):
            F=2
        lis.append(F)
        #################################
        c_7 = self.com7.currentText()
        if(c_7 == "None"):
            G=0
        if(c_7 == "Normal plaster"):
            G=1
        if(c_7 == "Marmarina"):
            G=2
        if(c_7 == "Natural stone"):
            G=3
        lis.append(G)
        #################################
        c_8 = self.com8.currentText()
        if(c_8 == "None"):
            H=0
        if(c_8 == "Central AC+False ceiling"):
            H=1
        if(c_8 == "Split unit"):
            H=2
        lis.append(H)
        #################################
        c_9 = self.com9.currentText()
        if(c_9 == "Ceramic"):
            I=1
        if(c_9 == "Terrazzo"):
            I=2
        if(c_9 == "Porcelain"):
            I=3
        lis.append(I)
        #################################
        c_10 = self.com10.currentText()
        if(c_10 == "Basic"):
            J=1
        if(c_10 == "Luxury"):
            J=2
        lis.append(J)
        #################################
        c_11 = self.com11.currentText()
        if(c_11 == "Basic"):
            K=1
        if(c_11 == "Luxury"):
            K=2
        lis.append(K)
        #################################
        df = pd.read_csv('dataff.csv')
        target_column = ['costLS']
        #predictors = list(set(list(df.columns))-set(target_column))
        predictors = ["Areaoftypicalfloor", "UseOfBuilding", "NoFloors", "FootingType"]
        m=df[target_column].max()
        loadmodel=p.load(open('finaln1.pkl','rb'))
        #lis=lis/df[predictors].max()
        lis=[1,2,1,1]/df[predictors].max()
        res=abs(loadmodel.predict([lis]))
        n=float(m)
        r=float(res)
        result =math.floor(r*n)
        
        QMessageBox.information(self," Finally Cost "," Your estimate cost is : "+str(result))
        

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()