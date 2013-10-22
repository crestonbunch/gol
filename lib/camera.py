class Camera:
    
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
    
    def focus(self, objects, zoom = 1):
        focused = {}
        for coord in objects.keys():
            obj = objects[coord]
            if self.in_view(coord, zoom):
                focused[coord] = obj
        return focused
                
    
    def in_view(self, point, zoom = 1):
        x = point[0]
        y = point[1]
        if x >= self.x and y >= self.y:
            if x < self.x+self.width*zoom and y < self.y+self.height*zoom:
                return True
        return False
        