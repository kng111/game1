"""
Platformer Game
"""
import arcade
from pathlib import Path
import random
import pymunk
import arcade
import math

space = pymunk.Space()
space.gravity = 0, -1000

mass = 1
radius = 30
# Constants
SPRITE_SCALING = 0.5

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "game"

MOVEMENT_SPEED = 5

TILE_SCALING = 0.5
GRAVITY = 2
CHARACTER_SCALING = 0.5
ANGLE_SPEED = 1
x = ['1_vagoni.jpg']
# ,'2_vagoni.jpg','3_vagoni.jpg'
x2 = (random.choice(x))

class Player(arcade.Sprite):
    """ Player class """

    def __init__(self, image, scale):
        """ Set up the player """

        # Call the parent init
        super().__init__(image, scale)

        # Create a variable to hold our speed. 'angle' is created by the parent
        self.speed = 0

    def update(self):
        # Convert angle in degrees to radians.
        angle_rad = math.radians(self.angle)

        # Rotate the ship
        self.angle += self.change_angle

        # Use math to find our change based on our speed and angle
        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)



class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.tile_map = None
        self.scene = None
        self.physics_engine = None

        arcade.set_background_color(arcade.csscolor.DARK_KHAKI)
        self.sprites = arcade.SpriteList()

        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.LIGHT_KHAKI)

        self.sprites = arcade.SpriteList()

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
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = Player("1_vagoni.jpg",
                                    SPRITE_SCALING)
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.player_list.append(self.player_sprite)

        # 5. Закрасим задний фон карты
        if self.tile_map.tiled_map.background_color:
            arcade.set_background_color(self.tile_map.tiled_map.background_color)

        # 6. Создаем 'physics engine', здесь (!!!) появляются объекты спрайтов слоя ground
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, self.scene.get_sprite_list("ground"), GRAVITY
        )
        

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # Forward/back
        if key == arcade.key.W:
            self.player_sprite.change_x = MOVEMENT_SPEED

        elif key == arcade.key.S:
            self.player_sprite.change_x = -MOVEMENT_SPEED

        elif key == arcade.key.A:
            self.player_sprite.speed = MOVEMENT_SPEED
            self.player_sprite.change_angle = ANGLE_SPEED
        elif key == arcade.key.D:
            self.player_sprite.speed = -MOVEMENT_SPEED
            self.player_sprite.change_angle = -ANGLE_SPEED

        # Rotate left/right
        elif key == arcade.key.Q:
            self.player_sprite.speed = -MOVEMENT_SPEED
            self.player_sprite.change_angle = ANGLE_SPEED
        elif key == arcade.key.E:
            self.player_sprite.speed = MOVEMENT_SPEED
            self.player_sprite.change_angle = -ANGLE_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.speed = 0
            self.player_sprite.change_angle = 0
        elif key == arcade.key.Q or key == arcade.key.E:
            self.player_sprite.speed = 0
            self.player_sprite.change_angle = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_x = 0


 
    def on_draw(self):

        arcade.start_render()

        self.scene.draw()
        self.player_list.draw()

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.player_list.update()
        # space.step(delta_time)
        # for index, sprite in enumerate(self.sprites):
        #     sprite.angle = degrees(space.bodies[index].angle)
            # sprite.set_position(space.bodies[index].position.x, space.bodies[index].position.y)
            # for body in space.bodies:
            #     if body.position.y < -100:
            #         self.sprites.remove(sprite)
            #         space.remove(body, body.shapes)


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()


# import arcade
# import arcade
# import os
# import math

# from arcade.key import A, D

# SPRITE_SCALING = 0.5

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "rotate"

# MOVEMENT_SPEED = 5
# ANGLE_SPEED = 5


# class Wagon(arcade.Sprite):
#     def __init__(self):
#         super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

#         self.tile_map = None
#         self.scene = None
#         self.physics_engine = None

#         arcade.set_background_color(arcade.csscolor.DARK_KHAKI)
#         self.sprites = arcade.SpriteList()

#         self.set_location(400, 200)

#         arcade.set_background_color(arcade.color.LIGHT_KHAKI)

#         self.sprites = arcade.SpriteList()

