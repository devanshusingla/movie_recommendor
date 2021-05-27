class GoogleVerifier:
    def __init__(self):
        self.items = []

    def verify(self,item,response,spider):
        self.items += [item]
    
    def print(self):
        for item in self.items:
            print("Name: {}\nRelease Date: {}\n".format(item["name"], item["release_date"]))