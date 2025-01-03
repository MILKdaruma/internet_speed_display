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
            # Speedtest インスタンス作成
            st = speedtest.Speedtest()
            st.get_servers()  # サーバーリストを取得
            best_server = st.get_best_server()  # 最適なサーバーを選択
            
            # インターネット速度を測定
            download_speed = st.download() / 1e6  # Mbps
            upload_speed = st.upload() / 1e6  # Mbps
        except Exception as e:
            self.get_logger().error(f"Failed to measure speed: {e}")
            return

        # トピックに速度情報をパブリッシュ
        msg = Float64MultiArray()
        msg.data = [download_speed, upload_speed]
        self.publisher_.publish(msg)

        # ログ出力
        self.get_logger().info(f"Published speeds: Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps")


def main(args=None):
    rclpy.init(args=args)
    node = InternetSpeedPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

