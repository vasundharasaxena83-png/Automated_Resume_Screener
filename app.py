import streamlit as st
import requests
import pandas as pd
import altair as alt

API = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 📍 ADD THE POP-SLIDE FUNCTION HERE (RIGHT AFTER CONFIG)
# =========================================================
@st.dialog("🚀 Welcome to AI Resume Analyzer!", width="large")
def show_welcome_slides():
    if "slide_num" not in st.session_state:
        st.session_state["slide_num"] = 1

    if st.session_state["slide_num"] == 1:
        st.markdown("### 📄 Optimize Your Application in Seconds")
        st.write("Welcome! Our platform uses intelligent parsing algorithms to match your current resume directly against competitive corporate job specifications.")
        st.info("💡 **Did you know?** Over 75% of resumes are filtered out by automatic tracking systems before an actual human recruiter looks at them.")

    elif st.session_state["slide_num"] == 2:
        st.markdown("### 📊 What You Can Do")
        st.write("1. **Instant ATS Scoring:** Get an immediate percentage score based on structural matching.")
        st.write("2. **Keyword Extraction:** Instantly find high-impact technical terms missing from your file.")
        st.write("3. **FAANG Templates:** Access clean markdown structures designed to pass strict high-volume filters.")

    elif st.session_state["slide_num"] == 3:
        st.markdown("### 🎯 Ready to land your dream role?")
        st.write("Create a quick account or log into your dashboard to save analysis histories and view personal recommendation trends.")
        st.success("✨ **Free Tier Activated:** Enjoy unlimited resume scoring runs!")

    st.write("---")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.session_state["slide_num"] > 1:
            if st.button("⬅️ Back"):
                st.session_state["slide_num"] -= 1
                st.rerun()
                
    with col2:
        if st.session_state["slide_num"] < 3:
            if st.button("Next ➡️"):
                st.session_state["slide_num"] += 1
                st.rerun()
        else:
            if st.button("🏁 Get Started"):
                st.session_state["welcome_seen"] = True
                st.rerun()


# =========================================================
# 📍 INITIALIZE SESSION STATES & AUTO-TRIGGER DIALOG
# =========================================================
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Signup"

if "welcome_seen" not in st.session_state:
    st.session_state["welcome_seen"] = False

# This triggers the popup immediately if the user hasn't seen it yet
if not st.session_state["welcome_seen"]:
    show_welcome_slides()


# 🌊 BLUE PREMIUM UI THEME
st.markdown("""
<style>
... Your custom CSS code stays here ...
</style>
""", unsafe_allow_html=True)

# ... The rest of your app navigation, login, signup, and dashboard code continues below ...
# 🌊 BLUE PREMIUM UI THEME
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #0a192f, #112240, #0f3460);
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a192f, #0f3460);
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 10px;
    padding: 0.5rem 1rem;
    border: none;
    font-weight: 600;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 15px #00c6ff;
}

/* Cards */
.card {
    background: rgba(255, 255, 255, 0.05);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid rgba(0, 198, 255, 0.2);
    box-shadow: 0 0 20px rgba(0, 114, 255, 0.1);
}

/* Titles */
h1, h2, h3 {
    color: #64ffda;
}

/* Metric box */
[data-testid="stMetric"] {
    background: rgba(0, 114, 255, 0.1);
    border-radius: 12px;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

# 🚀 HEADER
st.title("🚀 AI Resume Platform")
st.caption(" AI Powered Resume Intelligence System")

# 1️⃣ SAFE INITIALIZATION: Setup current page explicitly before layout components run
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Signup"

# 2️⃣ SIDEBAR NAVIGATION USING NATIVE STATE CALLBACKS
menu_options = ["Signup", "Login", "Dashboard"]

def on_nav_change():
    st.session_state["current_page"] = st.session_state["nav_radio"]

menu = st.sidebar.radio(
    "Navigation", 
    menu_options, 
    index=menu_options.index(st.session_state["current_page"]),
    key="nav_radio",
    on_change=on_nav_change
)

# ---------------- SIGNUP ----------------
if st.session_state["current_page"] == "Signup":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Create Account")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Signup"):
        res = requests.post(f"{API}/signup", params={
            "username": username,
            "password": password
        })
        st.success("Account Created Successfully 🚀")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- LOGIN ----------------
if st.session_state["current_page"] == "Login":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        res = requests.post(f"{API}/login", params={
            "username": username,
            "password": password
        })

        data = res.json()

        if "user_id" in data:
            st.session_state["user_id"] = data["user_id"]
            st.success("Login Successful 🚀")
        else:
            st.error("Invalid Credentials")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- DASHBOARD ----------------
