from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(334, 503)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.labl_ength = QLabel(self.centralwidget)
        self.labl_ength.setObjectName(u"labl_ength")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labl_ength)

        self.text_length = QPlainTextEdit(self.centralwidget)
        self.text_length.setObjectName(u"text_length")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.text_length)

        self.lab_width = QLabel(self.centralwidget)
        self.lab_width.setObjectName(u"lab_width")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lab_width)

        self.text_width = QPlainTextEdit(self.centralwidget)
        self.text_width.setObjectName(u"text_width")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.text_width)

        self.lab_height = QLabel(self.centralwidget)
        self.lab_height.setObjectName(u"lab_height")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lab_height)

        self.text_height = QPlainTextEdit(self.centralwidget)
        self.text_height.setObjectName(u"text_height")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.text_height)

        self.lab_rul = QLabel(self.centralwidget)
        self.lab_rul.setObjectName(u"lab_rul")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lab_rul)

        self.text_rul = QPlainTextEdit(self.centralwidget)
        self.text_rul.setObjectName(u"text_rul")

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.text_rul)

        self.lab_square = QLabel(self.centralwidget)
        self.lab_square.setObjectName(u"lab_square")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.lab_square)

        self.lab_ruls = QLabel(self.centralwidget)
        self.lab_ruls.setObjectName(u"lab_ruls")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.lab_ruls)

        self.button_save = QPushButton(self.centralwidget)
        self.button_save.setObjectName(u"button_save")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.button_save)

        self.button_import = QPushButton(self.centralwidget)
        self.button_import.setObjectName(u"button_import")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.button_import)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labl_ength.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430", None))
        self.lab_width.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430", None))
        self.lab_height.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430", None))
        self.lab_rul.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0440\u0443\u043b\u043e\u043d\u0435", None))
        self.lab_square.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u0441\u0442\u0435\u043d = \u043a\u0432. \u043c", None))
        self.lab_ruls.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0443\u0436\u043d\u043e \u0440\u0443\u043b\u043e\u043d\u0430 (\u043e\u0432)", None))
        self.button_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.button_import.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))