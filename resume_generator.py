import streamlit as st

def main():
    st.title("Resume Generator")

    # Personal Information
    name = st.text_input("Enter your name")
    job_title = st.text_input("Enter your job title")
    email = st.text_input("Enter your email")
    phone = st.text_input("Enter your phone number")

    # Skills Section
    skills = st.text_area("Enter your skills (comma-separated)")

    # Experience Section
    experience = st.text_area("Describe your work experience")

    # Resume Generation Button
    if st.button("Generate Resume"):
        if name and job_title:
            st.subheader("Your Resume")
            st.write(f"**Name:** {name.strip()}")
            st.write(f"**Job Title:** {job_title.strip()}")
            st.write(f"**Email:** {email.strip()}")
            st.write(f"**Phone:** {phone.strip()}")
            
            if skills:
                skill_list = [skill.strip() for skill in skills.split(",")]
                st.write("**Skills:**")
                st.write(", ".join(skill_list))
            
            if experience:
                st.write("**Experience:**")
                st.write(experience.strip())
        else:
            st.warning("Please enter both your name and job title to generate your resume.")

if __name__ == "__main__":
    main()
