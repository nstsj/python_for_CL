def test_func():
    print("successfully imported")
    
class NLP(object):
    def __init__(self,text):
        self.text = text

    def preprocess(self):
        return self.text.lower().strip().split()