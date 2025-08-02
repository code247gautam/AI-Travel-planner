document.getElementById('plannerForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const city = document.getElementById('city').value.trim();
  const days = document.getElementById('days').value.trim();
  const budget = document.getElementById('budget').value.trim();

  if (!city || !days || !budget) {
    alert("Please fill all fields");
    return;
  }

  const data = { city, days, budget };
  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = '<p>Generating your travel plan...</p>';

  try {
    const response = await fetch('/plan', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    if (!response.ok) throw new Error('Error fetching plan from server');
    const json = await response.json();

    resultDiv.innerHTML = ''; // Clear previous result

    const cardContainer = document.createElement('div');
    cardContainer.className = 'card-container';
    resultDiv.appendChild(cardContainer);

    // Row 1: 1×4 layout
    const row1 = document.createElement('div');
    row1.className = 'card-row';
    cardContainer.appendChild(row1);

    row1.appendChild(createCard('📍 Destination', json.destination));
    row1.appendChild(createCard('📅 Duration', `${json.days} days`));
    row1.appendChild(createCard('💰 Budget', `₹${json.budget}`));
    row1.appendChild(createCard('🌦️ Weather', json.weather));

    // Row 2: Full-width Itinerary
    cardContainer.appendChild(createCard('🗺️ Itinerary', json.itinerary));

    // Row 3: 1×2 layout
    const row3 = document.createElement('div');
    row3.className = 'card-row';
    cardContainer.appendChild(row3);

    row3.appendChild(createCard('🧾 Budget Breakdown', json.budget_plan));
    row3.appendChild(createCard('🎒 Travel Tips', json.tips));

  } catch (error) {
    resultDiv.innerHTML = '<p>Failed to get travel plan. Please try again later.</p>';
    console.error(error);
  }
});

function createCard(title, content) {
  const card = document.createElement('div');

  const normalized = title.replace(/[^\w\s]|_/g, "").toLowerCase();
  if (normalized.includes('itinerary')) {
    card.className = 'info-card wide-card';
  } else {
    card.className = 'info-card';
  }

  const heading = document.createElement('h3');
  heading.textContent = title;
  heading.className = 'card-title';
  card.appendChild(heading);

  if (Array.isArray(content)) {
    const list = document.createElement('ul');
    content.forEach(item => {
      const li = document.createElement('li');
      li.textContent = item;
      list.appendChild(li);
    });
    card.appendChild(list);
  } else if (typeof content === 'object') {
    const list = document.createElement('ul');
    for (const [key, value] of Object.entries(content)) {
      const li = document.createElement('li');
      li.textContent = `${key}: ₹${value}`;
      list.appendChild(li);
    }
    card.appendChild(list);
  } else {
    const paragraph = document.createElement('p');
    paragraph.textContent = content;
    card.appendChild(paragraph);
  }

  return card;
}
