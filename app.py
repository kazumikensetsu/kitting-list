import streamlit as st

# ==========================================
# 【基本設定：案件ごとにここを書き換える】
# ==========================================
CURRENT_ID = "houwa_20260117" 
PROJECT_NAME = "【HOUWA】iPhone16e (279台)"
DEFAULT_PASSWORD = "houwa0119"
# ==========================================

if 'last_id' not in st.session_state or st.session_state.last_id != CURRENT_ID:
    st.session_state.last_id = CURRENT_ID
    st.session_state.project = PROJECT_NAME
    st.session_state.target_pass = DEFAULT_PASSWORD

ADMIN_PASSWORD = "noda777"

st.title("🔐 資料共有システム")

# --- サイドバー（管理者メニュー） ---
with st.sidebar:
    st.header("管理者メニュー")
    admin_input = st.text_input("管理者パスワード", type="password")
    
    if admin_input == ADMIN_PASSWORD:
        st.success("認証済み")
        st.write(f"現在の正解: **{st.session_state.target_pass}**")
        
        st.divider()
        st.subheader("🤖 パスワード自動生成")
        # ここで略称と日付を入れると自動でパスワードができる
        p_id = st.text_input("案件略称", "houwa")
        p_date = st.text_input("日付 (4桁)", "0119")
        
        if st.button("✨ 自動生成を適用"):
            st.session_state.target_pass = f"{p_id}{p_date}"
            st.session_state.project = f"【{p_id.upper()}】案件"
            st.rerun()

        st.divider()
        st.subheader("✍️ 手動で直接書き換え")
        # 自動生成を使わず、好きな文字にしたい時はここ
        manual_name = st.text_input("表示名の変更", st.session_state.project)
        manual_pass = st.text_input("パスワードの直接変更", st.session_state.target_pass)
        
        if st.button("✅ 手動設定を適用"):
            st.session_state.project = manual_name
            st.session_state.target_pass = manual_pass
            st.rerun()

# --- メイン画面 ---
st.header(f"案件：{st.session_state.project}")
st.write("担当者から伝えられたパスワードを入力してください。")
user_pass = st.text_input("パスワード", type="password", key="user")

if st.button("認証してフォルダを開く"):
    if user_pass == st.session_state.target_pass:
        st.success("認証成功！")
        st.link_button("📂 MEGAで資料を確認する", "https://mega.nz/folder/sQ8W1BCB#sVCkHTzbntdJSpXF48FDJA") 
    else:
        st.error("パスワードが正しくありません。")
