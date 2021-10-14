

from PySide2 import QtWidgets
from mapclientplugins.trcsourcestep.ui_configuredialog import Ui_ConfigureDialog
import os

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QtWidgets.QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)

        self._workflow_location = None

        self._previousLocation = ''

        self._makeConnections()

    def _makeConnections(self):
        self._ui.locLineEdit.textChanged.connect(self.validate)
        self._ui.locButton.clicked.connect(self._locClicked)

    def setWorkflowLocation(self, location):
        self._workflow_location = location

    def accept(self):
        """
        Override the accept method so that we can confirm saving an
        invalid configuration.
        """
        result = QtWidgets.QMessageBox.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(self, 'Invalid Configuration',
                'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        """
        Validate the configuration dialog fields.  For any field that is not valid_identifier
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the 
        overall validity of the configuration.
        """
        output_directory = self._ui.locLineEdit.text()
        non_empty = len(output_directory)
        if not os.path.isabs(output_directory):
            output_directory = os.path.join(self._workflow_location, output_directory)

        valid_location = os.path.exists(output_directory) and non_empty

        self._ui.locLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET if valid_location else INVALID_STYLE_SHEET)

        return valid_location

    def getConfig(self):
        """
        Get the current value of the configuration from the dialog.
        """
        self._previousLocation = self._ui.locLineEdit.text()
        config = {}
        config['Location'] = self._ui.locLineEdit.text()
        return config

    def setConfig(self, config):
        """
        Set the current value of the configuration for the dialog.
        """
        self._previousLocation = config['Location']
        self._ui.locLineEdit.setText(config['Location'])

    def _locClicked(self):
        location, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select File Location', self._previousLocation)
        if location:
            self._previousLocation = location

            if self._workflow_location:
                self._ui.locLineEdit.setText(os.path.relpath(location, self._workflow_location))
            else:
                self._ui.locLineEdit.setText(location)
