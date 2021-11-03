import pandas as pd
class vehicle:

    def __init__(self):
        self.Title = None
        self.City= None
        self.Country= None
        self.Model=None
        self.MeterReading= None
        self.FuelType= None
        self.EngineCapacity = None
        self.AutoManuel= None
        self.Price= None
        self.Identity= None
        self.Contact= None

    def add(self,Title ,City,Country,Model,MeterReading,FuelType,EngineCapacity,AutoManuel,Price,Identity,Contact):
        
        self.Title = Title
        self.City= City
        self.Country= Country
        self.Model=Model
        self.MeterReading= MeterReading
        self.FuelType= FuelType
        self.EngineCapacity = EngineCapacity
        self.AutoManuel= AutoManuel
        self.Price= Price
        self.Identity= Identity
        self.Contact= Contact

    def load(self):
        df = pd.read_csv("Scrap.csv",encoding = 'utf8')
        # print(1)
        print(df.values.tolist())



v = vehicle()
v.loadData()