# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\minorua\.qgis2\python\developing_plugins\Qgis2threejs\ui\widgetComboEdit.ui'
#
# Created: Fri Sep 18 10:25:23 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ComboEditWidget(object):
    def setupUi(self, ComboEditWidget):
        ComboEditWidget.setObjectName(_fromUtf8("ComboEditWidget"))
        ComboEditWidget.resize(400, 32)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ComboEditWidget.sizePolicy().hasHeightForWidth())
        ComboEditWidget.setSizePolicy(sizePolicy)
        ComboEditWidget.setMinimumSize(QtCore.QSize(50, 0))
        self.formLayout = QtGui.QFormLayout(ComboEditWidget)
        self.formLayout.setContentsMargins(0, 2, 0, 2)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.horizontalLayout_1 = QtGui.QHBoxLayout()
        self.horizontalLayout_1.setSpacing(3)
        self.horizontalLayout_1.setObjectName(_fromUtf8("horizontalLayout_1"))
        self.label_1 = QtGui.QLabel(ComboEditWidget)
        self.label_1.setMinimumSize(QtCore.QSize(80, 0))
        self.label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.horizontalLayout_1.addWidget(self.label_1)
        self.comboBox = QtGui.QComboBox(ComboEditWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(125, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(125, 16777215))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout_1.addWidget(self.comboBox)
        self.checkBox = QtGui.QCheckBox(ComboEditWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_1.addWidget(self.checkBox)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.horizontalLayout_1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(ComboEditWidget)
        self.label_2.setMinimumSize(QtCore.QSize(45, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(ComboEditWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.toolButton = QtGui.QToolButton(ComboEditWidget)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)

        self.retranslateUi(ComboEditWidget)
        QtCore.QMetaObject.connectSlotsByName(ComboEditWidget)

    def retranslateUi(self, ComboEditWidget):
        ComboEditWidget.setWindowTitle(_translate("ComboEditWidget", "Form", None))
        self.label_1.setText(_translate("ComboEditWidget", "Name", None))
        self.label_2.setText(_translate("ComboEditWidget", "Value", None))
        self.toolButton.setText(_translate("ComboEditWidget", "...", None))

