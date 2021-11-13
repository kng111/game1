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




class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.tile_map = None
        self.scene = None
        self.physics_engine = None

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
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 200
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
        if key == arcade.key.DOWN:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player_sprite.change_x = MOVEMENT_SPEED
        # Градусы
        elif key == arcade.key.LEFT:
            self.player_sprite.change_angle = ANGLE_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_angle = -ANGLE_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_x = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_angle = 0



 
    def on_draw(self):

        arcade.start_render()

        self.scene.draw()

    def on_update(self, delta_time):
        self.physics_engine.update()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()






