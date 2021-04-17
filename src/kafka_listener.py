import threading
import logging

from kafka import KafkaConsumer

from thumbnails.screenshot import capture_screenshot


class KafkaListener():
    def __init__(self, topic, group_id, advertised_listeners):
        self.consumer = KafkaConsumer(
            topic,
            group_id=group_id,
            bootstrap_servers=advertised_listeners
        )

        logging.info('initializing kafka listener')

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def is_connected(self):
        return self.consumer.bootstrap_connected()

    def run(self):
        for msg in self.consumer:
            print(msg.value)
            capture_screenshot(
                'https://www.lambdatest.com', "testing_form", "element.png")
