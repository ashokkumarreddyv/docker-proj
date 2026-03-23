fetch(window.API_URL)
  .then(res => res.text())
  .then(data => {
    document.getElementById("data").innerHTML = data;
  })
  .catch(err => {
    document.getElementById("data").innerHTML = "Error: " + err;
  });