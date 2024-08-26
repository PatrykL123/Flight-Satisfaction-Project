
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer 
from sklearn.base import BaseEstimator, TransformerMixin

# The custom scaler class 
class CustomScaler(BaseEstimator, TransformerMixin): 
    
    def __init__(self, columns, copy=True, with_mean=True, with_std=True):
        self.scaler = StandardScaler(copy, with_mean, with_std)
        self.columns = columns

    def fit(self, X, y=None):
        self.scaler.fit(X[self.columns])
        return self

    def transform(self, X, y=None, copy=None):
        init_col_order = X.columns
        X_scaled = pd.DataFrame(self.scaler.transform(X[self.columns]), columns=self.columns, index=X.index)
        X_not_scaled = X.loc[:, ~X.columns.isin(self.columns)]
        return pd.concat([X_not_scaled, X_scaled], axis=1)[init_col_order]

# special class for prediction
class flight_satisfaction_model():
      
    def __init__(self, model_file, scaler_file):
        # Read the 'model' and 'scaler' files 
        with open(model_file, 'rb') as model_file, open(scaler_file, 'rb') as scaler_file:
            self.reg = pickle.load(model_file)
            self.scaler = pickle.load(scaler_file)
            self.data = None

    # Take a data file (*.csv) and preprocess it 
    def load_and_clean_data(self, data_file):
        # Import the data
        df = pd.read_csv(data_file, delimiter=',')
        self.df_with_predictions = df.copy()

        # Drop the 'ID', 'Age' column
        df = df.drop(['ID', 'Age'], axis=1, errors='ignore')

        columns_to_check = ['Ease of Online Booking', 'Check-in Service', 'Online Boarding', 'Gate Location',
                            'On-board Service', 'Seat Comfort', 'Leg Room Service', 'Cleanliness', 
                            'Food and Drink', 'In-flight Service', 'In-flight Wifi Service', 
                            'In-flight Entertainment', 'Baggage Handling']

        # Ensure columns to check exist in the DataFrame
        missing_cols = [col for col in columns_to_check if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing columns: {', '.join(missing_cols)}")

        mask = df[columns_to_check].ne(0).all(axis=1)
        df = df[mask]

        # Handle missing values
        df = df.fillna(0)

        # Change arrival delay to int
        df['Arrival Delay'] = df['Arrival Delay'].astype(int)

        # Map categorical data
        gender_mapping = {'Male': 0, 'Female': 1}
        df['Gender'] = df['Gender'].map(gender_mapping)
        customer_type_mapping = {'First-time': 0, 'Returning': 1}
        df['Customer Type'] = df['Customer Type'].map(customer_type_mapping)
        type_travel_mapping = {'Business': 0, 'Personal': 1}
        df['Type of Travel'] = df['Type of Travel'].map(type_travel_mapping)

        # One-hot encoding for 'Class'
        class_columns = pd.get_dummies(df['Class'], prefix='Class')
        class_columns.columns = ['Business Class','Economy Class', 'Economy Plus Class']
        df = pd.concat([df, class_columns], axis=1)
        df = df.drop(['Class'], axis=1)

        # Reorder columns
        columns_order = ['Gender', 'Customer Type', 'Type of Travel', 'Business Class', 'Economy Class', 'Economy Plus Class',
                         'Flight Distance', 'Departure Delay', 'Arrival Delay', 
                         'Departure and Arrival Time Convenience', 'Ease of Online Booking',
                         'Check-in Service', 'Online Boarding', 'Gate Location', 
                         'On-board Service', 'Seat Comfort', 'Leg Room Service', 
                         'Cleanliness', 'Food and Drink', 'In-flight Service', 
                         'In-flight Wifi Service', 'In-flight Entertainment', 'Baggage Handling']
        df = df[columns_order]

        # Handle missing values after preprocessing
        imputer = SimpleImputer(strategy='mean')
        df = pd.DataFrame(imputer.fit_transform(df), columns=columns_order)
        
        #convert to int 
        df = df.apply(lambda col: pd.to_numeric(col, errors='ignore', downcast='integer') 
                      if col.name not in ['Probability', 'Prediction'] 
                      else col)
     

        # Store the preprocessed data
        self.preprocessed_data = df.copy()

        # Transform the data using the scaler
        self.data = self.scaler.transform(df)

    # Function to output the probability of a data point being 1
    def predicted_probability(self):
        if self.data is not None:  
            pred = self.reg.predict_proba(self.data)[:, 1]
            return pred
        
    # Function to output 0 or 1 based on the model
    def predicted_output_category(self):
        if self.data is not None:
            pred_outputs = self.reg.predict(self.data)
            return pred_outputs
        
    # Predict the outputs and the probabilities and add columns with these values at the end of the new data
    def predicted_outputs(self):
        if self.data is not None:
            self.preprocessed_data['Probability'] = self.reg.predict_proba(self.data)[:, 1]
            self.preprocessed_data['Prediction'] = self.reg.predict(self.data)
            return self.preprocessed_data