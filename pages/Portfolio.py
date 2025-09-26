import streamlit as st
import info as info
import pandas as pd

#Title
st.set_page_config(page_title="Amy Ho - Portfolio", page_icon="🌟", layout="wide")

# About Me Section
def about_me_section():
    st.header("🌟 About Me")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(info.profile_picture, width=250)
    with col2:
        st.write(info.about_me)
        st.write("**Threads:** Media & Design")
        st.write("**Year:** 2nd Year")
        st.write("**Interests:** Digital Storytelling, UX Design, Creative Media, Interactive Experiences")
    st.write('---')

about_me_section()

# Sidebar Links
def links_section():
    st.sidebar.header("Connect With Me!")
    st.sidebar.text("Professional Network")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width="75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)

    st.sidebar.text("My Projects")
    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="GitHub" width="65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    
    st.sidebar.text("Get In Touch")
    email_html = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt="Email" width="75" height="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)

links_section()

# Education Section
def education_section(education_data, course_data):
    st.header("📚 Education")
    st.subheader(f'**{education_data["Institution"]}**')
    st.write(f'**Degree:** {education_data["Degree"]}')
    st.write(f'**Location:** {education_data["Location"]}')
    st.write(f'**Graduation Date:** {education_data["Graduation Date"]}')
    st.write(f'**GPA:** {education_data["GPA"]}')
    
    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Names", 
        "semester_taken": "Semester Taken",
        "skills": "Skills Learned"
    }, hide_index=True)
    st.write("---")

education_section(info.education_data, info.course_data)

# Professional Experience Section
def experience_section(experience_data):
    st.header("💼 Professional Experience")
    for job_title, job_description in experience_data.items():
        expander = st.expander(f"{job_title}")
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")

experience_section(info.experience_data)

# Projects Section
def project_section(projects_data):
    st.header("🛠️ Projects & Creative Work")
    for project_name, project_description in projects_data.items():
        expander = st.expander(f"{project_name}")
        expander.write(project_description)
    st.write("---")

project_section(info.projects_data)

# Skills Section
def skills_section(programming_data, spoken_data):
    st.header("👩‍💻 Skills & Proficiencies")
    
    st.subheader("Technical & Creative Skills")
    for skill, percentage in programming_data.items():
        st.write(f"{skill} {info.programming_icons.get(skill, '')}")
        st.progress(percentage / 100)
    
    st.subheader("Languages")
    for language, proficiency in spoken_data.items():
        st.write(f"{language} {info.spoken_icons.get(language, '')}: {proficiency}")
    
    st.write("---")

skills_section(info.programming_data, info.spoken_data)

# Activities Section
def activities_section(leadership_data, activity_data):
    st.header("🎭 Activities & Leadership")
    
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])
    
    with tab1:
        st.subheader("Leadership Roles")
        for title, details in leadership_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
    
    with tab2:
        st.subheader("Community Service")
        for title, details in activity_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
    
    st.write("---")

activities_section(info.leadership_data, info.activity_data)

# Footer
st.write("### Thanks for visiting my portfolio!")
st.write("Feel free to reach out through any of the links in the sidebar.")
