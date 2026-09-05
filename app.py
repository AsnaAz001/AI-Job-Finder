import streamlit as st
from job_finder.crew import JobFinder


st.set_page_config(
    page_title="AI Job Finder",
    page_icon="💼",
    layout="wide"
)


st.title("💼 AI Engineer Job Finder")

st.write(
    "Find current AI Engineer and Generative AI Engineer "
    "jobs in Pakistan and remote opportunities."
)

st.divider()


user_request = st.text_area(
    "🔎 What do you want to research?",
    value=(
        "Find current AI Engineer and Generative AI Engineer "
        "jobs in Pakistan and remote jobs. Also tell me the "
        "skills required for these jobs."
    ),
    height=120
)


if st.button(
    "🚀 Find AI Jobs",
    type="primary",
    use_container_width=True
):

    if not user_request.strip():
        st.warning("Please enter a research request.")

    else:

        with st.spinner(
            "🔍 Researching AI jobs and required skills..."
        ):

            try:
                inputs = {
                    "user_request": user_request
                }

                result = JobFinder().crew().kickoff(
                    inputs=inputs
                )

                st.success("✅ Search completed successfully!")

                st.divider()

                st.subheader("📋 AI Job Finder Results")

                st.markdown(str(result))

            except Exception:
                st.error(
                    "❌ The AI job search failed. "
                    "Please click 'Find AI Jobs' again."
                )