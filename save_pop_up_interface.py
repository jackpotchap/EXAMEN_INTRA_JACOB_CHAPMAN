# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_UI/save_pop_up_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 150)
        self.label_erreure_savwrong = QtWidgets.QLabel(Dialog)
        self.label_erreure_savwrong.setGeometry(QtCore.QRect(30, 50, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_erreure_savwrong.setFont(font)
        self.label_erreure_savwrong.setObjectName("label_erreure_savwrong")
        self.pushButton_hide_save_pop_up = QtWidgets.QPushButton(Dialog)
        self.pushButton_hide_save_pop_up.setGeometry(QtCore.QRect(140, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_hide_save_pop_up.setFont(font)
        self.pushButton_hide_save_pop_up.setObjectName("pushButton_hide_save_pop_up")
        self.label_titre_nom_2 = QtWidgets.QLabel(Dialog)
        self.label_titre_nom_2.setGeometry(QtCore.QRect(40, 30, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_titre_nom_2.setFont(font)
        self.label_titre_nom_2.setObjectName("label_titre_nom_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_erreure_savwrong.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">* Une erreure est survenue durant la sauvegarde.</span></p></body></html>"))
        self.pushButton_hide_save_pop_up.setText(_translate("Dialog", "fermer"))
        self.label_titre_nom_2.setText(_translate("Dialog", "Enregistrement executé avec succès"))