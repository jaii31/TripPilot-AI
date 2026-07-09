import streamlit as st

from app.services.llm_service import LLMService
from app.memory.session_memory import mission


def render_trip_copilot():

    st.divider()

    st.header("🤖 TripPilot AI Copilot")

    st.caption(
        "Ask questions about your route, budget, "
        "activities, accommodation, weather or packing."
    )

    col1, col2 = st.columns(
        [4, 1]
    )

    with col2:

        if st.button(
            "Clear chat",
            use_container_width=True
        ):
            
            st.session_state.chat_messages = []

            st.rerun()

    if "chat_messages" not in st.session_state:

        st.session_state.chat_messages = [
            {
                "role": "assistant",
                "content": (
                    "Your journey plan is ready. "
                    "How can I help you improve it?"
                )
            }
        ]

    for message in st.session_state.chat_messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )

    user_message = st.chat_input(
        "Ask TripPilot AI about your journey..."
    )

    if user_message:

        st.session_state.chat_messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        with st.chat_message("user"):

            st.markdown(user_message)

        with st.chat_message("assistant"):

            with st.spinner(
                "TripPilot agents are thinking..."
            ):

                try:

                    llm = LLMService()

                    answer = (
                        llm.generate_response(
                            user_message=user_message,
                            mission=mission,
                            chat_history=(
                                st.session_state
                                .chat_messages
                            )
                        )
                    )

                    st.markdown(answer)

                except Exception:

                    answer = (
                        "TripPilot AI is temporarily "
                        "unavailable. Please try again "
                        "in a moment."
                    )

                    st.warning(answer)

        st.session_state.chat_messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )