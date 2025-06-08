from PySide2 import QtWidgets
from ai.text_design import generate_from_text


class AIDesignDialog(QtWidgets.QDialog):
    """Simple dialog to enter a text command for AI design."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("AI Design")
        self.resize(300, 100)

        layout = QtWidgets.QVBoxLayout(self)
        self.text_edit = QtWidgets.QLineEdit(self)
        layout.addWidget(self.text_edit)

        button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            parent=self,
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def get_text(self):
        if self.exec_() == QtWidgets.QDialog.Accepted:
            return self.text_edit.text().strip()
        return None


def run_dialog():
    dialog = AIDesignDialog()
    command = dialog.get_text()
    if command:
        try:
            generate_from_text(command)
        except Exception as exc:
            QtWidgets.QMessageBox.warning(dialog, "Error", str(exc))
