'''

    This is the start window

'''


from PyQt5 import QtCore, QtGui, QtWidgets
from assets.qrc import app_bg
from assets.files import GLOBALS

import sys

class Ui_StartWindow(object):
    def setupUi(self, StartWindow):



        ''' Functions '''
        def exitApp():
            sys.exit()

        def checkLoginInputs():

            # Grabbing the username input text
            userNameLE = self.startWindow_UsernameLineEdit
            userNameLEText = userNameLE.text()

            # Grabbing the password input text
            passWordLE = self.startWindow_PasswordLineEdit;
            passWordLEText = passWordLE.text()

            # If the username is invalid, show the invalid hint
            if userNameLEText == "" or userNameLEText == None:

                # Resetting the validUsername variable
                if GLOBALS.validUsername:
                    GLOBALS.validUsername = False

                print("Invalid Username..")
                self.startWindow_InvalidUsernameLabel.setFixedHeight(20)

            # If the password is invalid, show the invalid hint
            if passWordLEText == "" or passWordLEText == None:

                # Resetting the validPassword variable
                if GLOBALS.validPassword:
                    GLOBALS.validPassword = False

                print("Invalid Password..")
                self.startWindow_InvalidPasswordLabel.setFixedHeight(20)


            # If the username is valid
            if not userNameLEText == "" and not userNameLEText == None:

                # Marking validUsername
                GLOBALS.validUsername = True

                # Do stuff once valid
                if GLOBALS.validUsername:
                    print("Valid Username.")

                    # Hiding the invalid hint if already displayed
                    self.startWindow_InvalidUsernameLabel.setFixedHeight(0)


            # If the password is valid
            if not passWordLEText == "" and not passWordLEText == None:

                # Marking validPassword
                GLOBALS.validPassword = True

                # Do stuff once valid
                if GLOBALS.validPassword:
                    print("Valid Password.")

                    # Hiding the invalid hint if already displayed
                    self.startWindow_InvalidPasswordLabel.setFixedHeight(0)


            # If both the username and password are valid, do something
            if GLOBALS.validUsername and GLOBALS.validPassword:

                print("Successful Login!")

        def displayInfoDialog():

            infoDialog = QtWidgets.QDialog()
            infoDialog.setStyleSheet("""
            
                QDialog {
                    background-color: #344D67;
                }
            
            """)

            # Dialog settings
            infoDialog.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Hides the title bar
            infoDialog.setWindowTitle("Meet the team.")
            infoDialog.setFixedSize(400, 400)

            # Dialog widgets
            infoDialogLayout = QtWidgets.QVBoxLayout()
            infoDialogCloseBtn = QtWidgets.QPushButton("CLOSE", infoDialog)
            infoDialogCloseBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

            infoDialogCloseBtn.setStyleSheet("""
            
            QPushButton {
                background-color: #ADE792; 
                border: none; 
                color: #344D67; 
                height: 44px; 
                width: 69px; 
                margin-bottom: 20px;
                font-weight: bold;
            }
            
            QPushButton::hover {
                color: white;
                background-color: rgb(139, 231, 100);
            }
            
            """)
            infoDialogCloseBtn.setFont(QtGui.QFont("Lato", 12))

            infoDialogCloseBtn.clicked.connect(infoDialog.close) # Closes the dialog box

            # Creating the team member names
            infoDialogNames = QtWidgets.QFrame()
            infoDialogNamesLayout = QtWidgets.QVBoxLayout()


            for name in GLOBALS.teamMembers:

                infoDialogName = QtWidgets.QLabel(name)

                infoDialogName.setStyleSheet("""
                
                    QLabel {
                        color: white;
                    }
                
                """)

                infoDialogName.setFont(QtGui.QFont("Lato", 13))
                infoDialogLayout.addWidget(infoDialogName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)


            infoDialogNames.setLayout(infoDialogNamesLayout)

            infoDialogLayout.addWidget(infoDialogNames, alignment=QtCore.Qt.AlignmentFlag.AlignBottom)
            infoDialogLayout.addWidget(infoDialogCloseBtn, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)


            infoDialog.setLayout(infoDialogLayout)

            # Displaying the dialog
            infoDialog.exec_()


        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(900, 900)
        StartWindow.setMinimumSize(QtCore.QSize(900, 900))
        StartWindow.setMaximumSize(QtCore.QSize(900, 900))
        StartWindow.setStyleSheet("border-image: url(:/newPrefix/imgs/app-bg.png);")
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startWindow_Heading1 = QtWidgets.QLabel(self.centralwidget)
        self.startWindow_Heading1.setGeometry(QtCore.QRect(0, 120, 901, 181))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.startWindow_Heading1.setFont(font)
        self.startWindow_Heading1.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.startWindow_Heading1.setAlignment(QtCore.Qt.AlignCenter)
        self.startWindow_Heading1.setObjectName("startWindow_Heading1")
        self.startWindow_Heading2 = QtWidgets.QLabel(self.centralwidget)
        self.startWindow_Heading2.setGeometry(QtCore.QRect(0, 220, 901, 121))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.startWindow_Heading2.setFont(font)
        self.startWindow_Heading2.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.startWindow_Heading2.setAlignment(QtCore.Qt.AlignCenter)
        self.startWindow_Heading2.setObjectName("startWindow_Heading2")
        self.startWindow_SubHeading = QtWidgets.QLabel(self.centralwidget)
        self.startWindow_SubHeading.setGeometry(QtCore.QRect(0, 340, 901, 41))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.startWindow_SubHeading.setFont(font)
        self.startWindow_SubHeading.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.startWindow_SubHeading.setAlignment(QtCore.Qt.AlignCenter)
        self.startWindow_SubHeading.setObjectName("startWindow_SubHeading")
        self.startWindow_UsernameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.startWindow_UsernameLineEdit.setGeometry(QtCore.QRect(290, 460, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.startWindow_UsernameLineEdit.setFont(font)
        self.startWindow_UsernameLineEdit.setStyleSheet("QLineEdit {\n"
"    border-image: none;\n"
"    background-color: #344D67;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    color: white;\n"
"}")
        self.startWindow_UsernameLineEdit.setObjectName("startWindow_UsernameLineEdit")
        self.startWindow_PasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.startWindow_PasswordLineEdit.setGeometry(QtCore.QRect(290, 560, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.startWindow_PasswordLineEdit.setFont(font)
        self.startWindow_PasswordLineEdit.setStyleSheet("QLineEdit {\n"
"    border-image: none;\n"
"    background-color: #344D67;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    color: white;\n"
"}")
        self.startWindow_PasswordLineEdit.setObjectName("startWindow_PasswordLineEdit")
        self.startWindow_LoginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startWindow_LoginBtn.clicked.connect(checkLoginInputs)
        self.startWindow_LoginBtn.setGeometry(QtCore.QRect(360, 650, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.startWindow_LoginBtn.setFont(font)
        self.startWindow_LoginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startWindow_LoginBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #ADE792;\n"
"    border: none;\n"
"    color: #344D67;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}")
        self.startWindow_LoginBtn.setObjectName("startWindow_LoginBtn")
        self.startWindow_ExitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startWindow_ExitBtn.clicked.connect(exitApp)
        self.startWindow_ExitBtn.setGeometry(QtCore.QRect(460, 650, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.startWindow_ExitBtn.setFont(font)
        self.startWindow_ExitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startWindow_ExitBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #ADE792;\n"
"    border: none;\n"
"    color: #344D67;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}")
        self.startWindow_ExitBtn.setObjectName("startWindow_ExitBtn")
        self.startWindow_InvalidUsernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.startWindow_InvalidUsernameLabel.setGeometry(QtCore.QRect(290, 430, 321, 0))
        self.startWindow_InvalidUsernameLabel.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setItalic(False)
        self.startWindow_InvalidUsernameLabel.setFont(font)
        self.startWindow_InvalidUsernameLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: rgb(0, 255, 127);\n"
"}")
        self.startWindow_InvalidUsernameLabel.setObjectName("startWindow_InvalidUsernameLabel")
        self.startWindow_InvalidPasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.startWindow_InvalidPasswordLabel.setGeometry(QtCore.QRect(290, 530, 321, 0))
        self.startWindow_InvalidPasswordLabel.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setItalic(False)
        self.startWindow_InvalidPasswordLabel.setFont(font)
        self.startWindow_InvalidPasswordLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: rgb(0, 255, 127);\n"
"}")
        self.startWindow_InvalidPasswordLabel.setObjectName("startWindow_InvalidPasswordLabel")
        self.startWindow_InfoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startWindow_InfoBtn.clicked.connect(displayInfoDialog)
        self.startWindow_InfoBtn.setGeometry(QtCore.QRect(420, 840, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(28)
        self.startWindow_InfoBtn.setFont(font)
        self.startWindow_InfoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startWindow_InfoBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: #F3ECB0;\n"
"    background-color: transparent;\n"
"    padding-bottom: 3px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    color: rgb(241, 243, 103);\n"
"}")
        self.startWindow_InfoBtn.setObjectName("startWindow_InfoBtn")
        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "Forsyth Family Practice Center - MOA"))
        self.startWindow_Heading1.setText(_translate("StartWindow", "Medical Office"))
        self.startWindow_Heading2.setText(_translate("StartWindow", "Administration"))
        self.startWindow_SubHeading.setText(_translate("StartWindow", "Forsyth Family Practice Center"))
        self.startWindow_UsernameLineEdit.setPlaceholderText(_translate("StartWindow", "Enter Username"))
        self.startWindow_PasswordLineEdit.setPlaceholderText(_translate("StartWindow", "Enter Password"))
        self.startWindow_LoginBtn.setText(_translate("StartWindow", "LOGIN"))
        self.startWindow_ExitBtn.setText(_translate("StartWindow", "EXIT"))
        self.startWindow_InvalidUsernameLabel.setText(_translate("StartWindow", "INVALID USERNAME"))
        self.startWindow_InvalidPasswordLabel.setText(_translate("StartWindow", "INVALID PASSWORD"))
        self.startWindow_InfoBtn.setText(_translate("StartWindow", "🛈"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartWindow = QtWidgets.QMainWindow()
    ui = Ui_StartWindow()
    ui.setupUi(StartWindow)
    StartWindow.show()
    sys.exit(app.exec_())
