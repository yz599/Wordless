#
# Wordless: Layout
#
# Copyright (C) 2018 Ye Lei (叶磊) <blkserene@gmail.com>
#
# License Information: https://github.com/BLKSerene/Wordless/blob/master/LICENSE.txt
#

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Wordless_Splitter(QSplitter):
    def __init__(self, parent):
        super().__init__(parent)

        self.setHandleWidth(1)
        self.setChildrenCollapsible(False)

class Wordless_Scroll_Area(QScrollArea):
    def __init__(self, parent, wrapped_widget):
        super().__init__(parent)

        self.setWidget(wrapped_widget)

        self.setWidgetResizable(True)
        self.setBackgroundRole(QPalette.Light)
        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

class Wordless_Tab(QWidget):
    def __init__(self, main, load_settings):
        super().__init__(main)

        self.main = main
        self.load_settings = load_settings

        self.wrapper_left = QWidget(self)

        self.wrapper_left.setLayout(QGridLayout())

        self.wrapper_right = QWidget(self)

        wrapper_settings = QWidget(self)
        wrapper_settings.setLayout(QGridLayout())

        self.scroll_area_settings = Wordless_Scroll_Area(self.main, wrapper_settings)
        button_restore_defaults = QPushButton(self.tr('Restore Defaults'), self.main)

        button_restore_defaults.clicked.connect(self.restore_defaults)

        self.wrapper_right.setLayout(QGridLayout())
        self.wrapper_right.layout().addWidget(self.scroll_area_settings, 0, 0)
        self.wrapper_right.layout().addWidget(button_restore_defaults, 1, 0)

        self.splitter_tab = Wordless_Splitter(self)
        self.splitter_tab.addWidget(self.wrapper_left)
        self.splitter_tab.addWidget(self.wrapper_right)

        self.splitter_tab.setSizes([main.width() * 0.77, main.width() * 0.23])

        self.setLayout(QGridLayout())
        self.layout().addWidget(self.splitter_tab)

        self.layout_table = self.wrapper_left.layout()
        self.layout_settings = wrapper_settings.layout()

    def restore_defaults(self):
        reply = QMessageBox.question(self.main,
                                     self.tr('Restore Defaults'),
                                     self.tr('Do you really want to reset all settings to defaults?'),
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.load_settings(defaults = True)

class Wordless_Separator(QFrame):
    def __init__(self, parent, orientation = 'Horizontal'):
        super().__init__(parent)

        if orientation == 'Horizontal':
            self.setFrameShape(QFrame.HLine)
        else:
            self.setFrameShape(QFrame.VLine)

        self.setStyleSheet('color: #D0D0D0;')