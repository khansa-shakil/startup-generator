import streamlit as st
from groq import Groq

st.set_page_config(page_title="Startup Generator", page_icon="💡")

st.title("💡 Startup Idea Generator")
st.write("Describe a problem, theme, or idea to get your startup plan.")

problem = st.text_area(
    "What problem do you want to solve?",
    placeholder="Example: Reducing food waste in restaurants"
)

if st.button("Generate Startup Plan"):
    if problem.strip():

        client = Groq(api_key=st.secrets["GROQ_API_KEY"])

        with st.spinner("Creating your startup plan..."):
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "system",
                        "content": """
                        You are a startup advisor.
                        Create a practical startup plan in Markdown.
                        Include:
                        1. Startup Name
                        2. Problem
                        3. Solution
                        4. Target Customers
                        5. Unique Selling Point
                        6. Revenue Model
                        7. Marketing Strategy
                        8. Estimated Startup Costs
                        9. Launch Roadmap
                        Keep the plan clear and beginner-friendly.
                        """
                    },
                    {
                        "role": "user",
                        "content": problem
                    }
                ],
                temperature=0.7
            )

        st.markdown(response.choices[0].message.content)

    else:
        st.warning("Please enter a problem or idea first.")

st.markdown("---")
st.caption("Developed by Khansa Shakeel | National Incubation Center")