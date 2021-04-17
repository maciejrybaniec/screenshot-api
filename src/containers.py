from dependency_injector import containers, providers

from kafka_listener import KafkaListener
from services import ConfigurationService


class Container(containers.DeclarativeContainer):
    kafka_listener = providers.Singleton(
        KafkaListener
    )

    confiuration_service = providers.Singleton(
        ConfigurationService
    )
