from pybtex.database import parse_file, BibliographyData, Person, Entry, OrderedCaseInsensitiveDict

def parse_and_check_bibfile(debug=False) -> None:
    bibfile = parse_file("file.bib")
    bibobj = BibliographyData(
        entries=OrderedCaseInsensitiveDict([
            ('TestKey', Entry('book',
                              fields=[
                                  ('title', 'Operating Systems'),
                                  ('year', '1991'),
                                  ('publisher', 'MacMillan'),
                                  ('volume', '682'),
                                  ('number', '1'),
                                  ('pages', '100-108'),
                                  ('month', 'Dec')],
                              persons=OrderedCaseInsensitiveDict([('author',
                                                                   [Person('Stallings')])])))]),
        preamble=[])
    if debug:
        print(bibfile)
    if not bibfile == bibobj:
        raise AssertionError("Bibtex file is not as expected")

if __name__ == "__main__":
    parse_and_check_bibfile(debug=True)
