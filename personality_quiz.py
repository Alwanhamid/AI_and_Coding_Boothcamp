import streamlit as st

st.title("Personality Type Quiz: Introvert, Extrovert, or Ambivert?")
st.write("Answer the following questions to find out your personality type!")

# Questions and options
def quiz():
    st.header("1. Energy Source")
    energy = st.radio(
        "How do you usually recharge your energy?",
        (
            "I feel recharged after alone time or quiet activities.",
            "I gain energy from social interactions and external stimulation.",
            "It depends on my mood or context; both solitude and social time can energize me."
        )
    )

    st.header("2. Social Preference")
    social = st.radio(
        "Which social setting do you prefer?",
        (
            "I prefer small groups or one-on-one connections.",
            "I enjoy large gatherings and meeting new people.",
            "I'm comfortable in both intimate and social settings; I adapt to the situation."
        )
    )

    st.header("3. Communication Style")
    communication = st.radio(
        "How do you usually communicate?",
        (
            "I think before speaking and prefer written communication.",
            "I speak easily and think out loud; verbal processing is common.",
            "I switch between reflective and expressive communication styles as needed."
        )
    )

    if st.button("Get My Personality Type"):
        # Scoring
        introvert = sum([
            energy == "I feel recharged after alone time or quiet activities.",
            social == "I prefer small groups or one-on-one connections.",
            communication == "I think before speaking and prefer written communication."
        ])
        extrovert = sum([
            energy == "I gain energy from social interactions and external stimulation.",
            social == "I enjoy large gatherings and meeting new people.",
            communication == "I speak easily and think out loud; verbal processing is common."
        ])
        ambivert = sum([
            energy == "It depends on my mood or context; both solitude and social time can energize me.",
            social == "I'm comfortable in both intimate and social settings; I adapt to the situation.",
            communication == "I switch between reflective and expressive communication styles as needed."
        ])

        # Determine result
        if max(introvert, extrovert, ambivert) == introvert:
            st.success("You are most likely an **Introvert**! 🧠")
        elif max(introvert, extrovert, ambivert) == extrovert:
            st.success("You are most likely an **Extrovert**! 🗣️")
        else:
            st.success("You are most likely an **Ambivert**! 🧍‍♀️")

quiz()
