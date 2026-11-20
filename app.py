# import plotly.express as px
# import streamlit as st
# from analysis import get_wifi_readings

# # Configure the dashboard
# st.set_page_config(
#     page_title="Campus Wi-Fi Intelligence System",
#     page_icon="📶",
#     layout="wide"
# )


# st.markdown("""
# <style>

# /* Main dashboard */
# .stApp {
#     background-color: #F2F3F5;
#     color: #101827;
# }

# /* Content layout */
# .block-container {
#     padding-top: 1rem;
#     padding-bottom: 2rem;
#     max-width: 1400px;
# }

# /* Headings */
# h1, h2, h3 {
#     color: #101827;
#     font-weight: 750;
#     letter-spacing: -0.035em;
# }

# /* Metric cards */
# div[data-testid="stMetric"] {
#     background: #FFFFFF;
#     border: 1px solid #E2E7EE;
#     border-top: 3px solid #2349F5;
#     border-radius: 18px;
#     padding: 24px;
#     min-height: 155px;
#     box-shadow: 0 6px 24px rgba(16, 24, 39, 0.05);
#     transition: transform 0.2s ease,
#                 box-shadow 0.2s ease;
# }

# /* Hover animation */
# div[data-testid="stMetric"]:hover {
#     transform: translateY(-4px);
#     box-shadow: 0 12px 30px rgba(16, 24, 39, 0.10);
# }

# /* Metric values */
# div[data-testid="stMetricValue"] {
#     font-size: 32px;
#     font-weight: 800;
#     color: #101827;
#     letter-spacing: -1px;
# }

# /* Metric labels */
# div[data-testid="stMetricLabel"] {
#     font-size: 12px;
#     font-weight: 700;
#     text-transform: uppercase;
#     color: #427D96;
# }

# /* Sidebar */
# section[data-testid="stSidebar"] {
#     background: #101827;
# }

# /* Dividers */
# hr {
#     border-color: #DCE3EA;
# }

# </style>
# """, unsafe_allow_html=True)


# # Custom futuristic dashboard header
# st.markdown(
#     """
# <div style="background: linear-gradient(120deg, #101827, #122E3B); padding: 40px; border-radius: 20px; margin-bottom: 25px;">

# <div style="color: #23D5C5; font-size: 12px; font-weight: bold; letter-spacing: 3px; margin-bottom: 20px;">
# ◉ SIGNAL / INTELLIGENCE
# </div>

# <div style="font-size: 46px; font-weight: 800; line-height: 1.2; letter-spacing: -2px; color: white;">
# See the signal.
# </div>

# <div style="font-size: 46px; font-weight: 800; line-height: 1.2; letter-spacing: -2px; color: #23D5C5;">
# Find the blind spots.
# </div>

# <div style="color: #B8C3D4; font-size: 16px; margin-top: 20px;">
# Campus Wi-Fi Dead-Zone Intelligence System
# </div>

# <div style="border-top: 1px solid #334457; margin-top: 25px; padding-top: 15px; color: #B8C3D4; font-size: 11px; letter-spacing: 2px;">
# NETWORK ANALYTICS PLATFORM
# </div>

# </div>
#     """,
#     unsafe_allow_html=True
# )


# # Description
# st.write(
#     "An interactive dashboard for monitoring Wi-Fi "
#     "signal strength, network performance, and "
#     "potential connectivity dead zones across campus."
# )

# st.divider()


# # Retrieve real Wi-Fi readings from MongoDB
# df = get_wifi_readings()

# if df.empty:
#     st.warning("No Wi-Fi readings available in the database.")

# else:

#     # Dashboard-wide location filter
#     st.subheader("📍 Filter Network Data")

#     available_locations = sorted(
#         df["location"].dropna().unique().tolist()
#     )

#     selected_location = st.selectbox(
#         "Select a location",
#         ["All Locations"] + available_locations,
#         key="dashboard_location_filter"
#     )

