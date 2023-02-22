


from PyQt5 import QtCore, QtGui, QtWidgets
from assets.qrc import app_bg
from assets.files import GLOBALS


class Ui_SchedulingAppointmentsWindow(object):
    def setupUi(self, SchedulingAppointmentsWindow):

        def resetInputsAndLabels():

                self.schedulingAppointmentsWindow_InvalidInputsLabel.setText("")
                self.schedulingAppointmentsWindow_InvalidStaffIDLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(52, 77, 103);
                                        }
                                
                                """)
                self.schedulingAppointmentsWindow_InvalidPatientIDLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(52, 77, 103);
                                        }
                                
                                """)
                self.schedulingAppointmentsWindow_InvalidAppointmentTypeIDLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(52, 77, 103);
                                        }
                                
                                """)
                self.schedulingAppointmentsWindow_InvalidLocationIDLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(52, 77, 103);
                                        }
                                
                                """)
                self.schedulingAppointmentsWindow_InvalidAppointmentReasonLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(52, 77, 103);
                                        }
                                
                                """)
                self.schedulingAppointmentsWindow_InvalidMeetTimeDateLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(52, 77, 103);
                                        }
                                
                                """)

                self.schedulingAppointmentsWindow_StaffIDLineEdit.setText("")
                self.schedulingAppointmentsWindow_PatientIDLineEdit.setText("")
                self.schedulingAppointmentsWindow_AppointmentTypeIDLineEdit.setText("")
                self.schedulingAppointmentsWindow_LocationIDLineEdit.setText("")
                self.schedulingAppointmentsWindow_AppointmentReasonLineEdit.setText("")

                self.schedulingAppointmentsWindow_MeetTimeDateDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
                self.schedulingAppointmentsWindow_MeetTimeDateDateTimeEdit.setDisplayFormat("M/d/yyyy hh:mm AP")

        def scheduleAppointment():

                if GLOBALS.validStaffID and GLOBALS.validPatientID and GLOBALS.validAppointmentTypeID and GLOBALS.validLocationID and GLOBALS.validAppointmentReason and GLOBALS.validMeetTimeDate:
                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setText("")

                        print("Scheduled Appointment!")

        def checkInputs():

                staffIDLineEdit = self.schedulingAppointmentsWindow_StaffIDLineEdit
                staffIDLineEditText = staffIDLineEdit.text()

                patientIDLineEdit = self.schedulingAppointmentsWindow_PatientIDLineEdit
                patientIDLineEditText = patientIDLineEdit.text()

                appointmentTypeIDLineEdit = self.schedulingAppointmentsWindow_AppointmentTypeIDLineEdit
                appointmentTypeIDLineEditText = appointmentTypeIDLineEdit.text()

                locationIDLineEdit = self.schedulingAppointmentsWindow_LocationIDLineEdit
                locationIDLineEditText = locationIDLineEdit.text()

                appointmentReasonLineEdit = self.schedulingAppointmentsWindow_AppointmentReasonLineEdit
                appointmentReasonLineEditText = appointmentReasonLineEdit.text()

                meetTimeDateDate = self.schedulingAppointmentsWindow_MeetTimeDateDateTimeEdit.date()

                # Checking staff id input
                if staffIDLineEditText == "" or staffIDLineEditText == None:

                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setText("INVALID INPUTS")
                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setMinimumSize(120, 30)

                        GLOBALS.validStaffID = False
                        GLOBALS.scheduleAppointment.clear()
                        GLOBALS.scheduleAppointment.append(False)

                        # Recoloring and resizing the invalid hint to display
                        self.schedulingAppointmentsWindow_InvalidStaffIDLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(0, 255, 127);
                                        }
                                
                                """)
                        self.schedulingAppointmentsWindow_InvalidStaffIDLabel.setMinimumSize(20, 20)

                        print("Invalid Staff ID")
                if not staffIDLineEditText == "" or staffIDLineEditText == None:
                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setMinimumSize(0, 0)

                        GLOBALS.validStaffID = True

                        # Recoloring the invalid hint when the input is valid to hide it
                        if GLOBALS.validStaffID:
                                self.schedulingAppointmentsWindow_InvalidStaffIDLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(52, 77, 103);
                                        }
                                
                                """)

                        print("Valid Staff ID")

                # Checking patient id input
                if patientIDLineEditText == "" or patientIDLineEditText == None:

                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setText("INVALID INPUTS")
                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setMinimumSize(120, 30)

                        GLOBALS.validPatientID = False
                        GLOBALS.scheduleAppointment.clear()
                        GLOBALS.scheduleAppointment.append(False)

                        # Recoloring and resizing the invalid hint to display
                        self.schedulingAppointmentsWindow_InvalidPatientIDLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(0, 255, 127);
                                        }
                                
                                """)
                        self.schedulingAppointmentsWindow_InvalidPatientIDLabel.setMinimumSize(20, 20)

                        print("Invalid Patient ID")
                if not patientIDLineEditText == "" or patientIDLineEditText == None:
                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setMinimumSize(0, 0)

                        GLOBALS.validPatientID = True

                        # Recoloring the invalid hint when the input is valid to hide it
                        if GLOBALS.validPatientID:
                                self.schedulingAppointmentsWindow_InvalidPatientIDLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(52, 77, 103);
                                        }
                                
                                """)

                        print("Valid Patient ID")

                # Checking appointment type id input
                if appointmentTypeIDLineEditText == "" or appointmentTypeIDLineEditText == None:

                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setText("INVALID INPUTS")
                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setMinimumSize(120, 30)

                        GLOBALS.validAppointmentTypeID = False
                        GLOBALS.scheduleAppointment.clear()
                        GLOBALS.scheduleAppointment.append(False)

                        # Recoloring and resizing the invalid hint to display
                        self.schedulingAppointmentsWindow_InvalidAppointmentTypeIDLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(0, 255, 127);
                                        }
                                
                                """)
                        self.schedulingAppointmentsWindow_InvalidAppointmentTypeIDLabel.setMinimumSize(20, 20)

                        print("Invalid Appointment Type ID")
                if not appointmentTypeIDLineEditText == "" or appointmentTypeIDLineEditText == None:
                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setMinimumSize(0, 0)

                        GLOBALS.validAppointmentTypeID = True

                        # Recoloring the invalid hint when the input is valid to hide it
                        if GLOBALS.validAppointmentTypeID:
                                self.schedulingAppointmentsWindow_InvalidAppointmentTypeIDLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(52, 77, 103);
                                        }
                                
                                """)

                        print("Valid Appointment Type ID")

                # Checking location id input
                if locationIDLineEditText == "" or locationIDLineEditText == None:

                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setText("INVALID INPUTS")
                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setMinimumSize(120, 30)

                        GLOBALS.validLocationID = False
                        GLOBALS.scheduleAppointment.clear()
                        GLOBALS.scheduleAppointment.append(False)

                        # Recoloring and resizing the invalid hint to display
                        self.schedulingAppointmentsWindow_InvalidLocationIDLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(0, 255, 127);
                                        }
                                
                                """)
                        self.schedulingAppointmentsWindow_InvalidLocationIDLabel.setMinimumSize(20, 20)

                        print("Invalid Location ID")
                if not locationIDLineEditText == "" or locationIDLineEditText == None:
                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setMinimumSize(0, 0)

                        GLOBALS.validLocationID = True

                        # Recoloring the invalid hint when the input is valid to hide it
                        if GLOBALS.validLocationID:
                                self.schedulingAppointmentsWindow_InvalidLocationIDLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(52, 77, 103);
                                        }
                                
                                """)

                        print("Valid Location ID")

                # Checking appointment reason input
                if appointmentReasonLineEditText == "" or appointmentReasonLineEditText == None:

                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setText("INVALID INPUTS")
                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setMinimumSize(120, 30)

                        GLOBALS.validAppointmentReason = False
                        GLOBALS.scheduleAppointment.clear()
                        GLOBALS.scheduleAppointment.append(False)

                        # Recoloring and resizing the invalid hint to display
                        self.schedulingAppointmentsWindow_InvalidAppointmentReasonLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(0, 255, 127);
                                        }
                                
                                """)
                        self.schedulingAppointmentsWindow_InvalidAppointmentReasonLabel.setMinimumSize(20, 20)

                        print("Invalid Appointment Reason")
                if not appointmentReasonLineEditText == "" or appointmentReasonLineEditText == None:
                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setMinimumSize(0, 0)

                        GLOBALS.validAppointmentReason = True

                        # Recoloring the invalid hint when the input is valid to hide it
                        if GLOBALS.validAppointmentReason:
                                self.schedulingAppointmentsWindow_InvalidAppointmentReasonLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(52, 77, 103);
                                        }
                                
                                """)

                        print("Valid Appointment Reason")

                # Checking meet time date
                if meetTimeDateDate < meetTimeDateDate.currentDate():
                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setText("INVALID INPUTS")
                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setMinimumSize(120, 30)

                        GLOBALS.validMeetTimeDate = False
                        GLOBALS.scheduleAppointment.clear()
                        GLOBALS.scheduleAppointment.append(False)

                        # Recoloring and resizing the invalid hint to display
                        self.schedulingAppointmentsWindow_InvalidMeetTimeDateLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(0, 255, 127);
                                        }
                                
                                """)
                        self.schedulingAppointmentsWindow_InvalidMeetTimeDateLabel.setMinimumSize(20, 20)

                        print("You cannot schedule something in the past..")
                if meetTimeDateDate >= meetTimeDateDate.currentDate():
                        self.schedulingAppointmentsWindow_InvalidInputsLabel.setMinimumSize(0, 0)

                        GLOBALS.validMeetTimeDate = True

                        # Recoloring the invalid hint when the input is valid to hide it
                        if GLOBALS.validMeetTimeDate:
                                self.schedulingAppointmentsWindow_InvalidMeetTimeDateLabel.setStyleSheet("""
                                
                                        QLabel {
                                                color: rgb(52, 77, 103);
                                        }
                                
                                """)

                        print("Valid Meet Date Time")

                scheduleAppointment()



        SchedulingAppointmentsWindow.setObjectName("SchedulingAppointmentsWindow")
        SchedulingAppointmentsWindow.resize(1800, 720)
        SchedulingAppointmentsWindow.setMinimumSize(QtCore.QSize(1800, 720))
        SchedulingAppointmentsWindow.setMaximumSize(QtCore.QSize(16777215, 720))
        SchedulingAppointmentsWindow.setStyleSheet("border-image: url(:/newPrefix/imgs/app-bg.png);")
        self.centralwidget = QtWidgets.QWidget(SchedulingAppointmentsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.schedulingAppointmentsWindow_CheckinBtn = QtWidgets.QPushButton(self.centralwidget)
        self.schedulingAppointmentsWindow_CheckinBtn.setGeometry(QtCore.QRect(317, 20, 80, 40))
        self.schedulingAppointmentsWindow_CheckinBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.schedulingAppointmentsWindow_CheckinBtn.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.schedulingAppointmentsWindow_CheckinBtn.setFont(font)
        self.schedulingAppointmentsWindow_CheckinBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.schedulingAppointmentsWindow_CheckinBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}")
        self.schedulingAppointmentsWindow_CheckinBtn.setObjectName("schedulingAppointmentsWindow_CheckinBtn")
        self.schedulingAppointmentsWindow_CheckoutBtn = QtWidgets.QPushButton(self.centralwidget)
        self.schedulingAppointmentsWindow_CheckoutBtn.setGeometry(QtCore.QRect(410, 20, 90, 40))
        self.schedulingAppointmentsWindow_CheckoutBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.schedulingAppointmentsWindow_CheckoutBtn.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.schedulingAppointmentsWindow_CheckoutBtn.setFont(font)
        self.schedulingAppointmentsWindow_CheckoutBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.schedulingAppointmentsWindow_CheckoutBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}")
        self.schedulingAppointmentsWindow_CheckoutBtn.setObjectName("schedulingAppointmentsWindow_CheckoutBtn")
        self.schedulingAppointmentsWindow_LabOrdersBtn = QtWidgets.QPushButton(self.centralwidget)
        self.schedulingAppointmentsWindow_LabOrdersBtn.setGeometry(QtCore.QRect(91, 20, 90, 40))
        self.schedulingAppointmentsWindow_LabOrdersBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.schedulingAppointmentsWindow_LabOrdersBtn.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.schedulingAppointmentsWindow_LabOrdersBtn.setFont(font)
        self.schedulingAppointmentsWindow_LabOrdersBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.schedulingAppointmentsWindow_LabOrdersBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}")
        self.schedulingAppointmentsWindow_LabOrdersBtn.setObjectName("schedulingAppointmentsWindow_LabOrdersBtn")
        self.schedulingAppointmentsWindow_LogoutBtn = QtWidgets.QPushButton(self.centralwidget)
        self.schedulingAppointmentsWindow_LogoutBtn.setGeometry(QtCore.QRect(18, 20, 60, 40))
        self.schedulingAppointmentsWindow_LogoutBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.schedulingAppointmentsWindow_LogoutBtn.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.schedulingAppointmentsWindow_LogoutBtn.setFont(font)
        self.schedulingAppointmentsWindow_LogoutBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.schedulingAppointmentsWindow_LogoutBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: rgb(30, 147, 143);\n"
"    color: black;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(14, 81, 85);\n"
"    color: white;\n"
"}")
        self.schedulingAppointmentsWindow_LogoutBtn.setObjectName("schedulingAppointmentsWindow_LogoutBtn")
        self.schedulingAppointmentsWindow_MakeReferralBtn = QtWidgets.QPushButton(self.centralwidget)
        self.schedulingAppointmentsWindow_MakeReferralBtn.setGeometry(QtCore.QRect(194, 20, 110, 40))
        self.schedulingAppointmentsWindow_MakeReferralBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.schedulingAppointmentsWindow_MakeReferralBtn.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.schedulingAppointmentsWindow_MakeReferralBtn.setFont(font)
        self.schedulingAppointmentsWindow_MakeReferralBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.schedulingAppointmentsWindow_MakeReferralBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}")
        self.schedulingAppointmentsWindow_MakeReferralBtn.setObjectName("schedulingAppointmentsWindow_MakeReferralBtn")
        self.schedulingAppointmentsWindow_HeadingLabel = QtWidgets.QLabel(self.centralwidget)
        self.schedulingAppointmentsWindow_HeadingLabel.setGeometry(QtCore.QRect(40, 100, 511, 101))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.schedulingAppointmentsWindow_HeadingLabel.setFont(font)
        self.schedulingAppointmentsWindow_HeadingLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.schedulingAppointmentsWindow_HeadingLabel.setObjectName("schedulingAppointmentsWindow_HeadingLabel")
        self.schedulingAppointmentsWindow_InputsHolderFrame = QtWidgets.QFrame(self.centralwidget)
        self.schedulingAppointmentsWindow_InputsHolderFrame.setGeometry(QtCore.QRect(40, 190, 511, 361))
        self.schedulingAppointmentsWindow_InputsHolderFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.schedulingAppointmentsWindow_InputsHolderFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.schedulingAppointmentsWindow_InputsHolderFrame.setStyleSheet("QFrame {\n"
"    border-image: none;\n"
"    background-color: rgb(52, 77, 103);\n"
"}")
        self.schedulingAppointmentsWindow_InputsHolderFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedulingAppointmentsWindow_InputsHolderFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schedulingAppointmentsWindow_InputsHolderFrame.setObjectName("schedulingAppointmentsWindow_InvalidStaffIDLabel_2")
        self.schedulingAppointmentsWindow_InputsHeadingLabel = QtWidgets.QLabel(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_InputsHeadingLabel.setGeometry(QtCore.QRect(20, 10, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.schedulingAppointmentsWindow_InputsHeadingLabel.setFont(font)
        self.schedulingAppointmentsWindow_InputsHeadingLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.schedulingAppointmentsWindow_InputsHeadingLabel.setObjectName("schedulingAppointmentsWindow_InputsHeadingLabel")
        self.labelschedulingAppointmentsWindow_StaffIDLabel = QtWidgets.QLabel(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.labelschedulingAppointmentsWindow_StaffIDLabel.setGeometry(QtCore.QRect(20, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelschedulingAppointmentsWindow_StaffIDLabel.setFont(font)
        self.labelschedulingAppointmentsWindow_StaffIDLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.labelschedulingAppointmentsWindow_StaffIDLabel.setObjectName("labelschedulingAppointmentsWindow_StaffIDLabel")
        self.schedulingAppointmentsWindow_PatientIDLabel = QtWidgets.QLabel(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_PatientIDLabel.setGeometry(QtCore.QRect(20, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schedulingAppointmentsWindow_PatientIDLabel.setFont(font)
        self.schedulingAppointmentsWindow_PatientIDLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.schedulingAppointmentsWindow_PatientIDLabel.setObjectName("schedulingAppointmentsWindow_PatientIDLabel")
        self.schedulingAppointmentsWindow_AppointmentTypeIDLabel = QtWidgets.QLabel(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_AppointmentTypeIDLabel.setGeometry(QtCore.QRect(20, 180, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schedulingAppointmentsWindow_AppointmentTypeIDLabel.setFont(font)
        self.schedulingAppointmentsWindow_AppointmentTypeIDLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.schedulingAppointmentsWindow_AppointmentTypeIDLabel.setObjectName("schedulingAppointmentsWindow_AppointmentTypeIDLabel")
        self.schedulingAppointmentsWindow_AppointmentReasonLabel = QtWidgets.QLabel(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_AppointmentReasonLabel.setGeometry(QtCore.QRect(20, 260, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schedulingAppointmentsWindow_AppointmentReasonLabel.setFont(font)
        self.schedulingAppointmentsWindow_AppointmentReasonLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.schedulingAppointmentsWindow_AppointmentReasonLabel.setObjectName("schedulingAppointmentsWindow_AppointmentReasonLabel")
        self.schedulingAppointmentsWindow_MeetTimeDateLabel = QtWidgets.QLabel(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_MeetTimeDateLabel.setGeometry(QtCore.QRect(20, 300, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schedulingAppointmentsWindow_MeetTimeDateLabel.setFont(font)
        self.schedulingAppointmentsWindow_MeetTimeDateLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.schedulingAppointmentsWindow_MeetTimeDateLabel.setObjectName("schedulingAppointmentsWindow_MeetTimeDateLabel")
        self.schedulingAppointmentsWindow_LocationIDLabel = QtWidgets.QLabel(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_LocationIDLabel.setGeometry(QtCore.QRect(20, 220, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schedulingAppointmentsWindow_LocationIDLabel.setFont(font)
        self.schedulingAppointmentsWindow_LocationIDLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.schedulingAppointmentsWindow_LocationIDLabel.setObjectName("schedulingAppointmentsWindow_LocationIDLabel")
        self.schedulingAppointmentsWindow_StaffIDLineEdit = QtWidgets.QLineEdit(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_StaffIDLineEdit.setGeometry(QtCore.QRect(100, 100, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.schedulingAppointmentsWindow_StaffIDLineEdit.setFont(font)
        self.schedulingAppointmentsWindow_StaffIDLineEdit.setStyleSheet("QLineEdit {\n"
"    border-image: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.schedulingAppointmentsWindow_StaffIDLineEdit.setObjectName("schedulingAppointmentsWindow_StaffIDLineEdit")
        self.schedulingAppointmentsWindow_PatientIDLineEdit = QtWidgets.QLineEdit(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_PatientIDLineEdit.setGeometry(QtCore.QRect(110, 140, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.schedulingAppointmentsWindow_PatientIDLineEdit.setFont(font)
        self.schedulingAppointmentsWindow_PatientIDLineEdit.setStyleSheet("QLineEdit {\n"
"    border-image: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.schedulingAppointmentsWindow_PatientIDLineEdit.setObjectName("schedulingAppointmentsWindow_PatientIDLineEdit")
        self.schedulingAppointmentsWindow_AppointmentTypeIDLineEdit = QtWidgets.QLineEdit(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_AppointmentTypeIDLineEdit.setGeometry(QtCore.QRect(190, 180, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.schedulingAppointmentsWindow_AppointmentTypeIDLineEdit.setFont(font)
        self.schedulingAppointmentsWindow_AppointmentTypeIDLineEdit.setStyleSheet("QLineEdit {\n"
"    border-image: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.schedulingAppointmentsWindow_AppointmentTypeIDLineEdit.setObjectName("schedulingAppointmentsWindow_AppointmentTypeIDLineEdit")
        self.schedulingAppointmentsWindow_LocationIDLineEdit = QtWidgets.QLineEdit(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_LocationIDLineEdit.setGeometry(QtCore.QRect(120, 220, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.schedulingAppointmentsWindow_LocationIDLineEdit.setFont(font)
        self.schedulingAppointmentsWindow_LocationIDLineEdit.setStyleSheet("QLineEdit {\n"
"    border-image: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.schedulingAppointmentsWindow_LocationIDLineEdit.setObjectName("schedulingAppointmentsWindow_LocationIDLineEdit")
        self.schedulingAppointmentsWindow_AppointmentReasonLineEdit = QtWidgets.QLineEdit(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_AppointmentReasonLineEdit.setGeometry(QtCore.QRect(180, 260, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.schedulingAppointmentsWindow_AppointmentReasonLineEdit.setFont(font)
        self.schedulingAppointmentsWindow_AppointmentReasonLineEdit.setStyleSheet("QLineEdit {\n"
"    border-image: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.schedulingAppointmentsWindow_AppointmentReasonLineEdit.setObjectName("schedulingAppointmentsWindow_AppointmentReasonLineEdit")
        self.schedulingAppointmentsWindow_MeetTimeDateDateTimeEdit = QtWidgets.QDateTimeEdit(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_MeetTimeDateDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.schedulingAppointmentsWindow_MeetTimeDateDateTimeEdit.setGeometry(QtCore.QRect(150, 301, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.schedulingAppointmentsWindow_MeetTimeDateDateTimeEdit.setFont(font)
        self.schedulingAppointmentsWindow_MeetTimeDateDateTimeEdit.setStyleSheet("QDateTimeEdit {\n"
"    border-image: none;\n"
"    background-color: white;\n"
"}")
        self.schedulingAppointmentsWindow_MeetTimeDateDateTimeEdit.setObjectName("schedulingAppointmentsWindow_MeetTimeDateDateTimeEdit")
        self.schedulingAppointmentsWindow_InvalidInputsLabel = QtWidgets.QLabel(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_InvalidInputsLabel.setGeometry(QtCore.QRect(20, 50, 471, 0))
        self.schedulingAppointmentsWindow_InvalidInputsLabel.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.schedulingAppointmentsWindow_InvalidInputsLabel.setFont(font)
        self.schedulingAppointmentsWindow_InvalidInputsLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: rgb(0, 255, 127);\n"
"}")
        self.schedulingAppointmentsWindow_InvalidInputsLabel.setObjectName("schedulingAppointmentsWindow_InvalidInputsLabel")
        self.schedulingAppointmentsWindow_InvalidStaffIDLabel = QtWidgets.QLabel(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_InvalidStaffIDLabel.setGeometry(QtCore.QRect(480, 110, 21, 0))
        self.schedulingAppointmentsWindow_InvalidStaffIDLabel.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        self.schedulingAppointmentsWindow_InvalidStaffIDLabel.setFont(font)
        self.schedulingAppointmentsWindow_InvalidStaffIDLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: rgb(0, 255, 127);\n"
"}")
        self.schedulingAppointmentsWindow_InvalidStaffIDLabel.setObjectName("schedulingAppointmentsWindow_InvalidStaffIDLabel")
        self.schedulingAppointmentsWindow_InvalidPatientIDLabel = QtWidgets.QLabel(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_InvalidPatientIDLabel.setGeometry(QtCore.QRect(480, 150, 21, 0))
        self.schedulingAppointmentsWindow_InvalidPatientIDLabel.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        self.schedulingAppointmentsWindow_InvalidPatientIDLabel.setFont(font)
        self.schedulingAppointmentsWindow_InvalidPatientIDLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: rgb(0, 255, 127);\n"
"}")
        self.schedulingAppointmentsWindow_InvalidPatientIDLabel.setObjectName("schedulingAppointmentsWindow_InvalidPatientIDLabel")
        self.schedulingAppointmentsWindow_InvalidAppointmentTypeIDLabel = QtWidgets.QLabel(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_InvalidAppointmentTypeIDLabel.setGeometry(QtCore.QRect(480, 190, 21, 0))
        self.schedulingAppointmentsWindow_InvalidAppointmentTypeIDLabel.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        self.schedulingAppointmentsWindow_InvalidAppointmentTypeIDLabel.setFont(font)
        self.schedulingAppointmentsWindow_InvalidAppointmentTypeIDLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: rgb(0, 255, 127);\n"
"}")
        self.schedulingAppointmentsWindow_InvalidAppointmentTypeIDLabel.setObjectName("schedulingAppointmentsWindow_InvalidAppointmentTypeIDLabel")
        self.schedulingAppointmentsWindow_InvalidLocationIDLabel = QtWidgets.QLabel(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_InvalidLocationIDLabel.setGeometry(QtCore.QRect(480, 230, 21, 0))
        self.schedulingAppointmentsWindow_InvalidLocationIDLabel.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        self.schedulingAppointmentsWindow_InvalidLocationIDLabel.setFont(font)
        self.schedulingAppointmentsWindow_InvalidLocationIDLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: rgb(0, 255, 127);\n"
"}")
        self.schedulingAppointmentsWindow_InvalidLocationIDLabel.setObjectName("schedulingAppointmentsWindow_InvalidLocationIDLabel")
        self.schedulingAppointmentsWindow_InvalidAppointmentReasonLabel = QtWidgets.QLabel(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_InvalidAppointmentReasonLabel.setGeometry(QtCore.QRect(480, 270, 21, 0))
        self.schedulingAppointmentsWindow_InvalidAppointmentReasonLabel.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        self.schedulingAppointmentsWindow_InvalidAppointmentReasonLabel.setFont(font)
        self.schedulingAppointmentsWindow_InvalidAppointmentReasonLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: rgb(0, 255, 127);\n"
"}")
        self.schedulingAppointmentsWindow_InvalidAppointmentReasonLabel.setObjectName("schedulingAppointmentsWindow_InvalidAppointmentReasonLabel")
        self.schedulingAppointmentsWindow_InvalidMeetTimeDateLabel = QtWidgets.QLabel(self.schedulingAppointmentsWindow_InputsHolderFrame)
        self.schedulingAppointmentsWindow_InvalidMeetTimeDateLabel.setGeometry(QtCore.QRect(480, 310, 21, 0))
        self.schedulingAppointmentsWindow_InvalidMeetTimeDateLabel.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        self.schedulingAppointmentsWindow_InvalidMeetTimeDateLabel.setFont(font)
        self.schedulingAppointmentsWindow_InvalidMeetTimeDateLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: rgb(0, 255, 127);\n"
"}")
        self.schedulingAppointmentsWindow_InvalidMeetTimeDateLabel.setObjectName("schedulingAppointmentsWindow_InvalidMeetTimeDateLabel")
        self.schedulingAppointmentsWindow_CalendarFrame = QtWidgets.QFrame(self.centralwidget)
        self.schedulingAppointmentsWindow_CalendarFrame.setGeometry(QtCore.QRect(590, 20, 1191, 671))
        self.schedulingAppointmentsWindow_CalendarFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.schedulingAppointmentsWindow_CalendarFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.schedulingAppointmentsWindow_CalendarFrame.setStyleSheet("QFrame {\n"
"    border-image: none;\n"
"    background-color: ghostwhite;\n"
"}")
        self.schedulingAppointmentsWindow_CalendarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedulingAppointmentsWindow_CalendarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schedulingAppointmentsWindow_CalendarFrame.setObjectName("schedulingAppointmentsWindow_CalendarFrame")
        self.schedulingAppointmentsWindow_AppointmentsCalendarLabel = QtWidgets.QLabel(self.schedulingAppointmentsWindow_CalendarFrame)
        self.schedulingAppointmentsWindow_AppointmentsCalendarLabel.setGeometry(QtCore.QRect(10, 10, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schedulingAppointmentsWindow_AppointmentsCalendarLabel.setFont(font)
        self.schedulingAppointmentsWindow_AppointmentsCalendarLabel.setStyleSheet("QLabel {\n"
"    color: rgb(161, 161, 161);\n"
"}")
        self.schedulingAppointmentsWindow_AppointmentsCalendarLabel.setObjectName("schedulingAppointmentsWindow_AppointmentsCalendarLabel")
        self.schedulingAppointmentsWindow_ScheduleBtn = QtWidgets.QPushButton(self.centralwidget)
        self.schedulingAppointmentsWindow_ScheduleBtn.clicked.connect(checkInputs)
        self.schedulingAppointmentsWindow_ScheduleBtn.setGeometry(QtCore.QRect(40, 570, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schedulingAppointmentsWindow_ScheduleBtn.setFont(font)
        self.schedulingAppointmentsWindow_ScheduleBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.schedulingAppointmentsWindow_ScheduleBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}")
        self.schedulingAppointmentsWindow_ScheduleBtn.setObjectName("schedulingAppointmentsWindow_ScheduleBtn")
        self.schedulingAppointmentsWindow_ClearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.schedulingAppointmentsWindow_ClearBtn.clicked.connect(resetInputsAndLabels)
        self.schedulingAppointmentsWindow_ClearBtn.setGeometry(QtCore.QRect(170, 570, 75, 41))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schedulingAppointmentsWindow_ClearBtn.setFont(font)
        self.schedulingAppointmentsWindow_ClearBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.schedulingAppointmentsWindow_ClearBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}")
        self.schedulingAppointmentsWindow_ClearBtn.setObjectName("schedulingAppointmentsWindow_ClearBtn")
        SchedulingAppointmentsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SchedulingAppointmentsWindow)
        QtCore.QMetaObject.connectSlotsByName(SchedulingAppointmentsWindow)

    def retranslateUi(self, SchedulingAppointmentsWindow):
        _translate = QtCore.QCoreApplication.translate
        SchedulingAppointmentsWindow.setWindowTitle(_translate("SchedulingAppointmentsWindow", "Forsyth Family Practice Center - Scheduling Appointments"))
        self.schedulingAppointmentsWindow_CheckinBtn.setText(_translate("SchedulingAppointmentsWindow", "Check-in"))
        self.schedulingAppointmentsWindow_CheckoutBtn.setText(_translate("SchedulingAppointmentsWindow", "Check-out"))
        self.schedulingAppointmentsWindow_LabOrdersBtn.setText(_translate("SchedulingAppointmentsWindow", "Lab Orders"))
        self.schedulingAppointmentsWindow_LogoutBtn.setText(_translate("SchedulingAppointmentsWindow", "Logout"))
        self.schedulingAppointmentsWindow_MakeReferralBtn.setText(_translate("SchedulingAppointmentsWindow", "Make Referral"))
        self.schedulingAppointmentsWindow_HeadingLabel.setText(_translate("SchedulingAppointmentsWindow", "Schedule An Appointment"))
        self.schedulingAppointmentsWindow_InputsHeadingLabel.setText(_translate("SchedulingAppointmentsWindow", "Please provide some information to schedule the appointment."))
        self.labelschedulingAppointmentsWindow_StaffIDLabel.setText(_translate("SchedulingAppointmentsWindow", "Staff ID:"))
        self.schedulingAppointmentsWindow_PatientIDLabel.setText(_translate("SchedulingAppointmentsWindow", "Patient ID:"))
        self.schedulingAppointmentsWindow_AppointmentTypeIDLabel.setText(_translate("SchedulingAppointmentsWindow", "Appointment Type ID:"))
        self.schedulingAppointmentsWindow_AppointmentReasonLabel.setText(_translate("SchedulingAppointmentsWindow", "Appointment Reason:"))
        self.schedulingAppointmentsWindow_MeetTimeDateLabel.setText(_translate("SchedulingAppointmentsWindow", "Meet time/date:"))
        self.schedulingAppointmentsWindow_LocationIDLabel.setText(_translate("SchedulingAppointmentsWindow", "Location ID:"))
        self.schedulingAppointmentsWindow_InvalidInputsLabel.setText(_translate("SchedulingAppointmentsWindow", "INVALID INPUTS"))
        self.schedulingAppointmentsWindow_InvalidStaffIDLabel.setText(_translate("SchedulingAppointmentsWindow", "*"))
        self.schedulingAppointmentsWindow_InvalidPatientIDLabel.setText(_translate("SchedulingAppointmentsWindow", "*"))
        self.schedulingAppointmentsWindow_InvalidAppointmentTypeIDLabel.setText(_translate("SchedulingAppointmentsWindow", "*"))
        self.schedulingAppointmentsWindow_InvalidLocationIDLabel.setText(_translate("SchedulingAppointmentsWindow", "*"))
        self.schedulingAppointmentsWindow_InvalidAppointmentReasonLabel.setText(_translate("SchedulingAppointmentsWindow", "*"))
        self.schedulingAppointmentsWindow_InvalidMeetTimeDateLabel.setText(_translate("SchedulingAppointmentsWindow", "*"))
        self.schedulingAppointmentsWindow_AppointmentsCalendarLabel.setText(_translate("SchedulingAppointmentsWindow", "Appointments Calendar"))
        self.schedulingAppointmentsWindow_ScheduleBtn.setText(_translate("SchedulingAppointmentsWindow", "SCHEDULE"))
        self.schedulingAppointmentsWindow_ClearBtn.setText(_translate("SchedulingAppointmentsWindow", "CLEAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SchedulingAppointmentsWindow = QtWidgets.QMainWindow()
    ui = Ui_SchedulingAppointmentsWindow()
    ui.setupUi(SchedulingAppointmentsWindow)
    SchedulingAppointmentsWindow.show()
    sys.exit(app.exec_())
