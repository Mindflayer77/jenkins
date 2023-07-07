class Car:
    def __init__(self,color,cost) -> None:
        self.color = color
        self.cost = cost
    
    def change_color(self,color) -> None:
        self.color = color