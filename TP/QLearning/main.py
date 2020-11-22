"""
RL Maze example
Main part to control the update method of the
"""

from TP.QLearning.maze_env import Maze
from TP.QLearning.Qlearning import QLearningTable


def update():
    for episode in range(1000):
        print(episode)
        # initial observation
        observation = env.reset()
        # print (str(observation))
        step_counter = 0
        while True:
            step_counter += 1
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break
        print('Episode %s: total_steps = %s' % (episode, step_counter))
    # end of game
    print('game over')
    env.destroy()


if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update())
    env.mainloop()
