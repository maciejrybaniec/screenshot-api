from flask import Blueprint, jsonify
from dependency_injector.wiring import inject, Provide

from kafka_listener import KafkaListener
from services import ConfigurationService
from containers import Container

health_module = Blueprint(
    "health",
    __name__,
    url_prefix="/"
)


@health_module.route("health_check", methods=['GET'])
@inject
def create_thumbnail(
    kafka_listener: KafkaListener = Provide[Container.kafka_listener],
    confiuration_service: ConfigurationService = Provide[
        Container.confiuration_service]
):
    return jsonify({
        "config_env": confiuration_service.get_env(),
        "listener_connected": kafka_listener.is_connected()
    })
