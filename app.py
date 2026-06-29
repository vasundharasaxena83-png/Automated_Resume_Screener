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
# 📍 POP-SLIDE FUNCTION (RIGHT AFTER CONFIG)
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

if not st.session_state["welcome_seen"]:
    show_welcome_slides()


# =========================================================
# 🌊 BLUE PREMIUM CYBER-LIGHTNING UI THEME
# =========================================================
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
    width: 100%;
}

.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0px 0px 20px #00c6ff, 0px 0px 40px rgba(0, 198, 255, 0.5);
    color: white;
}

/* Cards with Bluish Lightning Glow effect */
.card {
    background: rgba(10, 25, 47, 0.7);
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #00c6ff;
    box-shadow: 0 0 15px rgba(0, 198, 255, 0.4), inset 0 0 10px rgba(0, 114, 255, 0.2);
    margin-bottom: 25px;
    transition: all 0.3s ease-in-out;
}

.card:hover {
    border-color: #64ffda;
    box-shadow: 0 0 25px rgba(100, 255, 218, 0.6), inset 0 0 15px rgba(0, 198, 255, 0.3);
}

/* Titles */
h1, h2, h3, h4, h5 {
    color: #64ffda !important;
    text-shadow: 0 0 10px rgba(100, 255, 218, 0.3);
}

