import streamlit as st

# Title of App
st.title("Web Development Lab01")

# Assignment Data 
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Web Development - Section 1")
st.subheader("Amy Ho")


# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Page Name**: Description
#       2. **Page Name**: Description
#       3. **Page Name**: Description
#       4. **Page Name**: Description

st.write("""
Welcome to my Streamlit Web Development Lab01 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. **Home Page**: You're here! This is the main landing page that provides an overview 
   of the entire application and helps you navigate to other sections.


2. **Portfolio**: This page contains my personal portfolio, including information about 
   my background, skills, projects, and contact information. It serves as a digital resume 
   showcasing my experience in web development and programming.

3. **Quiz App**: An interactive BuzzFeed-style quiz that I created for Phase II of this lab. 
   The quiz features multiple question types and provides personalized results based on user input.

""")

st.divider()
st.write("### About This Lab")
st.write("""
This application was created as part of CS 1301 - Intro to Computing to demonstrate 
web development skills using Streamlit. The lab focuses on creating multi-page applications 
and interactive web elements using Python.
""")
st.info("💡 **Tip**: Use the sidebar on the left to navigate between pages!")
