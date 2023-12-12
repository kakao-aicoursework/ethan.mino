import time
import logging
import requests

from src.model.LangChainModel import LangChainModel
from src.skill.request import ChatbotRequest
from src.util import fileUtils

logger = logging.getLogger("Callback")

config = fileUtils.load_json_file("config.json")
knowledge_base_path = "./data/카카오싱크.txt"

system_prompt = f"""
{fileUtils.file_to_str(knowledge_base_path)} 
너는 위 내용을 기반으로 카카오 싱크에 대해 안내해주는 챗봇이야. 
"""

lang_chain_model = LangChainModel(
    open_ai_key=config["open-ai-key"],
    temperature=0.7,
    model_name="src-3.5-turbo",
    system_prompt=system_prompt,
)


def callback_handler(request: ChatbotRequest):
    callback_url = request.userRequest.callbackUrl

    if callback_url is None:
        return
    response = lang_chain_model.query(request.userRequest.utterance)

    time.sleep(1.0)
    requests.post(
        url=callback_url,
        json={
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": response
                        }
                    }
                ]
            }
        }
    )
