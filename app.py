import streamlit as st
import random
import string

# ==========================================
# 【基本設定：案件ごとにここを変更】
# ==========================================
# 案件を変える際、ここを書き換えて保存するとiPhoneが強制更新されます
CURRENT_VERSION = "20260117_FINAL" 

PROJECT_NAME = "【HOUWA】iPhone16e (279台)"
INITIAL_PASSWORD = "houwa0119"

# 共有資料のURL（MEGA）
MEGA_URL = "https://mega.nz/folder/sQ8W1BCB#sVCkHTzbntdJSpXF48FDJA"
# ==========================================

# ==========================================
# 【iPhone Safari + くるくるループ完全対策】
# ==========================================
if ('ver' not in st.session_state or 
    st.session_state.ver != CURRENT_VERSION or 
    st.query_params.get("refresh")):  # 半角? に修正済み
    
    st.session_state.ver = CURRENT_VERSION
    st.session_state.project = PROJECT_NAME
    st.session_state.target_pass = INITIAL_PASSWORD
    st.session_state.is_admin = False
    st.session_state.authenticated = False
    
    # リフレッシュフラグがある場合は消去
    if st.query_params.get("refresh"):
        st.query_params.clear()
    st.rerun()

ADMIN_PASSWORD = "noda777"

st.set_page_config(page_title="資料共有システム", layout="centered")
st.title("🔐 資料共有システム")

# --- サイドバー（管理者メニュー） ---
with st.sidebar:
    st.header("👤 管理者メニュー")
    admin_input = st.text_input("🔐 管理者パスワード", type="password", key="admin_input")
    
    if admin_input == ADMIN_PASSWORD:
        st.session_state.is_admin = True
        st.success("✅ 管理者認証完了")
        st.caption(f"📋 バージョン: {st.session_state.ver}")
        
        st.divider()
        st.subheader("🎲 パスワード生成")
        if st.button("✨ 8桁ランダム生成＆適用", use_container_width=True):
            chars = string.ascii_lowercase + string.digits
            new_pass = ''.join(random.choice(chars) for _ in range(8))
            st.session_state.target_pass = new_pass
            st.balloons()
            st.rerun()

        st.divider()
        st.subheader("✍️ 手動設定")
        col1, col2 = st.columns([2, 1])
        with col1:
            m_name = st.text_input("案件名変更", st.session_state.project)
        with col2:
            m_pass = st.text_input("パスワード", st.session_state.target_pass)
        
        if st.button("✅ 設定を保存", use_container_width=True):
            st.session_state.project = m_name
            st.session_state.target_pass = m_pass
            st.success("💾 保存しました")
            st.rerun()
        
        st.divider()
        if st.button("🔄 iPhone表示を強制更新", use_container_width=True):
            st.query_params["refresh"] = "1"
            st.rerun()

# --- メイン画面 ---
st.header(f"📁 案件：{st.session_state.project}")

# 管理者ログイン時は現在のパスを表示
if st.session_state.get("is_admin", False):
    st.warning(f"🔑 **現在の共有パスワード**: `{st.session_state.target_pass}`")
    st.caption("📱 このパスワードを現場スタッフに伝えてください")

st.divider()

user_pass = st.text_input("🔑 パスワードを入力してください", type="password", key="user_pass")

if st.button("🚀 認証してフォルダを開く", use_container_width=True):
    if user_pass == st.session_state.target_pass:
        st.session_state.authenticated = True
        st.success("🎉 認証成功！")
        st.caption("🌐 新しいタブでMEGAが開きます")
        st.link_button("📂 MEGA資料フォルダを開く", MEGA_URL, use_container_width=True)
        st.balloons()
        st.info("🔒 パスワードは他人に絶対共有しないでください")
    else:
        st.error("❌ パスワードが違います")
        st.session_state.authenticated = False

# 認証済み状態の補助表示
if st.session_state.get("authenticated", False):
    st.success("✅ 認証済みです。上のリンクからMEGAを開いてください")

# URLクリーンアップ
st.divider()
if st.button("🧹 URL表示をきれいにする", key="clear_url"):
    st.query_params.clear()
    st.rerun()

