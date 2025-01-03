#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Teruma Yamamoto <TRyamamototeruma@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import speedtest


class InternetSpeedPublisher(Node):
    def __init__(self):
        super().__init__('internet_speed_publisher')
        self.publisher_ = self.create_publisher(Float64MultiArray, 'internet_speed_data', 10)
        self.timer = self.create_timer(5.0, self.publish_speed)
        self.get_logger().info('Internet Speed Publisher Node has started.')

    def publish_speed(self):
        try:

            st = speedtest.Speedtest()
            st.get_servers()
            best_server = st.get_best_server()

            download_speed = st.download() / 1e6
            upload_speed = st.upload() / 1e6
        except Exception as e:
            self.get_logger().error(f"Failed to measure speed: {e}")
            return

        msg = Float64MultiArray()
        msg.data = [download_speed, upload_speed]
        self.publisher_.publish(msg)

        self.get_logger().info(f"Published speeds: Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps")


def main(args=None):
    rclpy.init(args=args)
    node = InternetSpeedPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

