import streamlit as st
import random

# Page configuration
st.set_page_config(page_title="Creative Career Quiz", page_icon="🎨")

# Title and description
st.title("🎨 What Creative Career Path Matches Your Personality?")
st.write("Discover which creative career aligns best with your skills, interests, and personality traits!")

# NEW: st.metric - shows quiz statistics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Questions", "5")
with col2:
    st.metric("Career Matches", "4")
with col3:
    st.metric("Fun Level", "100%")

st.write("---")

# Initialize session state for results
if 'score' not in st.session_state:
    st.session_state.score = {'UX Designer': 0, 'Content Strategist': 0, 'Digital Storyteller': 0, 'Media Producer': 0}

# Question 1: Radio button
st.header("1. What's your favorite part of the creative process?")
q1 = st.radio(
    "Choose the option that excites you most:",
    [
        "Researching user needs and solving problems",
        "Planning and organizing content structure", 
        "Crafting compelling narratives and stories",
        "Producing and editing visual/audio content"
    ],
    key="q1"
)

# NEW: st.image - display relevant image
st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400", caption="The creative process", width=400)

# Question 2: Selectbox
st.header("2. Which tool do you enjoy working with most?")
q2 = st.selectbox(
    "Select your preferred creative tool:",
    [
        "Figma or prototyping software",
        "Content management systems", 
        "Writing and storytelling platforms",
        "Video/audio editing software"
    ],
    key="q2"
)
st.image("https://images.unsplash.com/photo-1558655146-9f40138edfeb?ixlib=rb-4.0.3&w=400", 
         caption="Creative tools and technologies", 
         width=250)

# Question 3: Multiselect
st.header("3. What skills do you naturally excel at?")
q3 = st.multiselect(
    "Select all that apply:",
    [
        "User research and empathy",
        "Strategic planning and organization",
        "Creative writing and storytelling",
        "Visual design and multimedia production",
        "Technical problem-solving",
        "Collaboration and communication"
    ],
    key="q3"
)
st.image("https://images.unsplash.com/photo-1639762681485-074b7f938ba0?ixlib=rb-4.0.3&w=400", 
         caption="Your unique skill constellation", 
         width=300)

# Question 4
# NEW: st.slider - for preference level
st.header("4. How important is technical vs. creative work to you?")
st.write("1 = Mostly creative, 10 = Balanced mix of both")
q4 = st.slider(
    "Slide to indicate your preference:",
    1, 10, 5,
    key="q4"
)
st.image("https://images.unsplash.com/photo-1635070041078-e363dbe005cb?ixlib=rb-4.0.3&w=400", 
         caption="Finding your balance between technical and creative", 
         width=300)

# Question 5: Number input
st.header("5. How many collaborative projects do you enjoy per semester?")
q5 = st.number_input(
    "Enter your ideal number of team projects:",
    min_value=1,
    max_value=10,
    value=3,
    key="q5"
)
st.image("https://images.unsplash.com/photo-1521737852567-6949f3f9f2b5?ixlib=rb-4.0.3&w=350", 
         caption="The power of collaboration and connection", 
         width=350)

#Result
# NEW: st.progress - show quiz completion
st.write("### Quiz Progress")
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)

