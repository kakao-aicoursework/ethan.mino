from openai import OpenAI
import fileUtils

class KnowledgeBaseGptModel:
    def __init__(self, ai_key, system_prompt, knowledge_base_path, model="gpt-3.5-turbo", temperature=0.1):
        self.knowledge_base = fileUtils.file_to_str(knowledge_base_path)
        self.model = model
        self.temperature = temperature
        self.system_prompt = {"role": "system", "content": system_prompt + "\n" + self.knowledge_base}
        self.client = OpenAI(api_key=ai_key)

    def query(self, message_log):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[self.system_prompt]+message_log,
            temperature=self.temperature
        )

        return response.choices[0].message.content