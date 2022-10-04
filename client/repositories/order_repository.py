from client.models.order import Order


class OrderRepository:
    def __init__(self, file_name):
        self.file_name = file_name

    def save(self, order: Order):
        with open(self.file_name, "a") as file:
            file.write(order.description + "\n")
            file.flush()
