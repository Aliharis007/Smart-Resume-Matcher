from fpdf import FPDF

class ResumePDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "AYAN QURESHI", ln=True, align="C")
        self.set_font("Arial", "", 12)
        self.cell(0, 10, "Python Developer | NLP, Machine Learning & Data Science", ln=True, align="C")
        self.set_font("Arial", "", 10)
        self.cell(0, 8, "Karachi, Pakistan | ayan.qureshi.dev@example.com | +92-300-1234567", ln=True, align="C")
        self.cell(0, 8, "GitHub: github.com/ayanqureshi | LinkedIn: linkedin.com/in/ayanqureshi", ln=True, align="C")
        self.ln(4)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(50, 50, 50)
        self.cell(0, 10, title, ln=True)
        self.set_text_color(0, 0, 0)
        self.set_font("Arial", "", 11)

    def section_body(self, text):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 7, text)
        self.ln(2)

# Create instance
pdf = ResumePDF()
pdf.add_page()

# Sections
pdf.section_title("PROFESSIONAL SUMMARY")
pdf.section_body("Python developer with a strong background in Natural Language Processing, Machine Learning, and scalable API development. Adept at using transformers, handling large datasets, and deploying AI-driven services.")

pdf.section_title("TECHNICAL SKILLS")
pdf.section_body("""\
- Languages: Python, SQL, Bash
- Libraries: Transformers, Scikit-learn, Pandas, NumPy, TensorFlow, PyTorch
- Tools: FastAPI, Git, Docker, Jupyter, Postman, VS Code
- Cloud/DB: Google Colab, MySQL, Firebase, AWS (Basics)
""")

pdf.section_title("PROJECTS")
pdf.section_body("""\
💼 Resume Matcher using Transformers
- Built a semantic resume matching system using Sentence-BERT and FAISS vector store.
- Implemented query handling via FastAPI; handled both PDF and plain text inputs.
- GitHub: github.com/ayanqureshi/resume-matcher

🧠 Chat with PDF using LangChain
- Used LangChain + Groq API + FAISS to allow semantic querying over PDFs.
- Embedded PDF content using HuggingFace Transformers and answered questions via LLM.
- GitHub: github.com/ayanqureshi/langchain-playground
""")

pdf.section_title("EDUCATION")
pdf.section_body("""\
BS in Computer Science
National University of Computer and Emerging Sciences (FAST), Karachi
Expected Graduation: June 2026
""")

pdf.section_title("ADDITIONAL HIGHLIGHTS")
pdf.section_body("""\
- Experience with Hugging Face Transformers and open-source NLP models
- Proficient in building RESTful APIs with FastAPI
- Familiar with prompt engineering and RAG pipelines
- Regularly contribute to GitHub with AI + backend projects
""")

# Output PDF
pdf.output("AyanQureshi_Python_Resume.pdf")
