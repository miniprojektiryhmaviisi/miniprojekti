from time import sleep
from sqlite3 import IntegrityError
import os




class References:
    def __init__(self, io_handler, service):
        self.io_handler = io_handler
        self.service = service
        self.welcome(io_handler, service)




    def welcome(self, io_handler, service):
        io_handler.write("\033[38;5;18;48;5;189;2mWelcome to MyReferences!")
        # sleep(1)
        io_handler.write("Type 0 to Add a reference")
        # sleep(1)
        io_handler.write("Type 1 to View my references")
        # sleep(1)
        io_handler.write("Type 2 to Search")
        # sleep(1)
        io_handler.write(
            "Type 3 to Make your existing references into bibtex form")
        # sleep(1)
        io_handler.write("Type 4 to Delete all references")
        # sleep(1)
        io_handler.write("Type 5 to Exit")
        # sleep(1)
        io_handler.write("*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*")
        command = io_handler.read("What do you want to do? ")
        if command == "0":
            self.add(io_handler, service)
            self.welcome(io_handler, service)
        elif command == "1":
            self.view_references(io_handler, service)
        elif command == "2":
            self.reference_search()
            self.welcome(io_handler, service)
        elif command == "3":
            self.export_bibtex_file(io_handler, service)
        elif command == "4":
            action = io_handler.read("Confirm action by typing delete: ")
            if action == "delete":
                self.reset_all()
                io_handler.write("All references deleted!")
                io_handler.write("*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*")
            self.welcome(io_handler, service)
        elif command == "5":
            io_handler.write("Exiting...\033[0m")
            sleep(1)
            return
        else:
            io_handler.write(
                "\033[91mInvalid input\033[38;5;18;48;5;189;2m. Please enter '0', '1', '2', '3', '4' or '5'.")
            sleep(2)
            self.welcome(io_handler, service)

    def add(self, io_handler, service):
        # sleep(1)
        io_handler.write(
            "What type of reference? \n"
            "1. For the pages field, please use '--' as a separator, e.g., 2--7.\n"
            "2. For the month field, please enter an integer between 1-12"
        )
        # sleep(1)
        io_handler.write("Type A to Add a book")
        # sleep(1)
        io_handler.write("Type B to Add an article")
        # sleep(1)
        io_handler.write("Type C to Add inproceedings")
        # sleep(1)
        io_handler.write("Type Q to Return")
        # sleep(1)
        while True:
            command = io_handler.read("Input: ")
            if command in ["A", "B", "C"]:
                self.form(service, command)
                break
            if command == "Q":
                break
            io_handler.write("Invalid input.")

    def ask_for_input(self, prompt, optional=False, input_type=str):
        while True:
            prefix = "(Optional) " if optional else ""
            user_input = self.io_handler.read(prefix + prompt + ": ")
            if not user_input and not optional:
                self.io_handler.write(
                    "Field cannot be empty. Please provide a valid input.")
            elif user_input and input_type:
                try:
                    return {prompt: input_type(user_input)}
                except ValueError:
                    self.io_handler.write("Please enter a valid interger.")
            else:

                return {prompt: user_input}

    def ask_for_multiple_inputs(self, prompt):
        items = []
        first_item = self.ask_for_input(prompt)[prompt]
        items.append(first_item)

        while True:
            more_items = self.io_handler.read(
                f"Next {prompt}? Press enter to skip ")
            if more_items:
                items.append(more_items)
            else:
                break

        return {prompt: items}

    @staticmethod
    def get_form_data(ref_type):
        if ref_type == "A":
            form = {
                "mandatory": [("key", str, False), ("title", str, False),
                              ("author", str, True), ("publisher", str, False),
                              ("year", int, False)],
                "optional": [("volume", int, False), ("number", int, False),
                             ("pages", str, False), ("month", int, False),
                             ("notes", str, False)]
            }

        elif ref_type == "B":
            form = {
                "mandatory": [("key", str, False), ("title", str, False),
                              ("author", str, True), ("journal", str, False),
                              ("year", int, False)],
                "optional": [("volume", int, False), ("number", int, False),
                             ("pages", str, False), ("month", int, False),
                             ("notes", str, False)]
            }

        elif ref_type == "C":
            form = {
                "mandatory": [("key", str, False), ("title", str, False),
                              ("booktitle", str, False),
                              ("author", str, True),
                              ("year", int, False)],
                "optional": [("editor", str, False), ("volume", int, False),
                             ("number", int, False),
                             ("series", str, False), ("pages", str, False),
                             ("address", str, False),
                             ("month", int, False),
                             ("organization", str, False), ("publisher", str, False),
                             ("notes", str, False)]
            }
        else:
            raise NotImplementedError

        return form

    def form(self, service, ref_type):

        form = self.get_form_data(ref_type)

        ref_items = {}
        for item in form["mandatory"]:
            if item[2]:
                user_input = self.ask_for_multiple_inputs(item[0])
            else:
                user_input = self.ask_for_input(item[0], False, item[1])
            ref_items.update(user_input)

        for item in form["optional"]:
            if item[2]:
                user_input = self.ask_for_multiple_inputs(item[0])
            else:
                user_input = self.ask_for_input(item[0], True, item[1])
            ref_items.update(user_input)

        try:
            if ref_type == "A":
                service.config_book_reference(**ref_items)
            elif ref_type == "B":
                service.config_article_reference(**ref_items)
            elif ref_type == "C":
                service.config_inpro_reference(**ref_items)
            else:
                raise NotImplementedError
        except IntegrityError as e:
            self.io_handler.write(f"Failed to save new reference: {e}")
            sleep(2)
        else:
            self.io_handler.write("New reference added!")
            sleep(2)

    def view_references(self, io_handler, service):
        books = self.service.get_all_books()
        articles = self.service.get_all_articles()
        inproceedings = self.service.get_all_inproceedings()
        if not any([books, articles, inproceedings]):
            self.io_handler.write("No references")
        else:
            if books:
                self.display_book_references(books)
            if articles:
                self.display_article_references(articles)
            if inproceedings:
                self.display_inproceedings_references(inproceedings)
        sleep(2)
        self.welcome(io_handler, service)

    def get_month_name(self, month_number):
        month_names = ["", "Jan", "Feb", "Mar", "Apr", "May",
                       "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        try:
            return month_names[int(month_number)]
        except (ValueError, IndexError):
            return ""

    def export_bibtex_file(self, io_handler, service):
        with open("file.bib", "w", encoding="utf-8") as file:
            all_book_refs = self.service.get_all_books()
            for i in all_book_refs:
                file.write("@book{" + i[0] + ",\n")
                file.write("   author = {" + i[1] + "},\n")
                file.write("   title = {" + i[2] + "},\n")
                file.write("   year = {" + str(i[4]) + "},\n")
                file.write("   publisher = {" + i[3] + "},\n")
                if i[5] != "":
                    file.write("   volume = {" + str(i[5]) + "},\n")
                if i[6] != "":
                    file.write("   number = {" + str(i[6]) + "},\n")
                if i[7] != "":
                    file.write("   pages = {" + i[7] + "},\n")
                if i[8] != "":
                    month_name = self.get_month_name(i[8])
                    file.write("   month = {" + month_name + "},\n")
                if i[9] != "":
                    file.write("   note = {" + i[9] + "},\n")
                file.write("}\n\n")

            all_article_refs = self.service.get_all_articles()
            for j in all_article_refs:
                file.write("@article{" + j[0] + ",\n")
                file.write("   author = {" + j[1] + "},\n")
                file.write("   title = {{" + j[2] + "}},\n")
                file.write("   year = {" + str(j[4]) + "},\n")
                file.write("   journal = {" + j[3] + "},\n")
                if j[5] != "":
                    file.write("   volume = {" + str(j[5]) + "},\n")
                if j[6] != "":
                    file.write("   number = {" + str(j[6]) + "},\n")
                if j[7] != "":
                    file.write("   pages = {" + j[7] + "},\n")
                if j[8] != "":
                    month_name = self.get_month_name(j[8])
                    # print(month_name)
                    file.write("   month = {" + month_name + "},\n")
                if j[9] != "":
                    file.write("   note = {" + j[9] + "},\n")
                file.write("}\n\n")

            all_inproceeding_refs = self.service.get_all_inproceedings()
            for j in all_inproceeding_refs:
                file.write("@inproceedings{" + j[0] + ",\n")
                file.write("   author = {" + j[1] + "},\n")
                file.write("   title = {{" + j[2] + "}},\n")
                file.write("   booktitle = {" + j[3] + "},\n")
                file.write("   year = {" + str(j[4]) + "},\n")
                if j[5] != "":
                    file.write("   editor = {" + j[5] + "},\n")
                if j[6] != "":
                    file.write("   volume = {" + str(j[6]) + "},\n")
                if j[7] != "":
                    file.write("   number = {" + str(j[7]) + "},\n")
                if j[8] != "":
                    file.write("   series = {" + str(j[8]) + "},\n")
                if j[9] != "":
                    file.write("   pages = {" + j[9] + "},\n")
                if j[10] != "":
                    file.write("   address = {" + j[10] + "},\n")
                if j[11] != "":
                    month_name = self.get_month_name(j[11])
                    # print(month_name)
                    file.write("   month = {" + month_name + "},\n")
                if j[12] != "":
                    file.write("   organization = {" + j[12] + "},\n")
                if j[13] != "":
                    file.write("   publisher = {" + j[13] + "},\n")
                if j[14] != "":
                    file.write("   note = {" + j[14] + "},\n")
                file.write("}\n\n")
        sleep(2)
        #print("BibTeX file created successfully: file.bib")
        #print("You can access the file via this link: file://" +
        #      os.path.abspath("file.bib"))
        self.io_handler.write("BibTeX file created successfully: file.bib")
        self.io_handler.write("You can access the file via this link: file://" +
              os.path.abspath("file.bib"))

        # sleep(5)
        self.welcome(io_handler, service)

    def display_book_references(self, references):
        io_handler = self.io_handler
        io_handler.write("")
        io_handler.write("*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*")
        io_handler.write("Book references")
        io_handler.write("*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*\n")
        for entry in references:
            io_handler.write("Cite Key     : " + entry[0])
            io_handler.write("Author       : " + entry[1])
            io_handler.write("Title        : " + entry[2])
            io_handler.write("Publisher    : " + entry[3])
            io_handler.write("Year         : " + str(entry[4]))
            if entry[5] != "":
                io_handler.write("Volume       : " + str(entry[5]))
            if entry[6] != "":
                io_handler.write("Number       : " + str(entry[6]))
            if entry[7] != "":
                io_handler.write("Pages        : " + entry[7])
            if entry[8] != "":
                io_handler.write("Month        : " + str(entry[8]))
            if entry[9] != "":
                io_handler.write("Notes        : " + entry[9])
            io_handler.write("")
            io_handler.write("*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*")

    def display_article_references(self, references):
        io_handler = self.io_handler
        io_handler.write("*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*")
        io_handler.write("Article references")
        io_handler.write("*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*\n")
        for entry in references:
            io_handler.write("Cite Key     : " + entry[0])
            io_handler.write("Author       : " + entry[1])
            io_handler.write("Title        : " + entry[2])
            io_handler.write("Journal      : " + entry[3])
            io_handler.write("Year         : " + str(entry[4]))
            if entry[5] != "":
                io_handler.write("Volume       : " + str(entry[5]))
            if entry[6] != "":
                io_handler.write("Number       : " + str(entry[6]))
            if entry[7] != "":
                io_handler.write("Pages        : " + entry[7])
            if entry[8] != "":
                io_handler.write("Month        : " + str(entry[8]))
            if entry[9] != "":
                io_handler.write("Notes        : " + entry[9])
            io_handler.write("")
            io_handler.write("*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*")

    def display_inproceedings_references(self, references):
        io_handler = self.io_handler
        io_handler.write("*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*")
        io_handler.write("Inproceedings references")
        io_handler.write("*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*\n")
        for entry in references:
            io_handler.write("Cite Key     : " + entry[0])
            io_handler.write("Author       : " + entry[1])
            io_handler.write("Title        : " + entry[2])
            io_handler.write("Book Title   : " + entry[3])
            io_handler.write("Year         : " + str(entry[4]))
            if entry[5] != "":
                io_handler.write("Editor       : " + entry[5])
            if entry[6] != "":
                io_handler.write("Volume       : " + str(entry[6]))
            if entry[7] != "":
                io_handler.write("Number       : " + str(entry[7]))
            if entry[8] != "":
                io_handler.write("Series       : " + str(entry[8]))
            if entry[9] != "":
                io_handler.write("Pages        : " + entry[9])
            if entry[10] != "":
                io_handler.write("Address      : " + entry[10])
            if entry[11] != "":
                io_handler.write("Month        : " + str(entry[11]))
            if entry[12] != "":
                io_handler.write("Organization : " + entry[12])
            if entry[13] != "":
                io_handler.write("Publisher    : " + entry[13])
            if entry[14] != "":
                io_handler.write("Note         : " + entry[14])
            io_handler.write("")
            io_handler.write("*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*")

    def reference_search(self):
        self.io_handler.write("Type author's name, title or both")
        author = self.ask_for_input("Author", optional=True)["Author"]
        if not author:
            title = self.ask_for_input("Title", optional=False)["Title"]
        else:
            title = self.ask_for_input("Title", optional=True)["Title"]

        reference_dict = self.service.search_reference(author, title)

        book_refs = reference_dict["book"]
        article_refs = reference_dict["article"]
        inpro_refs = reference_dict["inproceedings"]

        if len(book_refs) == 0 and len(article_refs) == 0 and len(inpro_refs) == 0:
            self.io_handler.write("")
            self.io_handler.write("No references found!")
            self.io_handler.write("")
            return

        self.io_handler.write(f"\nWith author <{author}> and title <{title}> found "
                              f"{len(book_refs)} book references,\n {len(article_refs)} "
                              f"article references and {len(inpro_refs)} inproceedings "
                              f"references")
        if len(book_refs) != 0:
            self.display_book_references(book_refs)
        if len(article_refs) != 0:
            self.display_article_references(article_refs)
        if len(inpro_refs) != 0:
            self.display_inproceedings_references(inpro_refs)

    def reset_all(self):
        self.service.delete_all()
