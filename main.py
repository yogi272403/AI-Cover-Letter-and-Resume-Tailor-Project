from resume_parser import extract_text_from_pdf
from jd_parser import extract_text_from_txt
from generator import generate_cover_letter
from resume_tailor import tailor_resume

resume_path = input("Enter path to your resume PDF:")
jd_path = input("Enter path to your JD:")

resume_text = extract_text_from_pdf(resume_path)
jd_text = extract_text_from_txt(jd_path)

cover_letter = generate_cover_letter(resume_text, jd_text)

with open("cover_letter.txt", "w", encoding='utf-8') as f:
    f.write(cover_letter)

print("\nGenerated Cover Letter saved to 'cover_letter.txt'")

tailored_resume = tailor_resume(resume_text, jd_text)

print("\n --- Resume Tailoring Suggestions --- \n")
print(tailored_resume)