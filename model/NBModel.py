from sklearn.naive_bayes import GaussianNB
class brain:
    def __init__(self,X,y):
        self.X = X
        self.y = y
        self.model = GaussianNB()
    def train(self):
        self.model.fit(self.X,self.y)
    
    def test(self,X):
        X = X.reshape(1,X.shape[0])
        index = self.model.predict(X)[0]
        return index
       
        
