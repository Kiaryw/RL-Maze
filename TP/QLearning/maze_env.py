import numpy as np
import time
import sys

# 窗口界面库
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk

UNIT = 40  # 像素
MAZE_H = 4  # 网格高度
MAZE_W = 4  # 网格宽度


class Maze(tk.Tk, object):  # 新类继承父类tk.Tk
    def __init__(self):
        super(Maze, self).__init__()  # super类继承方法,初始化
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('maze')
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_H * UNIT))  # format格式化函数 geometry分辨率函数
        self._build_maze()

    # 迷宫布景
    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white',  # tk画图组件
                                height=MAZE_H * UNIT,
                                width=MAZE_W * UNIT)
        for c in range(0, MAZE_W * UNIT, UNIT):  # 网格
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        # 原点
        origin = np.array([20, 20])

        # hell 地狱
        hell1_center = origin + np.array([UNIT * 2, UNIT])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 15, hell1_center[1] - 15,  # [5, 5]
            hell1_center[0] + 15, hell1_center[1] + 15,  # [35, 35]
            fill='black')

        hell2_center = origin + np.array([UNIT, UNIT * 2])
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - 15, hell2_center[1] - 15,
            hell2_center[0] + 15, hell2_center[1] + 15,
            fill='black')

        # oval 宝藏
        oval_center = origin + UNIT * 2
        self.oval = self.canvas.create_oval(
            oval_center[0] - 15, oval_center[1] - 15,
            oval_center[0] + 15, oval_center[1] + 15,
            fill='yellow')

        # rect agent
        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red')

        self.canvas.pack()  # 打包
        # return(self.canvas)

    # agent复位
    def reset(self):
        self.update()
        time.sleep(0.5)
        self.canvas.delete(self.rect)
        origin = np.array([20, 20])
        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red'
        )
        return self.canvas.coords(self.rect)

    # 生成下一状态和奖惩机制策略
    def step(self, action):
        s = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])
        if action == 0:  # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:  # down
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:  # right
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:  # left
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect, base_action[0], base_action[1])

        s_ = self.canvas.coords(self.rect)

        # 奖惩判断
        if s_ == self.canvas.coords(self.oval):
            reward = 1
            done = True
            s_ = 'terminal'
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2)]:
            reward = -1
            done = True
            s_ = 'terminal'
        else:
            reward = 0
            done = False

        return s_, reward, done

    def render(self):
        time.sleep(0.1)
        self.update()


# --------------------------------------------------------
# 主函数：程序入口
"""
if __name__ == "__main__":
    env = Maze()
    env.after(100, update)
    env.mainloop()

"""
