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

def callback_handler(request: ChatbotRequest) -> dict:

    # ===================== start =================================
    response = lang_chain_model.query(request.userRequest.utterance)

    print(response)
   # 참고링크 통해 payload 구조 확인 가능
    payload = {
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
    # ===================== end =================================
    # 참고링크1 : https://kakaobusiness.gitbook.io/main/tool/chatbot/skill_guide/ai_chatbot_callback_guide
    # 참고링크1 : https://kakaobusiness.gitbook.io/main/tool/chatbot/skill_guide/answer_json_format

    time.sleep(1.0)

    url = request.userRequest.callbackUrl

    if url:
        requests.post(url=url, json=payload)