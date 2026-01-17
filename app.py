import streamlit as st
import random
import string

# ==========================================
# 【重要】案件が変わる時だけ、ここを書き換えて保存してください
# ==========================================
# 日付や時刻を「手動で」書き換えるのが一番安全です
UPDATE_ID = "20260117_v5" 

PROJECT_NAME = "【HOUWA】iPhone16e (279台)"
INITIAL_PASS = "houwa0119"
# ==========================================

# 初回起動時、またはUPDATE_IDが変わった時だけ実行
if 'ver' not in st.session_state or st.session_state.ver != UPDATE_ID:
    st.session_state.ver = UPDATE_ID
    st.session_state.project = PROJECT_NAME
    st.session_state.target_pass = INITIAL_PASS
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
        st.subheader("🎲 パスワード生成")
        st.write("ボタンを押すと8桁のランダムパスになります")
        if st.button("✨ ランダム生成して適用"):
            # 英数字を混ぜた8桁
            new_pass = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            st.session_state.target_pass = new_pass
            st.rerun()

        st.divider()
        st.subheader("✍️ 手動設定")
        m_name = st.text_input("案件名", st.session_state.project)
        m_pass = st.text_input("パスワード", st.session_state.target_pass)
        if st.button("✅ 設定を保存"):
            st.session_state.project = m_name
            st.session_state.target_pass = m_pass
            st.rerun()

# --- メイン画面 ---
st.header(f"📁 案件：{st.session_state.project}")

# 管理者の場合のみ、現在のパスワードを表示
if admin_input == ADMIN_PASSWORD:
    st.warning(f"🔑 **現在のパスワード： {st.session_state.target_pass}**")

st.divider()

user_pass = st.text_input("🔑 共有パスワードを入力", type="password")

if st.button("🚀 認証してフォルダを開く", use_container_width=True):
    if user_pass == st.session_state.target_pass:
        st.success("🎉 認証成功！")
        st.link_button("📂 MEGA資料フォルダを開く", "https://mega.nz/folder/sQ8W1BCB#sVCkHTzbntdJSpXF48FDJA", use_container_width=True)
    else:
        st.error("❌ パスワードが正しくありません。")
これは？
