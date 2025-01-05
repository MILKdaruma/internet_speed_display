#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Teruma Yamamoto <TRyamamototeruma@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import speedtest

class InternetSpeedPublisher(Node):
    def __init__(self):
        super().__init__('internet_speed_publisher')
        self.publisher_ = self.create_publisher(String, 'internet_speed', 10)
        self.timer = self.create_timer(5.0, self.publish_speed)

    def publish_speed(self):
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            download_speed = st.download() / 1_000_000
            upload_speed = st.upload() / 1_000_000
            msg = String()
            msg.data = f"Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps"
            self.publisher_.publish(msg)
        except Exception:
            pass

def main(args=None):
    rclpy.init(args=args)
    node = InternetSpeedPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

