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
        
        # 案件情報の入力（初期値をホウワ様にセットしておきました）
        p_id = st.text_input("案件略称 (例: houwa)", "houwa")
        p_date = st.text_input("日付 (例: 0119)", "0119")
        
        # 💡 自動生成ボタン
        if st.button("✨ パスワードを自動作成"):
            # 略称と日付をくっつけてパスワードにする
            generated = f"{p_id}{p_date}" 
            st.session_state.target_pass = generated
            st.session_state.project = f"{p_id.upper()}案件 ({p_date})"
            st.warning(f"パスワードを【 {generated} 】にセットしました！")

        st.divider()
        st.write("手動で変更したい場合↓")
        st.session_state.target_pass = st.text_input("現在のパスワード", st.session_state.target_pass)

# --- メイン画面 ---
st.header(f"案件：{st.session_state.project}")
user_pass = st.text_input("パスワードを入力してください", type="password", key="user")

if st.button("認証してフォルダを開く"):
    if user_pass == st.session_state.target_pass:
        st.success("認証成功！")
        # ここに実際のMEGAのリンクを貼ってください
        st.link_button("📂 MEGAで資料を確認する", "https://mega.nz/xxxx") 
    else:
        st.error("パスワードが違います。")

st.caption("Secure File Transfer System for Kazumi Kensetsu")
