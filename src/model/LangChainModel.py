import os

from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.schema import SystemMessage


class LangChainModel:
    def __init__(
        self,
        open_ai_key: str,
        temperature: float,
        model_name: str,
        system_prompt: str,
    ):
        self.llm = ChatOpenAI(
            open_ai_key=open_ai_key,
            temperature=0.8
        )
        self.temperature = temperature
        self.model_name = model_name
        self.system_prompt = SystemMessage(content=system_prompt)
        self.human_prompt = HumanMessagePromptTemplate.from_template("{text}")
        self.chat_prompt = ChatPromptTemplate.from_messages([self.system_prompt, self.human_prompt])
        self.llm_chain = LLMChain(llm=self.llm, prompt=self.chat_prompt)

    def query(self, message):
        return self.llm_chain.run(text = message)


class DataStoreConfig:
    def __init__(
            self,
            collection_name: str,
            init: bool,
            knowledge_base_path=None
    ):
        self.collection_name = collection_name
        self.init = init
        self.knowledge_base_path = knowledge_base_path
        if init and self.knowledge_base_path is None:
            raise ValueError("knowledge_base_path must be set when init is True")
