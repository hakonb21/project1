import json
from structured_logging.sinks.I_sink import ISink

class FileSink(ISink):
    def __init__(self,filepath):
        self.filepath = filepath

    def sink_data(self, data: dict):
        json_object = json.dumps(data)
        with open(self.filepath, 'a') as f:
            f.write(json_object)
        
    