
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Construction Intelligence",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- PROFESSIONAL THEME ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;600;700;800&display=swap');

.stApp {
    background: #f3f6fb;
    font-family: 'DM Sans', sans-serif;
    color: #17233c;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#101d35,#192f50);
}
[data-testid="stSidebar"] * {
    color: #edf4ff;
}
[data-testid="stSidebar"] hr {
    border-color: #344761;
}
.hero {
    background: linear-gradient(120deg,#12213d,#21466b,#087e80);
    border-radius: 20px;
    padding: 32px;
    color: white;
    margin-bottom: 25px;
}
.hero h1 {
    color: white;
    font-family: Manrope,sans-serif;
    font-size: 34px;
    font-weight: 800;
    margin: 12px 0;
}
.hero p {
    color: #dbeafe;
    font-size: 16px;
}
.tag {
    background: #1b666b;
    border: 1px solid #70d7c7;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 12px;
    color: white;
}
.metric-card {
    background: white;
    border: 1px solid #e3eaf3;
    border-radius: 16px;
    padding: 20px;
    min-height: 125px;
    box-shadow: 0 5px 18px rgba(20,40,70,.04);
}
.metric-label {
    color: #718096;
    font-size: 13px;
    font-weight: 600;
}
.metric-value {
    color: #152744;
    font-size: 28px;
    font-weight: 800;
    margin: 8px 0;
    font-family: Manrope,sans-serif;
}
.metric-note {
    color: #078779;
    font-size: 12px;
    font-weight: 600;
}
.section-title {
    font-family: Manrope,sans-serif;
    font-size: 23px;
    font-weight: 800;
    color: #17233c;
    margin-top: 12px;
}
.subtitle {
    color: #748198;
    font-size: 14px;
    margin-bottom: 18px;
}
.panel {
    background: white;
    padding: 22px;
    border: 1px solid #e2e9f2;
    border-radius: 16px;
}
div[data-testid="stButton"] button {
    border-radius: 10px;
    font-weight: 700;
    min-height: 42px;
}
div[data-testid="stDownloadButton"] button {
    border-radius: 10px;
    font-weight: 700;
}
.stTextInput input, .stNumberInput input, .stTextArea textarea {
    border-radius: 9px;
}
.footer {
    text-align: center;
    color: #8491a5;
    font-size: 12px;
    padding: 25px 0 5px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("# 🏗️")
    st.markdown("## CONSTRUCTION")
    st.markdown("### INTELLIGENCE")
    st.caption("SMART SITE MANAGEMENT")
    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "Dashboard",
            "PPE Safety Audit",
            "Crack Inspection",
            "Cost Estimation",
            "Weather Advisory",
            "Project Assistant"
        ]
    )

    st.divider()
    st.markdown("### 🟢 Application Status")
    st.caption("Prototype is running")
    st.caption("Construction Intelligence v1.0")


# ---------------- HELPER FUNCTIONS ----------------
def metric(label, value, note, icon):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">{icon} &nbsp; {label}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-note">{note}</div>
    </div>
    """, unsafe_allow_html=True)


def page_header(title, subtitle):
    st.markdown(f"""
    <div class="section-title">{title}</div>
    <div class="subtitle">{subtitle}</div>
    """, unsafe_allow_html=True)


def download_csv(data, filename):
    df = pd.DataFrame(data)
    st.download_button(
        "⬇️ Download Report",
        df.to_csv(index=False).encode("utf-8"),
        file_name=filename,
        mime="text/csv"
    )


# ---------------- DASHBOARD ----------------
if page == "Dashboard":

    st.markdown("""
    <div class="hero">
        <span class="tag">MULTIMODAL CONSTRUCTION PLATFORM</span>
        <h1>Build Smarter. Build Safer.</h1>
        <p>One intelligent workspace for construction safety,
        structural observations, project cost planning and site operations.</p>
    </div>
    """, unsafe_allow_html=True)

    page_header(
        "Project Overview",
        "A unified overview of your construction workspace."
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric("Safety Reviews", "24", "Sample dashboard data", "🦺")
    with c2:
        metric("Inspections", "12", "Sample dashboard data", "🧱")
    with c3:
        metric("Project Budget", "₹2.4 Cr", "Illustrative estimate", "💰")
    with c4:
        metric("Site Monitoring", "Active", "Prototype status", "📊")

    st.write("")

    left, right = st.columns([1.3, 1])

    with left:
        st.markdown('<div class="section-title">📈 Site Activity</div>',
                    unsafe_allow_html=True)
        st.caption("Illustrative weekly activity")

        chart_data = pd.DataFrame({
            "Safety Reviews": [5, 8, 6, 10, 7, 9, 4],
            "Inspections": [3, 4, 5, 4, 6, 3, 2]
        }, index=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

        st.bar_chart(chart_data, use_container_width=True)

    with right:
        st.markdown('<div class="section-title">🧭 Project Modules</div>',
                    unsafe_allow_html=True)

        st.markdown("""
        <div class="panel">
            <h4>🦺 PPE Safety Audit</h4>
            <p>Review construction-site safety observations.</p>
            <hr>
            <h4>🧱 Crack Inspection</h4>
            <p>Document visible concrete cracks.</p>
            <hr>
            <h4>💰 Cost Estimation</h4>
            <p>Calculate indicative project budgets.</p>
            <hr>
            <h4>🌦️ Weather Advisory</h4>
            <p>Review weather-related precautions.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.info(
        "Demo note: Dashboard numbers and charts are illustrative sample data, "
        "not live construction-site measurements."
    )


