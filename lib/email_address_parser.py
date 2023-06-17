import re

class EmailAddressParser:
    email_list = None
    def __init__(self, email_list):
        if not email_list:
            self.email_list=[]
        self.email_list = email_list

    def parse(self):
        self.regex_stuff()
        print(self.email_list)
        return self.email_list
    

    def regex_stuff(self):
        pattern = r"[\w.]+@[\w]+\.[\w]+"
        # pattern = r"\s|\,"
        regex = re.compile(pattern)
        self.email_list = regex.findall(self.email_list)
        self.email_list = sorted(self.email_list)