#     if selected_location == "All Locations":
#         df = df.copy()
#     else:
#         df = df[
#             df["location"] == selected_location
#         ].copy()

#     st.caption(
#         f"Displaying {len(df)} readings "
#         f"for {selected_location}."
#     )

#     st.divider()

#     st.subheader("📊 Network Overview")

#     # Calculate overall statistics
#     total_readings = len(df)
#     average_signal = df["signal_strength"].mean()
#     average_latency = df["latency_ms"].mean()
#     average_packet_loss = df["packet_loss_percent"].mean()

#     # Create four dashboard columns
#     col1, col2, col3, col4 = st.columns(4)

#     with col1:
#         st.metric("Total Readings", total_readings)

#     with col2:
#         st.metric("Average Signal Strength", f"{average_signal:.2f}%")

#     with col3:
#         st.metric("Average Latency", f"{average_latency:.2f} ms")

#     with col4:
#         st.metric("Average Packet Loss", f"{average_packet_loss:.2f}%")

#     st.divider()

#     st.subheader("📋 Collected Wi-Fi Readings")
    
#     # Display readings with user-friendly column names
#     display_df = df.rename(columns={
#         "location": "Location",
#         "ssid": "Wi-Fi Network",
#         "signal_strength": "Signal Strength (%)",
#         "latency_ms": "Latency (ms)",
#         "packet_loss_percent": "Packet Loss (%)",
#         "packets_sent": "Packets Sent",
#         "packets_received": "Packets Received",
#         "timestamp": "Recorded At",
#         "wifi_quality": "Wi-Fi Quality"
#     }).copy()

#     st.dataframe(
#         display_df,
#         use_container_width=True,
#         hide_index=True,
#         column_config={
#             "Signal Strength (%)": st.column_config.NumberColumn(
#                 "Signal Strength (%)",
#                 format="%.0f%%"
#             ),
#             "Latency (ms)": st.column_config.NumberColumn(
#                 "Latency (ms)",
#                 format="%.2f ms"
#             ),
#             "Packet Loss (%)": st.column_config.NumberColumn(
#                 "Packet Loss (%)",
#                 format="%.1f%%"
#             )
#         }

#     )




#     st.divider()

#     # Wi-Fi quality distribution
#     st.subheader("📊 Wi-Fi Quality Distribution")

    
#     if "wifi_quality" in df.columns:
#         quality_counts = (
#             df["wifi_quality"]
#             .value_counts()
#             .rename_axis("Quality")
#             .reset_index(name="Readings")
#         )

#         quality_colors = {
#             "Good": "#23B88E",
#             "Moderate": "#E5B64B",
#             "Poor": "#F08052",
#             "Potential Dead Zone": "#E05262"
#         }

#         quality_fig = px.bar(
#             quality_counts,
#             x="Quality",
#             y="Readings",
#             color="Quality",
#             color_discrete_map=quality_colors,
#             text="Readings"
#         )

#         quality_fig.update_traces(
#             textposition="outside",
#             marker_line_width=0
#         )

#         quality_fig.update_layout(
#             paper_bgcolor="#FFFFFF",
#             plot_bgcolor="#FFFFFF",
#             font=dict(color="#101827"),
#             showlegend=False,
#             height=360,
#             margin=dict(l=20, r=20, t=35, b=35),
#             xaxis_title=None,
#             yaxis_title="Number of Readings",
#             yaxis=dict(gridcolor="#E8EDF3")
#         )

#         st.plotly_chart(
#             quality_fig,
#             use_container_width=True
#         )

#     else:
#         st.warning(
#             "Wi-Fi quality classification is not available."
#         )


#     st.divider()

#     # Location-wise Wi-Fi analysis
#     st.subheader("📍 Location-wise Wi-Fi Performance")

#     location_stats = df.groupby("location").agg(
#         average_signal=("signal_strength", "mean"),
#         average_latency=("latency_ms", "mean"),
#         average_packet_loss=("packet_loss_percent", "mean"),
#         total_readings=("location", "count")
#     ).reset_index()

