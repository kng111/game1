"""
Platformer Game
"""
import arcade
from pathlib import Path
import random

# Constants
SPRITE_SCALING = 0.5

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "game"

MOVEMENT_SPEED = 5

TILE_SCALING = 0.5
GRAVITY = 5
CHARACTER_SCALING = 0.5
ANGLE_SPEED = 3
x = ['1_vagoni.jpg']
# ,'2_vagoni.jpg','3_vagoni.jpg'
x2 = (random.choice(x))


class Wagon(arcade.Sprite):
    def __init__(self, image_name, scale, x, y):
        super().__init(image_name, scale)

        self.center_x = x
        self.center_y = y
        self.theta = 1

    def move(self):
        self.center_x += MOVEMENT_SPEED

    def rotate(self):
        self.turn_right(self.theta)


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.tile_map = None
        self.scene = None
        self.physics_engine = None
        self.is_moving = False
        arcade.set_background_color(arcade.csscolor.DARK_KHAKI)

    def setup(self):
        # 1. указание названия файла
        map_name = "jjj.json"

        # 2. в этом словаре храним информации о слоях на карте
        layer_options = {
            "ground": {
                "use_spatial_hash": True,
            },
        }

        # 3. Загружаем объект карты
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # 4. Спрайт для персонажа возьмем стандартный
        image_source = x2
        self.player_sprite = Wagon(image_source, CHARACTER_SCALING, 200, 200)
        self.scene.add_sprite("Player", self.player_sprite)

        # 5. Закрасим задний фон карты
        if self.tile_map.tiled_map.background_color:
            arcade.set_background_color(self.tile_map.tiled_map.background_color)

        # 6. Создаем 'physics engine', здесь (!!!) появляются объекты спрайтов слоя ground
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, self.scene.get_sprite_list("ground"), GRAVITY
        )

    def on_key_press(self, key, modifiers):
        # Вперёд назад
        if key == arcade.key.RIGHT:
            self.is_moving = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.is_moving = False

    def on_draw(self):
        arcade.start_render()
        self.scene.draw()

    def update(self):
        self.physics_engine.update()
        if self.is_moving:
            self.player_sprite.move()
            self.player_sprite.rotate()
        self.player_sprite.update()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
