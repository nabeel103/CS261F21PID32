import pandas as pd

class vehicleBite:
        
        def load(self):
                df = pd.read_csv("Scrap.csv",encoding = 'utf8')
                return df
        




