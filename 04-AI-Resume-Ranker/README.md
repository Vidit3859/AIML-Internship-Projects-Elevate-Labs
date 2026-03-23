# 🤖 AI-Powered Resume Ranker

An NLP-based web application that automatically ranks candidate resumes based on their relevance to a given job description.

This project simulates a simplified **Applicant Tracking System (ATS)** used by HR teams to shortlist candidates efficiently.

---

## 🚀 Features

- Extracts text from PDF resumes  
- Performs NLP preprocessing using SpaCy  
- Converts text into numerical vectors using TF-IDF  
- Calculates similarity using cosine similarity  
- Automatically ranks multiple resumes  
- Flask-based web interface  
- Modern responsive UI  
- Download ranking report in CSV format  

---

## 🧠 How It Works

1. User enters a job description  
2. Uploads multiple resumes (PDF)  
3. System preprocesses resume text  
4. TF-IDF vectorization converts text into feature vectors  
5. Cosine similarity computes matching score  
6. Resumes are ranked based on relevance  
7. HR can download ranking report  

---

## 🛠️ Tech Stack

- Python  
- SpaCy  
- Scikit-learn  
- Flask  
- HTML & CSS  
- Pandas  
- PDFMiner  

---

## 📂 Project Structure

```
resume-ranker/
│
├── app.py
├── ranker.py
├── resumes/
├── templates/
│   └── index.html
├── static/
├── requirements.txt
└── ranking_report.csv
```

---

## ▶️ How to Run the Project

### Clone Repository

```
git clone https://github.com/Vidit3859/ai-resume-ranker.git
cd ai-resume-ranker
```

### Install Dependencies

```
pip install -r requirements.txt
```

### Download SpaCy Model

```
python -m spacy download en_core_web_sm
```

### Run Flask App

```
python app.py
```

### Open in Browser

```
http://127.0.0.1:5000
```

---

## 📊 Output

- Displays ranked resumes with similarity scores  
- Generates downloadable CSV report  

---

## 💡 Future Improvements

- Support DOCX resumes  
- OCR support for scanned resumes  
- Deep learning semantic similarity  
- Cloud deployment  

---

## 👨‍💻 Author

**Vidit Kumar**

AI & Web Development Enthusiast

- 📧 Email: vidit.kumar624@gmail.com  
- 🔗 LinkedIn: https://linkedin.com/in/viditkumar-in  
- 💻 GitHub: https://github.com/Vidit3859

---