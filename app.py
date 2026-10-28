import streamlit as st
from PIL import Image
from datetime import date

st.set_page_config(
page_title="Construction Intelligence",
page_icon="🏗️",
layout="wide"
)

st.title("🏗️ Multimodal Construction Intelligence Platform")
st.caption("AI-powered Construction Safety and Real Estate Decision Support")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
"Select Module",
[
"Dashboard",
"PPE Safety Audit",
"Crack Assessment",
"Construction Cost Estimator",
"Property Valuation",
"Weather Advisory",
"AI Construction Assistant"
]
)

if page == "Dashboard":
    st.header("Construction Intelligence Dashboard")
    st.write("Welcome to your construction intelligence platform.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Available Modules", "6")
    col2.metric("Platform Status", "Prototype")
    col3.metric("Date", date.today().strftime("%d %b %Y"))

    st.subheader("Platform Features")
    st.markdown("""
    - Construction site safety monitoring
    - Concrete crack image assessment
    - Construction cost estimation
    """)
elif page == "PPE Safety Audit":
    st.header("PPE Safety Audit")
    st.write("Upload a construction site image.")


file = st.file_uploader(
    "Choose site image",
    type=["jpg", "jpeg", "png"],
    key="ppe"
)

if file is not None:
    image = Image.open(file).convert("RGB")
    st.image(image, caption="Uploaded Site Image", use_container_width=True)
    st.info("Image uploaded. Connect a computer-vision model for actual PPE detection.")


elif page == "Crack Assessment":
    st.header("Concrete Crack Assessment")


file = st.file_uploader(
    "Upload concrete image",
    type=["jpg", "jpeg", "png"],
    key="crack"
)

if file is not None:
    image = Image.open(file).convert("RGB")
    st.image(image, caption="Concrete Image", use_container_width=True)
    st.info("Image uploaded. An AI vision model is required for automatic crack detection.")


elif page == "Construction Cost Estimator":
    st.header("Construction Cost Estimator")


area = st.number_input("Construction area (sq. ft.)", min_value=1.0, value=1000.0)
rate = st.number_input("Estimated rate per sq. ft. (₹)", min_value=1.0, value=1800.0)

if st.button("Calculate Cost"):
    st.success(f"Estimated construction cost: ₹{area * rate:,.2f}")
    st.caption("Indicative estimate based on the rate you entered.")


elif page == "Property Valuation":
    st.header("Real Estate Property Valuation")


location = st.text_input("Property location")
area = st.number_input("Property area (sq. ft.)", min_value=1.0, value=1000.0)
rate = st.number_input("Estimated market rate per sq. ft. (₹)", min_value=1.0, value=3000.0)

if st.button("Estimate Property Value"):
    st.success(f"Estimated property value: ₹{area * rate:,.2f}")
    st.write("Location:", location or "Not specified")
    st.caption("This is a user-input-based estimate, not a verified market valuation.")


elif page == "Weather Advisory":
    st.header("Weather-Aware Construction Advisory")

    condition = st.selectbox(
        "Select weather condition",
        ["Sunny", "Cloudy", "Rainy", "Stormy", "Very Hot", "Cold"]
    )

    advice = {
        "Sunny": "Provide drinking water, shade and regular breaks.",
        "Cloudy": "Monitor weather changes and inspect the worksite.",
        "Rainy": "Check drainage, slippery surfaces and electrical safety.",
        "Stormy": "Stop exposed outdoor work when conditions are unsafe.",
        "Very Hot": "Provide hydration and monitor workers for heat stress.",
        "Cold": "Use suitable protective equipment and inspect work surfaces."
    }

    if st.button("Get Recommendations"):
        st.info(advice[condition])

    st.caption("Recommendations are based on your selection, not live weather data.")

elif page == "AI Construction Assistant":
    st.header("AI Construction Assistant")


question = st.text_area(
    "Ask a construction-related question",
    placeholder="Example: What precautions are needed during concrete pouring?"
)

if st.button("Submit Question"):
    if question.strip():
        st.write("Your question:", question)
        st.info("Connect an LLM API to enable generated AI answers.")
    else:
        st.warning("Please enter a question.")


st.divider()
st.caption("Multimodal Construction Intelligence Platform | Prototype")
