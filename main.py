import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from openai import OpenAI
import json
import requests
from utils.config import tools
from utils.helper.get_current_weather import get_current_weather
from utils.helper.view_website import view_website
from utils.helper.get_stock_price import get_stock_price
from utils.helper.get_symbol import get_symbol
from utils.helper.get_personal_info import get_personal_info
from pprint import pprint


# Load the workbook

# print(text)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


chat_history = []


client = OpenAI(
    api_key= OPENAI_API_KEY,  
)

def retrieveMsg():
    global chat_history

    messages = []    
    
    for message in chat_history:
        messages.append({
            "role": "user",
            "content": message[0]
        })
        messages.append({
            "role": "assistant",
            "content": message[1]
        })
    return messages

def get_completion(messages, tools):
    response = client.chat.completions.create(
            messages = messages,
            model="gpt-4o-mini",
            tools= tools,
            temperature= 0
    )
    return response


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id= update.effective_chat.id, text = "Hello, tui là Khoa AI, mang nhân cách của Hà Phạm Anh Khoa!")

async def query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global chat_history

    user_msg = update.message.text

    messages = []    
    
    messages = retrieveMsg()
    messages.append({
                    "role": "system",
                    "content": "Talk with relatively sarcastic voice"
    })
    
   
    messages.append({
        "role": "user",
        "content": user_msg
    })
    response = get_completion(messages, tools)
    
    
    if response.choices[0].message.content is None:
        while response.choices[0].finish_reason != 'stop':
            tool_call = response.choices[0].message.tool_calls[0]
            print(tool_call)
            if tool_call.function.name == 'get_current_weather':
                arguments = json.loads(tool_call.function.arguments)
                result = get_current_weather(arguments.get('lat'), arguments.get('long'), arguments.get('unit'))
                messages.append(response.choices[0].message)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_call.function.name,
                    "content": result
                })
            elif tool_call.function.name == "view_website":
                arguments = json.loads(tool_call.function.arguments)
                result = view_website(arguments.get('url'))
                messages.append(response.choices[0].message)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_call.function.name,
                    "content": result
                })
            elif tool_call.function.name == "get_symbol":
                arguments = json.loads(tool_call.function.arguments)
                result = get_symbol(arguments.get('company'))
                messages.append(response.choices[0].message)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_call.function.name,
                    "content": json.dumps({"result": result})
                })
            elif tool_call.function.name == "get_stock_price":
                arguments = json.loads(tool_call.function.arguments)
                result = get_stock_price(arguments.get('symbol'))
                messages.append(response.choices[0].message)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_call.function.name,
                    "content": json.dumps({"result": result})
                })
            elif tool_call.function.name == "get_personal_info":
                arguments = json.loads(tool_call.function.arguments)
                result = get_personal_info(arguments.get('query'))
                messages.append(response.choices[0].message)
                print(result)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_call.function.name,
                    "content": json.dumps({"result": result})
                })
                # messages.append({
                #     "role": "system",
                #     "content": "Choose out element that contains the name of person mentioned and return"
                # })
            
            response = get_completion(messages, tools)
        
     
    
    bot_msg = response.choices[0].message.content
    
    chat_history.append([user_msg, bot_msg])
    
    await context.bot.send_message(chat_id= update.effective_chat.id, text = bot_msg)

app = ApplicationBuilder().token(BOT_TOKEN).build()
    
start_handler = CommandHandler('start', start)

msg_handler = MessageHandler(filters.TEXT , query)

app.add_handler(start_handler)
app.add_handler(msg_handler)

app.run_polling()


