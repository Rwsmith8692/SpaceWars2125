from enemy import Enemy

class Fleet():
    def __init__(self, row_count, column_count, initial_speed, enemy_img, starting_xcor, starting_ycor):
        self.direction = 1
        self.speed = initial_speed
        self.ships = self.get_initial_ships(row_count, column_count, enemy_img, starting_xcor, starting_ycor)

    def get_initial_ships(self, row_count, column_count, enemy_img, starting_xcor, starting_ycor):
        initial_ships = []
        for row in range(0, row_count):
            for col in range(0, column_count):
                current_xcor = starting_xcor + col * enemy_img.get_width()
                current_ycor = starting_ycor + row * enemy_img.get_height()
                initial_ships.append(Enemy(enemy_img, current_xcor, current_ycor))
        return initial_ships

    def show(self, game_display):
        for ship in self.ships:
            ship.show(game_display)

    def handle_wall_collision(self, left_wall, right_wall):
        for ship in self.ships:
            if ship.has_collided_with_left_wall(left_wall) or ship.has_collided_with_right_wall(right_wall):
                self.move_down()
                self.change_direction()
                break

    def move_down(self):
        for ship in self.ships:
            ship.move_down(10)

    def change_direction(self):
        self.direction *= -1

    def move_over(self):
        for ship in self.ships:
            ship.move_over(self.direction * self.speed)

    def remove_dead_ships(self):
        for i in range(len(self.ships) -1, -1, -1):
            if self.ships[i].is_alive == False:
                self.ships.pop(i)

