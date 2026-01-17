import streamlit as st

# ==========================================
# 【基本設定：案件ごとにここを書き換えて保存】
# ==========================================
# 案件を切り替える際にここを変えるとiPhoneがリフレッシュされます
CURRENT_ID = "houwa_20260117" 

# 画面に表示する案件名
PROJECT_NAME = "【HOUWA】iPhone16e (279台)"

# その案件のデフォルトパスワード
DEFAULT_PASSWORD = "houwa0119"
# ==========================================

# 強制リフレッシュの仕組み
if 'last_id' not in st.session_state or st.session_state.last_id != CURRENT_ID:
    st.session_state.last_id = CURRENT_ID
    st.session_state.project = PROJECT_NAME
    st.session_state.target_pass = DEFAULT_PASSWORD

# 管理者パスワード
ADMIN_PASSWORD = "noda777"

st.title("🔐 資料共有システム")

# --- サイドバー（管理者メニュー） ---
with st.sidebar:
    st.header("管理者メニュー")
    admin_input = st.text_input("管理者パスワード", type="password")
    
    if admin_input == ADMIN_PASSWORD:
        st.success("認証済み")
        st.write(f"現在の案件: {st.session_state.project}")
        st.info(f"現在の正解: {st.session_state.target_pass}")
        
        st.divider()
        st.subheader("現場での一時変更")
        new_name = st.text_input("新しい表示名", st.session_state.project)
        new_pass = st.text_input("新しいパスワード", st.session_state.target_pass)
        
        if st.button("✨ 設定を上書きする"):
            st.session_state.project = new_name
            st.session_state.target_pass = new_pass
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
