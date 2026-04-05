import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ══════════════════════════════════════════════════════════
#  CSS
# ══════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #070B12 !important;
    color: #D8E4F0;
}

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }
[data-testid="stSidebarNav"] { display: none; }

.main .block-container {
    padding: 0 0 3rem 0 !important;
    max-width: 100% !important;
}

[data-testid="stAppViewContainer"] > section > div:first-child {
    padding-top: 58px !important;
}

/* ══ LOGIN PAGE ══ */
.login-wrapper {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: radial-gradient(ellipse at 20% 50%, #0F2044 0%, #070B12 60%);
    padding-top: 0 !important;
}
.login-card {
    background: #0D1828;
    border: 1px solid #1E3A6A;
    border-radius: 20px;
    padding: 2.8rem 2.4rem;
    width: 100%;
    max-width: 420px;
    box-shadow: 0 30px 80px rgba(0,0,0,0.6), 0 0 0 1px rgba(59,139,255,0.08);
}
.login-logo {
    text-align: center;
    margin-bottom: 0.4rem;
    font-size: 2.5rem;
}
.login-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 800;
    color: #EDF2FF;
    text-align: center;
    margin-bottom: 0.2rem;
}
.login-title span { color: #5BA3FF; }
.login-sub {
    font-size: 0.82rem;
    color: #3A6090;
    text-align: center;
    margin-bottom: 2rem;
}
.login-label {
    font-size: 0.78rem;
    color: #4A6888;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    font-weight: 600;
    margin-bottom: 0.35rem;
    display: block;
}
.login-divider {
    border: none;
    border-top: 1px solid #142035;
    margin: 1.4rem 0;
}
.login-hint {
    font-size: 0.72rem;
    color: #1E3050;
    text-align: center;
    margin-top: 1rem;
}
.login-hint b { color: #2A5080; }

/* ══ TOP NAVBAR ══ */
.topbar {
    background: linear-gradient(90deg, #0F2044 0%, #1A3560 100%);
    border-bottom: 1px solid #1E3A6A;
    padding: 0 2.5rem;
    height: 58px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 9999;
    width: 100vw;
}
.topbar-brand {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    font-family: 'Syne', sans-serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: #FFFFFF;
}
.topbar-brand span { color: #5BA3FF; }
.topbar-nav { display: flex; align-items: center; gap: 2rem; }
.topbar-nav a {
    font-size: 0.88rem;
    color: #8AADD0;
    text-decoration: none;
    font-weight: 500;
}
.topbar-nav a.active { color: #FFFFFF; }
.admin-badge {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(255,255,255,0.07);
    border: 1px solid #2A4A7A;
    border-radius: 20px;
    padding: 4px 12px 4px 6px;
    font-size: 0.82rem;
    color: #C5D8F0;
}
.admin-avatar {
    width: 26px; height: 26px;
    background: linear-gradient(135deg, #3B8BFF, #1A5FCC);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.72rem; font-weight: 700; color: #fff;
}

/* ══ SIDEBAR ══ */
[data-testid="stSidebar"] {
    background: #0A1020 !important;
    border-right: 1px solid #142035 !important;
    min-width: 200px !important;
    max-width: 220px !important;
}
[data-testid="stSidebar"] > div { padding-top: 1.2rem !important; }
[data-testid="stSidebar"] * { color: #6A8AAA !important; }
[data-testid="stSidebar"] [data-testid="stRadio"] label { font-size: 0.9rem !important; padding: 0.35rem 0 !important; }
.sidebar-section {
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #2A4060 !important;
    padding: 0.8rem 1rem 0.3rem;
    font-weight: 600;
}
.sidebar-divider { border: none; border-top: 1px solid #142035; margin: 0.7rem 0; }

/* ══ CONTENT ══ */
.content-pad { padding: 1.6rem 2rem; }
.page-heading {
    font-family: 'Syne', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    color: #EDF2FF;
    margin-bottom: 1.2rem;
}

/* ══ STAT CARDS ══ */
.stats-grid { display: flex; gap: 1rem; margin-bottom: 1.4rem; }
.stat-card {
    flex: 1;
    background: #0D1828;
    border: 1px solid #162540;
    border-radius: 12px;
    padding: 1rem 1.3rem;
    position: relative;
    overflow: hidden;
}
.stat-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 2px;
    background: var(--c, #3B8BFF);
}
.stat-top { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.4rem; }
.stat-label { font-size: 0.72rem; color: #4A6888; text-transform: uppercase; letter-spacing: 0.8px; font-weight: 600; }
.stat-icon-box {
    width: 30px; height: 30px;
    background: rgba(255,255,255,0.04);
    border-radius: 7px;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.95rem;
}
.stat-value { font-family: 'Syne', sans-serif; font-size: 1.9rem; font-weight: 800; color: var(--c, #3B8BFF); line-height: 1; }
.stat-sub { font-size: 0.7rem; color: #2A4060; margin-top: 0.25rem; }

/* ══ PANEL ══ */
.panel { background: #0D1828; border: 1px solid #162540; border-radius: 14px; overflow: hidden; margin-bottom: 1.1rem; }
.panel-header {
    background: linear-gradient(90deg, #0F2044, #172D55);
    padding: 0.65rem 1.3rem;
    font-family: 'Syne', sans-serif;
    font-size: 0.85rem;
    font-weight: 700;
    color: #C5D8F0;
    letter-spacing: 0.3px;
    border-bottom: 1px solid #1A3060;
}
.panel-body { padding: 1.1rem 1.3rem; }

/* ══ TABLE ══ */
.styled-table { width: 100%; border-collapse: collapse; }
.styled-table th {
    background: #0A1525;
    color: #4A6888;
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    padding: 0.65rem 0.9rem;
    text-align: left;
    border-bottom: 1px solid #162540;
    font-weight: 600;
}
.styled-table td { padding: 0.6rem 0.9rem; font-size: 0.86rem; color: #B0C8E0; border-bottom: 1px solid #0F1E32; }
.styled-table tr:hover td { background: rgba(59,139,255,0.04); }
.styled-table tr:last-child td { border-bottom: none; }
.marks-pill {
    display: inline-block;
    padding: 2px 9px;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 700;
    font-family: 'Syne', sans-serif;
}
.pass { background:#0A2A18; color:#34D399; border:1px solid #34D39930; }
.fail { background:#2A0A10; color:#F87171; border:1px solid #F8717130; }
.sid {
    font-family: 'Syne', sans-serif;
    font-size: 0.76rem;
    background: #0A1525;
    color: #3B8BFF;
    border: 1px solid #1E3560;
    border-radius: 5px;
    padding: 1px 6px;
}

/* ══ INPUTS ══ */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input {
    background: #0A1525 !important;
    border: 1px solid #1E3050 !important;
    border-radius: 8px !important;
    color: #E0EEFF !important;
    font-family: 'DM Sans', sans-serif !important;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stNumberInput"] input:focus {
    border-color: #3B8BFF !important;
    box-shadow: 0 0 0 3px rgba(59,139,255,0.15) !important;
}
[data-testid="stSelectbox"] > div > div {
    background: #0A1525 !important;
    border: 1px solid #1E3050 !important;
    border-radius: 8px !important;
    color: #E0EEFF !important;
}
[data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"] { background: #3B8BFF !important; }

/* ══ BUTTONS ══ */
[data-testid="stButton"] button {
    background: linear-gradient(135deg, #1A4A8A, #2B6FCC) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    padding: 0.55rem 1.4rem !important;
    width: 100%;
    transition: opacity .2s, transform .1s !important;
}
[data-testid="stButton"] button:hover { opacity: 0.88; transform: translateY(-1px) !important; }

/* ══ LOGIN BUTTON ══ */
.login-btn [data-testid="stButton"] button {
    background: linear-gradient(135deg, #1560C0, #3B8BFF) !important;
    font-size: 0.95rem !important;
    padding: 0.7rem 1.4rem !important;
    border-radius: 10px !important;
    letter-spacing: 0.3px;
}

/* ══ TAB BUTTONS ══ */
[data-testid="stColumns"] [data-testid="stButton"] button[kind="primary"] {
    background: linear-gradient(135deg, #1560C0, #3B8BFF) !important;
    border-radius: 10px 10px 0 0 !important;
    font-size: 0.88rem !important;
}
[data-testid="stColumns"] [data-testid="stButton"] button[kind="secondary"] {
    background: #0A1525 !important;
    color: #3A6090 !important;
    border: 1px solid #1E3050 !important;
    border-radius: 10px 10px 0 0 !important;
    font-size: 0.88rem !important;
}

/* ══ LOGOUT BUTTON in sidebar ══ */
.logout-btn [data-testid="stButton"] button {
    background: linear-gradient(135deg, #2A0A10, #5A1A20) !important;
    color: #F87171 !important;
    font-size: 0.8rem !important;
    padding: 0.4rem 1rem !important;
}

/* ══ DATAFRAME ══ */
[data-testid="stDataFrame"] { border: 1px solid #162540 !important; border-radius: 10px !important; }
[data-testid="stDataFrame"] th { background: #0A1525 !important; color: #4A6888 !important; font-size: 0.72rem !important; text-transform: uppercase !important; }
[data-testid="stDataFrame"] td { color: #B0C8E0 !important; }

[data-testid="stAlert"] { background: #0D1828 !important; border-radius: 10px !important; border: 1px solid #162540 !important; }

hr { border-color: #142035 !important; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
#  SESSION STATE
# ══════════════════════════════════════════════════════════
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "admin_name" not in st.session_state:
    st.session_state.admin_name = ""
if "login_error" not in st.session_state:
    st.session_state.login_error = False
if "signup_msg" not in st.session_state:
    st.session_state.signup_msg = ""
if "signup_error" not in st.session_state:
    st.session_state.signup_error = ""
if "auth_tab" not in st.session_state:
    st.session_state.auth_tab = "login"

if "students" not in st.session_state:
    st.session_state.students = [
        {"ID":"S101","Name":"Anil Kumar",   "Branch":"CSE", "Year":"2nd","Subject":"Math",    "Marks":85,"Date":"2025-01-10"},
        {"ID":"S102","Name":"Priya Sharma",  "Branch":"ECE", "Year":"3rd","Subject":"Science", "Marks":78,"Date":"2025-01-11"},
        {"ID":"S103","Name":"Kiran Rao",     "Branch":"MECH","Year":"1st","Subject":"DBMS",    "Marks":65,"Date":"2025-01-12"},
        {"ID":"S104","Name":"Meera Nair",    "Branch":"CSE", "Year":"4th","Subject":"English",  "Marks":72,"Date":"2025-01-13"},
        {"ID":"S105","Name":"Ravi Patel",    "Branch":"IT",  "Year":"2nd","Subject":"Math",    "Marks":58,"Date":"2025-01-14"},
        {"ID":"S106","Name":"Sneha Joshi",   "Branch":"CSE", "Year":"3rd","Subject":"Science", "Marks":91,"Date":"2025-01-15"},
        {"ID":"S107","Name":"Arjun Singh",   "Branch":"ECE", "Year":"2nd","Subject":"DBMS",    "Marks":44,"Date":"2025-01-16"},
        {"ID":"S108","Name":"Divya Menon",   "Branch":"IT",  "Year":"1st","Subject":"English",  "Marks":80,"Date":"2025-01-17"},
    ]

# ══════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════
# Credentials stored in session state so new accounts persist during session
if "admin_credentials" not in st.session_state:
    st.session_state.admin_credentials = {
        "admin": "admin123",
        "principal": "principal@2025",
        "teacher": "teach123",
    }
ADMIN_CREDENTIALS = st.session_state.admin_credentials

def next_id():
    if not st.session_state.students:
        return "S101"
    ids = [int(s["ID"][1:]) for s in st.session_state.students]
    return f"S{max(ids)+1}"

def pass_fail(m): return "Pass" if m >= 50 else "Fail"

def grade(m):
    if m >= 85: return "A"
    if m >= 70: return "B"
    if m >= 50: return "C"
    return "D"

CHART_BG = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Sans", color="#5A7890"),
    margin=dict(t=20, b=10, l=10, r=10),
)

# ══════════════════════════════════════════════════════════
#  LOGIN PAGE
# ══════════════════════════════════════════════════════════
if not st.session_state.logged_in:
    # Hide sidebar on login page
    st.markdown("""
    <style>
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stAppViewContainer"] > section > div:first-child { padding-top: 0 !important; }
    .main .block-container { padding: 0 !important; }
    </style>
    """, unsafe_allow_html=True)

    _, center_col, _ = st.columns([1, 1.2, 1])

    with center_col:
        st.markdown("<br><br>", unsafe_allow_html=True)

        st.markdown("""
        <div class='login-logo'>🎓</div>
        <div class='login-title'><span>Student</span> Performance<br>Analytics</div>
        <div class='login-sub'>Admin Portal · Secure Access</div>
        """, unsafe_allow_html=True)

        # ── Tab switcher ──
        t1, t2 = st.columns(2)
        with t1:
            if st.button("🔓  Sign In", key="tab_login",
                         type="primary" if st.session_state.auth_tab == "login" else "secondary"):
                st.session_state.auth_tab = "login"
                st.session_state.login_error = False
                st.session_state.signup_msg = ""
                st.session_state.signup_error = ""
                st.rerun()
        with t2:
            if st.button("✨  Create Account", key="tab_signup",
                         type="primary" if st.session_state.auth_tab == "signup" else "secondary"):
                st.session_state.auth_tab = "signup"
                st.session_state.login_error = False
                st.session_state.signup_msg = ""
                st.session_state.signup_error = ""
                st.rerun()

        st.markdown("<div style='background:#0D1828;border:1px solid #1E3A6A;border-radius:20px;padding:2rem 2rem;margin-top:0.6rem;'>", unsafe_allow_html=True)

        # ══ LOGIN TAB ══
        if st.session_state.auth_tab == "login":
            username = st.text_input("👤 Admin Username", placeholder="Enter your username", key="login_user")
            password = st.text_input("🔒 Password", placeholder="Enter your password", type="password", key="login_pass")

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<div class='login-btn'>", unsafe_allow_html=True)
            login_clicked = st.button("🔓  Sign In to Dashboard", key="login_btn")
            st.markdown("</div>", unsafe_allow_html=True)

            if login_clicked:
                # Case-insensitive username match
                username_lower = username.strip().lower()
                if username_lower in ADMIN_CREDENTIALS and ADMIN_CREDENTIALS[username_lower] == password:
                    st.session_state.logged_in = True
                    # Show their registered display name if available, else capitalize username
                    display = st.session_state.get("admin_display_names", {}).get(username_lower, username_lower.capitalize())
                    st.session_state.admin_name = display
                    st.session_state.login_error = False
                    st.rerun()
                else:
                    st.session_state.login_error = True

            if st.session_state.login_error:
                st.markdown("""
                <div style='background:#1A0810;border:1px solid #5A1A2A;border-radius:8px;padding:0.6rem 1rem;margin-top:0.8rem;'>
                  <p style='color:#F87171;font-size:0.82rem;margin:0;'>❌ Invalid username or password. Please try again.</p>
                </div>""", unsafe_allow_html=True)

            st.markdown("""
            <hr class='login-divider'>
            <div class='login-hint'>
              Default credentials &nbsp;·&nbsp; Username: <b>admin</b> &nbsp;·&nbsp; Password: <b>admin123</b>
            </div>
            """, unsafe_allow_html=True)

        # ══ CREATE ACCOUNT TAB ══
        else:
            new_fullname = st.text_input("👤 Full Name", placeholder="e.g. Nisha Patil", key="su_fullname")
            new_user     = st.text_input("🆔 Choose Username", placeholder="e.g. nisha_patil  (used to log in)", key="su_user")

            c_p1, c_p2 = st.columns(2)
            with c_p1:
                new_pass     = st.text_input("🔒 Create Password", placeholder="Min. 6 chars", type="password", key="su_pass")
            with c_p2:
                confirm_pass = st.text_input("🔁 Confirm Password", placeholder="Re-enter", type="password", key="su_confirm")

            role = st.selectbox("🏷️ Role", ["Teacher", "HOD", "Principal", "Coordinator"], key="su_role")

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<div class='login-btn'>", unsafe_allow_html=True)
            signup_clicked = st.button("✨  Create My Account", key="signup_btn")
            st.markdown("</div>", unsafe_allow_html=True)

            if signup_clicked:
                clean_user = new_user.strip().lower()
                if not new_fullname.strip() or not clean_user:
                    st.session_state.signup_error = "Please fill in all fields."
                elif len(new_pass) < 6:
                    st.session_state.signup_error = "Password must be at least 6 characters."
                elif new_pass != confirm_pass:
                    st.session_state.signup_error = "Passwords do not match."
                elif clean_user in ADMIN_CREDENTIALS:
                    st.session_state.signup_error = f"Username '{clean_user}' already exists. Choose another."
                else:
                    st.session_state.admin_credentials[clean_user] = new_pass
                    # Store display name keyed by username
                    if "admin_display_names" not in st.session_state:
                        st.session_state.admin_display_names = {}
                    st.session_state.admin_display_names[clean_user] = new_fullname.strip()
                    st.session_state.signup_error = ""
                    st.session_state.signup_msg = (
                        f"✅ Account created! "
                        f"Login with username <b>{clean_user}</b> and your password."
                    )

            if st.session_state.signup_error:
                st.markdown(f"""
                <div style='background:#1A0810;border:1px solid #5A1A2A;border-radius:8px;padding:0.6rem 1rem;margin-top:0.8rem;'>
                  <p style='color:#F87171;font-size:0.82rem;margin:0;'>❌ {st.session_state.signup_error}</p>
                </div>""", unsafe_allow_html=True)

            if st.session_state.signup_msg:
                st.markdown(f"""
                <div style='background:#0A2A18;border:1px solid #34D39950;border-radius:8px;padding:0.8rem 1rem;margin-top:0.8rem;'>
                  <p style='color:#34D399;font-size:0.84rem;margin:0;'>{st.session_state.signup_msg}</p>
                </div>""", unsafe_allow_html=True)
                if st.button("→  Go to Sign In", key="goto_login"):
                    st.session_state.auth_tab = "login"
                    st.session_state.signup_msg = ""
                    st.session_state.signup_error = ""
                    st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    st.stop()

# ══════════════════════════════════════════════════════════
#  TOP NAVBAR (shown only after login)
# ══════════════════════════════════════════════════════════
admin_initial = st.session_state.admin_name[0].upper() if st.session_state.admin_name else "A"
st.markdown(f"""
<div class="topbar">
  <div class="topbar-brand">🎓 <span>Student</span>&nbsp;Performance Analytics</div>
  <div class="topbar-nav">
    <a href="#" class="active">Dashboard</a>
    <a href="#">Add Student</a>
    <a href="#">Analytics</a>
  </div>
  <div class="admin-badge">
    <div class="admin-avatar">{admin_initial}</div>
    {st.session_state.admin_name}
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
#  SIDEBAR (shown only after login)
# ══════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("<p class='sidebar-section'>Main Menu</p>", unsafe_allow_html=True)
    page = st.radio("", ["🏠  Dashboard", "➕  Add Student", "📊  Analytics", "🗑️  Remove Student"],
                    label_visibility="collapsed")
    st.markdown("<hr class='sidebar-divider'>", unsafe_allow_html=True)
    st.markdown("<p class='sidebar-section'>Summary</p>", unsafe_allow_html=True)
    df_all = pd.DataFrame(st.session_state.students)
    if not df_all.empty:
        p = int((df_all["Marks"] >= 50).sum())
        f = int((df_all["Marks"] < 50).sum())
        st.markdown(f"""
        <div style='padding:0 0.6rem;font-size:.82rem;'>
          <p style='color:#3A6090;margin:.2rem 0;'>Total: <b style='color:#5BA3FF'>{len(df_all)}</b></p>
          <p style='color:#3A6090;margin:.2rem 0;'>Passed: <b style='color:#34D399'>{p}</b></p>
          <p style='color:#3A6090;margin:.2rem 0;'>Failed: <b style='color:#F87171'>{f}</b></p>
        </div>""", unsafe_allow_html=True)
    st.markdown("<hr class='sidebar-divider'>", unsafe_allow_html=True)

    # Logged in as + Logout
    st.markdown(f"""
    <div style='padding:0 0.6rem 0.4rem;font-size:.75rem;color:#2A5070;'>
      Logged in as <b style='color:#3B6090;'>{st.session_state.admin_name}</b>
    </div>""", unsafe_allow_html=True)
    st.markdown("<div class='logout-btn'>", unsafe_allow_html=True)
    if st.button("🚪 Logout", key="logout_btn"):
        st.session_state.logged_in = False
        st.session_state.admin_name = ""
        st.session_state.login_error = False
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<hr class='sidebar-divider'>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:.66rem;color:#1E3050;text-align:center;padding:.4rem 0;'>v2.0 · Student Analytics</p>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
#  PAGE: DASHBOARD
# ══════════════════════════════════════════════════════════
if page == "🏠  Dashboard":
    st.markdown("<div class='content-pad'>", unsafe_allow_html=True)
    st.markdown("<p class='page-heading'>Dashboard</p>", unsafe_allow_html=True)

    df = pd.DataFrame(st.session_state.students)
    avg_marks  = round(df["Marks"].mean(), 1) if not df.empty else 0
    top_count  = int((df["Marks"] >= 80).sum()) if not df.empty else 0
    weak_count = int((df["Marks"] < 50).sum())  if not df.empty else 0

    st.markdown(f"""
    <div class='stats-grid'>
      <div class='stat-card' style='--c:#3B8BFF'>
        <div class='stat-top'><span class='stat-label'>Total Students</span><div class='stat-icon-box'>👥</div></div>
        <div class='stat-value'>{len(df)}</div><div class='stat-sub'>Registered</div>
      </div>
      <div class='stat-card' style='--c:#34D399'>
        <div class='stat-top'><span class='stat-label'>Average Marks</span><div class='stat-icon-box'>📈</div></div>
        <div class='stat-value'>{avg_marks}</div><div class='stat-sub'>Class average</div>
      </div>
      <div class='stat-card' style='--c:#FBBF24'>
        <div class='stat-top'><span class='stat-label'>Top Students</span><div class='stat-icon-box'>🏆</div></div>
        <div class='stat-value'>{top_count}</div><div class='stat-sub'>Scored 80+</div>
      </div>
      <div class='stat-card' style='--c:#F87171'>
        <div class='stat-top'><span class='stat-label'>Weak Students</span><div class='stat-icon-box'>⚠️</div></div>
        <div class='stat-value'>{weak_count}</div><div class='stat-sub'>Below 50</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    col_charts, col_form = st.columns([2.2, 1], gap="large")

    with col_charts:
        ch1, ch2 = st.columns(2, gap="medium")

        with ch1:
            st.markdown("<div class='panel'><div class='panel-header'>📊 Average Marks by Subject</div>", unsafe_allow_html=True)
            subj_avg = df.groupby("Subject")["Marks"].mean().round(1).reset_index()
            COLORS = ["#3B8BFF","#34D399","#FBBF24","#A78BFA","#F87171","#60C0FF"]
            fig_bar = go.Figure(go.Bar(
                x=subj_avg["Subject"], y=subj_avg["Marks"],
                marker_color=COLORS[:len(subj_avg)],
                marker_line_width=0,
                text=subj_avg["Marks"], textposition="outside",
                textfont=dict(color="#8AAAD0", size=11, family="Syne"),
            ))
            fig_bar.update_layout(**CHART_BG, height=220,
                xaxis=dict(tickfont=dict(color="#5A7890",size=11), showgrid=False),
                yaxis=dict(tickfont=dict(color="#5A7890"), gridcolor="#0F1E32", range=[0,115]),
                bargap=0.4)
            st.plotly_chart(fig_bar, use_container_width=True, config={"displayModeBar":False})
            st.markdown("</div>", unsafe_allow_html=True)

        with ch2:
            st.markdown("<div class='panel'><div class='panel-header'>🥧 Performance Overview</div>", unsafe_allow_html=True)
            p = int((df["Marks"] >= 50).sum()); f = int((df["Marks"] < 50).sum())
            pct_p = round(p/len(df)*100) if len(df) else 0
            pct_f = round(f/len(df)*100) if len(df) else 0
            fig_pie = go.Figure(go.Pie(
                labels=[f"Pass: {pct_p}%", f"Fail: {pct_f}%"],
                values=[p, f], hole=0.0,
                marker_colors=["#2A7A50","#B03030"],
                textfont=dict(family="Syne", size=13, color="#fff"),
                hovertemplate="<b>%{label}</b>: %{value}<extra></extra>",
            ))
            fig_pie.update_layout(**CHART_BG, height=220,
                legend=dict(font=dict(color="#5A7890",size=11),bgcolor="rgba(0,0,0,0)"))
            st.plotly_chart(fig_pie, use_container_width=True, config={"displayModeBar":False})
            st.markdown("</div>", unsafe_allow_html=True)

    with col_form:
        st.markdown("<div class='panel'><div class='panel-header'>➕ Add New Student</div><div class='panel-body'>", unsafe_allow_html=True)
        q_name    = st.text_input("Student Name", placeholder="Enter name", key="q_name")
        q_branch  = st.selectbox("Branch", ["CSE","ECE","IT","MECH","CIVIL","EEE"], key="q_branch")
        q_year    = st.selectbox("Year", ["1st","2nd","3rd","4th"], key="q_year")
        q_subject = st.selectbox("Subject", ["Math","Science","DBMS","English","Physics","Chemistry"], key="q_subj")
        q_marks   = st.number_input("Marks (0–100)", 0, 100, 70, key="q_marks")
        if st.button("➕  Add Student", key="quick_add"):
            if q_name.strip():
                st.session_state.students.append({
                    "ID": next_id(), "Name": q_name.strip(),
                    "Branch": q_branch, "Year": q_year,
                    "Subject": q_subject, "Marks": q_marks,
                    "Date": str(datetime.today().date())
                })
                st.success(f"✅ {q_name} added!")
                st.rerun()
            else:
                st.warning("Enter student name.")
        st.markdown("</div></div>", unsafe_allow_html=True)

    col_tbl, col_perf = st.columns([1.3, 1], gap="large")

    with col_tbl:
        st.markdown("<div class='panel'><div class='panel-header'>📋 Student Marks</div>", unsafe_allow_html=True)
        search = st.text_input("", placeholder="🔍 Search by name...", key="dash_search", label_visibility="collapsed")
        df_show = df[df["Name"].str.contains(search, case=False)] if search else df
        rows = ""
        for _, row in df_show.iterrows():
            pf = pass_fail(row["Marks"])
            badge = "pass" if pf == "Pass" else "fail"
            rows += f"<tr><td><span class='sid'>{row['ID']}</span></td><td>{row['Name']}</td><td>{row['Subject']}</td><td><span class='marks-pill {badge}'>{row['Marks']}</span></td></tr>"
        st.markdown(f"""
        <div style='overflow-x:auto;padding:0.7rem 1rem;'>
        <table class='styled-table'>
          <thead><tr><th>Student ID</th><th>Name</th><th>Subject</th><th>Marks</th></tr></thead>
          <tbody>{rows}</tbody>
        </table></div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_perf:
        st.markdown("<div class='panel'><div class='panel-header'>📈 Performance Analysis</div>", unsafe_allow_html=True)
        an1, an2 = st.columns(2, gap="small")

        with an1:
            st.markdown("<p style='font-size:.72rem;color:#3A6090;text-align:center;padding:.5rem 0 0;'>Student Marks Distribution</p>", unsafe_allow_html=True)
            top5 = df.sort_values("Marks", ascending=False).head(5)
            fig_d = go.Figure(go.Bar(x=top5["ID"], y=top5["Marks"], marker_color="#3B8BFF", marker_line_width=0))
            fig_d.update_layout(**CHART_BG, height=185,
                xaxis=dict(tickfont=dict(color="#5A7890",size=9), showgrid=False),
                yaxis=dict(tickfont=dict(color="#5A7890",size=9), gridcolor="#0F1E32"), bargap=0.35)
            st.plotly_chart(fig_d, use_container_width=True, config={"displayModeBar":False})

        with an2:
            st.markdown("<p style='font-size:.72rem;color:#3A6090;text-align:center;padding:.5rem 0 0;'>Pass vs Fail</p>", unsafe_allow_html=True)
            p2 = int((df["Marks"] >= 50).sum()); f2 = int((df["Marks"] < 50).sum())
            pct_p2 = round(p2/len(df)*100) if len(df) else 0
            pct_f2 = round(f2/len(df)*100) if len(df) else 0
            fig_pf = go.Figure(go.Pie(
                labels=[f"Pass: {pct_p2}%", f"Fail: {pct_f2}%"], values=[p2, f2],
                marker_colors=["#2A7A50","#B03030"],
                textfont=dict(family="Syne",size=11,color="#fff"), showlegend=False,
            ))
            fig_pf.update_layout(**CHART_BG, height=185)
            st.plotly_chart(fig_pf, use_container_width=True, config={"displayModeBar":False})

        st.markdown("<div style='padding:0.2rem 1rem 0.8rem;'>", unsafe_allow_html=True)
        col_map = {"A":"#34D399","B":"#60A5FA","C":"#FBBF24","D":"#F87171"}
        grade_counts = df["Marks"].apply(grade).value_counts()
        for g_lbl in ["A","B","C","D"]:
            cnt = grade_counts.get(g_lbl, 0)
            pct = int(cnt / len(df) * 100) if len(df) else 0
            c   = col_map[g_lbl]
            st.markdown(f"""
            <div style='display:flex;align-items:center;gap:.5rem;margin:.3rem 0;font-size:.78rem;'>
              <span style='color:{c};font-family:Syne,sans-serif;font-weight:800;min-width:52px;'>Grade {g_lbl}</span>
              <div style='flex:1;background:#0A1525;border-radius:4px;height:5px;overflow:hidden;'>
                <div style='width:{pct}%;background:{c};height:100%;border-radius:4px;'></div>
              </div>
              <span style='color:#3A6090;min-width:18px;text-align:right;'>{cnt}</span>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
#  PAGE: ADD STUDENT
# ══════════════════════════════════════════════════════════
elif page == "➕  Add Student":
    st.markdown("<div class='content-pad'>", unsafe_allow_html=True)
    st.markdown("<p class='page-heading'>➕ Add Student</p>", unsafe_allow_html=True)

    col_f, col_p = st.columns([1, 1], gap="large")

    with col_f:
        st.markdown("<div class='panel'><div class='panel-header'>Student Details</div><div class='panel-body'>", unsafe_allow_html=True)
        a_name    = st.text_input("Full Name", placeholder="e.g. Ananya Krishnan", key="a_name")
        a_branch  = st.selectbox("Branch", ["CSE","ECE","IT","MECH","CIVIL","EEE"], key="a_branch")
        c1, c2 = st.columns(2)
        with c1: a_year = st.selectbox("Year", ["1st","2nd","3rd","4th"], key="a_year")
        with c2: a_subj = st.selectbox("Subject", ["Math","Science","DBMS","English","Physics","Chemistry"], key="a_subj")
        a_marks = st.slider("Marks (out of 100)", 0, 100, 65, key="a_marks")
        a_date  = st.date_input("Date", value=datetime.today(), key="a_date")

        if st.button("✦  Save Student Record", key="full_add"):
            if a_name.strip():
                st.session_state.students.append({
                    "ID": next_id(), "Name": a_name.strip(),
                    "Branch": a_branch, "Year": a_year,
                    "Subject": a_subj, "Marks": a_marks,
                    "Date": str(a_date)
                })
                st.success(f"✅ **{a_name}** added — {a_marks}/100 in {a_subj}")
                st.balloons()
            else:
                st.warning("Please enter a student name.")
        st.markdown("</div></div>", unsafe_allow_html=True)

    with col_p:
        st.markdown("<div class='panel'><div class='panel-header'>Live Preview</div>", unsafe_allow_html=True)
        marks_val = a_marks if 'a_marks' in dir() else 65
        g_lbl = grade(marks_val)
        g_col = {"A":"#34D399","B":"#60A5FA","C":"#FBBF24","D":"#F87171"}.get(g_lbl,"#888")
        pf_lbl = pass_fail(marks_val)

        fig_g = go.Figure(go.Indicator(
            mode="gauge+number", value=marks_val,
            number={"font":{"color":"#EDF2FF","family":"Syne","size":40}},
            gauge={
                "axis":{"range":[0,100],"tickcolor":"#2A4060","tickfont":{"color":"#2A4060","size":10}},
                "bar":{"color":"#3B8BFF"}, "bgcolor":"#0A1525", "bordercolor":"#162540",
                "steps":[
                    {"range":[0,50],"color":"#0D0A14"},{"range":[50,70],"color":"#0A1020"},
                    {"range":[70,85],"color":"#0A1828"},{"range":[85,100],"color":"#0A2030"},
                ],
            }
        ))
        fig_g.update_layout(**CHART_BG, height=230)
        st.plotly_chart(fig_g, use_container_width=True, config={"displayModeBar":False})
        st.markdown(f"""
        <div style='text-align:center;padding:.5rem 1rem 1.2rem;'>
          <span style='background:#0A1525;border:1px solid {g_col}40;border-radius:20px;
                       padding:4px 22px;font-family:Syne,sans-serif;font-size:1.2rem;
                       font-weight:800;color:{g_col};'>Grade {g_lbl}</span>
          <p style='margin:.6rem 0 0;font-size:.82rem;color:#3A6090;'>
            Status: <b style='color:{"#34D399" if pf_lbl=="Pass" else "#F87171"}'>{pf_lbl}</b>
          </p>
        </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
#  PAGE: ANALYTICS
# ══════════════════════════════════════════════════════════
elif page == "📊  Analytics":
    st.markdown("<div class='content-pad'>", unsafe_allow_html=True)
    st.markdown("<p class='page-heading'>📊 Analytics</p>", unsafe_allow_html=True)

    df = pd.DataFrame(st.session_state.students)
    if df.empty:
        st.info("No data yet. Add students first.")
    else:
        df["Grade"]  = df["Marks"].apply(grade)
        df["Status"] = df["Marks"].apply(pass_fail)

        c1, c2, c3 = st.columns(3, gap="medium")

        with c1:
            st.markdown("<div class='panel'><div class='panel-header'>🏫 Branch-wise Average</div>", unsafe_allow_html=True)
            b_avg = df.groupby("Branch")["Marks"].mean().round(1).reset_index()
            fig_b = px.bar(b_avg, x="Branch", y="Marks",
                           color="Marks", color_continuous_scale=["#0F2044","#3B8BFF","#60C0FF"], text="Marks")
            fig_b.update_traces(textposition="outside", textfont=dict(color="#8AAAD0",size=11))
            fig_b.update_layout(**CHART_BG, height=250, coloraxis_showscale=False,
                xaxis=dict(tickfont=dict(color="#5A7890",size=10),showgrid=False),
                yaxis=dict(tickfont=dict(color="#5A7890"),gridcolor="#0F1E32",range=[0,115]), bargap=0.4)
            st.plotly_chart(fig_b, use_container_width=True, config={"displayModeBar":False})
            st.markdown("</div>", unsafe_allow_html=True)

        with c2:
            st.markdown("<div class='panel'><div class='panel-header'>📅 Year-wise Trend</div>", unsafe_allow_html=True)
            y_avg = df.groupby("Year")["Marks"].mean().round(1).reset_index()
            fig_y = go.Figure(go.Scatter(
                x=y_avg["Year"], y=y_avg["Marks"],
                mode="lines+markers+text",
                line=dict(color="#3B8BFF", width=2),
                marker=dict(color="#3B8BFF", size=8),
                text=y_avg["Marks"], textposition="top center",
                textfont=dict(color="#8AAAD0",size=11),
                fill="tozeroy", fillcolor="rgba(59,139,255,0.08)"
            ))
            fig_y.update_layout(**CHART_BG, height=250,
                xaxis=dict(tickfont=dict(color="#5A7890"),showgrid=False),
                yaxis=dict(tickfont=dict(color="#5A7890"),gridcolor="#0F1E32",range=[0,115]))
            st.plotly_chart(fig_y, use_container_width=True, config={"displayModeBar":False})
            st.markdown("</div>", unsafe_allow_html=True)

        with c3:
            st.markdown("<div class='panel'><div class='panel-header'>🏅 Grade Distribution</div>", unsafe_allow_html=True)
            gc = df["Grade"].value_counts().reset_index(); gc.columns = ["Grade","Count"]
            fig_gd = go.Figure(go.Pie(
                labels=gc["Grade"], values=gc["Count"], hole=0.55,
                marker_colors=["#34D399","#60A5FA","#FBBF24","#F87171"],
                textfont=dict(family="Syne",size=12,color="#fff"),
            ))
            fig_gd.update_layout(**CHART_BG, height=250,
                legend=dict(font=dict(color="#5A7890",size=11),bgcolor="rgba(0,0,0,0)"))
            st.plotly_chart(fig_gd, use_container_width=True, config={"displayModeBar":False})
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='panel'><div class='panel-header'>📋 Full Student Records</div>", unsafe_allow_html=True)
        df_disp = df.sort_values("Marks", ascending=False).reset_index(drop=True)
        df_disp.index += 1
        st.dataframe(df_disp, use_container_width=True,
            column_config={
                "ID":      st.column_config.TextColumn("ID", width="small"),
                "Name":    st.column_config.TextColumn("Name"),
                "Branch":  st.column_config.TextColumn("Branch", width="small"),
                "Year":    st.column_config.TextColumn("Year", width="small"),
                "Subject": st.column_config.TextColumn("Subject"),
                "Marks":   st.column_config.ProgressColumn("Marks", min_value=0, max_value=100, format="%d"),
                "Grade":   st.column_config.TextColumn("Grade", width="small"),
                "Status":  st.column_config.TextColumn("Status", width="small"),
                "Date":    st.column_config.DateColumn("Date"),
            })
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
#  PAGE: REMOVE STUDENT
# ══════════════════════════════════════════════════════════
elif page == "🗑️  Remove Student":
    st.markdown("<div class='content-pad'>", unsafe_allow_html=True)
    st.markdown("<p class='page-heading'>🗑️ Remove Student</p>", unsafe_allow_html=True)

    df = pd.DataFrame(st.session_state.students)
    if df.empty:
        st.info("No student records found.")
    else:
        col_del, col_info = st.columns([1, 1.2], gap="large")
        with col_del:
            st.markdown("<div class='panel'><div class='panel-header'>Select Student</div><div class='panel-body'>", unsafe_allow_html=True)
            options  = [f"{s['ID']} — {s['Name']}" for s in st.session_state.students]
            chosen   = st.selectbox("Student", options, label_visibility="collapsed")
            chosen_id = chosen.split(" — ")[0]
            match = next((s for s in st.session_state.students if s["ID"] == chosen_id), None)
            st.markdown("</div></div>", unsafe_allow_html=True)
            if match:
                st.warning(f"⚠️ This will permanently delete **{match['Name']}'s** record.")
                if st.button("🗑️  Confirm Delete", key="del_btn"):
                    st.session_state.students = [s for s in st.session_state.students if s["ID"] != chosen_id]
                    st.success(f"✅ {match['Name']} removed.")
                    st.rerun()

        with col_info:
            if match:
                g_l  = grade(match["Marks"])
                g_c  = {"A":"#34D399","B":"#60A5FA","C":"#FBBF24","D":"#F87171"}.get(g_l,"#888")
                pf   = pass_fail(match["Marks"])
                st.markdown(f"""
                <div class='panel'>
                  <div class='panel-header'>Record Preview</div>
                  <div class='panel-body'>
                    <p style='font-family:Syne,sans-serif;font-size:1.3rem;font-weight:800;color:#EDF2FF;margin:0 0 .9rem;'>{match['Name']}</p>
                    <table style='width:100%;font-size:.86rem;border-collapse:collapse;'>
                      <tr><td style='color:#3A6090;padding:.22rem 0;width:90px;'>Student ID</td><td><span class='sid'>{match['ID']}</span></td></tr>
                      <tr><td style='color:#3A6090;padding:.22rem 0;'>Branch</td><td style='color:#C5D8F0;'>{match['Branch']}</td></tr>
                      <tr><td style='color:#3A6090;padding:.22rem 0;'>Year</td><td style='color:#C5D8F0;'>{match['Year']}</td></tr>
                      <tr><td style='color:#3A6090;padding:.22rem 0;'>Subject</td><td style='color:#C5D8F0;'>{match['Subject']}</td></tr>
                      <tr><td style='color:#3A6090;padding:.22rem 0;'>Marks</td><td style='color:#EDF2FF;font-weight:700;'>{match['Marks']}/100</td></tr>
                      <tr><td style='color:#3A6090;padding:.22rem 0;'>Grade</td><td><span style='color:{g_c};font-weight:800;font-family:Syne,sans-serif;'>Grade {g_l}</span></td></tr>
                      <tr><td style='color:#3A6090;padding:.22rem 0;'>Status</td><td><b style='color:{"#34D399" if pf=="Pass" else "#F87171"};'>{pf}</b></td></tr>
                      <tr><td style='color:#3A6090;padding:.22rem 0;'>Date</td><td style='color:#C5D8F0;'>{match['Date']}</td></tr>
                    </table>
                  </div>
                </div>""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ── FOOTER ──
st.markdown("""
<div style='text-align:center;padding:1.2rem 2rem;border-top:1px solid #0F1E32;margin-top:1rem;'>
  <p style='font-size:.72rem;color:#1A3050;font-family:DM Sans,sans-serif;'>
    🎓 Student Performance Analytics &nbsp;·&nbsp; Built with Streamlit &amp; Plotly &nbsp;·&nbsp; v2.0
  </p>
</div>
""", unsafe_allow_html=True)