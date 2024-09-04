import gradio as gr
import os
os.system("lmdeploy serve gradio 'Rnglg2/InternLM2.5_NYA-chat' --chat-template='./chat_config.json'")