/* Metric box */
[data-testid="stMetric"] {
    background: rgba(0, 114, 255, 0.15);
    border-radius: 12px;
    padding: 15px;
    border: 1px solid #00c6ff;
    box-shadow: 0 0 10px rgba(0, 198, 255, 0.3);
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# 🛠️ SIDEBAR NAVIGATION USING NATIVE CALLBACKS
# =========================================================
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

st.sidebar.markdown("---")
st.sidebar.info("🚀 **Multi-Branch Engine Mode:** Activated to review CS, IT, ECE, Mechanical, and Civil profiles.")


# =========================================================
# 🚀 PAGE ROUTING LOGIC
# =========================================================

# ---------------- SIGNUP ----------------
if st.session_state["current_page"] == "Signup":
    st.title("🚀 AI Resume Platform")
    st.caption("AI Powered Resume Intelligence System")
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Create Account")

    username = st.text_input("Username", key="reg_user")
    password = st.text_input("Password", type="password", key="reg_pass")

    if st.button("Signup"):
        try:
            res = requests.post(f"{API}/signup", params={"username": username, "password": password})
            st.success("Account Created Successfully! Proceed to Login. 🚀")
        except Exception:
            st.error("Could not connect to the backend API server.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- LOGIN ----------------
elif st.session_state["current_page"] == "Login":
    st.title("🚀 AI Resume Platform")
    st.caption("AI Powered Resume Intelligence System")
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Login")

    username = st.text_input("Username", key="log_user")
    password = st.text_input("Password", type="password", key="log_pass")

    if st.button("Login"):
        try:
            res = requests.post(f"{API}/login", params={"username": username, "password": password})
            data = res.json()

            if "user_id" in data:
                st.session_state["user_id"] = data["user_id"]
                st.session_state["current_page"] = "Dashboard"
                st.rerun()
            else:
                st.error("Invalid Credentials")
        except Exception:
            st.error("Could not connect to the backend API server.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- DASHBOARD (AUTHENTICATED ONLY) ----------------
elif st.session_state["current_page"] == "Dashboard":
    if "user_id" not in st.session_state:
        st.warning("⚠️ Access Denied. Please login first.")
        st.stop()

    st.title("📊 Multi-Branch Resume Intelligence")
    st.caption("Automated processing dashboard for cross-domain engineering evaluation")

    # Layout Split: Main input panels
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Target Pipeline Configurations")
        
        job_roles = [
            "Auto Detect (All Branches)",
            "Data Analyst",
            "ML Engineer",
            "Web Developer",
            "Core Engineering",
            "IoT / Embedded"
        ]
        selected_role = st.selectbox("🎯 Target Domain Mapping", job_roles)
        resume = st.file_uploader("📄 Upload Candidate Document", type=["pdf", "txt"])
        
        analyze_btn = st.button("🚀 Run ATS Analysis Engine")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("💡 Evaluation Tips")
        st.write("• **Branch Agnostic:** Setting target to *Auto Detect* bypasses degree titles and maps skills automatically against our multi-branch taxonomy matrix.")
        st.write("• **File Optimization:** Ensure structural plain-text blocks or selectable PDF components are preserved.")
        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- RUN EVALUATION & DISPLAY ANALYSIS ----------------
    if analyze_btn:
        if resume:
            with st.spinner("Parsing resume dataset structures..."):
                files = {"file": (resume.name, resume.getvalue(), "application/pdf")}
                data = {"job_role": selected_role, "user_id": str(st.session_state["user_id"])}
                
                try:
                    res = requests.post(f"{API}/analyze", files=files, data=data)
                    result = res.json()

                    # Result Section Card
                    st.markdown("<div class='card'>", unsafe_allow_html=True)
                    
                    metric_col, chart_col = st.columns([1, 1])
                    score = result.get('ats_score', 0)
                    
                    with metric_col:
                        st.metric("🔥 ATS MATCH RATING", f"{score}%")
                        st.subheader("🤖 System Diagnosis Insights")
                        st.write(result.get("ai_feedback", "No feedback compiled."))
                        
                    with chart_col:
                        # Skill List Extraction
                        detected_list = result.get("matched_skills", [])
                        missing_list = result.get("missing_skills", [])
                        
                        detected_names = ", ".join(detected_list)[:30] + "..." if len(", ".join(detected_list)) > 30 else ", ".join(detected_list) if detected_list else "None"
                        missing_names = ", ".join(missing_list)[:30] + "..." if len(", ".join(missing_list)) > 30 else ", ".join(missing_list) if missing_list else "None"
                        
                        detected_count = len(detected_list) if detected_list else 1
                        missing_count = len(missing_list) if missing_list else 1
                        
                        label_detected = f"Found: {detected_names}"
                        label_missing = f"Gaps: {missing_names}"

                        chart_data = pd.DataFrame({
                            "Skill Status": [label_detected, label_missing],
                            "Count": [detected_count, missing_count]
                        })
                        
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
                        ).properties(width=200, height=200).configure_view(strokeWidth=0)
                        
                        st.altair_chart(skills_chart, use_container_width=True)

                    st.markdown("</div>", unsafe_allow_html=True)

                    # 📈 MNC SELECTION PROBABILITY GRAPH
                    st.markdown("<div class='card'>", unsafe_allow_html=True)
                    st.subheader("📊 Target Company Selection Probability")
                    st.caption("Estimated placement likelihood based on resume structural depth and keyword matching metrics.")
                    
                    # Fetching data safely with concrete fallbacks if the key doesn't load
                    prob_data = result.get("mnc_probabilities")
                    if not prob_data or not isinstance(prob_data, dict):
                        prob_data = {
                            "MAANG / Top Product Firms": 20,
                            "Fast-Growing Startups": 45,
                            "Global Tier-2 MNCs": 40
                        }
                    
                    prob_df = pd.DataFrame({
                        "Company Tier": list(prob_data.keys()),
                        "Probability (%)": [float(v) for v in prob_data.values()]
                    })
                    
                    prob_chart = (
                        alt.Chart(prob_df)
                        .mark_bar(cornerRadiusTopRight=8, cornerRadiusBottomRight=8)
                        .encode(
                            x=alt.X("Probability (%):Q", scale=alt.Scale(domain=[0, 100])),
                            y=alt.Y("Company Tier:N", sort="-x", axis=alt.Axis(labelAngle=0, labelColor="white")),
                            color=alt.Color(
                                "Probability (%):Q", 
                                scale=alt.Scale(scheme="blues"), 
                                legend=None
                            ),
                            tooltip=["Company Tier", "Probability (%)"]
                        )
                        .properties(height=180)
                        .configure_view(strokeWidth=0)
                    )
                    
                    st.altair_chart(prob_chart, use_container_width=True)
                    st.markdown("</div>", unsafe_allow_html=True)

                    # Dynamic Tool Gaps & Strength-Based Roadmap
                    st.markdown("<div class='card'>", unsafe_allow_html=True)
                    st.subheader("💡 Industry-Level Recommendations")

                    st.markdown("##### 🎯 Identified High-Impact Keyword Gaps:")
                    if result.get("missing_skills"):
                        tags_html = "".join([f"<span style='background-color:rgba(255,75,75,0.1); color:#ff4b4b; padding: 6px 12px; border-radius: 8px; margin-right: 8px; display:inline-block; margin-bottom:8px; border: 1px solid rgba(255,75,75,0.3); font-weight:600;'>{skill}</span>" for skill in result["missing_skills"]])
                        st.markdown(tags_html, unsafe_allow_html=True)
                    else:
                        st.success("No missing foundational keywords detected for this target track pipeline!")

                    st.write("") 
                    st.markdown("##### 🛠️ Custom Roadmap (Tailored to Your Resume Strength):")
                    
                    custom_roadmap = result.get("dynamic_roadmap", [
                        "1. Update technical matrices.",
                        "2. Integrate missing structural keywords."
                    ])
                    for step in custom_roadmap:
                        st.write(step)
                        
                    st.markdown("</div>", unsafe_allow_html=True)

                except Exception as e:
                    st.error("🚨 Frontend-Backend Communication Failure!")
                    st.exception(e)  # Handles displaying the clear python traceback
        else:
            st.warning("Please upload a file before executing engine scan.")

    # ---------------- VIEW HISTORY ACCORDION ----------------
    if st.button("📂 View Historic Scoring Indices"):
        try:
            res = requests.get(f"{API}/history/{st.session_state['user_id']}")
            history = res.json()

            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("Run Logs & History Tracker")
            for item in history:
                st.write(f"📄 **File:** {item['filename']} | **ATS Score Match:** {item['ats_score']}%")
                st.write("---")
            st.markdown("</div>", unsafe_allow_html=True)
        except Exception:
            st.error("Could not fetch user scoring history logs.")

    # ---------------- MANDATORY STRUCTURE ASSURANCE ----------------
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📋 Industry-Grade Structure Compliance Assurance")
    st.checkbox("🔗 **Contact info includes professional links:** Contains clean professional email, portfolio site, GitHub, or LinkedIn profile.", value=False)
    st.checkbox("🎯 **Impact-Driven Summary:** Replaced standard objectives with a 3-4 sentence hook stating tech stacks and data metrics.", value=False)
    st.checkbox("📊 **Logical Skills Matrix:** Skills are split into neat, scannable subsets (e.g., Languages, Frameworks, Developer Tools).", value=False)
    st.checkbox("🚀 **Google X-Y-Z Formula Bulletpoints:** Every role begins with an action verb and includes quantifiable metrics (e.g., *'Optimized database queries, reducing API latency by 40%'*).", value=False)
    st.checkbox("🛠️ **Strategic Projects:** Features independent/SaaS developments detailed exactly like corporate job entries.", value=False)
    st.markdown("</div>", unsafe_allow_html=True)


    # =========================================================
    # 🌟 MULTI-BRANCH PREMIUM ATS BULLETPROOF TEMPLATE BLUEPRINTS
    # =========================================================
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🌟 Multi-Branch Optimized ATS Templates")
    st.markdown("Select your specialized branch track below to populate a high-volume tracking compliance layout framework:")
    
    template_track = st.selectbox("📋 Choose Template Architecture", ["CS / IT (Software Engineering)", "ECE / EEE (Hardware, IoT, Embedded)", "Mech / Civil (Core Infrastructure & Design)"])
    
    if "CS / IT" in template_track:
        sample_template = """# FIRSTNAME LASTNAME
[Email](mailto:you@email.com) | [LinkedIn](https://linkedin.com/in/username) | [GitHub](https://github.com/username) | City, State

## PROFESSIONAL SUMMARY
Results-driven Software Engineer with specialization in building high-throughput web architectures and scalable pipeline platforms. Experienced with Agile software delivery lifecycles and modern technical framework configurations.

## TECHNICAL SKILLS
*   **Languages:** Python, SQL, JavaScript, HTML/CSS
*   **Frameworks & Libraries:** FastAPI, React, Node.js, Streamlit, Django
*   **Tools & Cloud Infrastructure:** Git, Docker, PostgreSQl, AWS (S3, EC2)

## PROFESSIONAL EXPERIENCE
**Tech Solutions Inc.** | *Software Engineer Intern* | Month Year – Present
*   Architected and deployed a microservice parsing utility using **FastAPI**, reducing structural asset indexing latency by **40%**.
*   Optimized backend relational query logic, recovering **15+ engineering hours** of batch cycle processes weekly.

## PROJECTS
**Automated Resume Screener SaaS** | *Python, Streamlit, Scikit-Learn*
*   Engineered a text processing parsing app calculating target alignment index metrics across unstructured text vectors via specialized keyword matching algorithms.
"""
    elif "ECE" in template_track:
        sample_template = """# FIRSTNAME LASTNAME
[Email](mailto:you@email.com) | [LinkedIn](https://linkedin.com/in/username) | [GitHub](https://github.com/username) | City, State

## PROFESSIONAL SUMMARY
Detail-oriented Electronics and Communications Engineer focused on prototyping embedded hardware setups, IoT networks, and real-time controller micro-architectures.

## TECHNICAL SKILLS
*   **Hardware & Embedded:** Embedded C, C++, Arduino IDE, ARM Cortex, Raspberry Pi
*   **Protocols & Tools:** SPI, I2C, UART, MATLAB, Keil uVision, Proteus
*   **Core Systems:** PCB Design, Signal Processing, Digital Systems Circuit Design

## PROFESSIONAL EXPERIENCE
**Robotics Infrastructure Lab** | *Embedded Engineering Trainee* | Month Year – Present
*   Programmed firmware controllers across **ARM Cortex-M4** targets executing automated peripheral tasks, minimizing sensor polling cycles by **25%**.
*   Assembled functional custom telemetry sensor arrays transmitting packet arrays securely via **MQTT / I2C** connection links.

## PROJECTS
**Autonomous Smart Grids & Telemetry Nodes** | *Embedded C, FreeRTOS, ESP32*
*   Designed an independent distributed power network monitoring rig using RTOS scheduling routines to track multi-node circuit loads cleanly.
"""
    else:
        sample_template = """# FIRSTNAME LASTNAME
[Email](mailto:you@email.com) | [LinkedIn](https://linkedin.com/in/username) | City, State

## PROFESSIONAL SUMMARY
Analytical Systems Engineer specializing in finite element modeling analysis, structural design engineering pipelines, and rigorous industrial workflow optimization protocols.

## TECHNICAL SKILLS
*   **CAD / CAE Software:** AutoCAD, SolidWorks, ANSYS Mechanical, CATIA
*   **Analysis Domains:** FEA, Computational Fluid Dynamics (CFD), Thermodynamics, HVAC
*   **Core Engineering:** Geometric Dimensioning & Tolerancing (GD&T), Materials Strength

## PROFESSIONAL EXPERIENCE
**Heavy Structural Dynamics Corp** | *Design Engineer Trainee* | Month Year – Present
*   Conducted high-fidelity static structural **FEA simulations inside ANSYS**, reducing prototype structural physical weight indices by **18%**.
*   Drafted compliant part configurations tracking strict international layout standards, expediting physical component sourcing velocities by **12 days**.

## PROJECTS
**High-Pressure Thermo Valve Simulation Assembly** | *SolidWorks, ANSYS Workbench*
*   Modeled stress tolerance limitations over structural thermal stress assemblies checking variable load tolerances across localized pressure changes.
"""

    st.code(sample_template, language="markdown")
    st.markdown("</div>", unsafe_allow_html=True)