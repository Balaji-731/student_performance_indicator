📘 Student Performance Prediction – ML Project

A complete end-to-end Machine Learning project that predicts students’ Math Scores based on demographic and academic factors.
This project follows a production-grade architecture with modular components, pipelines, logging, custom exception handling, and artifact saving.

🚀 Project Features

✔ Modular ML Pipeline
✔ Data Ingestion
✔ Data Transformation (Encoding + Scaling)
✔ Model Training (Multiple Algorithms)
✔ Best Model Selection using R² Score
✔ Saved Artifacts (model.pkl + preprocessor.pkl)
✔ Prediction Pipeline for new data
✔ Professional Logging
✔ Custom Exception Handling
✔ Clean Folder Structure

📂 Project Structure
MLProject/
│
├── README.md
├── requirements.txt
├── setup.py
├── render.yaml
├── app.py                      
│
├── templates/
│   ├── index.html              
│   ├── home.html               
│
├── artifacts/
│   ├── train.csv
│   ├── test.csv
│   ├── preprocessor.pkl
│   └── model.pkl
│
├── src/
│   ├── exception.py
│   ├── logger.py
│   ├── utils.py
│   │
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   │
│   └── notebook/
│       └── data/stud.csv

🧠 How The System Works
🔹 1. Data Ingestion

        Reads raw CSV

        Splits into train/test

        Saves:

        artifacts/data.csv
        artifacts/train.csv
        artifacts/test.csv

🔹 2. Data Transformation

Handles missing values

        One-Hot Encoding for categorical features

        Standard scaling for numerical features

        Saves:

        artifacts/preprocessor.pkl

🔹 3. Model Training

        Trains multiple algorithms:

        Random Forest

        XGBoost

        Gradient Boosting

        CatBoost

        Linear Regression

        KNN

        Decision Tree

        AdaBoost

        Finds best model using R² score

        Saves:

        artifacts/model.pkl

🔹 4. Prediction Pipeline

        Takes user input → applies preprocessor → predicts Math Score.

⚙️ Installation
    Step 1 — Clone the repo
    git clone https://github.com/<your-username>/<repo-name>.git
    cd <repo-name>

    Step 2 — Create virtual environment
    conda create -n mlproject python=3.10 -y
    conda activate mlproject

    Step 3 — Install dependencies
    pip install -r requirements.txt

    ▶️ Running the Training Pipeline
    python -m src.pipeline.train_pipeline


    This will:

    ✔ Read data
    ✔ Transform data
    ✔ Train multiple ML models
    ✔ Save best model + preprocessor in /artifacts/

    🔍 Using the Prediction Pipeline

    Sample code:

    from src.pipeline.predict_pipeline import PredictPipeline, CustomData

    # Create custom input data
    data = CustomData(
        gender="female",
        race_ethnicity="group B",
        parental_level_of_education="bachelor's degree",
        lunch="standard",
        test_preparation_course="none",
        reading_score=90,
        writing_score=88
    )

    df = data.get_data_as_dataframe()

    predict_pipeline = PredictPipeline()
    prediction = predict_pipeline.predict(df)

    print("Predicted Math Score:", prediction)

📊 Technologies Used

    Python

    NumPy

    Pandas

    Scikit-Learn

    XGBoost

    CatBoost

    Matplotlib (optional)

    Logging Module

    Custom Exception Handling

🎉 Author

Porala Balaji
📧 poralabalaji@gmail.com

🎓 Computer Science Student
🚀 Exploring Machine Learning & AI