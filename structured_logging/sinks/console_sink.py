import json
from structured_logging.sinks.I_sink import ISink

class ConsoleSink(ISink):
    def sink_data(self, data: dict):
        json_object = json.dumps(data)
        print(json_object)