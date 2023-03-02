import keyboard
import time
import streamlit as st


setumei = '''
0.1秒以内に同じキーが2回以上押された場合チャタリングと表示されます。
'''
st.title('キーを押してください')    
st.code(setumei, language="注意点")
                      
key_dict = {}

while True:
    try:
        event = keyboard.read_event()
        if event.event_type == "down":
            key = event.name
            current_time = time.time()
            if key in key_dict and current_time - key_dict[key] < 0.1:
                st.title("chattering→ {}".format(key))
            else:
                st.text("正常→ {}".format(key))
            key_dict[key] = current_time
    except KeyboardInterrupt:
        break

if st.button("Reset"):
    st.caching.clear_cache()

