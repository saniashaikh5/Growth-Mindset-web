import streamlit as st



#Header Section


st.subheader("Hi, I am Milo :wave:")
st.title("I am a cute Kitten :cat:")
st.write("I love to coding, I want to learn python")
st.write("You can know more about me")

# What I do

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write("""
     1. Atack Everything 🐾
     pouncing on my feet when i walk
    Attacking shoelaces, curtains, or even their own shadow.
    sneak-attacking from behind furniture like a tiny ninja!
    2. Climb here they Shouldn't
    scaling curtains like Spider-Kitten.😼
    3. I love Watching TV and other kitens like me
    I want to do something new i love to coding 👩‍💻
    I want to grow, and do things myself """)
        
    #interaction section

    st.markdown("## Show some love! :heart:")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("👍 Like"):
            st.write("Thank You for liking :heart:")
            with col2:
                if st.button("💬 Comment"):
                    st.write("Please leave a comment below :point_down:")
                    st.text_area("Comments")
                    with col3:
                        if st.button("🚀 Share"):
                            st.write("Share this page with your friends and family :point_down:")
                            with col4:
                                if st.button("🔔 Subscribe"):
                                    st.balloons()
                                    st.success("Subscribe successfully :tada:")
                                