import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model.sv"
model = pickle.load(open(filename, 'rb'))
# otwieramy wcześniej wytrenowany model

objawy_d = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5"}
choroby_d = {1: "0", 2: "1", 3: "2", 4: "3", 5: "4", 6: "5"}

# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem


def main():

    st.set_page_config(page_title="Tydzień powrotu do zdrowia!")
    overview = st.container()
    left, right = st.columns(2)
    prediction = st.container()

    st.image("https://thumbs.dreamstime.com/z/medical-healthcare-concept-top-view-toy-stethoscope-colorful-pen-syringe-blackboard-written-prevention-better-than-138420261.jpg")

    with overview:
        st.title("Tydzień powrotu do zdrowia!")
        st.text("Dane pacjenta:")

    with left:
        objawy_radio = st.radio("Liczba objawów", list(objawy_d.keys()),
                                format_func=lambda x: objawy_d[x])
        choroby_radio = st.radio("Ilość chorób współistniejących", list(
            choroby_d.keys()), format_func=lambda x: choroby_d[x])

    with right:
        wiek_slider = st.slider("Wiek", value=50, min_value=1, max_value=100)
        wzrost_slider = st.slider(
            "Wzrost", min_value=40, max_value=230, step=5)

    data = [[objawy_radio, choroby_radio,  wiek_slider, wzrost_slider]]
    cured = model.predict(data)
    s_confidence = model.predict_proba(data)

    with prediction:
        st.header("Czy dana osoba wyzrowieje? {0}".format(
            "Tak" if cured[0] == 1 else "Nie"))
        st.subheader("Pewność predykcji {0:.2f} %".format(
            s_confidence[0][cured][0] * 100))


if __name__ == "__main__":
    main()
