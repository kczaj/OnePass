from abc import ABC, abstractmethod


class VWindow(ABC):

    def __init__(self):
        self.controller = None

    def update_main_window(self, main_win):
        self.controller.set_main_window(main_win)

    def arrow_button_pressed(self):
        self.controller.arrow_button_handle()

    def show(self, where):
        self.setupUi(where)

    @abstractmethod
    def setupUi(self, where):
        pass
