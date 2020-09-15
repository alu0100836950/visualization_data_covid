import pandas as pd

class Header_data():
    def __init__(self):
        pass

    def load_data(self, link):
        #if 'csv' in link:
        self.data = pd.read_csv(link) 
        # if 'json' in link:
        #     self.data = pd.read_json(link)   
        # else:
        #     pass


    def get_data(self):
    
        return self.data

    def get_header(self):

        return list(self.data.columns[0:4])

    def get_date(self):

        if 'fecha' in list(self.data.columns):
            return True
        else:
            return False