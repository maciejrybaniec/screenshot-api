from health.routes import health_module

from containers import Container
import health.routes

from flask import Flask
import logging

logging.basicConfig(level=logging.INFO)


def create_app() -> Flask:
    container = Container()
    container.wire(modules=[health.routes])

    app = Flask(__name__)

    app.container = container
    app.config["DEBUG"] = True

    confiuration_service = container.confiuration_service()

    kafka_topic = confiuration_service.get('kafka_consumer_topic')

    container.kafka_listener(
        kafka_topic,
        confiuration_service.get('kafka_group_id'),
        confiuration_service.get('kafka_advertised_listeners')
    )

    app.register_blueprint(health_module)

    app.run()

    return app


create_app()
