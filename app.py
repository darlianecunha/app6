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
variables = {
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
        # Add more variables as needed...
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
        # Add more variables as needed...
    ]
}

# Application title
st.markdown("<h1 style='color: darkgreen;'>SDG Attributes - SDG 7 and 13</h1>", unsafe_allow_html=True)

# Tabs for SDG 7 and 13
tab1, tab2 = st.tabs(["SDG 7", "SDG 13"])

# Function to display content for each tab
def display_ods_tab(ods_group):
    st.header(f"{ods_group}")
    scores = []
    categories = []
    for variable in variables[ods_group]:
        option = st.selectbox(variable["name"], options=variable["options"])
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
        st.download_button("Download Chart as PNG", img_buffer, file_name="radar_chart.png", mime="image/png")

# Display variables and results for each tab
with tab1:
    display_ods_tab("SDG 7")

with tab2:
    display_ods_tab("SDG 13")

# Footer with source and credits
st.write("---")
st.markdown(
    "<p><strong>Tool developed by Darliane Cunha.</strong></p>", 
    unsafe_allow_html=True
)



