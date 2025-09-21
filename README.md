Absolutely! Here's a polished, professional README for your **House Price Prediction** project, modeled similarly to your Titanic README and including the accuracy:

---

# House Price Prediction - Django Web App 🏠

A web application that predicts house prices based on user input using a pre-trained ML model, built with Django and deployed with Gunicorn and Nginx.

![Python](https://img.shields.io/badge/Python-3.12-blue) ![Django](https://img.shields.io/badge/Django-5.2.6-green) ![AWS](https://img.shields.io/badge/AWS-EC2-orange) ![Accuracy](https://img.shields.io/badge/Accuracy-84%25-brightgreen)

---

## Overview

This is a **full-stack Django project** that predicts house prices using a **Random Forest Regression model** trained on historical data. It demonstrates the integration of **machine learning with web development** and **real-world deployment** on AWS.

---

## Features ✨

* User-friendly form to input house details (e.g., area, location, bedrooms)
* Pre-trained Machine Learning model predicts house price
* Display predicted price on a results page
* Responsive design using Django templates
* Deployed on AWS EC2 with Gunicorn and Nginx

---

## Screenshots 📸

1. **Home Page**  
![Home Page](https://github.com/user-attachments/assets/ab69f85b-ab90-401e-9399-887c34a83627)

2. **Prediction Result Page**  
![Result Page](https://github.com/user-attachments/assets/dda7744f-c5ed-4a0c-bef6-f2a2094fa397)

3. **Terminal / Deployment Logs**  
![Terminal](https://github.com/user-attachments/assets/e9532a06-895b-4cdd-9acb-67f8605cf341)


---

## Installation & Setup 🛠️

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction/house_prediction
```

2. **Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Run the development server locally**

```bash
python manage.py runserver
```

> Open `http://127.0.0.1:8000/` in your browser.

---

## Deployment 🚀

This project is deployed on an **AWS EC2 instance** using **Gunicorn** and **Nginx**:

1. **Gunicorn Service**

   * Configured as a `systemd` service
   * Runs Django app in the background

2. **Nginx Reverse Proxy**

   * Forwards HTTP requests to Gunicorn via Unix socket

3. **Important Notes**

   * `ALLOWED_HOSTS` must include your server IP or domain
   * Services need to be enabled with `systemctl` after instance reboot

---

## Model & Accuracy 📊

* **Model Used:** Random Forest Regressor
* **Accuracy:** 84% (R² score on test data)
* **Files:** `random_forest_model.pkl` (trained model), `scaler.pkl` (preprocessing)

---

## Project Structure 📂

```
house_prediction/       # Django project
├─ templates/          # HTML templates
├─ db.sqlite3           # SQLite database
├─ manage.py            # Django management script
├─ random_forest_model.pkl # Pre-trained ML model
├─ scaler.pkl           # Preprocessing scaler
├─ house_prediction.sock # Gunicorn socket for Nginx
```

---

## Key Learnings 🧠

This project demonstrates **real-world deployment and full-stack skills**:

* Integrating **ML models into Django** applications
* Deploying Django apps on **AWS EC2 with Gunicorn & Nginx**
* Debugging **502 Bad Gateway** and **permission issues**
* Configuring **systemd services for automatic startup**
* Organizing project structure and handling static & template files

> Shows hands-on experience bridging development, ML integration, and production deployment.

---

## License

MIT License © Atharva Sagane

---
