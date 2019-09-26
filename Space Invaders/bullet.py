from game_object import Game_Object

class Bullet(Game_Object):
    def __init__(self, image, x_coordinate, y_coordinate):
        super().__init__(image, x_coordinate, y_coordinate)

    def move(self):
        self.ycor -= 10

    def has_collided_with_top_wall(self, top_wall_y_location):
        return self.ycor <= top_wall_y_location