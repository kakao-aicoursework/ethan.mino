class QueryModel:
    def __init__(self, gpt_model):
        self.message_log = []
        self.gpt_model = gpt_model

    def query(self, message):
        self.message_log.append({"role": "user", "content": message})
        response = self.gpt_model.query(self.message_log)
        self.message_log.append({"role": "assistant", "content": response})
        return response