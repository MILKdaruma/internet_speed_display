#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Teruma Yamamoto <TRyamamototeruma@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import speedtest


class InternetSpeedNode(Node):
    def __init__(self):
        super().__init__('internet_speed_node')
        self.publisher_ = self.create_publisher(String, 'internet_speed', 10)
        self.timer = self.create_timer(10.0, self.publish_speed)
        self.get_logger().info('Internet Speed Node has started.')

    def publish_speed(self):
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            download_speed = st.download() / 1e6
            upload_speed = st.upload() / 1e6
            speed_info = f"Download Speed: {download_speed:.2f} Mbps, Upload Speed: {upload_speed:.2f} Mbps"
        except Exception as e:
            speed_info = f"Failed to get speed: {e}"

        msg = String()
        msg.data = speed_info
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {speed_info}')


def main(args=None):
    rclpy.init(args=args)
    node = InternetSpeedNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

