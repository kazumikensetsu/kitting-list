import streamlit as st
import random
import string

# ==========================================
# 【基本設定】
# ==========================================
CURRENT_VERSION = "20260117_RANDOM" 

if 'ver' not in st.session_state or st.session_state.ver != CURRENT_VERSION:
    st.session_state.ver = CURRENT_VERSION
    st.session_state.project = "【HOUWA】iPhone16e (279台)"
    st.session_state.target_pass = "houwa0119" # 最初だけこれ
    st.rerun()

ADMIN_PASSWORD = "noda777"

st.title("🔐 資料共有システム")

# --- サイドバー（管理者メニュー） ---
with st.sidebar:
    st.header("👤 管理者メニュー")
    admin_input = st.text_input("管理者パスワード", type="password")
    
    if admin_input == ADMIN_PASSWORD:
        st.success("✅ 認証済み")
        
        st.divider()
        st.subheader("🎲 パスワードをランダム生成")
        # 英数字を混ぜた8桁のランダムなパスを作る関数
        if st.button("✨ 新しいパスを生成＆適用"):
            chars = string.ascii_lowercase + string.digits
            new_pass = ''.join(random.choice(chars) for i in range(8))
            st.session_state.target_pass = new_pass
            st.rerun()

        st.divider()
        st.subheader("✍️ 手動設定（案件名など）")
        m_name = st.text_input("案件表示名", st.session_state.project)
        m_pass = st.text_input("現在のパスワード", st.session_state.target_pass)
        
        if st.button("✅ 設定を保存"):
            st.session_state.project = m_name
            st.session_state.target_pass = m_pass
            st.rerun()

# --- メイン画面 ---
st.header(f"📁 案件：{st.session_state.project}")

# 管理者でログインしている時だけ、現在のパスワードを画面に表示する
if admin_input == ADMIN_PASSWORD:
    st.info(f"🔑 **現在の正解パスワード： {st.session_state.target_pass}**")
    st.write("現場のスタッフには、上記のパスワードを伝えてください。")

st.divider()

user_pass = st.text_input("🔑 共有パスワードを入力", type="password")

if st.button("🚀 認証してフォルダを開く", use_container_width=True):
    if user_pass == st.session_state.target_pass:
        st.success("🎉 認証成功！")
        st.link_button("📂 MEGA資料フォルダを開く", "https://mega.nz/folder/sQ8W1BCB#sVCkHTzbntdJSpXF48FDJA", use_container_width=True)
    else:
        st.error("❌ パスワードが正しくありません。")
