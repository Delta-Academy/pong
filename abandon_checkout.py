from time import sleep

from pynput import keyboard
from pynput.keyboard import Key

from delta_pong.game_mechanics import PongEnv, play_pong, robot_choose_move


class StoreKeyPress:
    def __init__(self):
        self.key_pressed = None

    def on_press(self, key):
        self.key_pressed = key

    def on_release(self, key):
        self.key_pressed = None


def human_player(*args, **kwargs) -> int:

    if store.key_pressed is None:
        return 0
    elif store.key_pressed == Key.up:
        return 1
    elif store.key_pressed == Key.down:
        return -1
    else:
        raise ValueError("Invalid key pressed")


store = StoreKeyPress()
listener = keyboard.Listener(on_press=store.on_press, on_release=store.on_release)
listener.start()

game = PongEnv(robot_choose_move, render=True)
observation, reward, done, info = game.reset()
n = 0
while not done:
    n += 1
    action = human_player(observation)
    observation, reward, done, info = game.step(action)
    print(game)
    sleep(0.05 / 10)