if st.session_state["current_page"] == "Dashboard":
    if "user_id" not in st.session_state:
        st.warning("Please login first")
        st.stop()

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📊 Resume Analyzer Dashboard")
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        resume = st.file_uploader("📄 Upload Resume", type=["pdf", "docx", "txt"])
    with col2:
        jd = st.text_area("📌 Paste Job Description")

    if st.button("🚀 Analyze Resume"):
        if resume and jd:
            files = {"file": resume}
            data = {"user_id": st.session_state["user_id"], "jd_text": jd}
            res = requests.post(f"{API}/analyze", files=files, data=data)
            result = res.json()

            # Result Section Card
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            
            # Create side-by-side columns: text metric on left, beautiful pie chart on right
            metric_col, chart_col = st.columns([1, 1])
            
            score = result['ats_score']
            gap = round(100 - score, 2)
            
            with metric_col:
                st.metric("🔥 ATS SCORE", f"{score}/100")
                st.subheader("🤖 AI Feedback")
                st.write(result["ai_feedback"])
                
            with chart_col:
                import pandas as pd
                import altair as alt
                
                # 1. Pull the lists from your backend result safely
                detected_list = result.get("detected_skills", [])
                missing_list = result.get("suggested_skills", [])
                
                # Clean up names for display (e.g., "Python, SQL, FastAPI" or "None")
                detected_names = ", ".join(detected_list)[:30] + "..." if len(", ".join(detected_list)) > 30 else ", ".join(detected_list) if detected_list else "None"
                missing_names = ", ".join(missing_list)[:30] + "..." if len(", ".join(missing_list)) > 30 else ", ".join(missing_list) if missing_list else "None"
                
                # FALLBACK: If backend doesn't provide detected_skills, deduce from ATS score
                if not detected_list and missing_list:
                    score = result.get("ats_score", 0)
                    detected_pct = float(score)
                    missing_pct = round(100.0 - detected_pct, 1)
                    
                    detected_count = len(missing_list) if detected_pct == 0 else int((len(missing_list) * detected_pct) / missing_pct) if missing_pct > 0 else 10
                    missing_count = len(missing_list)
                    
                    label_detected = f"Detected ({detected_pct}%)"
                    label_missing = f"Missing: {missing_names} ({missing_pct}%)"
                else:
                    detected_count = len(detected_list)
                    missing_count = len(missing_list)
                    total_skills = detected_count + missing_count
                    
                    if total_skills > 0:
                        detected_pct = round((detected_count / total_skills) * 100, 1)
                        missing_pct = round((missing_count / total_skills) * 100, 1)
                    else:
                        detected_pct, missing_pct = 0.0, 0.0
                        
                    label_detected = f"Detected: {detected_names} ({detected_pct}%)"
                    label_missing = f"Missing: {missing_names} ({missing_pct}%)"

                # 2. Setup dataframe with the highly descriptive skill-name labels
                chart_data = pd.DataFrame({
                    "Skill Status": [label_detected, label_missing],
                    "Count": [detected_count, missing_count]
                })
                
                # 3. Render the donut chart
                skills_chart = alt.Chart(chart_data).mark_arc(innerRadius=50, stroke="#0a192f").encode(
                    theta=alt.Theta(field="Count", type="quantitative"),
                    color=alt.Color(
                        field="Skill Status", 
                        type="nominal",
                        scale=alt.Scale(
                            domain=[label_detected, label_missing], 
                            range=["#00c6ff", "rgba(255, 75, 75, 0.4)"]
                        ),
                        legend=alt.Legend(title=None, labelColor="white")
                    ),
                    tooltip=["Skill Status", "Count"]
                ).properties(
                    width=200,
                    height=200
                ).configure_view(
                    strokeWidth=0
                )
                
                st.altair_chart(skills_chart, use_container_width=True)

            st.markdown("</div>", unsafe_allow_html=True)

            # Industry-Level Recommendations Card
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("💡 Industry-Level Recommendations")

            st.markdown("##### 🎯 Missing High-Impact Keywords & Tools:")
            tags_html = "".join([f"<span style='background-color:rgba(0, 198, 255, 0.15); color:#64ffda; padding: 6px 12px; border-radius: 8px; margin-right: 8px; display:inline-block; margin-bottom:8px; border: 1px solid rgba(0, 198, 255, 0.4); font-weight:600;'>{skill}</span>" for skill in result["suggested_skills"]])
            st.markdown(tags_html, unsafe_allow_html=True)

            st.write("") # Spacer
            st.markdown("##### 🛠️ Roadmap to Strengthen your Resume:")
            st.write("1. **Contextual Integration:** Weave the custom-highlighted skills tags into your technical proficiency matrix.")
            st.write("2. **Action-Oriented Framing:** Start experience items with hard-hitting professional action verbs like *Architected, Accelerated, or Spearheaded* instead of passive statements.")
            st.write("3. **Tailored Formatting:** Place your newly added skills near the upper half of your document page to guarantee quick scanner retention.")
            st.markdown("</div>", unsafe_allow_html=True)

            # Industry-Grade Content Blueprint
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("📋 Industry-Grade Resume Checklist")
            st.markdown("Ensure your uploaded file checks off these structural standards used by top tech professionals:")

            st.checkbox("🔗 **Contact info includes professional links:** Contains clean professional email, portfolio site, GitHub, or LinkedIn profile.", value=False)
            st.checkbox("🎯 **Impact-Driven Summary:** Replaced standard objectives with a 3-4 sentence hook stating tech stacks and data metrics.", value=False)
            st.checkbox("📊 **Logical Skills Matrix:** Skills are split into neat, scannable subsets (e.g., Languages, Frameworks, Developer Tools).", value=False)
            st.checkbox("🚀 **Google X-Y-Z Formula Bulletpoints:** Every role begins with an action verb and includes quantifiable metrics (e.g., *'Optimized database queries, reducing API latency by 40%'*).", value=False)
            st.checkbox("🛠️ **Strategic Projects:** Features independent/SaaS developments detailed exactly like corporate job entries.", value=False)
            st.markdown("</div>", unsafe_allow_html=True)

            # Top-Tier Company Resume Template
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("🌟 Premium FAANG/Top-Tier Company Template")
            st.markdown("Copy this markdown structural template to build a layout optimized for high-volume corporate ATS scanners:")

            sample_template = """# FIRSTNAME LASTNAME
[Email](mailto:you@email.com) | [LinkedIn](https://linkedin.com/in/username) | [GitHub](https://github.com/username) | [Portfolio](https://yourportfolio.com) | City, State

## PROFESSIONAL SUMMARY
Results-driven [Your Title] with [X] years of experience specializing in [Core Domain/SaaS]. Proven track record of architecting [Frameworks/Systems] and delivering high-performance solutions. Adept at leveraging data-backed optimizations to improve efficiency by [X]% and support business scaling.

## TECHNICAL SKILLS
*   **Languages:** Python, SQL, JavaScript, HTML/CSS
*   **Frameworks & Libraries:** FastAPI, Streamlit, Scikit-Learn, SQLAlchemy, Flask
*   **Tools & Cloud Infrastructure:** Git, AWS (S3, EC2), Docker, PostgreSQL, MySQL

## PROFESSIONAL EXPERIENCE
**Company Name** | *Software Engineer* | City, State (or Remote) | Month Year – Present
*   Architected and deployed a [System/SaaS Tool] using [Tech Stack], reducing database API response latency by **40%** for **2,000+** active users.
*   Spearheaded the automation of [Process/Workflow], saving engineering teams **15+ hours** of manual labor per week.
*   Collaborated in an Agile team of [X] to ship features matching strict industry security configurations.

**Previous Company** | *Junior Developer* | City, State | Month Year – Month Year
*   Optimized backend relational database queries using [SQL Variant], increasing platform data processing throughput by **25%**.
*   Built and maintained over [X] clean, well-tested RESTful end-points consumed by production client UI interfaces.

## PROJECTS
**AI Resume SaaS Platform** | *Python, FastAPI, Streamlit, Scikit-Learn* | [GitHub Link]
*   Engineered a full-stack automated parsing engine analyzing unstructured text vectors via TF-IDF algorithms and cosine similarities.
*   Designed a programmatic frontend state management wrapper to automatically transition users across registration pipelines.
"""
            st.code(sample_template, language="markdown")
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("Please upload a file and enter a job description.")

    if st.button("📂 View History"):
        res = requests.get(f"{API}/history/{st.session_state['user_id']}")
        history = res.json()

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📜 Resume History")
        for item in history:
            st.write("📄", item["filename"])
            st.write("ATS:", item["ats_score"])
            st.write("---")
        st.markdown("</div>", unsafe_allow_html=True)