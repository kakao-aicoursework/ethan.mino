# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi import BackgroundTasks

from src.skill.callback import callback_handler
from src.skill.request import ChatbotRequest

app = FastAPI()


# callback.py 로 연결
@app.post("/callback")
async def skill(req: ChatbotRequest, background_tasks: BackgroundTasks):
    # 핸들러 호출 / background_tasks 변경가능
    background_tasks.add_task(callback_handler, req)
    out = {
        "version": "2.0",
        "useCallback": True,
        "data": {
            "text": "생각하고 있는 중이에요😘 \n15초 정도 소요될 거 같아요 기다려 주실래요?!"
        }
    }
    return out
