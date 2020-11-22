from maze_env import Maze
from Qlearning import QLearningTable


def update():
    for episode in range(100):
        observation = env.reset()
        # print(str(observation))
        step_counter = 0
        while True:
            step_counter += 1
            env.render()

            action = RL.choose_action(str(observation))
            # print(str(observation))

            observation_, reward, done = env.step(action)

            RL.learn(str(observation), action, reward, str(observation_))

            observation = observation_

            if done:
                break
        print('Episode %s: total_steps = %s' % (episode, step_counter))
    print('game over')
    env.destroy()


# --------------------------------------------------
# 程序入口，main函数
if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()
