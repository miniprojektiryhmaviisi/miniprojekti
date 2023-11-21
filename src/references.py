from time import sleep
# ainostaan book toimii. haluammeko kodakoodata bookform-metodin niin kuin on tehty alhaalla,
# eli mitkä fieldit on pakollisia jne (vai halutaanko me hakea tämä tieto jostain tiedostosta esim mitkä fieldit
# paikollisia dokumenttilähteille, mitkä kirjoille).


class References:
    def __init__(self,io,service):
        self.io=io
        self.service=service
        self.welcome(io,service)


    def welcome(self,io,service):
        io.write("Welcome to MyReferences!")
        sleep(1)
        io.write("Type in 0 or 1: ")
        sleep(1)
        io.write("0 for Add a reference")
        sleep(1)
        io.write("1 for View my references")
        sleep(1)
        command = io.read("What do you want to do? ")
        if command == "0":
            self.add(io,service)
        if command == "1":
            print("Not finished, directing you back to the start")
        else: 
            print("Invalid input. Please enter '0' or '1'.")
            sleep(2)
            self.welcome(io,service)

    def add(self, io, service):
        sleep(1)
        while True:
            reftype = io.read(
                "Is your source a book or an internet article? Type in book or article: ")
            if reftype.lower() == "book":
                self.bookform(service)
                #break
            elif reftype.lower() == "article":
                self.articleform(service)
                #break
            else:
                print("Invalid input. Please enter 'book' or 'article'.")

    def articleform(service):
        print("to be done")

    def ask_for_input(self, prompt, optional=False, input_type=str):
        while True:
            user_input = input(prompt)
            if user_input and not optional:
                try:
                    return input_type(user_input)
                except ValueError:
                    print(f"Please enter a valid integer.")
            elif not user_input and not optional:
                print(f"Field cannot be empty. Please provide a valid input.")
            elif optional:
                return user_input

# jos on optional ja int niin antaa mennä läpi vaikka ei olisi int.

    def bookform(self,service):
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
            "Optional: What is the month your book was published in? ", optional=True, input_type=int)
        book_note = self.ask_for_input(
            "Optional: Any notes? ", optional=True)
        book=service.config_reference(book_title,book_author,book_publisher,book_year,book_volume,book_number,book_pages, book_month,book_note)
        print(str(service.return_book()))
    def ask_for_multiple_inputs(self, prompt):
        authors = []
        first_author = self.ask_for_input(prompt)
        authors.append(first_author)

        while True:
            more_authors = input("Next author? Press enter to skip ")
            if more_authors:
                authors.append(more_authors)
            else:
                break
        return authors
