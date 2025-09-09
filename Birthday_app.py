import streamlit as st

# Title of the app
st.title("🎂 Birthday Wisher App 🎉")

# Take input from the user
name = st.text_input("Enter your name:")

# Button to trigger birthday wish
if st.button("Wish Me"):
    if name.strip() != "":
        # Birthday message
        st.success(f"🎉 Happy Birthday, {name}! 🥳🎂🎁")
        
        # Balloons animation
        st.balloons()
        

        # Extra confetti effect with Markdown emojis
        st.markdown(
            """
            <h2 style="text-align:center; color:#ff4b4b;">
            🎊🎉🎈 Have an amazing day! 🎈🎉🎊
            </h2>
            """,
            unsafe_allow_html=True
        )

    else:
        st.warning("Please enter your name first 😊")