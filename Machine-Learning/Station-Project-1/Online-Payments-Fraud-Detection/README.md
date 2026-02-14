\*Dataset link: https://www.kaggle.com/datasets/ealaxi/paysim1?resource=download\*



Project Overview



This project demonstrates how machine learning can be used to detect online payment fraud. Using historical transaction data, the model predicts whether a given transaction is fraudulent. Machine learning enables businesses to proactively identify suspicious activities and minimize financial losses.



Dataset Description



The dataset contains transaction records with the following features:



step	Represents a unit of time where 1 step equals 1 hour

type	Type of online transaction (e.g., CASH\_OUT, PAYMENT)

amount	The transaction amount in dollars

nameOrig	Customer starting the transaction (dropped in preprocessing)

oldbalanceOrg	Customer's balance before the transaction

newbalanceOrig	Customer's balance after the transaction

nameDest	Recipient of the transaction (dropped in preprocessing)

oldbalanceDest	Recipient's initial balance before the transaction

newbalanceDest	Recipient's balance after the transaction

isFraud	Target variable indicating whether the transaction is fraudulent (1) or not (0)

Data Preprocessing



Columns nameOrig and nameDest were removed as they are identifiers and do not carry predictive value.



The type column was transformed into numerical format to be used in the machine learning model.



Data Visualization



Two types of visualizations were created using Plotly Express:



Scatter plot: amount vs oldbalanceOrg, colored by isFraud

Pie chart: Distribution of fraudulent vs non-fraudulent transactions



Model Training

Model used: Linear Regression



Reason for choice: Simple, interpretable, and works for binary classification when thresholded (0.5).



Training method: Dataset split into 80% training and 20% testing using train\_test\_split.

Model Evaluation



Accuracy: Calculated using accuracy\_score from scikit-learn



The model achieves an accuracy of score, correctly identifying fraudulent and non-fraudulent transactions.



Usage



Clone the repository.

Install required packages:

\*pip install pandas numpy plotly scikit-learn\*

Run the notebook to explore data visualizations and model predictions.



Update the CSV dataset path if necessary.

