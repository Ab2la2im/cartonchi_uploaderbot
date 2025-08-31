from fastapi import FastAPI, Request
from aiogram import Dispatcher
from aiogram.types import Update
from bot import dp, bot
import handlers  # لود هندلرها
import os

app = FastAPI()

@app.post("/")
async def webhook_handler(request: Request):
    update = Update(**await request.json())
    await dp.process_update(update)
    return {"ok": True}

@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(os.getenv("WEBHOOK_URL"))

@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()