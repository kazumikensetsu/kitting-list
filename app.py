import streamlit as st

# --- 【初期設定】ここは最初だけGitHubで設定します ---
ADMIN_PASSWORD = "noda777"  # 野田さん専用の「設定変更用」合言葉

# データの保存（本来はデータベースが必要ですが、簡易的にセッションを使います）
if 'project' not in st.session_state:
    st.session_state.project = "鹿住建設 案件一覧"
if 'target_pass' not in st.session_state:
    st.session_state.target_pass = "kazumi0000"

st.title("🔐 資料共有システム")

# --- サイドバー（左側の隠しメニュー） ---
with st.sidebar:
    st.header("管理者メニュー")
    admin_input = st.text_input("管理者パスワード", type="password")
    
    if admin_input == ADMIN_PASSWORD:
        st.success("管理者認証済み")
        st.session_state.project = st.text_input("案件名を入力", st.session_state.project)
        st.session_state.target_pass = st.text_input("相手に伝えるパスワード", st.session_state.target_pass)
        st.info("ここで変えた内容は、右側の画面に即座に反映されます。")

# --- メイン画面（一般の人が見る画面） ---
st.header(f"案件：{st.session_state.project}")
user_pass = st.text_input("パスワードを入力してください", type="password", key="user")

if st.button("フォルダを開く"):
    if user_pass == st.session_state.target_pass:
        st.success("認証成功！")
        st.link_button("📂 MEGAで資料を確認する", "https://mega.nz/xxxx") # ここにURL
    else:
        st.error("パスワードが違います。")
