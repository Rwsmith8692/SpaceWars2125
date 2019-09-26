from game_object import Game_Object

class Enemy(Game_Object):
    def __init__(self, image, x_coordinate, y_coordinate):
        super().__init__(image, x_coordinate, y_coordinate)

    def has_collided_with_right_wall(self, right_wall_x_location):
        return self.xcor + self.width >= right_wall_x_location

    def has_collided_with_left_wall(self, left_wall_x_location):
        return self.xcor <= left_wall_x_location

    def move_over(self, amount_to_move):
        self.xcor += amount_to_move

    def move_down(self, amount_to_move):
        self.ycor += amount_to_move