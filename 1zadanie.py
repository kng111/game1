

import random
import arcade
import time
from arcade import key
import speech_recognition as sr
mic = sr.Microphone(device_index=1)

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "game"

MOVEMENT_SPEED = 5
x = ['ladybug.png','frog.png','mouse.png','fly.png' ,'slimeBlue.png']
x2 = (random.choice(x))

class Player(arcade.Sprite):


    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyGame(arcade.Window):


    def __init__(self, width, height, title):

        super().__init__(width, height, title)


        self.player_list = None
        self.player_sprite = None

        arcade.set_background_color(arcade.color.KHAKI)

    def setup(self):

        self.player_list = arcade.SpriteList()

        self.player_sprite = Player(f":resources:images/enemies/{x2}", SPRITE_SCALING)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 500
        self.player_list.append(self.player_sprite)

    def on_draw(self):


        arcade.start_render()

        self.player_list.draw()

    def on_update(self, delta_time):
        self.player_list.update()

    def voice():
            r = sr.Recognizer()
            with mic as source:
                print('Слушаю...')
                audio = r.listen(source)
                    
                    
                query = r.recognize_google(audio,language = 'ru-RU')
                print(f'вы сказали:{query.lower()}')
                f = open('txt.txt','w')
                f.write(query.lower())
                f.close()
                key = query.lower()
    


    def on_key_press(self, key, modifiers):
        # while True:
            r = sr.Recognizer()
            with mic as source:
                print('Слушаю...')
                audio = r.listen(source)
                    
                    
                query = r.recognize_google(audio,language = 'ru-RU')
                print(f'вы сказали:{query.lower()}')
                f = open('txt.txt','w')
                f.write(query.lower())
                f.close()
                key = query.lower()
                if key == 'вверх':
                    self.player_sprite.change_y = MOVEMENT_SPEED
                    self.player_sprite.change_x = 0

                elif key == 'вниз':
                    self.player_sprite.change_y = -MOVEMENT_SPEED
                    self.player_sprite.change_x = 0

                elif key == 'слева':
                    self.player_sprite.change_x = -MOVEMENT_SPEED
                    self.player_sprite.change_y = 0

                elif key == 'справа':
                    self.player_sprite.change_x = MOVEMENT_SPEED
                    self.player_sprite.change_y = 0
                elif key == 'стоп':
                    self.player_sprite.change_y = 0
                    self.player_sprite.change_x = 0
    def on_key_release(self, key, modifiers):
        if key == 'вверх' or key == 'вниз':
            self.player_sprite.change_y = 0
        elif key == 'слева' or key == 'справа':
            self.player_sprite.change_x = 0
        elif key == 'стоп':
            self.player_sprite.change_y = 0
            self.player_sprite.change_x = 0


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()






