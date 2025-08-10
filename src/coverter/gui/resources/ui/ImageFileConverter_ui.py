# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImageFileConvertereGxEAr.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

from resources.qrc import ImageFileConverter_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1036, 785)
        font = QFont()
        font.setFamilies([u"Bookman Old Style"])
        font.setPointSize(12)
        font.setBold(False)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setIconSize(QSize(48, 48))
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.header_layout = QVBoxLayout()
        self.header_layout.setObjectName(u"header_layout")
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setMinimumSize(QSize(0, 80))
        self.label_title.setMaximumSize(QSize(16777215, 150))
        self.label_title.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Bookman Old Style"])
        font1.setPointSize(26)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.label_title.setFont(font1)
        self.label_title.setAcceptDrops(True)
        self.label_title.setStyleSheet(u"background-color: rgb(85, 85, 127);")
        self.label_title.setFrameShape(QFrame.Shape.NoFrame)
        self.label_title.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_title.setTextFormat(Qt.TextFormat.PlainText)
        self.label_title.setScaledContents(False)
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_title.setWordWrap(False)
        self.label_title.setMargin(-1)
        self.label_title.setIndent(-1)

        self.header_layout.addWidget(self.label_title)


        self.verticalLayout_6.addLayout(self.header_layout)

        self.main = QHBoxLayout()
        self.main.setObjectName(u"main")
        self.main_vertical_layout_for_the_last_time = QVBoxLayout()
        self.main_vertical_layout_for_the_last_time.setObjectName(u"main_vertical_layout_for_the_last_time")
        self.groupbox_bulk_conversion = QGroupBox(self.centralwidget)
        self.groupbox_bulk_conversion.setObjectName(u"groupbox_bulk_conversion")
        self.groupbox_bulk_conversion.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupbox_bulk_conversion.sizePolicy().hasHeightForWidth())
        self.groupbox_bulk_conversion.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.groupbox_bulk_conversion)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_bulk_conversion = QLabel(self.groupbox_bulk_conversion)
        self.label_bulk_conversion.setObjectName(u"label_bulk_conversion")
        self.label_bulk_conversion.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_bulk_conversion.sizePolicy().hasHeightForWidth())
        self.label_bulk_conversion.setSizePolicy(sizePolicy2)
        self.label_bulk_conversion.setMaximumSize(QSize(16777215, 16))
        self.label_bulk_conversion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_bulk_conversion)

        self.tablewidget_bulk_conversion = QTableWidget(self.groupbox_bulk_conversion)
        self.tablewidget_bulk_conversion.setObjectName(u"tablewidget_bulk_conversion")
        self.tablewidget_bulk_conversion.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tablewidget_bulk_conversion.sizePolicy().hasHeightForWidth())
        self.tablewidget_bulk_conversion.setSizePolicy(sizePolicy3)
        self.tablewidget_bulk_conversion.setMinimumSize(QSize(0, 200))
        self.tablewidget_bulk_conversion.setMaximumSize(QSize(999999, 99999))
        self.tablewidget_bulk_conversion.setAcceptDrops(True)
        self.tablewidget_bulk_conversion.setStyleSheet(u"border:1px solid rgb(75, 75, 75);")
        self.tablewidget_bulk_conversion.setRowCount(0)
        self.tablewidget_bulk_conversion.setColumnCount(0)
        self.tablewidget_bulk_conversion.horizontalHeader().setCascadingSectionResizes(True)
        self.tablewidget_bulk_conversion.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_4.addWidget(self.tablewidget_bulk_conversion)

        self.button_bulk_conversion_browse_files = QPushButton(self.groupbox_bulk_conversion)
        self.button_bulk_conversion_browse_files.setObjectName(u"button_bulk_conversion_browse_files")
        self.button_bulk_conversion_browse_files.setEnabled(True)
        self.button_bulk_conversion_browse_files.setStyleSheet(u"QPushButton:hover {\n"
"background-color: #474769;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #383851;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: #565681;\n"
"padding: 3px 5px;\n"
"border-radius: 6px;\n"
"border: 1px solid #4a4a4a;\n"
"}")

        self.verticalLayout_4.addWidget(self.button_bulk_conversion_browse_files)

        self.line_2 = QFrame(self.groupbox_bulk_conversion)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.horizontalLayout_clear_listwidget = QHBoxLayout()
        self.horizontalLayout_clear_listwidget.setObjectName(u"horizontalLayout_clear_listwidget")
        self.button_remove_selected = QPushButton(self.groupbox_bulk_conversion)
        self.button_remove_selected.setObjectName(u"button_remove_selected")
        self.button_remove_selected.setStyleSheet(u"QPushButton:hover {\n"
"background-color: #763d3c;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #572f2e;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: #7b4240;\n"
"padding: 3px 5px;\n"
"border-radius: 6px;\n"
"border: 1px solid #4a4a4a;\n"
"}")

        self.horizontalLayout_clear_listwidget.addWidget(self.button_remove_selected)

        self.button_remove_all = QPushButton(self.groupbox_bulk_conversion)
        self.button_remove_all.setObjectName(u"button_remove_all")
        self.button_remove_all.setStyleSheet(u"QPushButton:hover {\n"
"background-color: #763d3c;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #572f2e;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: #7b4240;\n"
"padding: 3px 5px;\n"
"border-radius: 6px;\n"
"border: 1px solid #4a4a4a;\n"
"}")

        self.horizontalLayout_clear_listwidget.addWidget(self.button_remove_all)


        self.verticalLayout_4.addLayout(self.horizontalLayout_clear_listwidget)


        self.main_vertical_layout_for_the_last_time.addWidget(self.groupbox_bulk_conversion)

        self.groupbox_options = QGroupBox(self.centralwidget)
        self.groupbox_options.setObjectName(u"groupbox_options")
        sizePolicy1.setHeightForWidth(self.groupbox_options.sizePolicy().hasHeightForWidth())
        self.groupbox_options.setSizePolicy(sizePolicy1)
        self.groupbox_options.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.groupbox_options)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.groupbox_options)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setFamilies([u"Bookman Old Style"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_6.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.combobox_extension_type = QComboBox(self.groupbox_options)
        self.combobox_extension_type.addItem("")
        self.combobox_extension_type.addItem("")
        self.combobox_extension_type.addItem("")
        self.combobox_extension_type.addItem("")
        self.combobox_extension_type.addItem("")
        self.combobox_extension_type.setObjectName(u"combobox_extension_type")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.combobox_extension_type.sizePolicy().hasHeightForWidth())
        self.combobox_extension_type.setSizePolicy(sizePolicy5)
        self.combobox_extension_type.setFont(font)
        self.combobox_extension_type.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.combobox_extension_type)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.groupbox_options)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.horizontalSpacer_4 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.line_edit_save_image_to = QLineEdit(self.groupbox_options)
        self.line_edit_save_image_to.setObjectName(u"line_edit_save_image_to")
        sizePolicy5.setHeightForWidth(self.line_edit_save_image_to.sizePolicy().hasHeightForWidth())
        self.line_edit_save_image_to.setSizePolicy(sizePolicy5)
        self.line_edit_save_image_to.setFont(font)
        self.line_edit_save_image_to.setClearButtonEnabled(True)

        self.horizontalLayout_5.addWidget(self.line_edit_save_image_to)

        self.button_browse_save_image_to = QPushButton(self.groupbox_options)
        self.button_browse_save_image_to.setObjectName(u"button_browse_save_image_to")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.button_browse_save_image_to.sizePolicy().hasHeightForWidth())
        self.button_browse_save_image_to.setSizePolicy(sizePolicy6)
        self.button_browse_save_image_to.setFont(font)
        self.button_browse_save_image_to.setStyleSheet(u"QPushButton:hover {\n"
"background-color: #474769;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #383851;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: #565681;\n"
"padding: 3px 5px;\n"
"border-radius: 6px;\n"
"border: 1px solid #4a4a4a;\n"
"}")

        self.horizontalLayout_5.addWidget(self.button_browse_save_image_to)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupbox_options)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(125, 125, 186);")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(66, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.groupbox_options)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.spinbox_resize_image_width = QSpinBox(self.groupbox_options)
        self.spinbox_resize_image_width.setObjectName(u"spinbox_resize_image_width")
        sizePolicy6.setHeightForWidth(self.spinbox_resize_image_width.sizePolicy().hasHeightForWidth())
        self.spinbox_resize_image_width.setSizePolicy(sizePolicy6)
        self.spinbox_resize_image_width.setFont(font)
        self.spinbox_resize_image_width.setStyleSheet(u"")
        self.spinbox_resize_image_width.setMinimum(0)
        self.spinbox_resize_image_width.setMaximum(9999)

        self.horizontalLayout_4.addWidget(self.spinbox_resize_image_width)

        self.label_4 = QLabel(self.groupbox_options)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.spinbox_resize_image_height = QSpinBox(self.groupbox_options)
        self.spinbox_resize_image_height.setObjectName(u"spinbox_resize_image_height")
        sizePolicy6.setHeightForWidth(self.spinbox_resize_image_height.sizePolicy().hasHeightForWidth())
        self.spinbox_resize_image_height.setSizePolicy(sizePolicy6)
        self.spinbox_resize_image_height.setFont(font)
        self.spinbox_resize_image_height.setStyleSheet(u"")
        self.spinbox_resize_image_height.setMaximum(9999)

        self.horizontalLayout_4.addWidget(self.spinbox_resize_image_height)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.line = QFrame(self.groupbox_options)
        self.line.setObjectName(u"line")
        self.line.setFont(font)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.button_convert = QPushButton(self.groupbox_options)
        self.button_convert.setObjectName(u"button_convert")
        sizePolicy6.setHeightForWidth(self.button_convert.sizePolicy().hasHeightForWidth())
        self.button_convert.setSizePolicy(sizePolicy6)
        self.button_convert.setFont(font)
        self.button_convert.setStyleSheet(u"QPushButton:hover {\n"
"background-color: #474769;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #383851;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: #565681;\n"
"padding: 3px 5px;\n"
"border-radius: 6px;\n"
"border: 1px solid #4a4a4a;\n"
"}")

        self.verticalLayout_3.addWidget(self.button_convert)


        self.main_vertical_layout_for_the_last_time.addWidget(self.groupbox_options)


        self.main.addLayout(self.main_vertical_layout_for_the_last_time)

        self.image_info_layout = QVBoxLayout()
        self.image_info_layout.setObjectName(u"image_info_layout")
        self.groupbox_image_info = QGroupBox(self.centralwidget)
        self.groupbox_image_info.setObjectName(u"groupbox_image_info")
        sizePolicy1.setHeightForWidth(self.groupbox_image_info.sizePolicy().hasHeightForWidth())
        self.groupbox_image_info.setSizePolicy(sizePolicy1)
        self.groupbox_image_info.setMinimumSize(QSize(250, 0))
        self.groupbox_image_info.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.groupbox_image_info)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labe_metadata = QLabel(self.groupbox_image_info)
        self.labe_metadata.setObjectName(u"labe_metadata")
        sizePolicy2.setHeightForWidth(self.labe_metadata.sizePolicy().hasHeightForWidth())
        self.labe_metadata.setSizePolicy(sizePolicy2)
        self.labe_metadata.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.labe_metadata)

        self.text_edit_image_info = QTextEdit(self.groupbox_image_info)
        self.text_edit_image_info.setObjectName(u"text_edit_image_info")
        sizePolicy5.setHeightForWidth(self.text_edit_image_info.sizePolicy().hasHeightForWidth())
        self.text_edit_image_info.setSizePolicy(sizePolicy5)
        self.text_edit_image_info.setMinimumSize(QSize(0, 200))

        self.verticalLayout_2.addWidget(self.text_edit_image_info)

        self.label_image_preview_text = QLabel(self.groupbox_image_info)
        self.label_image_preview_text.setObjectName(u"label_image_preview_text")
        sizePolicy2.setHeightForWidth(self.label_image_preview_text.sizePolicy().hasHeightForWidth())
        self.label_image_preview_text.setSizePolicy(sizePolicy2)
        self.label_image_preview_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_image_preview_text)

        self.label_image_preview = QLabel(self.groupbox_image_info)
        self.label_image_preview.setObjectName(u"label_image_preview")
        self.label_image_preview.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"border:1px solid rgb(75, 75, 75);")
        self.label_image_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_image_preview)


        self.image_info_layout.addWidget(self.groupbox_image_info)


        self.main.addLayout(self.image_info_layout)


        self.verticalLayout_6.addLayout(self.main)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1036, 33))
        self.menubar.setStyleSheet(u"")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Image Converter", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Image File Converter", None))
        self.groupbox_bulk_conversion.setTitle(QCoreApplication.translate("MainWindow", u"Bulk Conversion", None))
        self.label_bulk_conversion.setText(QCoreApplication.translate("MainWindow", u"Drag and drop images into this container:", None))
        self.button_bulk_conversion_browse_files.setText(QCoreApplication.translate("MainWindow", u"... or browse files here", None))
        self.button_remove_selected.setText(QCoreApplication.translate("MainWindow", u"Remove Selected", None))
        self.button_remove_all.setText(QCoreApplication.translate("MainWindow", u"Remove All", None))
        self.groupbox_options.setTitle(QCoreApplication.translate("MainWindow", u"Options Selection", None))
        self.label_6.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(125, 125, 186);", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Output extension:", None))
        self.combobox_extension_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Choose file extension...", None))
        self.combobox_extension_type.setItemText(1, QCoreApplication.translate("MainWindow", u".png", None))
        self.combobox_extension_type.setItemText(2, QCoreApplication.translate("MainWindow", u".jpeg", None))
        self.combobox_extension_type.setItemText(3, QCoreApplication.translate("MainWindow", u".ico", None))
        self.combobox_extension_type.setItemText(4, QCoreApplication.translate("MainWindow", u".pdf", None))

        self.combobox_extension_type.setPlaceholderText("")
        self.label_7.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(125, 125, 186);", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Save image to:", None))
        self.line_edit_save_image_to.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Browse folder directory...", None))
        self.button_browse_save_image_to.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Resize image:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"W:", None))
        self.spinbox_resize_image_width.setSpecialValueText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"H:", None))
        self.button_convert.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.groupbox_image_info.setTitle(QCoreApplication.translate("MainWindow", u"Image Information", None))
        self.labe_metadata.setText(QCoreApplication.translate("MainWindow", u"Metadata:", None))
        self.text_edit_image_info.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: rgb(45, 45, 45);\n"
"border:1px solid rgb(75, 75, 75);", None))
        self.label_image_preview_text.setText(QCoreApplication.translate("MainWindow", u"Image Preview:", None))
        self.label_image_preview.setText("")
    # retranslateUi

