fun-project-1 --- 🧠 Mini Kuis Profesi by Dandi

A fun and interactive quiz app built using Streamlit to help users discover which profession suits them best — Programmer, Designer, Data Scientist, or even a Startup Founder!

🚀 Main Features
1. Modern and clean UI with per-question navigation
2. Interactive radio buttons to select answers

Single Submit action at the end, not per question

Auto-result based on highest score calculation

Animated GIFs and fun facts for each profession result

Option to restart the quiz anytime

🗂️ File Structure
bash
Copy
Edit
├── kuis_profesi.py        # Main Streamlit app
├── quiz_data.json         # Quiz data (questions and options)
└── README.md              # This documentation
🔧 How to Run
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/username/kuis-profesi-dandi.git
cd kuis-profesi-dandi
2. Install dependencies
Make sure you have Python 3.8+ installed. Then install Streamlit:

bash
Copy
Edit
```bash
pip install streamlit
``` 
3. Launch the app
bash
Copy
Edit
streamlit run kuis_profesi.py
The app will open in your browser at:

arduino
Copy
Edit
http://localhost:8501
📄 quiz_data.json Format
This file contains the list of questions, explanations, and answer options. Each option maps to a profession category.

Example:

json
Copy
Edit
[
  {
    "question": "What do you enjoy the most?",
    "information": "Choose the option that best describes you",
    "options": {
      "Building simple applications": "Programmer",
      "Creating digital illustrations": "Designer",
      "Analyzing Excel data": "Data Scientist",
      "Pitching startup ideas": "Startup Founder"
    }
  }
]
You can freely add or remove questions as long as they follow this structure.

🧠 Scoring Logic
Each answer adds a point to a specific profession.

The profession with the highest score is shown as the final result.

In the event of a tie, the first profession (by order of appearance) is selected — no randomness.

📸 Preview
(You can add a screenshot or GIF of the app UI here)

    
