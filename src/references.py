from time import sleep
# ainostaan book toimii. haluammeko kodakoodata bookform-metodin niin kuin on tehty alhaalla,
# eli mitkä fieldit on pakollisia jne
# (vai halutaanko me hakea tämä tieto jostain tiedostosta esim mitkä fieldit
# paikollisia dokumenttilähteille, mitkä kirjoille).

class References:
    def __init__(self, io_handler, service, storage_api):
        self.io_handler = io_handler
        self.service = service
        self.welcome(io_handler, service)
        self.storage_api = storage_api

    def welcome(self, io_handler, service):
        io_handler.write("Welcome to MyReferences!")
        sleep(1)
        io_handler.write("Type 0 for Add a reference")
        sleep(1)
        io_handler.write("Type 1 for View my references")
        sleep(1)
        io_handler.write("Type 2 to Exit")
        sleep(1)
        command = io_handler.read("What do you want to do? ")
        if command == "0":
            self.add(io_handler, service)
            self.welcome(io_handler, service)
        elif command == "1":
            io_handler.write("Not finished, directing you back to the start")
            sleep(2)
            self.welcome(io_handler, service)
        elif command == "2":
            io_handler.write("Exiting...")
            sleep(1)
            return
        else:
            io_handler.write("Invalid input. Please enter '0', '1' or '2'.")
            sleep(2)
            self.welcome(io_handler, service)

    def add(self, io_handler, service):
        sleep(1)
        while True:
            reftype = io_handler.read(
                "Is your source a book or an internet article? Type in book or article: ")
            if reftype.lower() == "book":
                self.bookform(service)
                break
            if reftype.lower() == "article":
                self.articleform(service)
                break
            io_handler.write("Invalid input. Please enter 'book' or 'article'.")

    # pylint: disable=fixme
    # FIXME: do something with the service
    # pylint: disable=unused-argument
    def articleform(self, service):
        print("Not finished, directing you back to the start")
        sleep(2)

    def ask_for_input(self, prompt, optional=False, input_type=str):
        while True:
            user_input = self.io_handler.read(prompt)
            if not user_input and not optional:
                self.io_handler.write(
                    "Field cannot be empty. Please provide a valid input.")
            elif user_input and input_type:
                try:
                    return input_type(user_input)
                except ValueError:
                    self.io_handler.write("Please enter a valid interger.")
            else:
                return user_input

    def bookform(self, service):
        book_key = self.ask_for_input(
            "What is the cite key in your paper? ")
        book_title = self.ask_for_input(
            "What is the title of your book? ")
        book_author = self.ask_for_multiple_inputs(
            "Who is the author/editor of your book? ")
        book_publisher = self.ask_for_input(
            "What is the publisher of your book? ")
        book_year = self.ask_for_input(
            "What is the publication year of your book? ", input_type=int)
        book_volume = self.ask_for_input(
            "Optional: What is the volume of your book? ", optional=True, input_type=int)
        book_number = self.ask_for_input(
            "Optional: What is the book number of your source? ", optional=True, input_type=int)
        book_pages = self.ask_for_input(
            "Optional: What are the pages of your book? ", optional=True)
        book_month = self.ask_for_input(
            "Optional: What month was your book published in? ", optional=True, input_type=int)
        book_note = self.ask_for_input(
            "Optional: Any notes? ", optional=True)
        print("Your entry has been saved: ")

        # pylint: disable=fixme
        # FIXME: do something with the book
        # pylint: disable=unused-variable
        book = service.config_reference(book_key, book_title, book_author, book_publisher, book_year,
            book_volume, book_number, book_pages, book_month, book_note)
        self.io_handler.write(str(service.return_book()))
        sleep(2)

    def ask_for_multiple_inputs(self, prompt):
        authors = []
        first_author = self.ask_for_input(prompt)
        authors.append(first_author)

        while True:
            more_authors = self.io_handler.read("Next author? Press enter to skip ")
            if more_authors:
                authors.append(more_authors)
            else:
                break
        return authors
