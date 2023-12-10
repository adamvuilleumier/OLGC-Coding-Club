# TODO: Make brick wall decrease score


"""
Complete game in Arcade

This game demonstrates some of the more advanced features of
Arcade, including:
- Using sprites to render complex graphics
- Handling user input
- Sound output
"""

from params import ASSETS_PATH
from helpers import get_random_sound
import time

# Import arcade allows the program to run in Python IDLE
import arcade

# To randomize coin placement
from random import randint

# To locate your assets
from pathlib import Path

# Set the width and height of your game window, in pixels
WIDTH = 1000
HEIGHT = 800

# Set the game window title
TITLE = "Pokemons Rule"

# Location of your assets


# How many coins must be on the screen before the game is over?
COIN_COUNT = 3

# How much is each coin worth?
COIN_VALUE = 2

# Classes
class ArcadeGame(arcade.Window):
    """The Arcade Game class"""

    def __init__(self, width: float, height: float, title: str):
        """Create the main game window

        Arguments:
            width {float} -- Width of the game window
            height {float} -- Height of the game window
            title {str} -- Title for the game window
        """

        # Call the super class init method
        super().__init__(width, height, title)

        # Set up a timer to create new coins
        self.coin_countdown = 3
        self.coin_interval = 0.1

        # Score is initially zero
        self.counter = 0
        self.score = 1

        # Set up empty sprite lists
        self.coins = arcade.SpriteList()
        self.obstacles = arcade.SpriteList()

        self.health= 1

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

    def setup(self):
        """Get the game ready to play"""

        # Set the background color
        arcade.set_background_color(color=arcade.color.DEEP_SKY_BLUE)

        # Set up the player
        sprite_image = f"{ASSETS_PATH}/images/013.png"
        shrek_image = f"{ASSETS_PATH}/images/shrek.png"

        self.player = arcade.Sprite(
            filename=sprite_image, center_x=WIDTH // 2, center_y=HEIGHT // 2, scale=0.5
        )

        self.shrek = arcade.Sprite(
            filename=shrek_image, center_x=WIDTH // 2, center_y=HEIGHT // 2, scale=0.1
        )

        # Spawn a new coin
        arcade.schedule(
            function_pointer=self.add_coins_and_obstacles, interval=self.coin_countdown
        )

        self.coin_pickup_sound = arcade.load_sound(get_random_sound())
        self.hit_sound = arcade.load_sound(get_random_sound())



    def add_coins_and_obstacles(self, dt: float):
        """Add a new coin to the screen, reschedule the timer if necessary

        Arguments:
            dt {float} -- Time since last call (unused)
        """

        # Create a new coin
        coin_image = f"{ASSETS_PATH}/images/coin.png"
        new_coin = arcade.Sprite(
            filename=coin_image,
            center_x=randint(20, WIDTH - 20),
            center_y=randint(20, HEIGHT - 20),
            scale=0.03
        )
        # Add the coin to the current list of coins
        self.coins.append(new_coin)

        # Create a new obstacle
        rand = randint(0,2)
        if int(rand) == 1: 
            obstacle_image = f"{ASSETS_PATH}/images/brick.jpg"
            new_obstacle = arcade.Sprite(
                filename=obstacle_image,
                center_x=randint(20, WIDTH - 20),
                center_y=randint(20, HEIGHT - 20),
                scale=0.3
            )
            self.obstacles.append(new_obstacle)


        # Decrease the time between coin appearances, but only if there are
        # fewer than three coins on the screen.
        if len(self.coins) < 3:
            self.coin_countdown -= self.coin_interval

            # Make sure you don't go too quickly
            if self.coin_countdown < 0.1:
                self.coin_countdown = 0.1

            # Stop the previously scheduled call
            arcade.unschedule(function_pointer=self.add_coins_and_obstacles)

            # Schedule the next coin addition
            arcade.schedule(
                function_pointer=self.add_coins_and_obstacles, interval=self.coin_countdown
            )

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """Processed when the mouse moves

        Arguments:
            x {float} -- X Position of the mouse
            y {float} -- Y Position of the mouse
            dx {float} -- Change in x position since last move
            dy {float} -- Change in y position since last move
        """
        # Ensure the player doesn't move off-screen
        self.player.center_x = arcade.clamp(x, 0, WIDTH)
        self.player.center_y = arcade.clamp(y, 0, HEIGHT)

    def on_update(self, delta_time: float):
        """Update all the game objects

        Arguments:
            delta_time {float} -- How many seconds since the last frame?
        """
        
        # increment counter
        if self.counter == 200:
            self.counter = 0
            self.score -= 1

        self.counter = self.counter + 1

        # Check if you've picked up a coin
        coins_hit = arcade.check_for_collision_with_list(
            sprite=self.player, sprite_list=self.coins
        )

        # Check if you've hit an obstacle
        obstacle_hit = arcade.check_for_collision_with_list(
            sprite=self.player, sprite_list=self.obstacles
        )

        for coin in coins_hit:
            # Add the coin score to your score
            self.score += COIN_VALUE

            # Play the coin sound
            arcade.play_sound(self.coin_pickup_sound)

            # Remove the coin
            coin.remove_from_sprite_lists()


        if len(obstacle_hit) > 0:
             # Decrease health.
            arcade.play_sound(self.hit_sound)
            self.health-=3

        

    def on_draw(self):
        """Draw everything"""

        # Start the rendering pass
        arcade.start_render()

        # Draw the coins
        self.coins.draw()

        # Draw the player
        self.player.draw()

        # Draw the score in the lower-left corner
        arcade.draw_text(
            text=f"Score: {self.score}",
            start_x=50,
            start_y=50,
            font_size=32,
            color=arcade.color.BLACK,
        )

        self.obstacles.draw()

        if self.health <=0:
        
            arcade.draw_text(
                text=f"GAME OVER",
                start_x=50,
                start_y=50,
                font_size=64,
                color=arcade.color.RED,
            )
            self.shrek.draw()
            time.sleep(3)
            exit()

if __name__ == "__main__":
    arcade_game = ArcadeGame(WIDTH, HEIGHT, TITLE)
    arcade_game.setup()
    arcade.run()