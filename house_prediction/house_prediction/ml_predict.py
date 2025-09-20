def prediction_model(area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus):
  import joblib
  x = [[area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus]]
  randomforest = joblib.load('random_forest_model.pkl')
  scaler = joblib.load('scaler.pkl')
  x_scaled = scaler.transform(x)
  prediction = randomforest.predict(x_scaled)
  return prediction[0]