# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(562, 238)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.gridLayout_2 = QGridLayout(self.configGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.locLineEdit = QLineEdit(self.configGroupBox)
        self.locLineEdit.setObjectName(u"locLineEdit")

        self.horizontalLayout.addWidget(self.locLineEdit)

        self.locButton = QPushButton(self.configGroupBox)
        self.locButton.setObjectName(u"locButton")

        self.horizontalLayout.addWidget(self.locButton)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.idLineEdit = QLineEdit(self.configGroupBox)
        self.idLineEdit.setObjectName(u"idLineEdit")

        self.gridLayout_2.addWidget(self.idLineEdit, 0, 1, 1, 1)

        self.locLabel = QLabel(self.configGroupBox)
        self.locLabel.setObjectName(u"locLabel")

        self.gridLayout_2.addWidget(self.locLabel, 1, 0, 1, 1)

        self.idLabel = QLabel(self.configGroupBox)
        self.idLabel.setObjectName(u"idLabel")

        self.gridLayout_2.addWidget(self.idLabel, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        QWidget.setTabOrder(self.idLineEdit, self.locLineEdit)
        QWidget.setTabOrder(self.locLineEdit, self.locButton)
        QWidget.setTabOrder(self.locButton, self.buttonBox)

        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure TRC Source Step", None))
        self.configGroupBox.setTitle("")
        self.locButton.setText(QCoreApplication.translate("ConfigureDialog", u"...", None))
        self.locLabel.setText(QCoreApplication.translate("ConfigureDialog", u"Location:  ", None))
        self.idLabel.setText(QCoreApplication.translate("ConfigureDialog", u"identifier:  ", None))
    # retranslateUi

