import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from app.resume_utils import extract_text_from_pdf
from app.jd_utils import read_job_description


load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")

model=SentenceTransformer('all-MiniLM-L6-v2')

resume_text=extract_text_from_pdf("Sample_Resume.pdf")
jd_text=read_job_description("sample_jd.txt")

resume_embedding = model.encode([resume_text])[0]
jd_embedding = model.encode([jd_text])[0]

score = cosine_similarity([resume_embedding], [jd_embedding])[0][0] * 100

print(f"\nResume Match Score: {score:.2f}%")


llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama3-8b-8192"
)

prompt = f"Here is a resume:\n\n{resume_text}\n\nAnd here is a job description:\n\n{jd_text}\n\nPlease analyze and give short feedback if the resume is a good fit."
response = llm.invoke([HumanMessage(content=prompt)])
print("\nAI Feedback:\n", response.content)
