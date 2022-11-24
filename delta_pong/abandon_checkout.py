from time import sleep

from delta_pong.game_mechanics import PongEnv, play_pong, robot_choose_move

game = PongEnv(robot_choose_move)
observation, reward, done, info = game.reset()
n = 0
while not done:
    n += 1
    action = robot_choose_move(observation)
    observation, reward, done, info = game.step(action)

    # Don't visualise the game on every timestep - there are too many!
    if n % 2 == 0:
        print(game)
    sleep(0.05 / 10)
