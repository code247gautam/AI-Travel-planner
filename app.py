from flask import Flask, request, jsonify, render_template_string, send_from_directory
import requests
import random

app = Flask(__name__)

WEATHER_API_KEY = "d37418f655596bc73fdb445cfd6ff49a"

DESTINATIONS = {
    "goa": ["Beach hopping", "Water sports", "Nightlife", "Old churches"],
    "jaipur": ["Amber Fort", "City Palace", "Johari Bazaar"],
    "kerala": ["Backwater tour", "Ayurvedic spa", "Tea garden walk"],
    "manali": ["Snow sports", "Mall Road shopping", "Solang Valley trek"],
    "ooty": ["Botanical Garden", "Tea Factory visit", "Boating at Ooty Lake"],
    "darjeeling": ["Toy Train Ride", "Tiger Hill sunrise", "Tea estate tour"]
}
TRAVEL_TIPS = [
    "Carry sunscreen and light clothes.",
    "Keep cash handy for local shopping.",
    "Try local street food!",
    "Download offline maps before you travel.",
    "Book your return tickets in advance."
]
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>AI Travel Planner India</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="main-wrapper">
    <!-- Form Box -->
    <div class="container">
      <h1>AI Travel Planner India</h1>
      <form id="plannerForm">
        <input type="text" id="city" placeholder="Destination City" required>
        <input type="number" id="days" placeholder="Number of Days" required>
        <input type="number" id="budget" placeholder="Total Budget (INR)" required>
        <button type="submit">Generate Plan</button>
      </form>
    </div>
    <!-- Result Box -->
    <div id="resultContainer">
      <h2>Your Travel Plan</h2>
      <div id="result"></div>
    </div>
  </div>
  <script src="app.js"></script>
</body>
</html>
'''

def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        condition = data['weather'][0]['description'].title()
        temp = data['main']['temp']
        return f"{condition}, {temp}°C"
    return "Weather data unavailable"

def generate_itinerary(destination, days):
    activities = DESTINATIONS.get(destination.lower(), ["Explore the city", "Visit local landmarks"])
    return [f"Day {i+1}: {random.choice(activities)}" for i in range(days)]

def generate_budget_plan(budget, days):
    return {
        "Stay": round(budget * 0.5, 2),
        "Food": round(budget * 0.25, 2),
        "Transport": round(budget * 0.15, 2),
        "Miscellaneous": round(budget * 0.10, 2),
        "Per Day Estimate": round(budget / days, 2)
    }

@app.route('/')
def index():
    return render_template_string(html_content)

@app.route('/style.css')
def serve_css():
    return send_from_directory('.', 'style.css')

@app.route('/app.js')
def serve_js():
    return send_from_directory('.', 'app.js')

@app.route('/plan', methods=['POST'])
def plan():
    data = request.json
    city = data['city']
    days = int(data['days'])
    budget = float(data['budget'])

    weather = fetch_weather(city)
    itinerary = generate_itinerary(city, days)
    budget_plan = generate_budget_plan(budget, days)
    tips = random.sample(TRAVEL_TIPS, 3)

    return jsonify({
        "destination": city.title(),
        "days": days,
        "budget": budget,
        "weather": weather,
        "itinerary": itinerary,
        "budget_plan": budget_plan,
        "tips": tips
    })

if __name__ == '__main__':
    app.run(debug=True)
