import fileUtils
from gpt.view.GptChatView import GptChatView
from gpt.model.KnowledgeBaseGptModel import KnowledgeBaseGptModel
from gpt.model.QueryModel import QueryModel

if __name__ == "__main__":
    config = fileUtils.load_json_file("./config.json")

    knowledge_base_path = "./data/카카오톡채널.txt"
    knowledge_base_model = KnowledgeBaseGptModel(
        ai_key=config["open-ai-key"],
        system_prompt="you are a kakao channel guide chatbot.",
        knowledge_base_path=knowledge_base_path,
        model="gpt-3.5-turbo",
        temperature=0.7
    )

    queryModel = QueryModel(knowledge_base_model)
    GptChatView(title="GPT AI", queryModel=queryModel)
