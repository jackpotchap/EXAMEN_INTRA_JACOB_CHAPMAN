# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_UI/list_avance_pop_up_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(802, 621)
        self.lineEdit_age_min = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_age_min.setGeometry(QtCore.QRect(410, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_age_min.setFont(font)
        self.lineEdit_age_min.setText("")
        self.lineEdit_age_min.setObjectName("lineEdit_age_min")
        self.label_titre_age_min = QtWidgets.QLabel(Dialog)
        self.label_titre_age_min.setGeometry(QtCore.QRect(410, 80, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_titre_age_min.setFont(font)
        self.label_titre_age_min.setObjectName("label_titre_age_min")
        self.label_titre_age_max = QtWidgets.QLabel(Dialog)
        self.label_titre_age_max.setGeometry(QtCore.QRect(410, 180, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_titre_age_max.setFont(font)
        self.label_titre_age_max.setObjectName("label_titre_age_max")
        self.lineEdit_age_max = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_age_max.setGeometry(QtCore.QRect(410, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_age_max.setFont(font)
        self.lineEdit_age_max.setText("")
        self.lineEdit_age_max.setObjectName("lineEdit_age_max")
        self.pushButton_age_rechercher = QtWidgets.QPushButton(Dialog)
        self.pushButton_age_rechercher.setGeometry(QtCore.QRect(420, 400, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_age_rechercher.setFont(font)
        self.pushButton_age_rechercher.setObjectName("pushButton_age_rechercher")
        self.listView_list_patient_avance = QtWidgets.QListView(Dialog)
        self.listView_list_patient_avance.setGeometry(QtCore.QRect(30, 20, 351, 541))
        self.listView_list_patient_avance.setObjectName("listView_list_patient_avance")
        self.pushButton_hide_list_avance = QtWidgets.QPushButton(Dialog)
        self.pushButton_hide_list_avance.setGeometry(QtCore.QRect(410, 470, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_hide_list_avance.setFont(font)
        self.pushButton_hide_list_avance.setObjectName("pushButton_hide_list_avance")
        self.label_titre_prix = QtWidgets.QLabel(Dialog)
        self.label_titre_prix.setGeometry(QtCore.QRect(410, 280, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_titre_prix.setFont(font)
        self.label_titre_prix.setObjectName("label_titre_prix")
        self.lineEdit_prix = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_prix.setGeometry(QtCore.QRect(410, 310, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_prix.setFont(font)
        self.lineEdit_prix.setText("")
        self.lineEdit_prix.setObjectName("lineEdit_prix")
        self.label_erreure_taille_age_min = QtWidgets.QLabel(Dialog)
        self.label_erreure_taille_age_min.setGeometry(QtCore.QRect(410, 140, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreure_taille_age_min.setFont(font)
        self.label_erreure_taille_age_min.setObjectName("label_erreure_taille_age_min")
        self.label_erreure_chiffreonly_num_age_min = QtWidgets.QLabel(Dialog)
        self.label_erreure_chiffreonly_num_age_min.setGeometry(QtCore.QRect(410, 160, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreure_chiffreonly_num_age_min.setFont(font)
        self.label_erreure_chiffreonly_num_age_min.setObjectName("label_erreure_chiffreonly_num_age_min")
        self.label_erreure_positif = QtWidgets.QLabel(Dialog)
        self.label_erreure_positif.setGeometry(QtCore.QRect(410, 340, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreure_positif.setFont(font)
        self.label_erreure_positif.setObjectName("label_erreure_positif")
        self.label_erreure_chiffreonly_num_prix = QtWidgets.QLabel(Dialog)
        self.label_erreure_chiffreonly_num_prix.setGeometry(QtCore.QRect(410, 360, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreure_chiffreonly_num_prix.setFont(font)
        self.label_erreure_chiffreonly_num_prix.setObjectName("label_erreure_chiffreonly_num_prix")
        self.label_erreure_taille_num_age_max = QtWidgets.QLabel(Dialog)
        self.label_erreure_taille_num_age_max.setGeometry(QtCore.QRect(410, 240, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreure_taille_num_age_max.setFont(font)
        self.label_erreure_taille_num_age_max.setObjectName("label_erreure_taille_num_age_max")
        self.label_erreure_chiffreonly_num_age_max = QtWidgets.QLabel(Dialog)
        self.label_erreure_chiffreonly_num_age_max.setGeometry(QtCore.QRect(410, 260, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreure_chiffreonly_num_age_max.setFont(font)
        self.label_erreure_chiffreonly_num_age_max.setObjectName("label_erreure_chiffreonly_num_age_max")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_titre_age_min.setText(_translate("Dialog", "Age Minimum"))
        self.label_titre_age_max.setText(_translate("Dialog", "Age Maximum"))
        self.pushButton_age_rechercher.setText(_translate("Dialog", "Rechercher"))
        self.pushButton_hide_list_avance.setText(_translate("Dialog", "fermer"))
        self.label_titre_prix.setText(_translate("Dialog", "Prix"))
        self.label_erreure_taille_age_min.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">* l\'age doit etre supérieure a 0.</span></p></body></html>"))
        self.label_erreure_chiffreonly_num_age_min.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">* l\'age doit etre un nombre entier.</span></p></body></html>"))
        self.label_erreure_positif.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">* Le numéro dois etre positif.</span></p></body></html>"))
        self.label_erreure_chiffreonly_num_prix.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">* Le numéro dois contenir uniquement des caratères numérique.</span></p></body></html>"))
        self.label_erreure_taille_num_age_max.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">* l\'age doit etre supérieure a 0.</span></p></body></html>"))
        self.label_erreure_chiffreonly_num_age_max.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">* l\'age doit etre un nombre entier.</span></p></body></html>"))
