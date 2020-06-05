# (c) Didier  LECLERC 2020 CMSIG MTES-MCTRCT/SG/SNUM/UNI/DRC Site de Rouen
# créé mars 2020 version 1.0


from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QAction, QMenu , QApplication, QMessageBox, QFileDialog, QPlainTextEdit, QDialog, QDockWidget, QVBoxLayout, QTabWidget, QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon, QStandardItem, QStandardItemModel

from . import bibli_ihm_camino
from .bibli_ihm_camino import *
from . import bibli_camino
from .bibli_camino import *

from qgis.core import *
from qgis.gui import *

import qgis
import os
import subprocess

class Ui_Dialog_Camino_onglet(object):
    def __init__(self):
        self.iface = qgis.utils.iface
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        self.lScreenDialog, self.hScreenDialog = 810, 700
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,self.lScreenDialog, self.hScreenDialog).size()).expandedTo(Dialog.minimumSizeHint()))
        Dialog.setWindowTitle("CAMINO (mining titles) International...")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        iconSource = bibli_camino.getThemeIcon("camino2.png")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconSource), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)

        #=====================================================
        #Image
        self.labelImage = QtWidgets.QLabel(Dialog)
        myPath = os.path.dirname(__file__)+"/icons/camino2.jpg";
        myDefPath = myPath.replace("\\","/");
        carIcon = QtGui.QImage(myDefPath)
        self.labelImage.setPixmap(QtGui.QPixmap.fromImage(carIcon))
        self.labelImage.setGeometry(QtCore.QRect(630, 10, 160, 100))
        self.labelImage.setObjectName("labelImage")
        
        #=====================================================
        #Param File URL
        monFichierPath = os.path.join(os.path.dirname(__file__))
        monFichierPath = monFichierPath.replace("\\","/") + "//urlcamino.par"
        self.monFichierPath = monFichierPath

        #=====================================================
        #Param File LOGIN
        monFichierPathLogin = os.path.join(os.path.dirname(__file__))
        monFichierPathLogin = monFichierPathLogin.replace("\\","/") + "//logincamino.par"
        self.monFichierPathLogin = monFichierPathLogin
        #---------
        monFichierPathLoginCourriel = os.path.join(os.path.dirname(__file__))
        monFichierPathLoginCourriel = monFichierPathLoginCourriel.replace("\\","/") + "//logincaminocourriel.par"
        self.monFichierPathLoginCourriel = monFichierPathLoginCourriel
        #=====================================================
        #Groupe liseré gauche
        self.groupBoxLeft_1 = QtWidgets.QGroupBox(Dialog)
        self.groupBoxLeft_1.setGeometry(QtCore.QRect(10,10,610,100))
        self.groupBoxLeft_1.setObjectName("groupBoxLeft_1")

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(245,255,0,125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Base,brush)
        self.groupBoxLeft_1.setPalette(palette)
        
        #Radio Affichage Etiquettes 
        self.groupBoxRadio = QtWidgets.QGroupBox(self.groupBoxLeft_1)
        self.groupBoxRadio.setGeometry(QtCore.QRect(10,5,125,85))
        self.groupBoxRadio.setObjectName("groupBoxRadio")
        self.groupBoxRadio.setStyleSheet("QGroupBox { color: red; }")
        self.radioOptionMdp3 = QtWidgets.QRadioButton(self.groupBoxRadio)
        self.radioOptionMdp3.setGeometry(QtCore.QRect(10,15,150,23))
        self.radioOptionMdp3.setObjectName("radioOptionMdp3")
        self.radioOptionMdp1 = QtWidgets.QRadioButton(self.groupBoxRadio)
        self.radioOptionMdp1.setGeometry(QtCore.QRect(10,37,150,23))
        self.radioOptionMdp1.setObjectName("radioOptionMdp1")
        self.radioOptionMdp2 = QtWidgets.QRadioButton(self.groupBoxRadio)
        self.radioOptionMdp2.setGeometry(QtCore.QRect(10,59,150,23))
        self.radioOptionMdp2.setObjectName("radioOptionMdp2")
        self.radioOptionMdp2.setChecked(True)
        
        #Label et zone LOGIN   
        self.labelLogin = QtWidgets.QLabel(self.groupBoxLeft_1)
        self.labelLogin.setGeometry(QtCore.QRect(100,10,120,18))
        self.labelLogin.setObjectName("labelLogin")
        self.labelLogin.setAlignment(Qt.AlignRight)
        #-----------
        self.textEditLogin = QtWidgets.QTextEdit(self.groupBoxLeft_1)
        self.textEditLogin.setGeometry(QtCore.QRect(220,10,270,23))
        self.textEditLogin.setObjectName("textEditLogin")

        #Label et zone ORGANISATION   
        self.labelOrga = QtWidgets.QLabel(self.groupBoxLeft_1)
        self.labelOrga.setGeometry(QtCore.QRect(140,38,80,18))
        self.labelOrga.setObjectName("labelOrga")
        self.labelOrga.setAlignment(Qt.AlignRight)
        #-----------
        self.textEditOrga = QtWidgets.QTextEdit(self.groupBoxLeft_1)
        self.textEditOrga.setGeometry(QtCore.QRect(220,38,270,23))
        self.textEditOrga.setObjectName("textEditOrga")

        #Label et zone MDP  
        self.labelMdp = QtWidgets.QLabel(self.groupBoxLeft_1)
        self.labelMdp.setGeometry(QtCore.QRect(140,65,80,18))
        self.labelMdp.setObjectName("labelMdp")
        self.labelMdp.setAlignment(Qt.AlignRight)
        #-----------
        self.textEditMdp = QtWidgets.QTextEdit(self.groupBoxLeft_1)
        self.textEditMdp.setGeometry(QtCore.QRect(220,65,270,23))
        self.textEditMdp.setObjectName("textEditMdp")
        #-----------
        #-----------
        #Label et zone COURRIEL   
        self.labelCourriel = QtWidgets.QLabel(self.groupBoxLeft_1)
        self.labelCourriel.setGeometry(QtCore.QRect(100,20,120,18))
        self.labelCourriel.setObjectName("labelCourriel")
        self.labelCourriel.setAlignment(Qt.AlignRight)
        #-----------
        self.textEditCourriel = QtWidgets.QTextEdit(self.groupBoxLeft_1)
        self.textEditCourriel.setGeometry(QtCore.QRect(220,20,270,23))
        self.textEditCourriel.setObjectName("textEditCourriel")

        #Label et zone MDP COURRIEL  
        self.labelMdpCourriel = QtWidgets.QLabel(self.groupBoxLeft_1)
        self.labelMdpCourriel.setGeometry(QtCore.QRect(140,55,80,18))
        self.labelMdpCourriel.setObjectName("labelMdpCourriel")
        self.labelMdpCourriel.setAlignment(Qt.AlignRight)
        #-----------
        self.textEditMdpCourriel = QtWidgets.QTextEdit(self.groupBoxLeft_1)
        self.textEditMdpCourriel.setGeometry(QtCore.QRect(220,55,270,23))
        self.textEditMdpCourriel.setObjectName("textEditMdpCourriel")

        #ComboBox Adresse 
        self.labelAdresse = QtWidgets.QLabel(Dialog)
        self.labelAdresse.setGeometry(QtCore.QRect(20,120,100,18))
        self.labelAdresse.setObjectName("labelAdresse")
        self.labelAdresse.setAlignment(Qt.AlignRight)

        self.comboAdresse = QtWidgets.QComboBox(Dialog)
        self.comboAdresse.setGeometry(QtCore.QRect(130,120,660,23))
        self.comboAdresse.setObjectName("comboAdresse")

        #Zone affichage  
        self.resultTextEdit = QtWidgets.QTextEdit(Dialog)
        self.resultTextEdit.setGeometry(QtCore.QRect(5, 150, 650,90))
        self.resultTextEdit.setObjectName("resultTextEdit") 
        
        #Zone Filtre Affichage  
        #self.resultFilterCombo = QtWidgets.QComboBox(Dialog)
        #self.resultFilterCombo.setGeometry(QtCore.QRect(800, 150, 295, 500))
        #self.resultFilterCombo.setObjectName("resultFilterCombo") 
        
        #==========================              
        #Zone Onglets
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QtCore.QRect(5, 250, 800,440))
        #--------------------------
        self.tab_widget_map = QWidget()
        self.tab_widget_map.setObjectName("tab_widget_map")
        labelTab1 = QtWidgets.QApplication.translate("camino_onglet_ui", "   Map   ", None)
        self.tabWidget.addTab(self.tab_widget_map,labelTab1)
        #--------------------------
        self.tab_widget_Provider = QWidget()
        self.tab_widget_Provider.setObjectName("tab_widget_Provider")
        labelTab2 = QtWidgets.QApplication.translate("camino_onglet_ui", "   Provider   ", None)
        #self.tabWidget.addTab(self.tab_widget_Provider,labelTab2)
        #--------------------------
        self.tab_widget_Data = QWidget()
        self.tab_widget_Data.setObjectName("tab_widget_Data")
        labelTab3 = QtWidgets.QApplication.translate("camino_onglet_ui", "   Data   ", None)
        self.tabWidget.addTab(self.tab_widget_Data,labelTab3)
        #--------------------------
        self.tab_widget_Filter = QWidget()
        self.tab_widget_Filter.setObjectName("tab_widget_Filter")
        labelTab4 = QtWidgets.QApplication.translate("camino_onglet_ui", "   Filter   ", None)
        self.tabWidget.addTab(self.tab_widget_Filter,labelTab4)
        #--------------------------
        self.tab_widget_Critere = QWidget()
        self.tab_widget_Critere.setObjectName("tab_widget_Critere")
        labelTab5 = QtWidgets.QApplication.translate("camino_onglet_ui", "  Filter with criteria  ", None)
        self.tabWidget.addTab(self.tab_widget_Critere,labelTab5)
        self.tabWidget.setCurrentIndex(3)
        #--------------------------
        # premier Onglet
        #====== Zone affichage Layer 
        self.resultLayer = QtWidgets.QTextEdit(self.tab_widget_map)
        self.resultLayer.setGeometry(QtCore.QRect(5, 250, 790,400))
        self.resultLayer.setObjectName("resultLayer") 
        self.resultLayer.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "Map display", None))
        #------       
        self.resultLayerLayout = QVBoxLayout()
        self.resultLayerLayout.addWidget(self.resultLayer)
        self.tab_widget_map.setLayout(self.resultLayerLayout)
        # deuxième Onglet
        #====== Zone affichage Web structure 
        self.resultProvider = QtWidgets.QTextEdit(self.tab_widget_Provider)
        self.resultProvider.setGeometry(QtCore.QRect(5, 230, 790,400))
        self.resultProvider.setObjectName("resultProvider")
        self.resultProvider.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "Structure display", None))
        #------       
        self.resultProviderLayout = QVBoxLayout()
        self.resultProviderLayout.addWidget(self.resultProvider)
        self.tab_widget_Provider.setLayout(self.resultProviderLayout)
        # troisième Onglet
        #====== Zone affichage données 
        self.resultData = QtWidgets.QTextEdit(self.tab_widget_Data)
        self.resultData.setGeometry(QtCore.QRect(5, 230, 790,400))
        self.resultData.setObjectName("resultData")
        self.resultData.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "Data display", None))
        #------       
        self.resultDataLayout = QVBoxLayout()
        self.resultDataLayout.addWidget(self.resultData)
        self.tab_widget_Data.setLayout(self.resultDataLayout)
        # quatrième Onglet
        #====== Zone affichage données 
        self.resulFilter = QtWidgets.QTextEdit(self.tab_widget_Filter)
        self.resulFilter.setGeometry(QtCore.QRect(5, 230, 790,390))
        self.resulFilter.setObjectName("resulFilter")
        self.resulFilter.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "Filter display", None))
        #------       
        self.resultFilterLayout = QVBoxLayout()
        self.resultFilterLayout.addWidget(self.resulFilter)
        self.tab_widget_Filter.setLayout(self.resultFilterLayout)        
        # cinquième Onglet
        #====== Zone affichage données avec critères
        self.resulCritere = QtWidgets.QTextEdit(self.tab_widget_Critere)
        self.resulCritere.setGeometry(QtCore.QRect(10, 10, 775, 395))
        self.resulCritere.setObjectName("resulCritere")
        #------ Création de l'IHM Critère
        createIhmCritere(self)     
        #==========================              

        #Boutons  
        self.valideLoginMdp = QtWidgets.QPushButton(self.groupBoxLeft_1)
        self.valideLoginMdp.setGeometry(QtCore.QRect(500, 10, 100,23))
        self.valideLoginMdp.setObjectName("valideLoginMdp")
        #------       
        self.okhButton = QtWidgets.QPushButton(self.groupBoxLeft_1)
        self.okhButton.setGeometry(QtCore.QRect(500, 38, 100,23))
        self.okhButton.setObjectName("okhButton")
        #------       
        self.helpButton = QtWidgets.QPushButton(self.groupBoxLeft_1)
        self.helpButton.setGeometry(QtCore.QRect(500, 65, 100,23))
        self.helpButton.setObjectName("helpButton")
        self.helpButton.setStyleSheet("QPushButton { color: green; }")
        #------       
        #Filtre bouton multi selection rows 
        self.buttonFilter = QtWidgets.QPushButton(Dialog)
        self.buttonFilter.setGeometry(QtCore.QRect(670, 180, 120, 23))
        self.buttonFilter.setObjectName("buttonFilter")
        self.buttonFilter.setStyleSheet("QPushButton { color: red; }")
        self.buttonFilter.setVisible(False)
        #Label nb occurrences
        self.labelOccurrence = QtWidgets.QLabel(Dialog)
        self.labelOccurrence.setGeometry(QtCore.QRect(670,215,120,18))
        self.labelOccurrence.setObjectName("labelOccurrence")
        self.labelOccurrence.setAlignment(Qt.AlignCenter)    
        self.labelOccurrence.setStyleSheet("QLabel { color: red; }")
        self.labelOccurrence.setVisible(False)
        #------       
        #------  
        #Connections  
        self.helpButton.clicked.connect(Dialog.myHelpCamino)
        self.okhButton.clicked.connect(Dialog.reject)
        self.valideLoginMdp.clicked.connect(Dialog.findTokenApiCamino)
        self.radioOptionMdp1.toggled.connect(Dialog.showHideLogin)
        self.radioOptionMdp2.toggled.connect(Dialog.showHideLogin)
        self.radioOptionMdp3.toggled.connect(Dialog.showHideLogin)
        self.showHideLogin()                                     
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        #========================== 
        #Alimentation de la ComboBox Adresse
        self.returnAdresse = self.returnDicoFlux(self.monFichierPath)
        modelComboAdresse = QStandardItemModel()
        for key, value in self.returnAdresse.items() :
            valueCombo = "%s \t--->>  %s" %(str(value[1]), str(value[0]))
            modelComboAdresseCol1 = QStandardItem(str(valueCombo))
            modelComboAdresseCol2 = QStandardItem(str(key))
            modelComboAdresse.appendRow([modelComboAdresseCol1, modelComboAdresseCol2])
        self.comboAdresse.setModel(modelComboAdresse)
        #========================== 
        self.retranslateUi(Dialog)
        returnToken = ""
                                       
    def findTokenApiCamino(self):
        iden = self.textEditLogin.toPlainText()
        orga = self.textEditOrga.toPlainText()        
        mdp  = self.textEditMdp.toPlainText() 
        idenCourriel = self.textEditCourriel.toPlainText()
        mdpCourriel  = self.textEditMdpCourriel.toPlainText()                 
        if self.radioOptionMdp2.isChecked() :
           fluxAdresse  = self.returnAdresse[self.comboAdresse.currentIndex()][0]
           fluxTitre    = self.returnAdresse[self.comboAdresse.currentIndex()][1]
           fluxProvider = self.returnAdresse[self.comboAdresse.currentIndex()][2]
           #------       
           self.resultTextEdit.clear()
           zMess = self.zMess
           zMess += self.zMess3 + " : \t" + str(fluxAdresse) + "\n"
           zMess += self.zMess4 + " : \t" + str(fluxTitre) + "\n"
           zMess += self.zMess5 + " : \t" + str(fluxProvider)
           self.resultTextEdit.setText(zMess)
           #------       
           openLayer(self, fluxAdresse,fluxTitre,fluxProvider)
        elif self.radioOptionMdp1.isChecked() :
           #affiche dans la zone
           if (iden == "" or mdp == "" or orga == "") :
               myTokenTitre = QtWidgets.QApplication.translate("camino_onglet_ui", "Warning !!", None)
               myToken = QtWidgets.QApplication.translate("camino_onglet_ui", "Please enter your username, organization and password please.", None)
               QMessageBox.warning(None, myTokenTitre,myToken)
           else :
               mGestionLogin("SAVE", self.monFichierPathLogin, iden, orga) 
               fluxAdresse  = self.returnAdresse[self.comboAdresse.currentIndex()][0]
               fluxTitre    = self.returnAdresse[self.comboAdresse.currentIndex()][1]
               fluxProvider = self.returnAdresse[self.comboAdresse.currentIndex()][2]
               #------       
               self.resultTextEdit.clear()
               zMess = self.zMess
               zMess += self.zMess1 + " : " + str(iden) + " " + self.zMessOrga + " : " + str(orga) + " " + self.zMess2 + " : " + str(mdp) +"\n"
               zMess += self.zMess3 + " : \t" + str(fluxAdresse) + "\n"
               zMess += self.zMess4 + " : \t" + str(fluxTitre) + "\n"
               zMess += self.zMess5 + " : \t" + str(fluxProvider)
               self.resultTextEdit.setText(zMess)
               #------       
               #============
               #Gestion de l'adresse et du login
               mFindCaminoAdresse, mCodeUrl, mSepMdp, mSepAdresse = "https://", "%40", ":", "@"  
               mPos = fluxAdresse.find(mFindCaminoAdresse)
               if mPos == -1 :
                  urlMySourceLogin = fluxAdresse
               else :
                  urlMySourceLogin = fluxAdresse[0:len(mFindCaminoAdresse)] + iden + mCodeUrl + orga + mSepMdp + mdp + mSepAdresse + fluxAdresse[len(mFindCaminoAdresse):]
               if self.radioOptionMdp1.isChecked() : fluxAdresse = urlMySourceLogin
               #============
               openLayer(self, fluxAdresse,fluxTitre,fluxProvider)
        elif self.radioOptionMdp3.isChecked() :
           #affiche dans la zone
           if (idenCourriel == "" or mdpCourriel == "") :
               myTokenTitre = QtWidgets.QApplication.translate("camino_onglet_ui", "Warning !!", None)
               myToken = QtWidgets.QApplication.translate("camino_onglet_ui", "Please enter your mail address and password please.", None)
               QMessageBox.warning(None, myTokenTitre,myToken)
           else :
               mGestionLoginCourriel("SAVE", self.monFichierPathLoginCourriel, idenCourriel) 
               fluxAdresse  = self.returnAdresse[self.comboAdresse.currentIndex()][0]
               fluxTitre    = self.returnAdresse[self.comboAdresse.currentIndex()][1]
               fluxProvider = self.returnAdresse[self.comboAdresse.currentIndex()][2]
               #------       
               self.resultTextEdit.clear()
               #Gestion de l'adresse et du login
               mFindCaminoAdresse, mCodeUrl, mSepMdp, mSepAdresse = "https://", "%40", ":", "@"  
               idenCourriel = idenCourriel.replace(mSepAdresse, mCodeUrl)
               zMess = self.zMess
               zMess += self.zMess1 + " : " + str(idenCourriel) + " " + self.zMess2 + " : " + str(mdpCourriel) +"\n"
               zMess += self.zMess3 + " : \t" + str(fluxAdresse) + "\n"
               zMess += self.zMess4 + " : \t" + str(fluxTitre) + "\n"
               zMess += self.zMess5 + " : \t" + str(fluxProvider)
               self.resultTextEdit.setText(zMess)
               #------       
               #============
               #Gestion de l'adresse et du login
               mPos = fluxAdresse.find(mFindCaminoAdresse)
               if mPos == -1 :
                  urlMySourceLogin = fluxAdresse
               else :
                  urlMySourceLogin = fluxAdresse[0:len(mFindCaminoAdresse)] + idenCourriel + mSepMdp + mdpCourriel + mSepAdresse + fluxAdresse[len(mFindCaminoAdresse):]
               if self.radioOptionMdp3.isChecked() : fluxAdresse = urlMySourceLogin
               #============
               openLayer(self, fluxAdresse,fluxTitre,fluxProvider)               
    #------       
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("camino_onglet_ui", "CAMINO (mining titles) International...", None))
        self.labelCourriel.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "mail address : ", None))
        self.labelMdpCourriel.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "Password : ", None))
        self.labelLogin.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "First/Last name : ", None))
        self.labelOrga.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "Organization : ", None))
        self.labelMdp.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "Password : ", None))
        self.helpButton.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "Help", None))
        self.okhButton.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "Close", None))
        self.buttonFilter.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "multi-line filter", None))
        self.valideLoginMdp.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "layer loading", None))
        self.labelAdresse.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "layer address : ", None))
        self.radioOptionMdp1.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "with identifier", None))
        self.radioOptionMdp2.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "without identifier", None))
        self.radioOptionMdp3.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "with email address", None))
        self.groupBoxRadio.setTitle(QtWidgets.QApplication.translate("camino_onglet_ui", " Login ", None))
        self.zMess = QtWidgets.QApplication.translate("camino_onglet_ui", "Here is the return of the Camino API : ", None) +"\n"
        self.zMess1 = QtWidgets.QApplication.translate("camino_onglet_ui", "Username", None)
        self.zMessOrga = QtWidgets.QApplication.translate("camino_onglet_ui", "Organization", None)
        self.zMess2 = QtWidgets.QApplication.translate("camino_onglet_ui", "and Password", None)
        self.zMess3 = QtWidgets.QApplication.translate("camino_onglet_ui", "layer adress", None)
        self.zMess4 = QtWidgets.QApplication.translate("camino_onglet_ui", "name adress", None)
        self.zMess5 = QtWidgets.QApplication.translate("camino_onglet_ui", "provider adress", None)

     #------       
    def returnDicoFlux(self,monFichierPath): return loadFichierParam(self.monFichierPath)
    
    def returnIcon(self, iconAdress) :
        iconSource = iconAdress
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconSource), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon

    #-----------------------------------
    def showHideCtrl(self,Dialog):
        lScreen, hScreen =  QDesktopWidget().width(), QDesktopWidget().height()
        lDelta = 300 if self.caseFilter.isChecked() else 0
        hDelta =   0 if self.caseFilter.isChecked() else 0
        x, y = (lScreen/2) - (self.lScreenDialog + lDelta)/2, (hScreen/2) - (self.hScreenDialog + hDelta)/2
        self.move(x, y)
        self.resize(self.lScreenDialog + lDelta, self.hScreenDialog + hDelta)
        return
        
    #-----------------------------------
    def showHideLogin(self):
        if self.radioOptionMdp2.isChecked() :
           self.labelLogin.hide()
           self.textEditLogin.hide()
           self.labelOrga.hide()
           self.textEditOrga.hide()
           self.labelMdp.hide()
           self.textEditMdp.hide()
           #-------
           self.labelCourriel.hide()
           self.textEditCourriel.hide()
           self.labelMdpCourriel.hide()
           self.textEditMdpCourriel.hide()           
        elif self.radioOptionMdp1.isChecked() :
           mIden, mOrga = mGestionLogin("RESTORE", self.monFichierPathLogin, '', '') 
           if self.textEditLogin.toPlainText() == '' : self.textEditLogin.setPlainText(mIden) 
           if self.textEditOrga.toPlainText() == '' : self.textEditOrga.setPlainText(mOrga)
           self.labelLogin.show()
           self.textEditLogin.show()
           self.labelOrga.show()
           self.textEditOrga.show()
           self.labelMdp.show()
           self.textEditMdp.show()
           #-------
           self.labelCourriel.hide()
           self.textEditCourriel.hide()
           self.labelMdpCourriel.hide()
           self.textEditMdpCourriel.hide()  
        elif self.radioOptionMdp3.isChecked() :
           mIdenCourriel = mGestionLoginCourriel("RESTORE", self.monFichierPathLoginCourriel, '') 
           if self.textEditCourriel.toPlainText() == '' : self.textEditCourriel.setPlainText(mIdenCourriel) 
           self.labelCourriel.show()
           self.textEditCourriel.show()
           self.labelMdpCourriel.show()
           self.textEditMdpCourriel.show()
           #-------
           self.labelLogin.hide()
           self.textEditLogin.hide()
           self.labelOrga.hide()
           self.textEditOrga.hide()
           self.labelMdp.hide()
           self.textEditMdp.hide()
        return 
        
    #-----------------------------------
    def myHelpCamino(self):
        MonFichierPath = os.path.join(os.path.dirname(__file__) + "/doc/")
        MonFichierPath = MonFichierPath.replace("\\","/")        
        MonFichierReport = os.path.join(MonFichierPath, "camino_doc.pdf")
        execPdf(MonFichierReport)
        return 