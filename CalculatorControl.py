from PySide6.QtCore import Qt
class CalculatorControl:
    def __init__(self, model, view):
        self.model=model
        self.view = view
        if self.view.scheme == Qt.ColorScheme.Dark:
             self.view.dark_mode()
             self.view.mode.setChecked(True)
        else:
            self.view.light_mode()
        self.view.mode.toggled.connect(self.modes)

    def text_handle(self):
        values = self.view.screen.text().split()
        answer = self.manager(values)
        if answer != None:
            self.view.display_answer(answer)
        if answer == None:
            self.view.press()
            return
    def manager(self, values):
        if len(values) == 0:
            self.view.press()
            return
        else:
             self.model.bracket(values)
             answer = self.model.conversion(values)
             answer = self.model.validation(answer)
             answer = self.model.normalization(answer)
             answer = self.model.bidmas(answer)
             return answer
    def modes(self,checked):
        if checked:
            self.view.dark_mode()
        else:
            self.view.light_mode()