#     def setup(self):
#         # 1. указание названия файла
#         map_name = "jjj.json"

#         # 2. в этом словаре храним информации о слоях на карте
#         layer_options = {
#             "ground": {
#                 "use_spatial_hash": True,
#             },
#         }

#         # 3. Загружаем объект карты
#         self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

#         self.scene = arcade.Scene.from_tilemap(self.tile_map)

#         # 4. Спрайт для персонажа возьмем стандартный
#         image_source = x2
#         self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
#         self.player_sprite.center_x = 200
#         self.player_sprite.center_y = 200
#         self.scene.add_sprite("Player", self.player_sprite)

#         # 5. Закрасим задний фон карты
#         if self.tile_map.tiled_map.background_color:
#             arcade.set_background_color(self.tile_map.tiled_map.background_color)

#         # 6. Создаем 'physics engine', здесь (!!!) появляются объекты спрайтов слоя ground
#         self.physics_engine = arcade.PhysicsEnginePlatformer(
#             self.player_sprite, self.scene.get_sprite_list("ground"), GRAVITY
#         )

#     def move(self,key):
#         if key == arcade.key.W:
#             self.player_sprite.change_x = MOVEMENT_SPEED
#         elif key == arcade.key.S:
#             self.player_sprite.change_x = -MOVEMENT_SPEED

#     #     # Градусы
#     #   elif key == arcade.key.LEFT:
#     #     #     self.player_sprite.change_angle = ANGLE_SPEED
#     #     # elif key == arcade.key.RIGHT:
#     #     #     self.player_sprite.change_angle = -ANGLE_SPEED

#     def on_key_release(self, key, modifiers):
#         if key == arcade.key.UP or key == arcade.key.DOWN:
#             self.player_sprite.change_x = 0
#         elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
#             self.player_sprite.change_angle = 0

#     def rotate(self,key, angle):
#         if key == arcade.key.A:
#             self.player_sprite.change_angle = ANGLE_SPEED
#         elif key == arcade.key.D:
#             self.player_sprite.change_angle = -ANGLE_SPEED

# #     def on_key_release(self, key, modifiers):
# #         if key == arcade.key.UP or key == arcade.key.DOWN:
# #             self.player_sprite.change_x = 0
# #         # elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
# #         #     self.player_sprite.change_angle = 0

#     def update(self):
#         angle_rad = math.radians(self.angle)

#         # Rotate the ship
#         self.angle += self.change_angle

#         # Use math to find our change based on our speed and angle
#         self.center_x += -self.speed * math.sin(angle_rad)
#         self.center_y += self.speed * math.cos(angle_rad)


# class Train(arcade.SpriteList):
#     def __init__(length):
#         super().__init__()
#         self.length = length
#         self.setup()
#         self.is_moving = False
#         ...

#     def setup():
#         for _ in range(self.length):
#             self.sprite_list.append(Wagon())

#     def on_key_press(self, key, modifiers):
#         if key == arcade.key.UP:
#             self.player_sprite.speed = MOVEMENT_SPEED
#             self.player_sprite.change_angle = ANGLE_SPEED
#         elif key == arcade.key.DOWN:
#             self.player_sprite.speed = -MOVEMENT_SPEED
#             self.player_sprite.change_angle = -ANGLE_SPEED

#         elif key == arcade.key.LEFT:
#             self.player_sprite.speed = -MOVEMENT_SPEED
#             self.player_sprite.change_angle = ANGLE_SPEED
#         elif key == arcade.key.RIGHT:
#             self.player_sprite.speed = MOVEMENT_SPEED
#             self.player_sprite.change_angle = -ANGLE_SPEED

#     def on_key_release(self, key, modifiers):

#         if key == arcade.key.UP or key == arcade.key.DOWN:
#             self.player_sprite.speed = 0
#             self.player_sprite.change_angle = 0
#         elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
#             self.player_sprite.speed = 0
#             self.player_sprite.change_angle = 0

#     # def on_key_release(self, key, modifies)
#     #      if key == arcade.key.LEFT:
#     #         self.is_moving = False

#     def update():
#         if self.is_moving:
#             ...
#         else:
#             ...