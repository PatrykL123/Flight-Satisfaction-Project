Airline Passenger Satisfaction Project

Project Overview

The goal of this project is to analyze and predict airline passenger satisfaction using logistic regression. 
The project involves data preprocessing, model training, making predictions on new data, integrating the results with a MySQL database, and visualizing and analyzing the results using Tableau.
---------------------------------------------------------------------------------------------------------------------------------------

Project Structure

Data Files:

- airline_passenger_satisfaction.csv: Raw dataset containing various features related to passenger satisfaction.

- flight_satisfaction_preprocessed.csv: Preprocessed data used for training and testing the model.

- data_to_module.csv: New data used for making predictions with the created model and integrating with the MySQL database.

- data_dictionary.csv: A data dictionary file describing the variables in the dataset.

- raw_data_dictionary.txt and preprocessed_data_dictionary.txt: Data dictionaries for the raw and preprocessed data.

Jupyter Notebooks:

- DATA_PREPROCESSING.ipynb: Notebook for data cleaning, preprocessing, and feature engineering.

- data_ML.ipynb: Notebook for model training, evaluation, and hyperparameter tuning using logistic regression.

- Integration_with_mysql.ipynb: Notebook demonstrating how to integrate new data (data_to_module.csv) and model results with a MySQL database.

PDF Files:

- DATA_PREPROCESSING.pdf, data_ML.pdf, Integration_with_mysql.pdf, FS_VISUALIZATION.pdf: PDF versions of the Jupyter notebooks and visualizations.

Python Modules:

- satisfaction_module2.py: Custom Python module containing functions for data processing and predicting passenger satisfaction.

- modell and scalerr: Serialized logistic regression model and scaler object used for making predictions on passenger satisfaction.

Data Visualization and Analysis:

- FS_VISUALIZATION.twb: Tableau workbook file containing visualizations and analyses of the data, presenting key insights from the conducted analysis.

-------------------------------------------------------------------------------------------------------------------

Installation and Setup (!!UIF YOU WANT YOU CAN JUST CHECK PDFs SUBSTITUTES!!!)

Clone the Repository:

git clone <repository-url>
cd <repository-directory>

Database Setup:

Ensure you have MySQL installed and running.
Update the database configuration in the Integration_with_mysql.ipynb file to match your MySQL setup.
Run the notebook to create the necessary tables and populate them with data.

---------------------------------------------------------------------------------------------------------------------

Usage

Data Preprocessing:

Run the DATA_PREPROCESSING.ipynb notebook to clean and preprocess the raw data.
The processed data will be saved as flight_satisfaction_preprocessed.csv.

Model Training and Evaluation:

Use the data_ML.ipynb notebook to train a logistic regression model on the preprocessed data.
The notebook includes sections for evaluating model performance and tuning hyperparameters.

Prediction and Database Integration:

The new data from data_to_module.csv can be used to make predictions using the trained model(like in integration_with_mysql file).
Run the Integration_with_mysql.ipynb notebook to integrate these data and prediction results with a MySQL database.

Visualization and Analysis
(You can check the visualization under the link: https://public.tableau.com/app/profile/patryk.lewandowski7453/viz/Book2_17245195125680/Story1
or in pdf file):

Explore the Tableau workbook (FS_VISUALIZATION.twb) to view visualizations and analyses of the prediction results and passenger satisfaction data.
