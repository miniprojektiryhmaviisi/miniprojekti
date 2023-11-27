from references import References


class ReferencesLibrary:
    def __init__(self):
        self._references = References()

    def ask_bookform(self):
        self._references.bookform()

    def ask_articleform(self):
        self._references.articleform()

    def ask_inproceedingsform(self):
        self._references.inproceedingsform()


