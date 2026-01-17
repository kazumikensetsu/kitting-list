import streamlit as st

# ==========================================
# 【ここを案件ごとに書き換えて保存してください】
# ==========================================

# 1. 案件を切り替えるたびに、ここを適当な文字に変えるとiPhoneがリフレッシュされます
CURRENT_ID = "houwa_20260119" 

# 2. 画面に表示する案件名
PROJECT_NAME = "【HOUWA】iPhone16e (279台)"

# 3. その案件の正解パスワード
TARGET_PASSWORD = "houwa0119"

# ==========================================

# 強制リフレッシュの仕組み
if 'last_id' not in st.session_state or st.session_state.last_id != CURRENT_ID:
    st.session_state.last_id = CURRENT_ID
    st.session_state.project = PROJECT_NAME
    st.session_state.target_pass = TARGET_PASSWORD

# 管理者パスワード（野田さん用）
ADMIN_PASSWORD = "noda777"

st.title("🔐 資料共有システム")

# --- サイドバー（管理者メニュー） ---
with st.sidebar:
    st.header("管理者メニュー")
    admin_input = st.text_input("管理者パスワード", type="password")
    
    if admin_input == ADMIN_PASSWORD:
        st.success("認証済み")
        st.info(f"現在の正解: {st.session_state.target_pass}")
        p_id = st.text_input("案件略称", "new")
        p_date = st.text_input("日付", "0000")
        
        if st.button("✨ この設定に一時変更"):
            st.session_state.target_pass = f"{p_id}{p_date}"
            st.session_state.project = f"【{p_id.upper()}】臨時案件"
            st.warning("設定を一時的に変更しました")

# --- メイン画面 ---
st.header(f"案件：{st.session_state.project}")
st.write("担当者から伝えられたパスワードを入力してください。")
user_pass = st.text_input("パスワード", type="password", key="user")

if st.button("認証してフォルダを開く"):
    if user_pass == st.session_state.target_pass:
        st.success("認証成功！")
        # 野田さんのMEGA共有リンク
        st.link_button("📂 MEGAで資料を確認する", "https://mega.nz/folder/sQ8W1BCB#sVCkHTzbntdJSpXF48FDJA") 
    else:
        st.error("パスワードが正しくありません。")
