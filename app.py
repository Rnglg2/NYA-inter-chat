import gradio as gr
import os
os.system("lmdeploy serve gradio './internlm2_5-20b-chat-NYA-R2' --chat-template='./chat_config.json'")