#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Faktöriyel Hesaplama")
        grid = QGridLayout()
        
        grid.addWidget(QLabel("Sayı Giriniz:"),1,0)
        self.sayi = QLineEdit()
        grid.addWidget(self.sayi,1,1,1,2)
        
        self.buton = QPushButton("Hesapla")
        grid.addWidget(self.buton,2,1,1,2)
        self.buton.clicked.connect(self.hesapla)
        self.yazi = QLabel("")
        grid.addWidget(self.yazi,3,1)
        
        
        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(grid)
        h_box.addStretch()
        
        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addStretch()
        
        self.setLayout(v_box)
        self.setGeometry(100,100,350,200)
        self.show()
        
    def hesapla(self):
        sayi = 0
        try: sayi = int(self.sayi.text())
        except: pass
        carpim = 1
        
        if (sayi == 0):
            self.yazi.setText(str(sayi) +" sayısının faktoriyeli: " + str(carpim))
        
        elif(sayi > 0):
            if(sayi == 1):
                self.yazi.setText(str(sayi) +" sayısının faktoriyeli: " + str(carpim))
            else:
                for i in range(1,sayi+1):
                    carpim *= i
                self.yazi.setText(str(sayi) +" sayısının faktoriyeli: " + str(carpim))
        elif(sayi < 0):
            self.yazi.setText("Faktöriyel negatif sayılar için geçersizdir.\nLütfen pozitif bir sayı giriniz.")
        else:
            self.yazi.setText("Hatalı veri girişi")
        
uygulama = QApplication(sys.argv)
pencere = MainWindow()
sys.exit(uygulama.exec_())


# In[ ]:




