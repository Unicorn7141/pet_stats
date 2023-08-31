import streamlit as st
from streamlit_option_menu import option_menu

from pet import Pet


# --- SETTINGS ---
page_title = "Pet Stats Calculator"
page_icon = ":abacus:"
layout = "centered"


st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(f"{page_title} {page_icon}")

# --- HIDE STREAMLIT STYLING ---
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""

# st.markdown(hide_st_style, unsafe_allow_html=True)


# --- MENU BAR ---
menu = option_menu(
    menu_title=None,
    options=["Fill Stats", "View Results"],
    icons=["pencil-fill", "person-vcard-fill"],
    orientation="horizontal",
)

# --- PET STATS INPUT ---
st.session_state["pet"] = Pet()
if menu == "Fill Stats":
    with st.form("pet_stats"):
        with st.expander("Pet's Stats"):
            strength = st.number_input("Strength:", 1, 255, 200, key="strength")
            intellect = st.number_input("Intellect:", 1, 250, 200, key="intellect")
            agility = st.number_input("Agility:", 1, 260, 200, key="agility")
            will = st.number_input("Will:", 1, 260, 200, key="will")
            power = st.number_input("Power:", 1, 250, 200, key="power")

        with st.expander("Selfish Talents"):
            for talent in st.session_state["pet"].selfish_talents.keys():
                st.checkbox(talent, key=talent)

        submitted = st.form_submit_button("Calculate Talents")
        if submitted:
            pet = Pet(strength, agility, intellect, will, power)
            for talent in pet.selfish_talents.keys():
                if st.session_state[talent]:
                    bonus = pet.selfish_talents[talent]
                    for key, value in bonus.items():
                        pet.stats[key] += value
            pet.load_talents()
            st.session_state["pet"] = pet
            st.success("Results available!")

elif st.session_state["pet"]:
    pet = st.session_state["pet"]
    for category, talents in pet.talents.items():
        st.header(category)
        cols = st.columns(len(talents.items()))
        i = 0
        for name, value in talents.items():
            cols[i].metric(label=name, value=value)
            i += 1

        "---"
