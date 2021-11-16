

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

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None

        self._previousLocation = ''

        self._makeConnections()

    def _makeConnections(self):
        self._ui.idLineEdit.textChanged.connect(self.validate)
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
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.idLineEdit.text())
        valid_identifier = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.idLineEdit.text())
        self._ui.idLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET if valid_identifier else INVALID_STYLE_SHEET)
        self._ui.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(valid_identifier)

        output_location = self._output_location()
        if self._workflow_location:
            output_location = os.path.join(self._workflow_location, output_location)

        # valid_location = os.path.isfile(os.path.join(self._workflow_location, self._ui.locLineEdit.text()))
        valid_location = os.path.isfile(output_location)
        self._ui.locLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET if valid_location else INVALID_STYLE_SHEET)

        return valid_identifier and valid_location

    def getConfig(self):
        """
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = self._ui.idLineEdit.text()
        self._previousLocation = self._ui.locLineEdit.text()
        config = {}
        config['identifier'] = self._ui.idLineEdit.text()
        config['Location'] = self._ui.locLineEdit.text()
        return config

    def setConfig(self, config):
        """
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = config['identifier']
        self._previousLocation = config['Location']
        self._ui.idLineEdit.setText(config['identifier'])
        self._ui.locLineEdit.setText(config['Location'])

    def _locClicked(self):
        location, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select File Location', self._previousLocation)
        if location:
            self._previousLocation = location
            # self._ui.locLineEdit.setText(os.path.relpath(location, self._workflow_location))
            display_location = self._output_location(location)
            self._ui.locLineEdit.setText(display_location)

    def _output_location(self, location=None):
        if location is None:
            display_path = self._ui.locLineEdit.text()
        else:
            display_path = location
        if self._workflow_location and os.path.isabs(display_path):
            display_path = os.path.relpath(display_path, self._workflow_location)

        return display_path