## *📧 Spam Email Detection System*

A machine learning web application that classifies messages as Spam or Not Spam (Ham) using Natural Language Processing (NLP) techniques.

The project uses TF-IDF Vectorization and the Multinomial Naive Bayes algorithm to detect spam messages with high accuracy.

## *🚀 Features*

📩 Detects whether a message is spam or not
🧠 Uses Machine Learning for prediction
🔤 Converts text into numerical features using TF-IDF
🌐 Interactive web interface built with Flask
💾 Saves the trained model for reuse
⚡ Real-time predictions

## *🛠️ Technologies Used*
Python
Flask
Pandas
Scikit-learn
Joblib
HTML
CSS

## *📂 Project Structure*
spam-detection/
│
├── app.py
├── train_model.py
├── spam.csv
├── model.pkl
├── vectorizer.pkl
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

## *📊 Dataset*

This project uses the SMS Spam Collection Dataset.

Total messages: 5,572
Ham messages: 4,825
Spam messages: 747

Dataset columns:

v1 → Label (ham or spam)
v2 → Message text


## *🧠 Machine Learning Workflow*

Load the dataset
Remove unnecessary columns
Rename columns
Convert labels (ham → 0, spam → 1)
Split the dataset into training and testing sets
Convert text to numerical features using TF-IDF
Train the model using Multinomial Naive Bayes
Evaluate model performance
Save the model and vectorizer
Deploy using Flask


## *⚙️ Installation and Setup*

1. Clone the Repository
git clone <repository-url>
2. Navigate to the Project Directory
cd spam-detection
3. Install Dependencies
pip install flask pandas scikit-learn joblib openpyxl xlrd
4. Train the Model
python train_model.py

This generates:

model.pkl
vectorizer.pkl
5. Run the Flask Application
python app.py
6. Open the Browser

Visit:

http://127.0.0.1:5000

## *📈 Model Performance*
Algorithm: Multinomial Naive Bayes
Vectorization: TF-IDF
Accuracy: 96.68%
Classification Report
              precision    recall    f1-score

Ham (0)          0.96       1.00       0.98
Spam (1)         1.00       0.75       0.86

Overall Accuracy: 0.97

## *🖥️ Example Predictions*
Input
Congratulations! You won a free iPhone. Claim now!
Output
Spam ❌

Input
Hey, are we meeting tomorrow at 10 AM?
Output
Not Spam ✅

## *🔮 Future Enhancements*
📊 Display prediction confidence score
🌙 Add dark mode
📱 Improve mobile responsiveness
☁️ Deploy using Render or Railway
🗄️ Store prediction history in a database
📧 Support email file uploads
🎯 Learning Outcomes

Through this project, you will learn:

Data preprocessing with Pandas
Natural Language Processing basics
TF-IDF vectorization
Supervised machine learning
Model evaluation metrics
Saving and loading models with Joblib
Flask web development
Integrating machine learning with web applications

## *👩‍💻 Author*

Sowmya M
Machine Learning Enthusiast | Python Learner | Aspiring AI Engineer

## *📜 License*

This project is created for educational purposes and is free to use and modify.