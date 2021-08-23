# (c) Didier  LECLERC 2020 CMSIG MTES-MCTRCT/SG/SNUM/UNI/DRC Site de Rouen
# créé mars 2020 version 1.0

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog
from qgis.core import *

from .camino_onglet_ui import Ui_Dialog_Camino_onglet
from . import bibli_ihm_camino
from .bibli_ihm_camino import *

class Dialog(QDialog, Ui_Dialog_Camino_onglet):
      def __init__(self):
          QDialog.__init__(self)
          self.setupUi(self)

      def reject(self):
          try :
            bibli_ihm_camino.saveRequestCritere(self, [self.mDicCaseDom, self.mDicCaseType, self.mDicCaseStatus, self.mDicCaseZoneLibre], mOption = "SaveQuit")
          except:
            pass

          self.hide()        