# ---------------- PPE SAFETY ----------------
elif page == "PPE Safety Audit":

    page_header(
        "🦺 PPE Safety Audit",
        "Upload a site image and record a construction safety checklist."
    )

    left, right = st.columns(2)

    with left:
        uploaded = st.file_uploader(
            "Upload construction-site image",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded:
            st.image(uploaded, caption="Uploaded Site Image",
                     use_container_width=True)
        else:
            st.markdown("""
            <div class="panel" style="text-align:center;padding:40px">
                <h1>📷</h1>
                <h3>Site Image Preview</h3>
                <p>Upload a JPG or PNG image to begin your review.</p>
            </div>
            """, unsafe_allow_html=True)

    with right:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.subheader("Safety Checklist")

        helmet = st.selectbox(
            "Hard hats",
            ["Not reviewed", "Compliant", "Needs attention", "Not applicable"]
        )
        vest = st.selectbox(
            "High-visibility vests",
            ["Not reviewed", "Compliant", "Needs attention", "Not applicable"]
        )
        shoes = st.selectbox(
            "Safety footwear",
            ["Not reviewed", "Compliant", "Needs attention", "Not applicable"]
        )
        protection = st.selectbox(
            "Fall protection",
            ["Not reviewed", "Compliant", "Needs attention", "Not applicable"]
        )
        notes = st.text_area("Safety observations", placeholder="Enter observations...")

        if st.button("Generate Safety Report", type="primary",
                     use_container_width=True):

            data = [{
                "Date": datetime.now().strftime("%d-%m-%Y %H:%M"),
                "Image": uploaded.name if uploaded else "Not uploaded",
                "Hard Hats": helmet,
                "Safety Vests": vest,
                "Safety Footwear": shoes,
                "Fall Protection": protection,
                "Observations": notes
            }]

            st.session_state["safety_data"] = data
            st.success("Safety review recorded successfully.")

        st.markdown('</div>', unsafe_allow_html=True)

    if "safety_data" in st.session_state:
        st.subheader("📋 Safety Review Summary")
        st.dataframe(
            pd.DataFrame(st.session_state["safety_data"]),
            use_container_width=True,
            hide_index=True
        )
        download_csv(st.session_state["safety_data"], "safety_report.csv")

    st.warning(
        "PPE observations are entered manually. This prototype does not "
        "automatically detect helmets or safety equipment."
    )


# ---------------- CRACK INSPECTION ----------------
elif page == "Crack Inspection":

    page_header(
        "🧱 Concrete Crack Inspection",
        "Record preliminary visual observations and inspection details."
    )

    left, right = st.columns(2)

    with left:
        uploaded = st.file_uploader(
            "Upload concrete image",
            type=["jpg", "jpeg", "png"],
            key="crack_image"
        )

        if uploaded:
            st.image(uploaded, caption="Concrete Inspection Image",
                     use_container_width=True)
        else:
            st.markdown("""
            <div class="panel" style="text-align:center;padding:40px">
                <h1>🧱</h1>
                <h3>Structural Image Review</h3>
                <p>Upload a concrete or wall image.</p>
            </div>
            """, unsafe_allow_html=True)

    with right:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.subheader("Inspection Details")

        location = st.text_input(
            "Site location",
            placeholder="e.g. Block A, Level 2"
        )
        crack_type = st.selectbox(
            "Observed crack pattern",
            ["Not classified", "Hairline", "Vertical", "Horizontal",
             "Diagonal", "Map / network", "Other"]
        )
        width = st.number_input(
            "Estimated width (mm)",
            min_value=0.0,
            max_value=100.0,
            value=0.3,
            step=0.1
        )
        severity = st.selectbox(
            "Reviewer-assessed priority",
            ["Low", "Moderate", "High", "Urgent"]
        )
        observations = st.text_area(
            "Observations",
            placeholder="Describe the visible condition..."
        )

        if st.button("Save Inspection", type="primary",
                     use_container_width=True):

            record = [{
                "Date": datetime.now().strftime("%d-%m-%Y %H:%M"),
                "Image": uploaded.name if uploaded else "Not uploaded",
                "Location": location or "Not specified",
                "Pattern": crack_type,
                "Estimated Width (mm)": width,
                "Priority": severity,
                "Observations": observations
            }]

            st.session_state["crack_data"] = record
            st.success("Inspection record saved.")

        st.markdown('</div>', unsafe_allow_html=True)

    if "crack_data" in st.session_state:
        st.subheader("📋 Inspection Report")
        st.dataframe(
            pd.DataFrame(st.session_state["crack_data"]),
            use_container_width=True,
            hide_index=True
        )
        download_csv(st.session_state["crack_data"], "crack_report.csv")

    st.warning(
        "This tool records observations; it does not automatically detect "
        "cracks or establish structural safety. Consult a qualified engineer."
    )


# ---------------- COST ESTIMATION ----------------
elif page == "Cost Estimation":

    page_header(
        "💰 Construction Cost Estimation",
        "Calculate an indicative project cost using editable assumptions."
    )

    left, right = st.columns(2)

    with left:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.subheader("Project Inputs")

        area = st.number_input(
            "Built-up area (sq. ft.)",
            min_value=100,
            value=25000,
            step=500
        )
        rate = st.number_input(
            "Construction rate per sq. ft. (₹)",
            min_value=100,
            value=1800,
            step=100
        )
        contingency = st.slider("Contingency (%)", 0, 30, 10)
        fees = st.slider("Professional fees (%)", 0, 20, 5)
        land = st.number_input(
            "Land cost (₹)",
            min_value=0,
            value=5000000,
            step=500000
        )
        market_rate = st.number_input(
            "Estimated market rate per sq. ft. (₹)",
            min_value=100,
            value=3200,
            step=100
        )

        st.markdown('</div>', unsafe_allow_html=True)

    base = area * rate
    extra = base * contingency / 100
    professional = base * fees / 100
    total = base + extra + professional + land
    valuation = area * market_rate

    with right:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.subheader("📊 Estimate Summary")

        st.metric(
            "Estimated Total Project Cost",
            f"₹{total / 10000000:.2f} Cr"
        )
        st.metric(
            "Indicative Market Value",
            f"₹{valuation / 10000000:.2f} Cr"
        )
        st.metric(
            "Value Difference",
            f"₹{(valuation-total) / 100000:.2f} L"
        )

        st.markdown('</div>', unsafe_allow_html=True)

        breakdown = pd.DataFrame({
            "Cost Component": [
                "Construction",
                "Contingency",
                "Professional Fees",
                "Land",
                "Total Project Cost"
            ],
            "Amount (₹)": [
                round(base),
                round(extra),
                round(professional),
                round(land),
                round(total)
            ]
        })

        st.subheader("Cost Breakdown")
        st.dataframe(breakdown, use_container_width=True, hide_index=True)
        download_csv(breakdown, "construction_estimate.csv")

    st.info(
        "Estimates are illustrative. Actual costs depend on location, "
        "specifications, approvals, taxes and market conditions."
    )


# ---------------- WEATHER ADVISORY ----------------
elif page == "Weather Advisory":

    page_header(
        "🌦️ Weather Advisory",
        "Generate a basic precaution checklist using entered site conditions."
    )

    left, right = st.columns(2)

    with left:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.subheader("Site Conditions")

        temperature = st.slider("Temperature (°C)", -5, 55, 32)
        rain = st.selectbox(
            "Rain conditions",
            ["No rain expected", "Light rain", "Heavy rain / storm"]
        )
        wind = st.slider("Wind speed (km/h)", 0, 120, 15)
        lightning = st.checkbox("Thunderstorm / lightning alert")

        st.markdown('</div>', unsafe_allow_html=True)

    alerts = []

    if temperature >= 40:
        alerts.append(
            ("🔥 High Temperature",
             "Provide shade, water and frequent rest breaks. Monitor heat stress.")
        )
    elif temperature >= 34:
        alerts.append(
            ("🌡️ Heat Awareness",
             "Ensure hydration, shade and regular worker monitoring.")
        )

    if rain == "Light rain":
        alerts.append(
            ("🌧️ Wet Surfaces",
             "Check slippery access routes and electrical protection.")
        )
    elif rain == "Heavy rain / storm":
        alerts.append(
            ("⛈️ Heavy Rain",
             "Review drainage, excavation safety and exposed work.")
        )

    if wind >= 40:
        alerts.append(
            ("💨 Strong Wind",
             "Review lifting operations, scaffolds and loose materials.")
        )

    if lightning:
        alerts.append(
            ("⚡ Lightning Risk",
             "Suspend exposed outdoor work according to site safety procedures.")
        )

    if not alerts:
        alerts.append(
            ("✅ Routine Monitoring",
             "Continue normal site checks and monitor official local forecasts.")
        )

    with right:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.subheader("Recommended Precautions")

        for title, detail in alerts:
            st.markdown(f"### {title}")
            st.write(detail)
            st.divider()

        st.markdown('</div>', unsafe_allow_html=True)

    report = [
        {"Condition": title, "Recommended Action": detail}
        for title, detail in alerts
    ]
    download_csv(report, "weather_advisory.csv")

    st.info(
        "Conditions are entered manually. This prototype does not fetch live "
        "weather data. Follow official alerts and site-specific safety rules."
    )


# ---------------- PROJECT ASSISTANT ----------------
elif page == "Project Assistant":

    page_header(
        "🤖 Project Assistant",
        "Explore predefined guidance for common construction tasks."
    )

    question = st.text_area(
        "Enter your construction-related question",
        placeholder="e.g. What should be checked before a concrete pour?",
        height=120
    )

    if st.button("Get Guidance", type="primary"):

        q = question.lower()

        if any(word in q for word in ["concrete", "pour", "curing", "mix"]):
            answer = """
            ### Concrete Pour Checklist
            - Verify approved drawings and concrete mix specifications.
            - Inspect formwork, reinforcement and cover blocks.
            - Check equipment, access routes and worker PPE.
            - Follow the approved placement, compaction and curing procedure.
            - Record quality checks and inspection results.
            """

        elif any(word in q for word in ["ppe", "helmet", "safety", "hazard"]):
            answer = """
            ### Site Safety Checklist
            - Verify task-appropriate PPE.
            - Inspect access routes, signage and housekeeping.
            - Review fall protection, electrical and lifting hazards.
            - Document hazards and corrective actions.
            - Escalate immediate risks to the site safety officer.
            """

        elif any(word in q for word in ["crack", "structural", "beam", "column"]):
            answer = """
            ### Crack Observation Checklist
            - Record the location, date, approximate width and length.
            - Take clear photographs with a scale reference.
            - Note moisture, displacement and changes over time.
            - Escalate concerning cracks to a qualified structural engineer.
            - Do not rely on a photograph alone to determine structural safety.
            """

        elif any(word in q for word in ["cost", "budget", "estimate", "valuation"]):
            answer = """
            ### Project Cost Planning
            - Define scope, area, location and specifications.
            - Estimate labour, materials, services and professional fees.
            - Include approvals, land costs and contingency.
            - Record rate sources and estimate dates.
            - Validate estimates against local market information.
            """

        elif any(word in q for word in ["weather", "rain", "wind", "heat"]):
            answer = """
            ### Weather Planning Checklist
            - Review the official local weather forecast.
            - Check lifting, scaffolding and excavation risks.
            - Follow site-specific stop-work thresholds.
            - Communicate changes to the site team.
            - Record decisions and safety precautions.
            """

        else:
            answer = """
            I can provide predefined guidance about:
            - Construction safety and PPE
            - Concrete pouring and curing
            - Crack observation
            - Project cost estimation
            - Weather-related site precautions

            Try asking about one of these topics.
            """

        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown(answer)
        st.markdown('</div>', unsafe_allow_html=True)

    st.info(
        "This prototype uses predefined guidance rather than a connected "
        "generative-AI model."
    )


# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    CONSTRUCTION INTELLIGENCE · SMART CONSTRUCTION WORKSPACE<br>
    Demo prototype | Verify safety-critical decisions with qualified professionals.
</div>
""", unsafe_allow_html=True)

