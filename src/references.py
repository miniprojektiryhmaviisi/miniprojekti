from time import sleep
from sqlite3 import IntegrityError
import os

class References:
    def __init__(self, io_handler, service):
        self.io_handler = io_handler
        self.service = service
        self.welcome()

    def welcome(self):
        io = self.io_handler
        io.write("\nWelcome to MyReferences!\n")
        io.write("Type 0 to \033[92mAdd a reference\033[0m")
        io.write("Type 1 to View my references")
        io.write("Type 2 to Search")
        io.write(
            "Type 3 to Make your existing references into bibtex form")
        io.write("Type 4 to \033[91mDelete all\033[0m references")
        io.write("Type 5 to \033[91mDelete\033[0m individual references")
        io.write("Type 9 to Exit\n")
        io.write("*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*")
        command = io.read("What do you want to do? \n")
        if command == "0":
            self.add()
            self.welcome()
        elif command == "1":
            self.view_references()
        elif command == "2":
            self.reference_search()
            self.welcome()
        elif command == "3":
            self.export_bibtex_file()
        elif command == "4":
            action = io.read("\033[4mConfirm action by typing delete: \033[0m")
            if action == "delete":
                self.reset_all()
                io.write("All references deleted!")
                io.write("*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*")
            self.welcome()
        elif command == "9":
            io.write("Exiting...\033[0m")
            return
        elif command == "5":
            self.delete_by_cite_key()
            self.welcome()
        else:
            io.write(
                "\033[91mInvalid input\033[0m. Please enter '0', '1', '2', '3', '4', '5' or '9'.")
            sleep(2)
            self.welcome()

    def add(self):
        io = self.io_handler
        io.write(
            "\nWhat type of reference? \n"
            "\n\033[4m1. For the pages field, please use '--' as a separator, e.g., 2--7.\n"
            "2. For the month field, please enter an integer between 1-12\033[0m\n"
        )
        io.write("Type A to Add a book")
        io.write("Type B to Add an article")
        io.write("Type C to Add inproceedings")
        io.write("Type Q to Return\n")
        while True:
            command = io.read("Input: ")
            if command in ["A", "B", "C"]:
                self.form(command)
                break
            if command == "Q":
                break
            io.write("Invalid input.")

    def ask_for_input(self, prompt, optional=False, input_type=str):
        io = self.io_handler
        while True:
            prefix = "(Optional) " if optional else ""
            user_input = io.read(prefix + prompt + ": ")
            if not user_input and not optional:
                io.write(
                    "Field cannot be empty. Please provide a valid input.")
            elif user_input and input_type:
                try:
                    return {prompt: input_type(user_input)}
                except ValueError:
                    io.write("Please enter a valid interger.")
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

    def form(self, ref_type):
        service = self.service
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
            self.io_handler.write(f"\033[91mFailed to save new reference: {e}\033[0m")
            sleep(2)
        else:
            self.io_handler.write("\033[92mNew reference added!\033[0m")
            sleep(2)

    def view_references(self):
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
        self.welcome()

    def get_month_name(self, month_number):
        month_names = ["", "Jan", "Feb", "Mar", "Apr", "May",
                       "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        try:
            return month_names[int(month_number)]
        except (ValueError, IndexError):
            return ""

    def export_bibtex_file(self):
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
                    file.write("   month = {" + month_name + "},\n")
                if j[12] != "":
                    file.write("   organization = {" + j[12] + "},\n")
                if j[13] != "":
                    file.write("   publisher = {" + j[13] + "},\n")
                if j[14] != "":
                    file.write("   note = {" + j[14] + "},\n")
                file.write("}\n\n")

        self.io_handler.write("BibTeX file created successfully: file.bib")
        self.io_handler.write("You can access the file via this link: file://" +
              os.path.abspath("file.bib"))
        self.welcome()

    def display_book_references(self, references):
        io = self.io_handler
        io.write("")
        io.write("\n*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*\n")
        io.write("Book references")
        io.write("\n*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*\n")
        for entry in references:
            io.write("Cite Key     : " + entry[0])
            io.write("Author       : " + entry[1])
            io.write("Title        : " + entry[2])
            io.write("Publisher    : " + entry[3])
            io.write("Year         : " + str(entry[4]))
            if entry[5] != "":
                io.write("Volume       : " + str(entry[5]))
            if entry[6] != "":
                io.write("Number       : " + str(entry[6]))
            if entry[7] != "":
                io.write("Pages        : " + entry[7])
            if entry[8] != "":
                io.write("Month        : " + str(entry[8]))
            if entry[9] != "":
                io.write("Notes        : " + entry[9])
            io.write("")

    def display_article_references(self, references):
        io = self.io_handler
        io.write("\n*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*\n")
        io.write("Article references")
        io.write("\n*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*\n")
        for entry in references:
            io.write("Cite Key     : " + entry[0])
            io.write("Author       : " + entry[1])
            io.write("Title        : " + entry[2])
            io.write("Journal      : " + entry[3])
            io.write("Year         : " + str(entry[4]))
            if entry[5] != "":
                io.write("Volume       : " + str(entry[5]))
            if entry[6] != "":
                io.write("Number       : " + str(entry[6]))
            if entry[7] != "":
                io.write("Pages        : " + entry[7])
            if entry[8] != "":
                io.write("Month        : " + str(entry[8]))
            if entry[9] != "":
                io.write("Notes        : " + entry[9])
            io.write("")


    def display_inproceedings_references(self, references):
        io = self.io_handler
        io.write("\n*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*\n")
        io.write("Inproceedings references")
        io.write("*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*\n")
        for entry in references:
            io.write("Cite Key     : " + entry[0])
            io.write("Author       : " + entry[1])
            io.write("Title        : " + entry[2])
            io.write("Book Title   : " + entry[3])
            io.write("Year         : " + str(entry[4]))
            if entry[5] != "":
                io.write("Editor       : " + entry[5])
            if entry[6] != "":
                io.write("Volume       : " + str(entry[6]))
            if entry[7] != "":
                io.write("Number       : " + str(entry[7]))
            if entry[8] != "":
                io.write("Series       : " + str(entry[8]))
            if entry[9] != "":
                io.write("Pages        : " + entry[9])
            if entry[10] != "":
                io.write("Address      : " + entry[10])
            if entry[11] != "":
                io.write("Month        : " + str(entry[11]))
            if entry[12] != "":
                io.write("Organization : " + entry[12])
            if entry[13] != "":
                io.write("Publisher    : " + entry[13])
            if entry[14] != "":
                io.write("Note         : " + entry[14])
            io.write("")
            io.write("\n*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*\n")

    def reference_search(self):
        io = self.io_handler
        io.write("Type author's name, title or both")
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
            io.write("")
            io.write("No references found!")
            io.write("")
            return

        io.write(f"\nWith author <{author}> and title <{title}> found "
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

    def delete_by_cite_key(self):
        io = self.io_handler
        list_of_keys = []
        io.write("Type the cite key(s) of the references you want to delete")
        io.write("You can find the cite keys by viewing the references from main menu")

        key = io.read("Cite key: ")
        list_of_keys.append(key)
        while True:
            next_key = io.read("Next Cite Key (empty stops and deletes): ")
            if next_key == "":
                io.write(self.service.delete_reference(list_of_keys))
                return
            list_of_keys.append(next_key)
