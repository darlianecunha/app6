import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

# Function to calculate the final score
def calculate_final_score(scores):
    max_score = len(scores) * 3  # Maximum score if all variables are scored 3
    total_score = sum(scores)
    percentage_score = (total_score / max_score) * 100
    return percentage_score

# Function to plot the radar chart
def plot_radar_chart(scores, categories):
    if len(scores) != len(categories):
        st.error("The number of scores and categories does not match.")
        return None

    values = scores + scores[:1]  # Repeat the first value to close the circle
    angles = np.linspace(0, 2 * np.pi, len(scores), endpoint=False).tolist()
    angles += angles[:1]  # Repeat the first angle to close the chart

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='teal', alpha=0.25)
    ax.plot(angles, values, color='teal', linewidth=2)
    ax.set_yticks(range(1, 4))  # Set the radial grid
    ax.set_yticklabels(range(1, 4))  # Add radial labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    # Adding labels for each data point
    for angle, value in zip(angles, values):
        ax.text(angle, value + 0.1, f"{value:.0f}", ha='center', va='center', fontsize=10)

    return fig

# Function to export the chart as an image
def export_chart_as_image(fig):
    img_buffer = BytesIO()
    fig.savefig(img_buffer, format='png', dpi=300, bbox_inches="tight")
    img_buffer.seek(0)
    return img_buffer

# Variables grouped by SDG with prefixes
variables =
    "SDG 7": [
        {
            "name": "7.1 Number of awareness programs on rational energy use",
            "options": [
                "0: No program in operation.",
                "1: Up to 2 programs in operation, reaching up to 100 people.",
                "2: 3-5 programs in operation, reaching 101-500 people.",
                "3: More than 5 programs in operation, reaching over 500 people."
            ]
        },
        {
            "name": "7.2 Number of energy efficiency management programs",
            "options": [
                "0: No program in operation.",
                "1: At least one program, resulting in up to 5% reduction in energy consumption.",
                "2: At least one program, resulting in a reduction greater than 5% and less than or equal to 10% in energy consumption.",
                "3: At least one program with energy consumption reductions exceeding 10%."
            ]
        },
        {
            "name": "7.3 Number of technological innovation initiatives in energy efficiency",
            "options": [
                "0: No initiative.",
                "1: Up to 2 technological initiatives implemented.",
                "2: 3-5 technological initiatives implemented.",
                "3: More than 5 initiatives implemented."
            ]
        },
        {
            "name": "7.4 Percentage of renewable energy contracted and produced in port facilities",
            "options": [
                "0: No use of renewable energy.",
                "1: Up to 10% of the energy used is renewable.",
                "2: More than 10% up to 50% of the energy used is renewable.",
                "3: More than 50% of the energy used is renewable."
            ]
        },
        {
            "name": "7.5 Percentage of biofuels in electrical and mechanical loads",
            "options": [
                "0: No use of biofuels.",
                "1: Less than 5% of the loads are operated with biofuels.",
                "2: 5% to 20% of the loads are operated with biofuels.",
                "3: More than 20% of the loads are operated with biofuels."
            ]
        },
        {
            "name": "7.6 Number of technological innovation initiatives in renewable energy",
            "options": [
                "0: No initiative.",
                "1: Up to 2 initiatives in the planning or pilot phase.",
                "2: 3-5 initiatives in the implementation phase with preliminary results.",
                "3: More than 5 initiatives in full operation with proven results."
            ]
        },
        {
            "name": "7.7 Diversity of renewable energy sources in port facilities",
            "options": [
                "0: No use of renewable sources.",
                "1: Use of 1 different type of renewable energy.",
                "2: Use of 2 different types of renewable energy.",
                "3: Use of 3 or more different types of renewable energy."
            ]
        },
        {
            "name": "7.8 Number of partnerships for the promotion of clean energy",
            "options": [
                "0: No partnership established.",
                "1: Up to 2 partnerships established with a focus on clean energy.",
                "2: 3-5 partnerships established with a focus on clean energy.",
                "3: More than 5 partnerships established with a focus on clean energy."
            ]
        },
        {
            "name": "7.9 Number of charging stations for electric vehicles",
            "options": [
                "0: No charging station available.",
                "1: Up to 5 charging stations available.",
                "2: 6-15 charging stations available.",
                "3: More than 15 charging stations available."
        ]}
],

