from dependency_injector import containers, providers
from client.infrastructure.logging.logger_adapter import LoggerAdapter
from client.infrastructure.logging.logger_config_factory import create_logger_config
from client.infrastructure.settings.settings import Settings
from client.repositories.order_repository import OrderRepository
from client.services.order_service import OrderService
from client.services.payment_service_stub import PaymentServiceStub
from structured_logging.logger.logger import Logger
from structured_logging.logger_creation.logger_factory import create_logger


class Container(containers.DeclarativeContainer):
    config: Settings = providers.Configuration()
    external_logger: Logger = providers.Object(
        create_logger(create_logger_config(Settings())))
    logger = providers.Factory(
        LoggerAdapter,
        external_logger = external_logger
    )
    payment_service = providers.Factory(
        PaymentServiceStub,
        should_succeed = config.should_payment_succeed,
        logger = logger
    )
    order_repository = providers.Factory(
        OrderRepository,
        file_name = config.order_file_path
    )
    order_service = providers.Factory(
        OrderService,
        payment_service = payment_service,
        order_repository = order_repository,
        logger = logger
    )
