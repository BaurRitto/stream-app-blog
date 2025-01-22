import streamlit as st

# Set page configuration
st.set_page_config(page_title="Portfolio Blog", page_icon="📚", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Portfolio", "Blog", "About", "Contact"])

# Home Page
if page == "Home":
    st.title("Welcome to My Portfolio Blog")
    # st.image("assets/home_banner.jpg", use_column_width=True)
    st.write("""
    Hi! I'm Bauyrzhan, a data enthusiast passionate about AI, data engineering, and creating impactful projects.
    Use the navigation menu to explore my portfolio, blog, and contact me.
    """)

# Portfolio Page
elif page == "Portfolio":
    st.title("Portfolio")
    st.write("Here are some of my recent projects:")
    project_data = [
        {"title": "Project 1", "description": "A cool project about X.", "link": "#"},
        {"title": "Project 2", "description": "Another project focusing on Y.", "link": "#"},
    ]
    for project in project_data:
        st.subheader(project["title"])
        st.write(project["description"])
        st.markdown(f"[Learn more]({project['link']})")

# Blog Page
elif page == "Blog":
    st.title("Blog")
    st.write("Welcome to my blog! Check out my latest posts:")
    blog_posts = [
        {"title": "Blog Post 1", "excerpt": "An introduction to AI.", "link": "#"},
        {"title": "Blog Post 2", "excerpt": "Understanding data engineering.", "link": "#"},
    ]
    for post in blog_posts:
        st.subheader(post["title"])
        st.write(post["excerpt"])
        st.markdown(f"[Read more]({post['link']})")

# About Page
elif page == "About":
    st.title("About Me")
    st.write("""
    I'm [Your Name], a data professional with expertise in AI, data engineering, and web development. 
    My mission is to solve real-world problems with data and technology.
    """)

# Contact Page
elif page == "Contact":
    st.title("Contact Me")
    st.write("Feel free to reach out via the form below:")
    contact_form = """
    <form action="https://formsubmit.co/your-email@example.com" method="POST">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
