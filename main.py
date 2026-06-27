from fastapi import FastAPI, UploadFile, File, Form, HTTPException, status
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("🔥 MAIN.PY IS SUCCESSFULLY INITIALIZED 🔥")

app = FastAPI()

# 🗄️ Fake In-Memory Database for Users (For testing)
# In production, you'd use SQLAlchemy and a real database file
USERS_DB = {}

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
    
    # Save the user (In-memory)
    USERS_DB[username] = {
        "id": len(USERS_DB) + 1,
        "password": password  # In production, hash this using passlib!
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

# ---------------- ATS SCORE ----------------
def get_score(resume, jd):
    if not resume.strip() or not jd.strip():
        return 0.0
    tfidf = TfidfVectorizer().fit_transform([resume, jd])
    score = cosine_similarity(tfidf[0], tfidf[1])[0][0]
    return round(score * 100, 2)

# ---------------- ANALYZE ENDPOINT ----------------
@app.post("/analyze")
def analyze(file: UploadFile = File(...), jd_text: str = Form(...)):
    resume_text = extract_text(file)
    score = get_score(resume_text, jd_text)

    # 🧠 Dynamic Keyword Gap Analysis
    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())
    
    # Filter filler words
    stop_words = {"and", "the", "with", "that", "this", "from", "your", "have", "will", "shall", "should", "for", "are", "our", "their", "using"}
    
    # Clean and filter unique high-impact matching words missing from the resume
    missing_keywords = []
    for word in jd_words:
        clean_word = word.strip(",.():\"'-/*•")
        if clean_word not in resume_words and clean_word not in stop_words and len(clean_word) > 3:
            if clean_word not in missing_keywords:
                missing_keywords.append(clean_word)
    
    suggested_skills = missing_keywords[:6] if missing_keywords else ["None detected"]

    # Industry-level feedback mapping
    if score > 70:
        feedback = "Excellent alignment! Your resume strongly matches industry expectations for this role. To make it bulletproof, ensure you quantify your impact with specific data metrics (e.g., 'Improved conversion by 15%')."
    elif score > 40:
        feedback = "Moderate match. Your profile has the foundation, but to reach a premium industry-grade standard, you must directly integrate missing technical skills and functional terms highlighted below."
    else:
        feedback = "Weak match. Your resume requires a substantial overhaul to pass enterprise ATS filtering. Tailor your professional summary and experience bullet points to echo the core phrasing of the target role."

    return {
        "ats_score": score,
        "match_level": "High" if score > 70 else "Medium" if score > 40 else "Low",
        "resume_length": len(resume_text),
        "ai_feedback": feedback,
        "suggested_skills": suggested_skills
    }

# ---------------- HISTORY ENDPOINT ----------------
@app.get("/history/{user_id}")
def get_history(user_id: int):
    return [
        {"filename": "sample_resume.pdf", "ats_score": 75.5},
        {"filename": "old_resume.txt", "ats_score": 42.0}
    ]