import streamlit as st
import json

st.set_page_config(page_title="Kuis Profesi by Dandi", page_icon="🧠", layout="centered")

# Load quiz data
with open("quiz_data.json", "r", encoding="utf-8") as f:
    quiz_data = json.load(f)

# State Initialization
if "answers" not in st.session_state:
    st.session_state.answers = [None] * len(quiz_data)
    st.session_state.index = 0
    st.session_state.submitted = False

# Reset Quiz
def restart():
    st.session_state.answers = [None] * len(quiz_data)
    st.session_state.index = 0
    st.session_state.submitted = False

# Modular scoring
def calculate_scores(answers, data):
    score = {}
    for i, ans in enumerate(answers):
        prof = data[i]['options'].get(ans)
        if prof:
            score[prof] = score.get(prof, 0) + 1
    return score

# UI
st.title("🎯 Mini Kuis Nentuin Profesi Kamu by Dandi")

idx = st.session_state.index
question = quiz_data[idx]

st.subheader(f"Pertanyaan {idx + 1} dari {len(quiz_data)}")
st.write(question["question"])
st.caption(question["information"])

# Radio Button per pertanyaan
options = list(question["options"].keys())
st.session_state.answers[idx] = st.radio(
    label="",
    options=options,
    index=options.index(st.session_state.answers[idx]) if st.session_state.answers[idx] else 0,
    key=f"radio_{idx}"
)

# Navigasi
col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    if idx > 0:
        st.button("⬅️ Sebelumnya", on_click=lambda: st.session_state.update(index=idx-1))
with col2:
    if idx < len(quiz_data) - 1:
        st.button("➡️ Selanjutnya", on_click=lambda: st.session_state.update(index=idx+1))
with col3:
    if idx == len(quiz_data) - 1:
        if None in st.session_state.answers:
            st.warning("🚫 Masih ada pertanyaan yang belum dijawab.")
        else:
            st.button("🎉 Submit Jawaban", on_click=lambda: st.session_state.update(submitted=True))

st.markdown("---")

# Hasil
if st.session_state.submitted:
    scores = calculate_scores(st.session_state.answers, quiz_data)
    max_score = max(scores.values())
    top_professions = [k for k, v in scores.items() if v == max_score]

    # Tentukan satu hasil secara sistematis jika seri: berdasarkan urutan kemunculan
    result = top_professions[0]

    st.success(f"🔥 Kamu cocok jadi **{result}**!")

    # Konten hasil
    gifs = {
        "Programmer": "https://media.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif",
        "Designer": "https://media.giphy.com/media/3o7TKMt1VVNkHV2PaE/giphy.gif",
        "Data Scientist": "https://media.giphy.com/media/3ov9jNziFTMfzSumAw/giphy.gif",
        "Startup Founder": "https://media.giphy.com/media/26BRrSvJUa0crqw4E/giphy.gif"
    }

    descriptions = {
        "Programmer": "Kamu suka menyusun logika, menyelesaikan masalah, dan membangun sistem dari nol.",
        "Designer": "Kamu punya mata tajam untuk estetika, dan ide visualmu bisa mengubah dunia.",
        "Data Scientist": "Kamu suka merangkai angka menjadi cerita dan menciptakan keputusan berbasis data.",
        "Startup Founder": "Kamu ambisius, suka kerja, dan punya semangat ngopi tanpa henti!"
    }

    funfacts = {
        "Programmer": "💻 Fun fact: Programmer bisa kerja dari mana aja... kecuali dari masa lalu.",
        "Designer": "🎨 Designer punya 1000 font, tapi tetap pakai Helvetica.",
        "Data Scientist": "📊 Banyak Data Scientist menggunakan Python dan... kopi! ☕",
        "Startup Founder": "🚀 Founder sejati kerja 20 jam sehari dan sisanya buat pitching."
    }

    st.image(gifs.get(result, ""), width=300)
    st.info(descriptions.get(result, ""))
    st.markdown(f"**Fun Fact:** {funfacts.get(result, '')}")

    st.markdown("---")
    st.button("🔁 Mulai Ulang", on_click=restart)