# 🎬 Movie Recommender System (ML Project)

A machine learning based **Movie Recommender System** that suggests movies similar to the one selected by the user.
This project demonstrates the complete ML pipeline — from **data cleaning** and **preprocessing**, to building a **content-based recommendation model**, and finally **deploying it as a web app** using **Streamlit** and **ngrok**.

---

## 📌 Features

* ✅ Data cleaning & preprocessing on raw dataset
* ✅ Content-based recommendation system using cosine similarity
* ✅ Pickle files (`.pkl`) used to transfer model & data between Jupyter Notebook and PyCharm
* ✅ Interactive website built using **Streamlit**
* ✅ Local server exposed with **ngrok** for external access

---

## 📂 Repository Structure

```
├── Movie-Recommendor-system.ipynb   # Notebook: data cleaning, preprocessing, model building
├── movies.pkl                       # Preprocessed movie features (vectors)
├── movie_dict.pkl                   # Dictionary mapping movie titles to metadata
├── app.py                           # Streamlit web application
├── run_app.py                       # Alternate script to run app
├── requirements.txt                 # Dependencies
├── setup.sh / Procfile / runtime.txt  # For deployment (Heroku/ngrok setup)
├── ngrok_connect.py                 # Script to connect local server via ngrok
├── Data.zip                         # Dataset (compressed)
└── Example.png / Example (2).png    # Screenshots of UI & recommendations
```

---

## ⚙️ Installation & Setup

1. Clone the repository

   ```bash
   git clone https://github.com/mangal-singh001/Movie-Recommender-System-ML-Project.git
   cd Movie-Recommender-System-ML-Project
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Unzip dataset (if required)

   ```bash
   unzip Data.zip
   ```

4. Run the Streamlit app

   ```bash
   streamlit run app.py
   ```

5. (Optional) Expose server with ngrok

   ```bash
   python ngrok_connect.py
   ```

---

## 🚀 How It Works

1. **Data Cleaning & Preprocessing**

   * Removed null values, duplicates, and unnecessary columns
   * Transformed text data (genres, tags, etc.) into numerical form

2. **Model Training (Content-Based)**

   * Used **cosine similarity** to find movies similar to the input
   * Stored processed features in `movies.pkl` and `movie_dict.pkl`

3. **Pickle Transfer**

   * Saved trained data into `.pkl` files in Jupyter Notebook
   * Loaded them into PyCharm for integration with the app

4. **Deployment**

   * Built web interface using **Streamlit**
   * Deployed locally & shared via **ngrok**

---

## 🎥 Screenshots

| Input Page         | Recommendation Results                  |
| ------------------ | --------------------------------------- |
| ![UI](Example.png) | ![Recommendations](Example%20\(2\).png) |

---

## 📌 Future Improvements

* Add **collaborative filtering** or **hybrid** models
* Improve UI with movie posters & search autocomplete
* Deploy permanently on **Heroku / Render / AWS**
* Handle larger datasets more efficiently

---

## 📝 License

This project is for **educational purposes** only.
You may use and modify it freely.

---
