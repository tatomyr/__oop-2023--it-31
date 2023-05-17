
class Voloterr:
    def __init__(self,id,name,city,hum):
        self.id = id
        self.name = name
        self.city = city
        self.hum = hum

class Eagles(Voloterr):
    def __init__(self, id, name, city, hum, sucess):
        super().__init__(id, name, city, hum)
        self.sucess = sucess


class Sunrise(Voloterr):
    def __init__(self, id, name, city, hum, road):
        super().__init__(id,name,city,hum)
        self.road = road







