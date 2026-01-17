import streamlit as st

# --- 【初期設定】 ---
ADMIN_PASSWORD = "noda777" 

if 'project' not in st.session_state:
    st.session_state.project = "案件未設定"
if 'target_pass' not in st.session_state:
    st.session_state.target_pass = "kazumi0000"

st.title("🔐 資料共有システム")

# --- サイドバー（管理者メニュー） ---
with st.sidebar:
    st.header("管理者メニュー")
    admin_input = st.text_input("管理者パスワード", type="password")
    
    if admin_input == ADMIN_PASSWORD:
        st.success("認証済み")
        
        # 19日の案件情報を初期値にセットしました
        p_id = st.text_input("案件略称", "houwa")
        p_date = st.text_input("日付", "0119")
        
        if st.button("✨ パスワードを自動作成"):
            generated = f"{p_id}{p_date}" 
            st.session_state.target_pass = generated
            st.session_state.project = f"【{p_id.upper()}】iPhone16e (279台)"
            st.warning(f"パスワードを【 {generated} 】にセットしました！")

        st.divider()
        st.write("現在の正解パスワード↓")
        st.session_state.target_pass = st.text_input("パスワード手動修正", st.session_state.target_pass)

# --- メイン画面 ---
st.header(f"案件：{st.session_state.project}")
st.write("担当者から伝えられたパスワードを入力してください。")
user_pass = st.text_input("パスワード", type="password", key="user")

if st.button("認証してフォルダを開く"):
    if user_pass == st.session_state.target_pass:
        st.success("認証成功！資料を表示します。")
        # 野田さんの正しいリンクをここに設定しました
        st.link_button("📂 MEGAでリストを確認する", "https://mega.nz/folder/sQ8W1BCB#sVCkHTzbntdJSpXF48FDJA") 
    else:
        st.error("パスワードが正しくありません。")

st.caption("Secure File Transfer System for Kazumi Kensetsu")
