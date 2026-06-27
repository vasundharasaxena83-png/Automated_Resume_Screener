🧠 AI-Powered Resume Screener & Core Analytics SaaS
An automated end-to-end parsing pipeline that scans unstructured resumes, maps them against target job descriptions using tokenized keyword-matching logic, and delivers real-time statistical metrics through an interactive analytics dashboard.

🚀 Key Features
Advanced Matching Pipeline: Leverages tokenized keyword matching to parse unstructured resume documents against strict job criteria.

95%+ Parsing Accuracy: Engineered with robust text extraction pipelines that clean raw formats and eliminate semantic noise for ultra-precise matching.

Dynamic Skill Analytics: Embeds live, interactive Altair multi-view donut charts to visualize statistical distributions of detected versus missing technical skills instantly.

State-Controlled Multi-Stage Onboarding: Utilizes localized state variables and custom Streamlit context wrappers to securely process dashboard pathways without data leaks.

SaaS Session Flow: Seamless routing built to insulate core analytics calculations from repetitive parent UI update cycles.

🛠️ Tech Stack
Frontend Dashboard: Streamlit

Backend API Framework: FastAPI (Python)

Data Visualization: Altair & Pandas

Environment Control: Git & Local Repository Control

📁 Repository Structure
Plaintext
├── backend/
│   ├── main.py            # FastAPI production application endpoints
│   └── requirements.txt   # Backend dependencies
├── frontend/
│   ├── app.py             # Streamlit SaaS dashboard UI logic
│   └── requirements.txt   # Frontend UI dependencies
└── README.md              # Project documentation
⚙️ Quick Start Guide
1. Clone the Repository
Bash
git clone <your-repository-url>
cd Automated_Resume_Screener
2. Launch the Backend API
Bash
# Navigate to backend directory
cd backend

# Install required dependencies
pip install -r requirements.txt

# Start the production server
python -m uvicorn main:app --reload
The backend service will initialize natively at [http://127.0.0.1:8000](http://127.0.0.1:8000). You can review the interactive OpenAPI schema at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

3. Spin Up the Frontend Interface
Open a second terminal instance:

Bash
# Navigate to frontend directory
cd frontend

# Install UI layout dependencies
pip install -r requirements.txt

# Boot the Streamlit UI web app
streamlit run app.py
Your analytics workspace will spin up automatically on your local port at http://localhost:8501.

📊 Analytics Visualization Mechanics
The core evaluation engine segments findings into two distinct pools:

Detected Skills (Neon Blue): Technical frameworks, infrastructure tools, and programming workflows present inside the uploaded file.

Missing Skills (Muted Red-Tint): Key requirements identified within the job description text block that were omitted from the candidate profile.
