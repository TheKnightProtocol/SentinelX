import pandas as pd     
    
    def  train_anomaly_detector(feature_dataframe):
        # Ensure your dataframe contains only numerical features
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(feature_dataframe)

        # Isolation Forest is good for identifying outliers.
        # 'contamination' is the expected proportion of anomalies in your data.
        # You'll need to tune this or use other methods to set it.
        model = IsolationForest(contamination='auto', random_state=42)
        model.fit(scaled_features)
        return model, scaler

    def predict_anomalies(model, scaler, new_data_dataframe):
        scaled_new_data = scaler.transform(new_data_dataframe)
        # predict returns -1 for anomalies, 1 for normal
        # decision_function gives a score, lower means more anomalous
        new_data_dataframe['anomaly_score'] = model.decision_function(scaled_new_data)
        new_data_dataframe['is_anomaly'] = model.predict(scaled_new_data)
        return new_data_dataframe

    # Usage:
    # network_df = pd.DataFrame(your_extracted_network_features)
    # ml_features = network_df[['protocol_encoded', 'packet_length', 'num_connections_to_dest']].copy() # Example numerical features
    # anomaly_model, feature_scaler = train_anomaly_detector(ml_features)
    # results_df = predict_anomalies(anomaly_model, feature_scaler, ml_features)
    ```
