# Fun-project-1 --- 🧠 Mini Kuis Profesi by Dandi

A fun and interactive quiz app built using Streamlit to help users discover which profession suits them best — Programmer, Designer, Data Scientist, or even a Startup Founder!

# 🚀 Main Features
1. Modern and clean UI with per-question navigation
2. Interactive radio buttons to select answers
3. Auto-result based on highest score calculation
4. Animated GIFs and fun facts for each profession result
5. Option to restart the quiz anytime

# 🗂️ File Structure
```bash
├── app.py                 # Main Streamlit app
├── quiz_data.json         # Quiz data (questions and options)
└── README.md              # This documentation
```

# 🔧 How to Run
1. Clone the repository
```bash
git clone https://github.com/duaribusatu/fun-project-1---Mini-Quiz-Kepribadian
cd fun-project-1---Mini-Quiz-Kepribadian
```

2. Install dependencies
Make sure you have Python 3.8+ installed. Then install Streamlit:
```bash
pip install streamlit
``` 
3. Launch the app
```bash
streamlit run app.py
```
The app will open in your browser at:
```bash
http://localhost:8501
```

# 📄 quiz_data.json Format
This file contains the list of questions, explanations, and answer options. Each option maps to a profession category.

Example:
```[
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
```
You can freely add or remove questions as long as they follow this structure.

#🧠 Scoring Logic
1. Each answer adds a point to a specific profession.
2. The profession with the highest score is shown as the final result.
3. In the event of a tie, the first profession (by order of appearance) is selected — no randomness.

# 📸 Preview   
![image](https://github.com/user-attachments/assets/3dba7567-4ae1-44e6-b24d-b5f56b318c9b)

Result
![image](https://github.com/user-attachments/assets/4f1619e1-5359-4dbb-9190-29b12655c10a)

