#
# Wordless: Widgets - Button
#
# Copyright (C) 2018-2019  Ye Lei (叶磊)
#
# This source file is licensed under GNU GPLv3.
# For details, see: https://github.com/BLKSerene/Wordless/blob/master/LICENSE.txt
#
# All other rights reserved.
#

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from wordless_dialogs import wordless_msg_box
from wordless_utils import wordless_misc

class Wordless_Button(QPushButton):
    def __init__(self, text, parent):
        super().__init__(text, parent)

        self.main = wordless_misc.find_wordless_main(parent)

class Wordless_Button_Reset_Settings(Wordless_Button):
    def __init__(self, parent):
        super().__init__(parent.tr('Reset Settings'), parent)

        self.parent = parent

        self.clicked.connect(self.reset_settings)

    def reset_settings(self):
        if wordless_msg_box.wordless_msg_box_reset_settings(self.main):
            self.parent.load_settings(defaults = True)

        self.parent.activateWindow()

class Wordless_Button_Reset_All_Settings(Wordless_Button):
    def __init__(self, parent):
        super().__init__(parent.tr('Reset All Settings'), parent)

        self.parent = parent

        self.clicked.connect(self.reset_settings)

    def reset_settings(self):
        if wordless_msg_box.wordless_msg_box_reset_all_settings(self.main):
            self.parent.load_settings(defaults = True)

        self.parent.activateWindow()
        