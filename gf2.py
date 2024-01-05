def values():
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    from pathlib import Path

    script_dir = Path(__file__).resolve().parent
    print(script_dir)
    # Construct the full path to 'dataset.csv'
    file_path = script_dir / 'dataset.csv'

    # Load the dataset
    # Assuming the dataset is stored in a CSV file named 'green_finance_data.csv'
    data = pd.read_csv(file_path)

    # Convert 'Month' column to numerical values (optional)
    data['Month'] = pd.to_datetime(data['Month'], format='%b').dt.month

    # Separate the data by domain
    solar_data = data[data['Domain'] == 'Solar Power']
    hydro_data = data[data['Domain'] == 'Hydro Power']
    ev_data = data[data['Domain'] == 'EV Vehicles']
    wind_data = data[data['Domain'] == 'Wind Power']

    # Function to train a model and make predictions for a specific domain
    def predict_domain(data, target):
        # Features and target variable
        X = data[['Year', 'Month']]
        y = data[target]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize and train the model (Random Forest Regressor used as an example)
        model = RandomForestRegressor(random_state=42)
        model.fit(X_train, y_train)

        # Make predictions
        predictions = model.predict(X_test)

        # Return predictions for evaluation or further use
        return predictions

    # Example usage for Solar Power domain
    solar_predictions = predict_domain(solar_data, ['No. of Companies', 'No. of Loans Given', 'Success Rate (%)', 'Failure Rate (%)'])
    #print("Solar Power Predictions:", solar_predictions)

    # Similarly, repeat the process for other domains (Hydro Power, EV Vehicles, Wind Power)
    hydro_predictions = predict_domain(hydro_data, ['No. of Companies', 'No. of Loans Given', 'Success Rate (%)', 'Failure Rate (%)'])
    #print("Hydro Power Predictions:", hydro_predictions)

    ev_predictions = predict_domain(ev_data, ['No. of Companies', 'No. of Loans Given', 'Success Rate (%)', 'Failure Rate (%)'])
    #print("EV Predictions:", ev_predictions)

    wind_predictions = predict_domain(wind_data, ['No. of Companies', 'No. of Loans Given', 'Success Rate (%)', 'Failure Rate (%)'])
    #print("wind Power Predictions:", wind_predictions)
    
    return [solar_predictions,hydro_predictions,ev_predictions,wind_predictions]

