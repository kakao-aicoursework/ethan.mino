import fileUtils
from gpt.view.GptChatView import GptChatView
from gpt.model.LangChainModel import LangChainModel
from gpt.model.QueryModel import QueryModel

if __name__ == "__main__":
    config = fileUtils.load_json_file("./config.json")
    knowledge_base_path = "./data/카카오싱크.txt"

    system_prompt = f"""
    {fileUtils.file_to_str(knowledge_base_path)} 
    너는 위 내용을 기반으로 카카오 싱크에 대해 안내해주는 챗봇이야. 
    """

    lang_chain_model = LangChainModel(
        open_ai_key = config["open-ai-key"],
        temperature = 0.7,
        model_name = "gpt-3.5-turbo",
        system_prompt = system_prompt,
    )

    queryModel = QueryModel(lang_chain_model)
    GptChatView(title="GPT AI", queryModel=queryModel)
