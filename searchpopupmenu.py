from customdialogs import MDInputDialog


class SearchPopupMenu(MDInputDialog):
    title = "Search by Address"
    text_button_ok = "Go!"

    def __init__(self):
        super().__init__()
        self.size_hint = [0.9, 0.3]