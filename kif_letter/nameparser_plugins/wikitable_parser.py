'''
    Finds out the gender of all Names in a table on wikipedia.org
    @author: tbach, slau
'''


from ..nameparser import *
import stringhelper
import urllib2


class WikiTableParser(NameParser):

    WIKI_BASE = "https://de.wikipedia.org"
    WIKI_PAGE = WIKI_BASE + "/wiki/"

    def __init__(self, address, url):
        NameParser.__init__(self, address, url)
        start_table = "<table class=\"prettytable sortable\">"
        if self.pageContent.find(start_table) == -1:
            print("Did not find a table on the page found under '{}'").format(url)
        self.pageContent = stringhelper.get_part_between(self.pageContent, start_table, "</table>")
        self._make_name_list()

    def _make_name_list(self):
        ''' Parses all wiki links in table for MDB to get the gender'''
        all_tr = self.pageContent.split("<tr>")
        count_male = 0
        count_female = 0
        count_unknown = 0
        for tr in all_tr[1:]:
            td = stringhelper.get_part_between(tr, "<td>", "</td>")
            name_family = stringhelper.get_part_between_after(td, "\">", ",", "display:none")
            name = stringhelper.get_part_between(td, "display:none\">", ",")
            if "usgeschieden" in tr or "nahm sein Mandat nicht an" in tr \
                    or "verstorben" in tr:
                print "Skipped {}, {}...".format(name_family, name)
                continue
            if "span" in name_family:  # glockner...
                name_family = stringhelper.get_part_between_after(td, "\">", "!", "display:non")
            name_full = stringhelper.get_part_between_after(td, "\">", "</a>", "title")
            partei = stringhelper.get_part_between_n_occurrences(tr, "<td>", "</td>", 3)
            gender = ""

            link = self.WIKI_BASE + stringhelper.get_part_between(td, "a href=\"", "\"")
            wiki_person_content = urllib2.urlopen(link).read()
            if "/wiki/Kategorie:Mann" in wiki_person_content:
                count_male += 1
                gender = "male"
            elif "/wiki/Kategorie:Frau" in wiki_person_content:
                count_female += 1
                gender = "female"
            else:
                count_unknown += 1
            self._make_name(name, name_family, partei, gender)
        total = count_female + count_male
        print "sum: {} female: {} male: {} unknown: {}".format(total, count_female, count_male, count_unknown)

