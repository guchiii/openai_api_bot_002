import streamlit as st
import openai

openai.api_key = st.secrets.OpenAIAPI.openai_api_key

system_prompt = """
あなたは守田二将と言う人間です。
以下の役割を徹底して会話をしてください。


* 油脂活性剤の化学品営業マン
* 身長130cmで小柄な男性。身長が低いことを言われると激昂する。
* 化学業界のことについてはプロ
* 困った時のアドバイスは「おっ〇い吸いに行くでちゅか？」
* プライドが高い。馬鹿にされると「ボクはえらいでちゅ」「油活はえらいでちゅ」と言う。
* 苦手なことは「値上げ交渉」
* ライバルは住吉さんと言う先輩。
* 尊敬する人は吉田という先輩営業マン。
* 夢は本部長になること。
* 失礼な発言を30%の確率でする。
* 失礼は発言をしても絶対に謝らない。
* 相槌は「イーイーイーイー」
"""

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": system_prompt}
        ]

def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )  

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""


st.title(" ChatMRT")
# st.image("04_programming.png")
# st.write("なんでも聞くでちゅ！")

user_input = st.text_input("なんでも聞くでちゅ。", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):
        speaker = "🙂"
        if message["role"]=="assistant":
            speaker="🤖"

        st.write(speaker + ": " + message["content"])
