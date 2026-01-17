import streamlit as st

# ==========================================
# 【基本設定：案件ごとにここを書き換えて保存】
# ==========================================
# 案件を変える際、ここを適当な数字に変えるだけでiPhoneは更新されます
CURRENT_VERSION = "20260117_01" 

PROJECT_NAME = "【HOUWA】iPhone16e (279台)"
TARGET_PASSWORD = "houwa0119"
# ==========================================

# くるくるループを防ぐためのシンプルな初期化
if 'ver' not in st.session_state or st.session_state.ver != CURRENT_VERSION:
    st.session_state.ver = CURRENT_VERSION
    st.session_state.project = PROJECT_NAME
    st.session_state.target_pass = TARGET_PASSWORD

ADMIN_PASSWORD = "noda777"

st.title("🔐 資料共有システム")

# --- サイドバー（管理者メニュー） ---
with st.sidebar:
    st.header("👤 管理者メニュー")
    admin_input = st.text_input("管理者パスワード", type="password")
    
    if admin_input == ADMIN_PASSWORD:
        st.success("✅ 認証済み")
        st.write(f"現在の正解: **{st.session_state.target_pass}**")
        
        st.divider()
        st.subheader("🤖 パスワード自動生成")
        p_id = st.text_input("略称", "houwa")
        p_date = st.text_input("日付", "0119")
        if st.button("✨ 自動生成を適用"):
            st.session_state.target_pass = f"{p_id}{p_date}"
            st.session_state.project = f"【{p_id.upper()}】案件"
            st.rerun()

        st.divider()
        st.subheader("✍️ 手動設定")
        m_name = st.text_input("表示名", st.session_state.project)
        m_pass = st.text_input("パスワード", st.session_state.target_pass)
        if st.button("✅ 手動設定を適用"):
            st.session_state.project = m_name
            st.session_state.target_pass = m_pass
            st.rerun()

# --- メイン画面 ---
st.header(f"📁 案件：{st.session_state.project}")
user_pass = st.text_input("🔑 共有パスワード", type="password")

if st.button("🚀 認証してフォルダを開く", use_container_width=True):
    if user_pass == st.session_state.target_pass:
        st.success("🎉 認証成功！")
        st.link_button("📂 MEGA資料フォルダを開く", "https://mega.nz/folder/sQ8W1BCB#sVCkHTzbntdJSpXF48FDJA", use_container_width=True)
    else:
        st.error("❌ パスワードが正しくありません。")

st.divider()
st.caption("※ 画面が古い場合はブラウザを再読み込みしてください。")
