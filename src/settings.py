import os

if "environment" in os.environ:
    env = os.environ["environment"]
else:
    env = "dev"

settings = {
    "kafka_protocol": {
        "dev": "PLAINTEXT",
    },

    "kafka_consumer_topic": {
        "dev": "dashboard",
    },

    "kafka_group_id": {
        "dev": "dashboard_thumbnails",
    },

    "kafka_advertised_listeners": {
        "dev": ["localhost:9094"],
    },
}
