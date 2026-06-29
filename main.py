from fastapi import FastAPI, UploadFile, File, Form, HTTPException, status
from fastapi import Form, UploadFile, File
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("🔥 MAIN.PY IS SUCCESSFULLY INITIALIZED 🔥")

app = FastAPI()

# 🗄️ Fake In-Memory Database for Users (For testing)
USERS_DB = {}

# ========================================================
# 🎯 NEW MULTI-BRANCH SKILL DATABASE & LOGIC
# ========================================================
JOB_ROLES = {
    "Data Analyst": ["python", "sql", "excel", "power bi", "pandas", "tableau"],
    "ML Engineer": ["python", "machine learning", "tensorflow", "pytorch", "scikit-learn"],
    "Web Developer": ["html", "css", "javascript", "react", "node", "django"],
    "Core Engineering": ["autocad", "solidworks", "ansys", "matlab", "thermodynamics"],
    "IoT / Embedded": ["c", "c++", "arduino", "raspberry pi", "embedded systems"]
}

def calculate_ats_score(resume_text, target_role):
    resume_text = resume_text.lower()
    
    # Auto-detection logic if they select "Auto Detect (All Branches)"
    if target_role == "Auto Detect (All Branches)":
        scores = {}
        for role, skills in JOB_ROLES.items():
            matched = [s for s in skills if s in resume_text]
            scores[role] = len(matched)
        # Choose the role with the maximum overlapping keywords, fallback to Data Analyst
        target_role = max(scores, key=scores.get) if any(scores.values()) else "Data Analyst"

    required_skills = JOB_ROLES[target_role]
    matched_skills = [skill for skill in required_skills if skill in resume_text]
    missing_skills = list(set(required_skills) - set(matched_skills))
    
    # Calculate skill-based score
    score = (len(matched_skills) / len(required_skills)) * 100 if required_skills else 0
    return round(score, 2), matched_skills, missing_skills, target_role

# ---------------- ROOT ----------------
@app.get("/")
def home():
    return {"message": "AI Resume Running 🚀"}

# ---------------- SIGNUP ENDPOINT ----------------
@app.post("/signup")
def signup(username: str, password: str):
    if not username or not password:
        raise HTTPException(status_code=400, detail="Username and password cannot be empty")
    
    if username in USERS_DB:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    USERS_DB[username] = {
        "id": len(USERS_DB) + 1,
        "password": password  
    }
    return {"message": "Account Created Successfully"}

# ---------------- LOGIN ENDPOINT ----------------
@app.post("/login")
def login(username: str, password: str):
    user = USERS_DB.get(username)
    if not user or user["password"] != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials"
        )
    return {"user_id": user["id"]}

# ---------------- TEXT EXTRACT ----------------
def extract_text(file: UploadFile):
    file.file.seek(0)
    if file.filename.endswith(".pdf"):
        with pdfplumber.open(file.file) as pdf:
            return "".join([p.extract_text() or "" for p in pdf.pages])
    elif file.filename.endswith(".txt"):
        return file.file.read().decode("utf-8")
    else:
        try:
            return file.file.read().decode("utf-8")
        except Exception:
            return ""

# ---------------- UPDATE ANALYZE ENDPOINT ----------------
@app.post("/analyze")
async def analyze(file: UploadFile = File(...), job_role: str = Form(...), user_id: str = Form(...)):
    # 1. Extract raw text from the uploaded resume
    resume_text = extract_text(file)
    
    # 2. Run your new branch-agnostic skill-based parsing function
    score, matched_skills, missing_skills, final_role = calculate_ats_score(resume_text, job_role)

    # 3. Dynamic Roadmap & Feedback Mapping according to structural depth
    if score > 70:
        feedback = f"Excellent alignment! Your resume strongly matches industry expectations for a {final_role}. To make it bulletproof, ensure you quantify your impact with metrics."
        roadmap = [
            "🏆 **Quantify Engineering Metrics:** Focus on changing passive phrasing to impact-driven metrics (e.g., *'Optimized database queries, reducing latency by 40%'*).",
            "🚀 **System Design & Scale:** Shift project descriptions from basic CRUD tasks to system architecture, concurrency, and caching architectures.",
            "🎯 **Tailor for Top-Tier (FAANG):** Fine-tune your vocabulary to mirror advanced project lifecycles expected in competitive roles."
        ]
    elif score > 40:
        feedback = f"Moderate match for a {final_role}. Your profile has the foundation, but you must directly integrate missing technical skills highlighted below to pass standard filters."
        roadmap = [
            "🛠️ **Bridge Key Tool Gaps:** Create or update a targeted micro-project incorporating the missing core frameworks found in this scan.",
            "📚 **Build a Structural Skills Matrix:** Categorize your technical list cleanly into subsections (e.g., Languages, Frameworks, Core Tools) for parsing accuracy.",
            "🔗 **Expand Portfolio Evidence:** Ensure every project listed has a functional GitHub repository link attached directly to its title."
        ]
    else:
        feedback = f"Weak match for a {final_role}. Your resume requires a substantial overhaul to pass enterprise ATS filtering. Focus on gaining the core missing keywords."
        roadmap = [
            "🏗️ **Rebuild from Foundations:** Completely restructure your core document layout using the optimized templates provided in your dashboard below.",
            "🎯 **Target Foundational Tools:** Master at least 2 highly requested keywords from your gap profile before sending out fresh applications.",
            "✍️ **Eliminate Generic Objectives:** Drop vague career overview lines and swap them out for a clean summary describing active tech stacks."
        ]

   # 4. Calculate dynamic selection probability metrics for company tiers
    mnc_probabilities = {
        "MAANG / Top Product Firms": min(100, max(5, int(score * 1.1) - 20 if score > 50 else int(score * 0.3))),
        "Fast-Growing Startups": min(100, max(10, int(score * 1.05) + 5 if score > 40 else int(score * 0.6))),
        "Global Tier-2 MNCs": min(100, max(15, int(score * 1.2) if score > 30 else 30))
    }

    return {
        "ats_score": score,
        "detected_role": final_role,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "ai_feedback": feedback,
        "dynamic_roadmap": roadmap,
        "mnc_probabilities": mnc_probabilities,  # <-- Double check this exact key name
        "match_level": "High" if score > 70 else "Medium" if score > 40 else "Low"
    }

# ---------------- HISTORY ENDPOINT ----------------
@app.get("/history/{user_id}")
def get_history(user_id: int):
    return [
        {"filename": "sample_resume.pdf", "ats_score": 75.5},
        {"filename": "old_resume.txt", "ats_score": 42.0}
    ]