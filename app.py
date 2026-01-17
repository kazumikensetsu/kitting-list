import streamlit as st
import hashlib
import time

# ==========================================
# 【基本設定：案件ごとにここを書き換える】
# ==========================================
CURRENT_ID = "houwa_20260117" 
PROJECT_NAME = "【HOUWA】iPhone16e (279台)"
DEFAULT_PASSWORD = "houwa0119"
DEPLOY_TIMESTAMP = "2026-01-17T18:47:00"  # GitHub更新時のタイムスタンプ
# ==========================================

# ==========================================
# 【GitHub更新直後のiPhone Safari対策：CACHE-BUSTER】
# ==========================================
# 1. URLクエリ + 2. タイムスタンプ + 3. ハッシュで強制更新検知
cache_buster = st.query_params.get("cb", "0")
timestamp_hash = hashlib.md5(DEPLOY_TIMESTAMP.encode()).hexdigest()[:8]

# セッション状態の初期化（3重チェックで確実性UP）
if ('last_id' not in st.session_state or 
    st.session_state.last_id != CURRENT_ID or
    st.session_state.get('deploy_hash', '') != timestamp_hash or
    cache_buster != "0"):
    
    st.session_state.last_id = CURRENT_ID
    st.session_state.project = PROJECT_NAME
    st.session_state.target_pass = DEFAULT_PASSWORD
    st.session_state.authenticated = False
    st.session_state.deploy_hash = timestamp_hash  # デプロイハッシュ記録
    st.query_params["cb"] = timestamp_hash  # 自動で最新URL生成
    st.rerun()

ADMIN_PASSWORD = "noda777"

st.title("🔐 資料共有システム")

# ==========================================
# 【重要：初回アクセス時の自動更新通知】
# ==========================================
st.warning("""
🚨 **GitHubコード更新直後の重要なお知らせ**

野田さんが`CURRENT_ID`を変更したばかりの場合：
1. **画面上部のこの警告が古い内容**の可能性があります
2. **URL末尾に `?cb=xxxxxxxx` が自動付与**されました → これが最新版です
3. それでも不安なら **手動で `?1` を追加**してリロードしてください

**現在のデプロイ時刻**: {DEPLOY_TIMESTAMP}
**バージョン**: {timestamp_hash}
""")

# --- サイドバー（管理者メニュー） ---
with st.sidebar:
    st.header("👤 管理者メニュー")
    admin_input = st.text_input("🔐 管理者パスワード", type="password")
    
    if admin_input == ADMIN_PASSWORD:
        st.success("✅ 管理者認証完了")
        st.caption(f"📋 現在: **{st.session_state.project}** / **{st.session_state.target_pass}**")
        st.caption(f"🔄 デプロイ: {timestamp_hash}")
        
        st.divider()
        st.subheader("🤖 自動生成")
        col1, col2 = st.columns(2)
        with col1: p_id = st.text_input("略称", "houwa", key="pid")
        with col2: p_date = st.text_input("日付", "0119", key="pdate")
        
        if st.button("✨ 自動生成適用", use_container_width=True):
            st.session_state.target_pass = f"{p_id}{p_date}"
            st.session_state.project = f"【{p_id.upper()}】案件"
            st.query_params["refresh"] = str(int(time.time()))  # ユニークタイムスタンプ
            st.rerun()

        st.divider()
        st.subheader("✍️ 手動設定")
        manual_name = st.text_input("表示名", st.session_state.project, key="mname")
        manual_pass = st.text_input("パスワード", st.session_state.target_pass, key="mpass")
        
        if st.button("✅ 手動適用", use_container_width=True):
            st.session_state.project = manual_name
            st.session_state.target_pass = manual_pass
            st.query_params["refresh"] = str(int(time.time()))
            st.rerun()

        st.divider()
        if st.button("🔄 強制リフレッシュ（iPhone用）", key="force_refresh"):
            st.query_params["cb"] = str(int(time.time()))
            st.rerun()

# --- メイン画面 ---
st.header(f"📁 案件：{st.session_state.project}")
st.caption("💡 iPhone Safari: 反映されない場合はURL末尾に `?1` を追加")

user_pass = st.text_input("🔑 共有パスワード", type="password", key="user_pass")

if st.button("🚀 認証 → MEGA資料", use_container_width=True):
    if user_pass == st.session_state.target_pass:
        st.session_state.authenticated = True
        st.success("🎉 認証成功！")
        st.caption("🌐 新しいタブで開きます")
        st.link_button("📂 MEGAフォルダ", "https://mega.nz/folder/sQ8W1BCB#sVCkHTzbntdJSpXF48FDJA", use_container_width=True)
        st.info("🔒 パスワードは絶対に他人と共有しないでください")
        st.balloons()
    else:
        st.error("❌ パスワード不一致")
        st.session_state.authenticated = False

if st.session_state.get("authenticated", False):
    st.success("✅ 認証済み状態")

# URLクリーンアップ
if st.button("🧹 URL整理", key="clear_params"):
    st.query_params.clear()
    st.rerun()

