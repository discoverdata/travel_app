import streamlit as st
from agents.agents import agents
from tasks.tasks import create_tasks
from crewai import Crew, Process

st.title("🌍 AI Powered Travel Planner")

# --------------- INPUT FORM ---------------
with st.form("travel_form"):
    from_city = st.text_input("From:", value = 'Australia')
    to_city = st.text_input("To:", value = 'Bali')
    from_date = st.date_input("Date From:")
    to_date = st.date_input("Date To:")
    interests = st.text_area("Your interests:", value='sightseeing, good food, temples, water sports activities')

    submitted = st.form_submit_button("Plan my trip!")
# --------------- END OF FORM ---------------

if submitted:
    trip_info = {
        'from_city': from_city,
        'to_city': to_city,
        'from_date': from_date.strftime("%d %B %Y"),
        'to_date': to_date.strftime("%d %B %Y"),
        'interests' : interests
    }

    # Create tasks based on user input
    tasks = create_tasks(trip_info, agents)

    # Example: Create crew and run
    crew = Crew(
        agents = [agents['guide_expert'], agents['location_expert'], agents['planner_expert']],
        tasks = [tasks['guide_task'], tasks['location_task'], tasks['planner_task']],
        process = Process.sequential, 
        full_output = True, 
        verbose = True
    )
    with st.spinner('Planning your amazing trip... ✈️🌴'):
        result = crew.kickoff()

    location_result = tasks['location_task'].output
    guide_result = tasks['guide_task'].output
    planner_result = tasks['planner_task'].output

    st.success("✅ Your trip plan is ready!")
    # Show nice sections
    with st.expander("🌦️ Location Report"):
        st.markdown(location_result, unsafe_allow_html=True)

    with st.expander("🍽️ Interest-Based City Guide"):
        st.markdown(guide_result, unsafe_allow_html=True)

    with st.expander("📅 Travel Plan and Day-by-Day Itinerary"):
        st.markdown(planner_result, unsafe_allow_html=True)

    travel_plan_text = str(result.raw)

    st.download_button(
        label = "📥 Download your Travel Plan",
        data = travel_plan_text,
        file_name=f"Travel_Plan_{to_city}.txt",
        mime = "text/plain"
        )