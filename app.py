import streamlit as st

# --- 設定エリア ---
PASSWORD = "kazumi0000"
FILE_URL = "https://mega.nz/folder/sQ8W1BCB#sVCkHTzbntdJSpXF48FDJA"
# ----------------

st.set_page_config(page_title="Data Share", page_icon="🔐")

st.title("🔐 資料共有システム")
st.write("認証後、共有フォルダ「kitting_list」へアクセスできます。")

st.write("---")
pwd_input = st.text_input("パスワードを入力してください", type="password")

if st.button("認証してフォルダを開く"):
    if pwd_input == PASSWORD:
        st.success("認証に成功しました。")
        st.markdown(f"### [👉 kitting_list フォルダを開く]({FILE_URL})")
    else:
        st.error("パスワードが正しくありません。")

st.write("---")
st.caption("Secure File Transfer System")