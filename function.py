import pickle
import json
import numpy as np
import config

class ForestFire():
    def __init__(self,X,Y,month,FFMC,DMC,DC,ISI,temp,RH,wind,rain):
        print("****** INIT Function *********")
        self.X = X
        self.Y = Y
        self.month = month
        self.FFMC = FFMC
        self.DMC = DMC
        self.DC = DC
        self.ISI = ISI
        self.temp = temp
        self.RH = RH
        self.wind = wind
        self.rain = rain
    
    def __load_saved_data(self):

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_area(self):
        self.__load_saved_data()
        month = self.json_data['month'][self.month]
        array = np.zeros([1,self.model.n_features_in_])
        array[0,0] = self.X
        array[0,1] = self.Y
        array[0,2] = month
        array[0,3] = self.FFMC
        array[0,4] = self.DMC
        array[0,5] = self.DC
        array[0,6] = self.ISI
        array[0,7] = self.temp
        array[0,8] = self.RH
        array[0,9] = self.wind
        array[0,10] = self.rain
        predicted_area = np.around(self.model.predict(array)[0],3)
        return predicted_area