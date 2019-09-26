from bullet import Bullet 
from game_object import Game_Object

class Hero(Game_Object):
    def __init__(self, image, x_coordinate, y_coordinate):
        self.direction = 0
        self.speed = 10
        self.bullets_fired = []
        super().__init__(image, x_coordinate, y_coordinate)

    def has_collided_with_right_wall(self, right_wall_x_location):
        return self.xcor + self.width >= right_wall_x_location

    def has_collided_with_left_wall(self, left_wall_x_location):
        return self.xcor <= left_wall_x_location

    def shoot(self, bullet_image):
        new_bullet = Bullet(bullet_image, self.xcor + self.width / 2 - bullet_image.get_width() / 2, self.ycor)
        self.bullets_fired.append(new_bullet)

    def handle_wall_collision_with_bullets(self, top_wall):
        for bullet in self.bullets_fired:
            if bullet.has_collided_with_top_wall(top_wall):
                bullet.is_alive = False

        self.remove_dead_bullets()

    def remove_dead_bullets(self):
        for i in range(len(self.bullets_fired) -1, -1, -1):
            if self.bullets_fired[i].is_alive == False:
                self.bullets_fired.pop(i)

    def move_all_bullets(self):
        for bullet in self.bullets_fired:
            bullet.move()

    def show_all_bullets(self, game_display):
        for bullet in self.bullets_fired:
            bullet.show(game_display)

    def move(self, left_wall, right_wall):
        if self.direction == -1 and self.has_collided_with_left_wall(left_wall) == False:
            self.xcor += self.speed * self.direction
        elif self.direction == 1 and self.has_collided_with_right_wall(right_wall) == False:
            self.xcor += self.speed * self.direction

    def set_direction_right(self):
        self.direction = 1

    def set_direction_left(self):
        self.direction = -1

    def set_direction_none(self):
        self.direction = 0
