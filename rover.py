class Rover:
    def __init__(self, x, y, max_x, max_y, direction):
        self.x = abs(int(x))
        self.y = abs(int(y))
        self.direction = direction
        self.max_x = abs(int(max_x))
        self.max_y = abs(int(max_y))

    def too_far(self):
        return f"failed - {self.x} {self.y} {self.direction}"

    def move(self):
        if self.direction == "N":
            if self.y == 0:
                return self.too_far()
            else:
                self.y = self.y - 1
                
        elif self.direction == "S":
            if self.y == self.max_y:
                return self.too_far()
            else:
                self.y = self.y + 1
                
        elif self.direction == "E":
            if self.x == self.max_x:
                return self.too_far()
            else:
                self.x = self.x + 1
                        
        elif self.direction == "W":
            if self.x == 0:
                return self.too_far()
            else:
                self.x = self.x - 1
        else:
            return f"invalid direction - {self.x} {self.y} {self.direction}"
        return f"success - {self.x} {self.y} {self.direction}"
    
    def rotate_left(self):
        if self.direction == "N":
            self.direction = "W"            
        elif self.direction == "W":
            self.direction = "S"
        elif self.direction == "S":
            self.direction == "E"
        elif self.direction == "E":
            self.direction = "N"
        else:
            return f"invalid direction - {self.x} {self.y} {self.direction}"
        return f"changed direction to {self.direction}"
    
    def rotate_right(self):
        if self.direction == "N":
            self.direction = "E"            
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction == "W"
        elif self.direction == "W":
            self.direction = "N"
        else:
            return f"invalid direction - {self.x} {self.y} {self.direction}"
        return f"changed direction to {self.direction}"
