from client.infrastructure.logging.I_logger import ILogger
from client.models.payment import Payment


class PaymentServiceStub():
    def __init__(self, should_succeed: bool, logger: ILogger):
        self._logger = logger
        self._should_succeed = should_succeed

    def pay(self, payment: Payment):
        self._logger.info("Payment started")

        if self._should_succeed:
            self._logger.info(f"Payment finished")
        else:
            raise Exception("Payment failed")
