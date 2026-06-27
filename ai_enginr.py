def generate_feedback(resume, jd, score):
    return f"""
🔍 AI RESUME ANALYSIS REPORT

📊 ATS SCORE: {score}/100

✔ Strengths:
- Resume contains relevant technical keywords
- Partial alignment with job description

❌ Weaknesses:
- Lacks measurable achievements (numbers, impact missing)
- Projects not detailed enough
- Missing key JD skills

📈 Suggestions:
- Add quantified results (e.g., improved performance by 30%)
- Improve project descriptions with real impact
- Match JD keywords more closely

🎯 Final Verdict:
{"Strong Match" if score > 70 else "Needs Improvement"}
"""