"SDG 13": [
        {
            "name": "13.1 Status of Climate Change Strategy Plan",
            "options": [
                "0: No strategies.",
                "1: Strategy plan under development, no actions implemented.",
                "2: Strategy plan implemented, with some actions in practice.",
                "3: Fully operational strategy plan, with regular review and updates."
            ]
        },
        {
            "name": "13.2 Emissions Inventory",
            "options": [
                "0: Emissions inventory not carried out.",
                "1: Emissions inventory conducted, but outdated.",
                "2: Emissions inventory conducted, updated more than a year ago.",
                "3: Emissions inventory updated annually and actively used for emissions management."
            ]
        },
        {
            "name": "13.3 Carbon Credit Management Program",
            "options": [
                "0: No Carbon Credit Program.",
                "1: Program in initial phase, without credits generated or purchased.",
                "2: Active program, with carbon credits being generated or purchased.",
                "3: Well-established program, with carbon credits being actively managed."
            ]
        },
        {
            "name": "13.4 Climate Monitoring Program",
            "options": [
                "0: Non-existent program.",
                "1: Program in implementation phase.",
                "2: Program implemented, but data used in a limited way.",
                "3: Program implemented and integrated into a climate response and planning system."
            ]
        },
        {
            "name": "13.5 Number of Collaborations and Partnerships for Climate Action",
            "options": [
                "0: No collaboration or partnership established.",
                "1: Up to 2 collaborations or partnerships established.",
                "2: 3-5 collaborations or partnerships with initial results.",
                "3: More than 5 collaborations or partnerships with significant and measurable impact on climate action."
            ]
        },
        {
            "name": "13.6 Climate-Resilient Infrastructure",
            "options": [
                "0: No infrastructure assessed as climate resilient.",
                "1: Less than 25% of infrastructure assessed as climate resilient.",
                "2: 25-50% of infrastructure assessed as climate resilient.",
                "3: More than 50% of infrastructure assessed as climate-resilient and adapted."
            ]
        },
        {
            "name": "13.7 Cargo Traffic Efficiency Index",
            "options": [
                "0: Index not calculated.",
                "1: Efficiency index below the industry average.",
                "2: Efficiency index at the industry average.",
                "3: Efficiency index above the industry average, with continuous improvements."
            ]
        },
        {
            "name": "13.8 Percentage Reduction of Emissions Through New Technology Implementation",
            "options": [
                "0: No emission reduction programs.",
                "1: Less than 5% reduction in emissions through new technologies.",
                "2: 5-10% reduction in emissions through new technologies.",
                "3: More than 10% reduction in emissions through new technologies."
        ]}
    
 ]}

# Application title
st.markdown("<h1 style='color: darkgreen;'>SDG Attributes - SDG 7 and 13</h1>", unsafe_allow_html=True)

# Tabs for SDG 7 and 13
tab1, tab2 = st.tabs(["SDG 7", "SDG 13"])

# Function to display content for each tab
def display_ods_tab(ods_group, tab_key):
    st.header(f"{ods_group}")
    scores = []
    categories = []
    for variable in variables[ods_group]:
        option = st.selectbox(variable["name"], options=variable["options"], key=f"{tab_key}_{variable['name']}")
        scores.append(int(option[0]))  # Convert the first character of the selected option to integer
        categories.append(variable["name"].split(" ")[0])

    if len(scores) != len(categories):
        st.error("Error: The number of scores and categories does not match.")
        return

    # Calculate the final score
    percentage_score = calculate_final_score(scores)
    st.write(f"Final Score {ods_group}: {percentage_score:.2f}%")

    # Display the radar chart
    st.subheader("Radar Chart")
    radar_chart = plot_radar_chart(scores, categories)
    if radar_chart:
        st.pyplot(radar_chart)

        # Add a button to download the chart
        img_buffer = export_chart_as_image(radar_chart)
        st.download_button("Download Chart as PNG", img_buffer, file_name=f"radar_chart_{ods_group}.png", mime="image/png", key=f"{tab_key}_download_button")

# Display variables and results for each tab
with tab1:
    display_ods_tab("SDG 7", "tab1")

with tab2:
    display_ods_tab("SDG 13", "tab2")

# Footer with source and credits
st.write("---")
st.markdown(
    "<p><strong>Tool developed by Darliane Cunha.</strong></p>", 
    unsafe_allow_html=True
)




