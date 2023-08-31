#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math as m
import numpy as np


class ObstacleDetection:
    def __init__(self):
        self.rang = None
        self.poin = None
        self.grph = None

        # Initialize ROS node and subscriber
        rospy.init_node('distance_check')
        sub = rospy.Subscriber('/scan', LaserScan, self.callback)

        # Create a figure and axis
        self.fig, self.ax = plt.subplots()

        # Set the background color to white
        self.ax.set_facecolor('white')

        # Set the plot limits and labels
        self.ax.set_xlim(-8, 8)
        self.ax.set_ylim(-8, 8)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title('OBSTACLE IS Red Dots')

        # Create the animation
        self.animation = animation.FuncAnimation(self.fig, self.update_plot, interval=50)

    def callback(self, data):
        self.rang = data.ranges
        an_inc = data.angle_increment
        print(an_inc)

        self.poin = [rang if 1 / rang != 0 else 0 for rang in self.rang]

        self.grph = np.zeros((1946, 2))
        for i in range(1946):
            self.grph[i][0] = self.poin[i] * m.sin(i * an_inc)
            self.grph[i][1] = self.poin[i] * m.cos(i * an_inc)

    def update_plot(self, frame):
        # Clear the previous plot
        self.ax.cla()

        # Set the background color to white
        self.ax.set_facecolor('white')

        # Set the plot limits and labels
        self.ax.set_xlim(-8, 8)
        self.ax.set_ylim(-8, 8)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title('OBSTACLE DETECTION')
        
        if self.grph is not None:
            self.ax.fill(*zip(*self.grph), facecolor='lightgreen', edgecolor='red', linewidth=1)
            self.ax.plot(0, 0, 'go', markersize=4)

          


    def run(self):
        # Display the plot
        plt.show()


if __name__ == "__main__":
    obstacle_detection = ObstacleDetection()
    obstacle_detection.run()