#     location_stats = location_stats.round(2)

#     # Show location-wise statistics
#     st.dataframe(location_stats, use_container_width=True)

    
#     # Compact location-wise performance charts

#     st.subheader("📊 Network Performance Comparison")

#     def create_performance_chart(column, title, color, unit):
#         chart = px.bar(
#             location_stats,
#             x="location",
#             y=column,
#             text=column,
#             labels={
#                 "location": "Location",
#                 column: unit
#             }
#         )

#         chart.update_traces(
#             marker_color=color,
#             marker_line_width=0,
#             texttemplate="%{text:.2f}",
#             textposition="outside",
#             cliponaxis=False
#         )

#         chart.update_layout(
#             title=dict(
#                 text=title,
#                 font=dict(size=16, color="#101827")
#             ),
#             height=300,
#             margin=dict(l=35, r=20, t=65, b=55),
#             paper_bgcolor="#FFFFFF",
#             plot_bgcolor="#FFFFFF",
#             font=dict(color="#101827", size=12),
#             showlegend=False,
#             xaxis=dict(
#                 title=None,
#                 tickangle=0,
#                 automargin=True,
#                 showgrid=False
#             ),
#             yaxis=dict(
#                 title=unit,
#                 rangemode="tozero",
#                 gridcolor="#E8EDF3",
#                 automargin=True
#             )
#         )

#         return chart

#     # First row: signal and latency
#     chart_col1, chart_col2 = st.columns(2)

#     with chart_col1:
#         signal_fig = create_performance_chart(
#             "average_signal",
#             "Average Signal Strength",
#             "#2349F5",
#             "Signal Strength (%)"
#         )
#         signal_fig.update_yaxes(range=[0, 110])
#         st.plotly_chart(
#             signal_fig,
#             use_container_width=True
#         )

#     with chart_col2:
#         latency_fig = create_performance_chart(
#             "average_latency",
#             "Average Latency",
#             "#23B9B0",
#             "Latency (ms)"
#         )
#         st.plotly_chart(
#             latency_fig,
#             use_container_width=True
#         )

#     # Second row: packet loss
#     packet_fig = create_performance_chart(
#         "average_packet_loss",
#         "Average Packet Loss",
#         "#427D96",
#         "Packet Loss (%)"
#     )
#     packet_fig.update_yaxes(range=[0, 100])

#     st.plotly_chart(
#         packet_fig,
#         use_container_width=True
#     )


#     st.divider()

#     st.subheader("🗺️ Wi-Fi Signal Heatmap")


#     # Prepare location-wise signal strength data
#     heatmap_data = location_stats.set_index("location")[
#         ["average_signal"]
#     ].T

#     # Create interactive heatmap
#     fig = px.imshow(
#         heatmap_data,
#         labels={
#             "x": "Location",
#             "y": "Measurement",
#             "color": "Signal Strength (%)"
#         },
#         color_continuous_scale="RdYlGn",
#         zmin=0,
#         zmax=100,
#         aspect="auto",
#         text_auto=".1f"
#     )

#     fig.update_layout(
#         title="Average Wi-Fi Signal Strength by Location",
#         height=350
#     )

#     st.plotly_chart(fig, use_container_width=True)

#     st.caption(
#         "This heatmap displays signal strength for recorded "
#         "locations. It is not yet a geographic campus map."
#     )


#     st.divider()

   

import html

import plotly.express as px
import streamlit as st

from analysis import get_wifi_readings


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Campus Wi-Fi Intelligence System",
    page_icon="📶",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# --------------------------------------------------
# DESIGN SYSTEM
# --------------------------------------------------

COBALT = "#2349F5"
TEAL = "#23B9B0"
NAVY = "#101827"
DEEP_OCEAN = "#122E3B"
MUTED = "#64748B"
BACKGROUND = "#F2F3F5"
WHITE = "#FFFFFF"

