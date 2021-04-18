import threading
import logging
import json

from kafka import KafkaConsumer


class KafkaListener():
    def __init__(self, topic, group_id, advertised_listeners, message_handler):
        self.consumer = KafkaConsumer(
            topic,
            group_id=group_id,
            bootstrap_servers=advertised_listeners
        )

        self.message_handler = message_handler

        logging.info('initializing kafka listener')

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def is_connected(self):
        return self.consumer.bootstrap_connected()

    def run(self):
        for msg in self.consumer:
            try:
                json_message = json.loads(msg.value)

                self.message_handler(
                    url=json_message['url'],
                    html_element_id=json_message['html_element_id'],
                    filename=json_message['output_file']
                )

            except Exception:
                logging.error('cannot parse message')
