# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_UI/interface_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 706)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_nom = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nom.setGeometry(QtCore.QRect(20, 160, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_nom.setFont(font)
        self.lineEdit_nom.setText("")
        self.lineEdit_nom.setObjectName("lineEdit_nom")
        self.label_titre_nom = QtWidgets.QLabel(self.centralwidget)
        self.label_titre_nom.setGeometry(QtCore.QRect(20, 130, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_titre_nom.setFont(font)
        self.label_titre_nom.setObjectName("label_titre_nom")
        self.label_erreure_troplong_nom = QtWidgets.QLabel(self.centralwidget)
        self.label_erreure_troplong_nom.setGeometry(QtCore.QRect(20, 190, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreure_troplong_nom.setFont(font)
        self.label_erreure_troplong_nom.setObjectName("label_erreure_troplong_nom")
        self.label_erreure_lettreonly_nom = QtWidgets.QLabel(self.centralwidget)
        self.label_erreure_lettreonly_nom.setGeometry(QtCore.QRect(20, 210, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreure_lettreonly_nom.setFont(font)
        self.label_erreure_lettreonly_nom.setObjectName("label_erreure_lettreonly_nom")
        self.label_erreure_chiffreonly_num = QtWidgets.QLabel(self.centralwidget)
        self.label_erreure_chiffreonly_num.setGeometry(QtCore.QRect(20, 100, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreure_chiffreonly_num.setFont(font)
        self.label_erreure_chiffreonly_num.setObjectName("label_erreure_chiffreonly_num")
        self.label_titre_num = QtWidgets.QLabel(self.centralwidget)
        self.label_titre_num.setGeometry(QtCore.QRect(20, 20, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_titre_num.setFont(font)
        self.label_titre_num.setObjectName("label_titre_num")
        self.label_erreure_taille_num = QtWidgets.QLabel(self.centralwidget)
        self.label_erreure_taille_num.setGeometry(QtCore.QRect(20, 80, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreure_taille_num.setFont(font)
        self.label_erreure_taille_num.setObjectName("label_erreure_taille_num")
        self.lineEdit_num = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_num.setGeometry(QtCore.QRect(20, 50, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_num.setFont(font)
        self.lineEdit_num.setText("")
        self.lineEdit_num.setObjectName("lineEdit_num")
        self.label_erreure_lettreonly_prenom = QtWidgets.QLabel(self.centralwidget)
        self.label_erreure_lettreonly_prenom.setGeometry(QtCore.QRect(20, 320, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreure_lettreonly_prenom.setFont(font)
        self.label_erreure_lettreonly_prenom.setObjectName("label_erreure_lettreonly_prenom")
        self.label_titre_prenom = QtWidgets.QLabel(self.centralwidget)
        self.label_titre_prenom.setGeometry(QtCore.QRect(20, 240, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_titre_prenom.setFont(font)
        self.label_titre_prenom.setObjectName("label_titre_prenom")
        self.label_erreure_troplong_prenom = QtWidgets.QLabel(self.centralwidget)
        self.label_erreure_troplong_prenom.setGeometry(QtCore.QRect(20, 300, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreure_troplong_prenom.setFont(font)
        self.label_erreure_troplong_prenom.setObjectName("label_erreure_troplong_prenom")
        self.lineEdit_prenom = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_prenom.setGeometry(QtCore.QRect(20, 270, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_prenom.setFont(font)
        self.lineEdit_prenom.setText("")
        self.lineEdit_prenom.setObjectName("lineEdit_prenom")
        self.dateEdit_naissance_patient = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_naissance_patient.setGeometry(QtCore.QRect(500, 50, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit_naissance_patient.setFont(font)
        self.dateEdit_naissance_patient.setObjectName("dateEdit_naissance_patient")
        self.label_titre_naissance_patient = QtWidgets.QLabel(self.centralwidget)
        self.label_titre_naissance_patient.setGeometry(QtCore.QRect(500, 10, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_titre_naissance_patient.setFont(font)
        self.label_titre_naissance_patient.setObjectName("label_titre_naissance_patient")
        self.label_erreure_pasnee_date = QtWidgets.QLabel(self.centralwidget)
        self.label_erreure_pasnee_date.setGeometry(QtCore.QRect(500, 80, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreure_pasnee_date.setFont(font)
        self.label_erreure_pasnee_date.setObjectName("label_erreure_pasnee_date")
        self.label_erreure_chiffreonly_nbvisite = QtWidgets.QLabel(self.centralwidget)
        self.label_erreure_chiffreonly_nbvisite.setGeometry(QtCore.QRect(500, 200, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreure_chiffreonly_nbvisite.setFont(font)
        self.label_erreure_chiffreonly_nbvisite.setObjectName("label_erreure_chiffreonly_nbvisite")
        self.label_erreure_positif_nbvisite = QtWidgets.QLabel(self.centralwidget)
        self.label_erreure_positif_nbvisite.setGeometry(QtCore.QRect(500, 180, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreure_positif_nbvisite.setFont(font)
        self.label_erreure_positif_nbvisite.setObjectName("label_erreure_positif_nbvisite")
        self.label_titre_nbvisite = QtWidgets.QLabel(self.centralwidget)
        self.label_titre_nbvisite.setGeometry(QtCore.QRect(500, 120, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_titre_nbvisite.setFont(font)
        self.label_titre_nbvisite.setObjectName("label_titre_nbvisite")
        self.lineEdit_nbvisite = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nbvisite.setGeometry(QtCore.QRect(500, 150, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_nbvisite.setFont(font)
        self.lineEdit_nbvisite.setText("")
        self.lineEdit_nbvisite.setObjectName("lineEdit_nbvisite")
        self.label_titre_commentaire = QtWidgets.QLabel(self.centralwidget)
        self.label_titre_commentaire.setGeometry(QtCore.QRect(20, 350, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_titre_commentaire.setFont(font)
        self.label_titre_commentaire.setObjectName("label_titre_commentaire")
        self.textEdit_commentaire = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_commentaire.setGeometry(QtCore.QRect(20, 380, 421, 181))
        self.textEdit_commentaire.setObjectName("textEdit_commentaire")
        self.pushButton_cree = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cree.setGeometry(QtCore.QRect(20, 600, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_cree.setFont(font)
        self.pushButton_cree.setObjectName("pushButton_cree")
        self.textBrowser_affichage_patients = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_affichage_patients.setGeometry(QtCore.QRect(500, 280, 421, 291))
        self.textBrowser_affichage_patients.setObjectName("textBrowser_affichage_patients")
        self.label_titre_affichage_patients = QtWidgets.QLabel(self.centralwidget)
        self.label_titre_affichage_patients.setGeometry(QtCore.QRect(500, 240, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_titre_affichage_patients.setFont(font)
        self.label_titre_affichage_patients.setObjectName("label_titre_affichage_patients")
        self.pushButton_sauvegarder = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sauvegarder.setGeometry(QtCore.QRect(240, 600, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_sauvegarder.setFont(font)
        self.pushButton_sauvegarder.setObjectName("pushButton_sauvegarder")
        self.pushButton_ouvrir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ouvrir.setGeometry(QtCore.QRect(500, 600, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_ouvrir.setFont(font)
        self.pushButton_ouvrir.setObjectName("pushButton_ouvrir")
        self.pushButton_afficherlist = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_afficherlist.setGeometry(QtCore.QRect(720, 600, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_afficherlist.setFont(font)
        self.pushButton_afficherlist.setObjectName("pushButton_afficherlist")
        self.label_erreure_introuvable_ouvrire = QtWidgets.QLabel(self.centralwidget)
        self.label_erreure_introuvable_ouvrire.setGeometry(QtCore.QRect(500, 660, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreure_introuvable_ouvrire.setFont(font)
        self.label_erreure_introuvable_ouvrire.setObjectName("label_erreure_introuvable_ouvrire")
        self.label_erreure_generic_ouvrire = QtWidgets.QLabel(self.centralwidget)
        self.label_erreure_generic_ouvrire.setGeometry(QtCore.QRect(500, 680, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreure_generic_ouvrire.setFont(font)
        self.label_erreure_generic_ouvrire.setObjectName("label_erreure_generic_ouvrire")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_titre_nom.setText(_translate("MainWindow", "Nom du patient"))
        self.label_erreure_troplong_nom.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">* Le nom du patient ne peut contenir plus de 30 caratères.</span></p></body></html>"))
        self.label_erreure_lettreonly_nom.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">* Le nom dois contenir uniquement des carateres alphabétiques.</span></p></body></html>"))
        self.label_erreure_chiffreonly_num.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">* Le numéro dois contenir uniquement des caratères numérique.</span></p></body></html>"))
        self.label_titre_num.setText(_translate("MainWindow", "Numéro du patient"))
        self.label_erreure_taille_num.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">* Le numéro dois etre composé de 7 caractères.</span></p></body></html>"))
        self.label_erreure_lettreonly_prenom.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">* Le prénom dois contenir uniquement des carateres alphabétiques.</span></p></body></html>"))
        self.label_titre_prenom.setText(_translate("MainWindow", "Prénom du patient"))
        self.label_erreure_troplong_prenom.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">* Le prénom du patient ne peut contenir plus de 30 caratères.</span></p></body></html>"))
        self.label_titre_naissance_patient.setText(_translate("MainWindow", "Date de naissance du patient"))
        self.label_erreure_pasnee_date.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">* La date de naissance doit etre inférieur ou égale à la date de aujourd\'hui.</span></p></body></html>"))
        self.label_erreure_chiffreonly_nbvisite.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">* Le numéro dois contenir uniquement des caratères numérique.</span></p></body></html>"))
        self.label_erreure_positif_nbvisite.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">* Le nombre doit etre positif.</span></p></body></html>"))
        self.label_titre_nbvisite.setText(_translate("MainWindow", "Nombre de visite du patient"))
        self.label_titre_commentaire.setText(_translate("MainWindow", "Commentaire "))
        self.pushButton_cree.setText(_translate("MainWindow", "Ajouter"))
        self.label_titre_affichage_patients.setText(_translate("MainWindow", "List de patients :"))
        self.pushButton_sauvegarder.setText(_translate("MainWindow", "Sauvegarder"))
        self.pushButton_ouvrir.setText(_translate("MainWindow", "Ouvrir"))

        self.pushButton_afficherlist.setText(_translate("MainWindow", "list avancé"))
        self.label_erreure_introuvable_ouvrire.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">* Patient introuvable!</span></p></body></html>"))
        self.label_erreure_generic_ouvrire.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">* Erreure lors de l\'ouverture du fichier.</span></p></body></html>"))
