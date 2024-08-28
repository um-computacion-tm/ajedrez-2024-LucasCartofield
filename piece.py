class Piece:
    def __init__(self, color):
        self.__color__ = color
        
    def get_color(self):
        return self.__color__
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str
