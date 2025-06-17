import streamlit as st
from resume_parser import extract_text_from_pdf
from jd_parser import extract_text_from_txt
from generator import generate_cover_letter
from resume_tailor import tailor_resume
import re
from pdf_utils import generate_cover_letter_pdf

st.set_page_config(page_title="AI Resume and Cover Letter Generator", layout="centered")

st.markdown("""
    <style>
    html, body, .stApp {
        background-image: linear-gradient(to right, #dbe9f4, #ffffff);
        background-attachment: fixed;
        color: #1f2937;  /* Text color: dark slate */
    }
    
    [data-baseweb="radio"] span {
        color: #1f2937 !important;
        font-weight: 600 !important;
    }

    .stTextInput > label, .stFileUploader > label, .stTextArea > label, .stMarkdown {
        color: #1f2937 !important;
    }

    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #111827 !important;
        font-size: 0.9rem;
        line-height: 1.5;
    }

    .stButton button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    
    .stSuccess success {
        background-color: #26d128;
    }
    
    div[data-testid="stDownloadButton"] > button {
        background-color: #2563eb !important;
        color: white !important;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        border: none;
        margin-top: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Smart Resume Assistant: AI Cover Letter + Tailoring Tips")
st.markdown("Upload your resume and job description. Get a tailored cover letter and resume improvement tips!")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_file = st.file_uploader("Upload Job Description (TXT)", type=["txt"])

if "cover_letter" not in st.session_state:
    st.session_state.cover_letter = None

if "resume_suggestions" not in st.session_state:
    st.session_state.resume_suggestions = None

if st.button("Generate"):
    if resume_file is None or jd_file is None:
        st.warning("Please upload both resume and job description.")
    else:
        with st.spinner("Reading Resume..."):
            resume_text = extract_text_from_pdf(resume_file)

        with st.spinner("Reading Job Description..."):
            jd_text = extract_text_from_txt(jd_file)

        with st.spinner("Generating Cover Letter..."):
            st.session_state.cover_letter = generate_cover_letter(resume_text, jd_text)

        with st.spinner("Analyzing Resume..."):
            st.session_state.resume_suggestions = tailor_resume(resume_text, jd_text)

if st.session_state.cover_letter and st.session_state.resume_suggestions:
    st.subheader("Tailored Cover Letter")
    st.markdown("**Choose how to view your cover letter:**", unsafe_allow_html=True)
    option = st.selectbox("", ["Download PDF", "View in App"])

    if option == "Download PDF":
        pdf_path = generate_cover_letter_pdf(st.session_state.cover_letter)
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="Download Cover Letter (PDF)",
                data=f,
                file_name="cover_letter.pdf",
                mime="application/pdf"
            )

    elif option == "View in App":
        st.text_area("Your Cover Letter", value=st.session_state.cover_letter, height=300)

    st.subheader("Resume Tailoring Suggestions")

    points = re.split(r"\s*(?:[•\-]|\d\.)\s*", st.session_state.resume_suggestions.strip())
    points = [p.strip() for p in points if p.strip()]
    formatted = "\n\n".join([f"• {p}" for p in points])
    st.markdown(formatted)

    st.markdown("""
        <div style="background-color:#34d399; padding:10px; border-radius:8px; color:#000; font-weight:500;">
            ✅ Done!
        </div>
    """, unsafe_allow_html=True)