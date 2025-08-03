
# 🌏 AI Travel Planner India

AI Travel Planner India is a simple web application built with **HTML, CSS, JavaScript**, and **Python (Flask)** that generates a travel plan based on your chosen destination city, number of days, and total budget. It uses the **OpenWeatherMap API** to fetch real-time weather data and dynamically generates itineraries and tips.



## 📁 Project Structure

├── app.py           # Main Flask backend server
<br>
├── index.html       # Frontend HTML UI
<br>
├── style.css        # Styling for the web app
<br>
├── app.js           # JavaScript for client-side interaction
<br>
├── README.md        # Project documentation


## 🚀 Features

* 🌦️ Live weather report from OpenWeatherMap
* 📍 Destination-based itineraries
* 💰 Intelligent budget breakdown
* 🧾 Real-time tips for Indian travelers
* 🎨 Responsive and modern UI design
* ⚡ Lightweight and easy to deploy with Flask


## 🔧 Requirements

* Python 3.x
* pip (Python package installer)
* OpenWeatherMap API Key (free from [https://openweathermap.org/api](https://openweathermap.org/api))


## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/code247gautam/AI-Travel-planner.git
   cd ai-travel-planner-india
   ```

2. **Install dependencies**

   ```bash
   pip install flask requests
   ```

3. **Set your OpenWeatherMap API Key**

   Replace the value of `WEATHER_API_KEY` in `app.py`:

   `python
   WEATHER_API_KEY = "YOUR_API_KEY_HERE"
   
4. **Run the server**

   ```cmd
   python app.py
   

5. **Visit the app in your browser**

   
   http://localhost:5000/


## 🧠 How It Works

1. User enters:

   * Destination city
   * Number of travel days
   * Total trip budget

2. On form submission:

   * JavaScript (`app.js`) sends a POST request to `/plan`.
   * Flask (`app.py`) processes the request:

     * Fetches weather using OpenWeatherMap API
     * Generates a random but realistic itinerary based on the city
     * Creates a smart budget breakdown
     * Selects random travel tips

3. The result is rendered back on the same page as styled cards.


## 🖼️ Screenshots

<img width="1917" height="756" alt="Screenshot 2025-08-02 191146" src="https://github.com/user-attachments/assets/e715e201-00c8-4a16-8eab-d3f701cdf670" />


## 🧪 Sample Input


  "city": "Goa",
  "days": 3,
  "budget": 15000

### ➡️ Sample Output


  "destination": "Goa",
  "days": 3,
  "budget": 15000,
  "weather": "Clear, 31°C",
  "itinerary": [
    "Day 1: Beach hopping",
    "Day 2: Nightlife",
    "Day 3: Water sports"
  
  "budget_plan": {
    "Stay": 7500.0,
    "Food": 3750.0,
    "Transport": 2250.0,
    "Miscellaneous": 1500.0,
    "Per Day Estimate": 5000.0

  "tips": [
    "Carry sunscreen and light clothes.",
    "Download offline maps before you travel.",
    "Book your return tickets in advance."


---

## 📝 License

This project is open-source and free to use. You can modify, share, and distribute it is only for educational purpose and gain knowledge

---

## 🙌 Acknowledgements

* [OpenWeatherMap API](https://openweathermap.org/)
* [Flask](https://flask.palletsprojects.com/)
* [Google Fonts (Poppins)](https://fonts.google.com/specimen/Poppins)

