import streamlit as st
from app.resume_utils import extract_text_from_pdf
from app.jd_utils import read_job_description, match_resume_to_jd
import os

st.set_page_config(page_title="Resume Matcher", page_icon="🧠", layout="centered")

with st.sidebar:
    st.title("🧠 Resume Matcher")
    st.markdown("Compare your resume to a job description using NLP + ML.")
    st.markdown("---")
    st.markdown("Made with ❤️ by Ali")
    st.markdown("[GitHub](https://github.com/Aliharis007)")


st.title("📄 Resume vs JD Matcher")
st.markdown("Upload your **resume** and **job description**, and see how well they match using semantic similarity!")


resume_file = st.file_uploader("📎 Upload Resume (PDF)", type=["pdf"])
jd_file = st.file_uploader("📎 Upload Job Description (TXT)", type=["txt"])


if st.button("🔍 Match Resume to Job Description"):
    if resume_file and jd_file:
        with st.spinner("Processing files..."):

            
            resume_path = os.path.join("temp_resume.pdf")
            jd_path = os.path.join("temp_jd.txt")

            with open(resume_path, "wb") as f:
                f.write(resume_file.read())

            with open(jd_path, "wb") as f:
                f.write(jd_file.read())

            
            resume_text = extract_text_from_pdf(resume_path)
            jd_text = read_job_description(jd_path)

            similarity_score = match_resume_to_jd(resume_text, jd_text)

        st.success("✅ Matching Complete!")
        st.markdown("### 📊 Similarity Score")
        st.metric(label="Match Percentage", value=f"{similarity_score:.2f} %")

        if similarity_score > 70:
            st.success("🟢 Great Match! Your resume aligns well with the JD.")
        elif similarity_score > 40:
            st.warning("🟡 Decent Match. Consider tailoring your resume more.")
        else:
            st.error("🔴 Low Match. Customize your resume to better fit the JD.")

    else:
        st.error("🚫 Please upload both the resume PDF and JD text file.")