QUALITY_COLORS = {
    "Good": "#23B88E",
    "Moderate": "#E5B64B",
    "Poor": "#F08052",
    "Potential Dead Zone": "#E05262"
}

st.markdown(
    """
    <style>
    .stApp {
        background: #F2F3F5;
        color: #101827;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 1.2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #101827;
        font-weight: 750;
        letter-spacing: -0.035em;
    }

    h3 {
        margin-top: 0.4rem;
    }

    hr {
        border-color: #DCE3EA;
        margin: 1.5rem 0;
    }

    /* Hero section */
    .hero {
        background: linear-gradient(
            115deg,
            #101827 0%,
            #122E3B 70%,
            #174653 100%
        );
        padding: 42px 46px;
        border-radius: 22px;
        margin-bottom: 20px;
        position: relative;
        overflow: hidden;
    }

    .hero::after {
        content: "";
        position: absolute;
        right: -70px;
        top: -110px;
        width: 340px;
        height: 340px;
        border: 1px solid rgba(35, 213, 197, 0.18);
        border-radius: 50%;
        pointer-events: none;
    }

    .hero-eyebrow {
        color: #23D5C5;
        font-size: 12px;
        font-weight: 750;
        letter-spacing: 3px;
        margin-bottom: 18px;
    }

    .hero-title {
        color: #FFFFFF;
        font-size: clamp(32px, 4vw, 52px);
        font-weight: 850;
        line-height: 1.12;
        letter-spacing: -2px;
    }

    .hero-accent {
        color: #23D5C5;
    }

    .hero-description {
        color: #B8C3D4;
        font-size: 15px;
        margin-top: 18px;
        max-width: 650px;
    }

    .hero-footer {
        border-top: 1px solid #334457;
        margin-top: 28px;
        padding-top: 16px;
        color: #B8C3D4;
        font-size: 11px;
        letter-spacing: 2px;
    }

    /* Section headings */
    .section-eyebrow {
        color: #427D96;
        font-size: 11px;
        font-weight: 750;
        letter-spacing: 2px;
        margin-bottom: 5px;
    }

    .section-heading {
        color: #101827;
        font-size: 25px;
        font-weight: 800;
        letter-spacing: -0.7px;
        margin-bottom: 12px;
    }

    .section-description {
        color: #64748B;
        font-size: 13px;
        margin-bottom: 14px;
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid #E2E7EE;
        border-top: 4px solid #2349F5;
        border-radius: 17px;
        padding: 22px 23px;
        min-height: 148px;
        box-shadow: 0 5px 20px rgba(16, 24, 39, 0.045);
        transition: transform 0.2s ease,
                    box-shadow 0.2s ease;
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 28px rgba(16, 24, 39, 0.09);
    }

    div[data-testid="stMetricLabel"] {
        color: #64748B;
        font-size: 12px;
        font-weight: 750;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    div[data-testid="stMetricValue"] {
        color: #101827;
        font-size: clamp(22px, 2.3vw, 32px);
        font-weight: 850;
        letter-spacing: -1px;
    }

    /* Filter and table */
    div[data-testid="stSelectbox"] > div {
        border-radius: 12px;
    }

    div[data-testid="stDataFrame"] {
        border: 1px solid #E2E7EE;
        border-radius: 14px;
        overflow: hidden;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #101827;
    }

    /* Small screens */
    @media (max-width: 768px) {
        .hero {
            padding: 28px 24px;
        }

        .hero-title {
            letter-spacing: -1px;
        }

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# REUSABLE DISPLAY FUNCTIONS
# --------------------------------------------------

def section_heading(number, eyebrow, title, description=""):
    description_html = ""

    if description:
        description_html = (
            f'<div class="section-description">'
            f'{html.escape(description)}</div>'
        )

    st.markdown(
        f"""
        <div class="section-eyebrow">
            {html.escape(number)} / {html.escape(eyebrow)}
        </div>
        <div class="section-heading">
            {html.escape(title)}
        </div>
        {description_html}
        """,
        unsafe_allow_html=True
    )


def style_chart(fig, height=320):
    fig.update_layout(
        height=height,
        paper_bgcolor=WHITE,
        plot_bgcolor=WHITE,
        font=dict(
            family="Arial, sans-serif",
            color=NAVY,
            size=12
        ),
        margin=dict(l=30, r=25, t=40, b=45),
        showlegend=False,
        xaxis=dict(
            showgrid=False,
            automargin=True,
            linecolor="#E2E7EE"
        ),
        yaxis=dict(
            gridcolor="#E8EDF3",
            zeroline=False,
            automargin=True
        )
    )

    return fig


def create_performance_chart(
    data, column, title, color, unit
):
    fig = px.bar(
        data,
        x="location",
        y=column,
        text=column,
        labels={
            "location": "Location",
            column: unit
        }
    )

    fig.update_traces(
        marker_color=color,
        marker_line_width=0,
        texttemplate="%{text:.2f}",
        textposition="outside",
        cliponaxis=False,
        hovertemplate=(
            "<b>%{x}</b><br>"
            + unit
            + ": %{y:.2f}<extra></extra>"
        )
    )

    style_chart(fig, height=310)

    fig.update_layout(
        title=dict(
            text=title,
            font=dict(size=16, color=NAVY),
            x=0.02
        ),
        margin=dict(l=35, r=25, t=65, b=55),
        xaxis_title=None,
        yaxis_title=unit
    )

    fig.update_yaxes(rangemode="tozero")

    return fig


st.markdown(
    """
<div class="hero">
    <div class="hero-eyebrow">◉ SIGNAL / INTELLIGENCE</div>
    <div class="hero-title">See the signal.</div>
    <div class="hero-title hero-accent">Find the blind spots.</div>
    <div class="hero-description">
        Campus Wi-Fi Dead-Zone Intelligence System
        <br>
        Monitor signal strength, network performance,
        and connectivity issues across campus.
    </div>
    <div class="hero-footer">NETWORK ANALYTICS PLATFORM</div>
</div>
    """,
    unsafe_allow_html=True
)


try:
    df = get_wifi_readings()

except Exception as error:
    st.error("Unable to retrieve Wi-Fi readings.")
    st.exception(error)
    st.stop()

if df.empty:
    st.warning(
        "No Wi-Fi readings are available yet. "
        "Collect readings to populate the dashboard."
    )
    st.stop()


# --------------------------------------------------
# LOCATION FILTER
# --------------------------------------------------

section_heading(
    "01",
    "DATA EXPLORER",
    "Explore Network Data",
    "Choose a campus location to update all analytics."
)

available_locations = sorted(
    df["location"].dropna().unique().tolist()
)

filter_col, info_col = st.columns([2, 3])

with filter_col:
    selected_location = st.selectbox(
        "Location",
        ["All Locations"] + available_locations,
        key="dashboard_location_filter"
    )

if selected_location != "All Locations":
    df = df[
        df["location"] == selected_location
    ].copy()
else:
    df = df.copy()

with info_col:
    st.write("")
    st.info(
        f"Showing {len(df)} readings "
        f"for {selected_location}."
    )

st.divider()


# --------------------------------------------------
# NETWORK OVERVIEW
# --------------------------------------------------

section_heading(
    "02",
    "LIVE DATA SUMMARY",
    "Network Overview",
    "Key performance indicators from collected measurements."
)

total_readings = len(df)
average_signal = df["signal_strength"].mean()
average_latency = df["latency_ms"].mean()
average_packet_loss = df["packet_loss_percent"].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Readings",
        f"{total_readings:,}",
        help="Number of recorded Wi-Fi measurements."
    )

with col2:
    st.metric(
        "Average Signal",
        f"{average_signal:.1f}%",
        help="Average reported Wi-Fi signal strength."
    )

with col3:
    st.metric(
        "Average Latency",
        f"{average_latency:.1f} ms",
        help="Average measured network response time."
    )

with col4:
    st.metric(
        "Packet Loss",
        f"{average_packet_loss:.1f}%",
        help="Average packet loss across readings."
    )

st.divider()


# --------------------------------------------------
# WI-FI QUALITY DISTRIBUTION
# --------------------------------------------------

section_heading(
    "03",
    "CONNECTION HEALTH",
    "Wi-Fi Quality Distribution",
    "How recorded readings are classified by network quality."
)

if "wifi_quality" in df.columns:

    quality_counts = (
        df["wifi_quality"]
        .value_counts()
        .rename_axis("Quality")
        .reset_index(name="Readings")
    )

    quality_fig = px.bar(
        quality_counts,
        x="Quality",
        y="Readings",
        color="Quality",
        color_discrete_map=QUALITY_COLORS,
        text="Readings",
        category_orders={
            "Quality": [
                "Good",
                "Moderate",
                "Poor",
                "Potential Dead Zone"
            ]
        }
    )

    quality_fig.update_traces(
        textposition="outside",
        marker_line_width=0,
        cliponaxis=False
    )

    style_chart(quality_fig, height=340)

    quality_fig.update_layout(
        xaxis_title=None,
        yaxis_title="Number of Readings",
        yaxis=dict(
            gridcolor="#E8EDF3",
            rangemode="tozero"
        )
    )

    st.plotly_chart(
        quality_fig,
        use_container_width=True
    )

else:
    st.warning(
        "Wi-Fi quality classification is not available."
    )

st.divider()


# --------------------------------------------------
# LOCATION-WISE ANALYSIS
# --------------------------------------------------

section_heading(
    "04",
    "CAMPUS PERFORMANCE",
    "Location Performance",
    "Compare signal quality and network performance by location."
)

location_stats = (
    df.groupby("location")
    .agg(
        average_signal=("signal_strength", "mean"),
        average_latency=("latency_ms", "mean"),
        average_packet_loss=(
            "packet_loss_percent", "mean"
        ),
        total_readings=("location", "count")
    )
    .reset_index()
    .round(2)
)

location_display = location_stats.rename(
    columns={
        "location": "Location",
        "average_signal": "Avg Signal (%)",
        "average_latency": "Avg Latency (ms)",
        "average_packet_loss": "Avg Packet Loss (%)",
        "total_readings": "Readings"
    }
)

st.dataframe(
    location_display,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Avg Signal (%)": st.column_config.NumberColumn(
            "Avg Signal (%)",
            format="%.1f%%"
        ),
        "Avg Latency (ms)": st.column_config.NumberColumn(
            "Avg Latency (ms)",
            format="%.2f ms"
        ),
        "Avg Packet Loss (%)": st.column_config.NumberColumn(
            "Avg Packet Loss (%)",
            format="%.1f%%"
        )
    }
)

st.markdown("#### Network Performance Comparison")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    signal_fig = create_performance_chart(
        location_stats,
        "average_signal",
        "Average Signal Strength",
        COBALT,
        "Signal Strength (%)"
    )

    signal_fig.update_yaxes(range=[0, 110])

    st.plotly_chart(
        signal_fig,
        use_container_width=True
    )

with chart_col2:
    latency_fig = create_performance_chart(
        location_stats,
        "average_latency",
        "Average Latency",
        TEAL,
        "Latency (ms)"
    )

    st.plotly_chart(
        latency_fig,
        use_container_width=True
    )

packet_fig = create_performance_chart(
    location_stats,
    "average_packet_loss",
    "Average Packet Loss",
    "#427D96",
    "Packet Loss (%)"
)

packet_fig.update_yaxes(range=[0, 100])

st.plotly_chart(
    packet_fig,
    use_container_width=True
)

st.divider()


# --------------------------------------------------
# SIGNAL HEATMAP
# --------------------------------------------------

section_heading(
    "05",
    "SIGNAL VISUALIZATION",
    "Wi-Fi Signal Heatmap",
    "Average signal strength across recorded locations."
)

heatmap_data = (
    location_stats
    .set_index("location")[["average_signal"]]
    .T
)

heatmap_fig = px.imshow(
    heatmap_data,
    labels={
        "x": "Location",
        "y": "Measurement",
        "color": "Signal (%)"
    },
    color_continuous_scale=[
        [0.0, "#E05262"],
        [0.25, "#F08052"],
        [0.50, "#E5B64B"],
        [0.75, "#23B9B0"],
        [1.0, "#2349F5"]
    ],
    zmin=0,
    zmax=100,
    aspect="auto",
    text_auto=".1f"
)

heatmap_fig.update_layout(
    height=260,
    paper_bgcolor=WHITE,
    plot_bgcolor=WHITE,
    font=dict(color=NAVY),
    margin=dict(l=20, r=20, t=25, b=35),
    coloraxis_colorbar=dict(
        title="Signal (%)"
    )
)

heatmap_fig.update_xaxes(title=None)
heatmap_fig.update_yaxes(title=None)

st.plotly_chart(
    heatmap_fig,
    use_container_width=True
)

if len(location_stats) == 1:
    st.info(
        "Only one location is currently selected. "
        "Choose All Locations to compare locations."
    )

st.caption(
    "This visualization compares recorded locations. "
    "It is not yet a geographic campus heatmap."
)

st.divider()


# --------------------------------------------------
# COLLECTED WI-FI READINGS
# --------------------------------------------------

section_heading(
    "06",
    "MEASUREMENT LOG",
    "Collected Wi-Fi Readings",
    "Detailed records retrieved from MongoDB Atlas."
)

display_df = df.rename(
    columns={
        "location": "Location",
        "ssid": "Wi-Fi Network",
        "signal_strength": "Signal Strength (%)",
        "latency_ms": "Latency (ms)",
        "packet_loss_percent": "Packet Loss (%)",
        "packets_sent": "Packets Sent",
        "packets_received": "Packets Received",
        "timestamp": "Recorded At",
        "wifi_quality": "Wi-Fi Quality"
    }
).copy()

# Hide MongoDB's internal identifier if present.
display_df = display_df.drop(
    columns=["_id"],
    errors="ignore"
)

preferred_columns = [
    "Recorded At",
    "Location",
    "Wi-Fi Network",
    "Signal Strength (%)",
    "Latency (ms)",
    "Packet Loss (%)",
    "Wi-Fi Quality",
    "Packets Sent",
    "Packets Received"
]

display_df = display_df[
    [
        column for column in preferred_columns
        if column in display_df.columns
    ]
]

if "Recorded At" in display_df.columns:
    display_df = display_df.sort_values(
        "Recorded At",
        ascending=False
    )

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
    height=360,
    column_config={
        "Signal Strength (%)": st.column_config.ProgressColumn(
            "Signal Strength (%)",
            min_value=0,
            max_value=100,
            format="%.0f%%"
        ),
        "Latency (ms)": st.column_config.NumberColumn(
            "Latency (ms)",
            format="%.2f ms"
        ),
        "Packet Loss (%)": st.column_config.NumberColumn(
            "Packet Loss (%)",
            format="%.1f%%"
        ),
        "Wi-Fi Quality": st.column_config.TextColumn(
            "Wi-Fi Quality"
        )
    }
)

st.caption(
    f"{len(display_df)} measurement records displayed."
)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown(
    """
    <div style="
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 12px;
        padding: 10px 0 20px;
        color: #64748B;
        font-size: 12px;
    ">
        <span>
            CAMPUS WI-FI / SIGNAL INTELLIGENCE
        </span>
        <span>
            Python · Streamlit · Plotly · MongoDB Atlas
        </span>
    </div>
    """,
    unsafe_allow_html=True
)









