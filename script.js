async function getSuggestion() {
  const income = document.getElementById('income').value;
  const expense = document.getElementById('expense').value;
  const res = await fetch('/suggest', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({income, expense})
  });
  const data = await res.json();
  document.getElementById('result').innerText = data.suggestion;
}