# Calculate results button
if st.button("✨ Discover Your Creative Career Path!"):
    # Reset scores
    st.session_state.score = {'UX Designer': 0, 'Content Strategist': 0, 'Digital Storyteller': 0, 'Media Producer': 0}
    
    # Score question 1
    if q1 == "Researching user needs and solving problems":
        st.session_state.score['UX Designer'] += 3
    elif q1 == "Planning and organizing content structure":
        st.session_state.score['Content Strategist'] += 3
    elif q1 == "Crafting compelling narratives and stories":
        st.session_state.score['Digital Storyteller'] += 3
    else:
        st.session_state.score['Media Producer'] += 3
    
    # Score question 2
    if q2 == "Figma or prototyping software":
        st.session_state.score['UX Designer'] += 2
    elif q2 == "Content management systems":
        st.session_state.score['Content Strategist'] += 2
    elif q2 == "Writing and storytelling platforms":
        st.session_state.score['Digital Storyteller'] += 2
    else:
        st.session_state.score['Media Producer'] += 2
    
    # Score question 3 (multiselect - can score multiple)
    for choice in q3:
        if choice in ["User research and empathy", "Technical problem-solving"]:
            st.session_state.score['UX Designer'] += 1
        elif choice in ["Strategic planning and organization", "Collaboration and communication"]:
            st.session_state.score['Content Strategist'] += 1
        elif choice == "Creative writing and storytelling":
            st.session_state.score['Digital Storyteller'] += 1
        elif choice == "Visual design and multimedia production":
            st.session_state.score['Media Producer'] += 1
    
    # Score question 4 (slider)
    if q4 <= 3:
        st.session_state.score['Digital Storyteller'] += 2  # More creative
        st.session_state.score['Media Producer'] += 2
    elif q4 >= 7:
        st.session_state.score['UX Designer'] += 2  # More technical
        st.session_state.score['Content Strategist'] += 1
    
    # Score question 5 (number input)
    if q5 >= 5:
        st.session_state.score['Content Strategist'] += 2  # Likes collaboration
        st.session_state.score['UX Designer'] += 1
    else:
        st.session_state.score['Digital Storyteller'] += 1  # Prefers independent work
    
    # NEW: st.balloons() - celebration effect
    st.balloons()
    
    # Determine result
    result_career = max(st.session_state.score, key=st.session_state.score.get)
    max_score = st.session_state.score[result_career]
    
    # Display result
    st.write("---")
    st.header(f"🎯 Your Creative Career Match: {result_career}!")
    
    # Result descriptions with images
    results = {
        'UX Designer': {
            'description': """
            **You're a UX Designer!** 🎨
            - You thrive on understanding user needs and creating intuitive experiences
            - Your strengths include empathy, problem-solving, and technical thinking
            - Perfect for someone who loves both creativity and structure
            - Common roles: UX Researcher, UI Designer, Product Designer
            """,
            'image': 'https://images.unsplash.com/photo-1551650975-87deedd944c3?w=400'
        },
        'Content Strategist': {
            'description': """
            **You're a Content Strategist!** 📊
            - You excel at organizing information and planning content ecosystems
            - Your strengths include strategic thinking, organization, and communication
            - Perfect for someone who loves making complex information accessible
            - Common roles: Content Manager, Information Architect, Digital Strategist
            """,
            'image': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400'
        },
        'Digital Storyteller': {
            'description': """
            **You're a Digital Storyteller!** ✍️
            - You have a natural talent for crafting compelling narratives across media
            - Your strengths include creativity, writing, and emotional intelligence
            - Perfect for someone who loves connecting with audiences through stories
            - Common roles: Content Writer, Narrative Designer, Digital Journalist
            """,
            'image': 'https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?w=400'
        },
        'Media Producer': {
            'description': """
            **You're a Media Producer!** 🎬
            - You shine in creating and editing visual/audio content that captivates
            - Your strengths include technical skills, creativity, and attention to detail
            - Perfect for someone who loves bringing ideas to life through multimedia
            - Common roles: Video Producer, Multimedia Specialist, Creative Director
            """,
            'image': 'https://images.unsplash.com/photo-1579389083078-4e7018379f7e?w=400'
        }
    }
    
    result_info = results[result_career]
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(result_info['image'], width=250)
    with col2:
        st.write(result_info['description'])
    
    # Show detailed scores
    st.subheader("📊 Your Detailed Scores:")
    for career, score in st.session_state.score.items():
        st.write(f"**{career}**: {score}/12 points")
        st.progress(score / 12)
    
    # Career advice
    st.write("---")
    st.subheader("💡 Next Steps for Your Career Path:")
    st.write("""
    1. **Take relevant courses** in your LMC Media & Design threads
    2. **Build a portfolio** with projects that showcase these skills
    3. **Seek internships** in your identified area of interest
    4. **Connect with professionals** in your target industry
    """)
    
    # Share result
    st.write("---")
    st.write("### 📣 Share your result!")
    st.code(f"My creative career match is {result_career}! Take the quiz to find yours.")

# Footer
st.write("---")
st.write("*Created for CS 1301 - Web Development Lab 01*")
