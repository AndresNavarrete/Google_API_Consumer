import pandas as pd

class InputManager:
    
    def __init__(self):
        self.df = self.readExcel()
    
    def readExcel(self):
        df = pd.read_excel('data.xlsx')
        df = df.replace(np.nan, '', regex=True)
        return df