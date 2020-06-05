# (c) Didier  LECLERC 2020 CMSIG MTES-MCTRCT/SG/SNUM/UNI/DRC Site de Rouen
# créé mars 2020 version 1.0

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog

from qgis.core import *
from .about import Ui_Dialog

class Dialog(QDialog, Ui_Dialog):
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
		
