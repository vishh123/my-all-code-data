const apiKey = "4a30cb6db3c1f0d01414599de5ca7495";
const apiUrl = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=";

const searchBtn = document.getElementById('btn');
const search = document.getElementById('search');
const weatherIcon = document.getElementById('weather-icon');

searchBtn.addEventListener('click', (event) => {
    event.preventDefault();
    checkWeather(search.value);
    forecastData(search.value);
});

async function checkWeather(city) {
    try {
        // Fix: Use proper template literals
        const response = await fetch(`${apiUrl}${city}&appid=${apiKey}`);
        if (!response.ok) throw new Error("City not found");
        const data = await response.json();
        // console.log("current weather:", data);

        // Set weather icon based on weather condition
        if (data.weather[0].main === "Clouds") {
            weatherIcon.src = "https://static.vecteezy.com/system/resources/previews/026/571/030/non_2x/weather-icon-with-sun-and-cloud-on-transparent-background-free-png.png";
        } else if (data.weather[0].main === "Clear") {
            weatherIcon.src = "https://static.vecteezy.com/system/resources/thumbnails/010/989/531/small_2x/hot-weather-3d-rendering-isolated-on-transparent-background-ui-ux-icon-design-web-and-app-trend-png.png";
        } else if (data.weather[0].main === "Rain") {
            weatherIcon.src = "https://www.freeiconspng.com/uploads/cloud-rain-weather-icon-25.png";
        } else if (data.weather[0].main === "Drizzle") {
            weatherIcon.src = "https://www.freeiconspng.com/uploads/cloud-rain-weather-icon-25.png";
        } else if (data.weather[0].main === "Mist") {
            weatherIcon.src = "https://cdn-icons-png.flaticon.com/512/4151/4151022.png";
        }

        document.querySelector('#weather').style.display = "block";

        document.getElementById('city').innerHTML = data.name;
        document.getElementById("temp").innerHTML = `${data.main.temp} °C`; // Fix: Proper template literal syntax
    } catch (error) {
        console.log("Error fetching current weather:", error);
        alert(error.message);
    }
}

async function forecastData(city) {
    try {
        // Fix: Use proper template literals and quotes
        const response = await fetch(`https://api.openweathermap.org/data/2.5/forecast?units=metric&q=${city}&appid=${apiKey}`);
        if (!response.ok) throw new Error("City not found");
        const data = await response.json();
        console.log("Forecast data:", data);

        const forecastContainer = document.getElementById('forecast');
        forecastContainer.innerHTML = ""; // Clear previous forecast data

        // Filter forecast for every 8th item (representing daily data)
        data.list.forEach((item, index) => {
            if (index % 8 === 0) {
                const forecastDiv = document.createElement("div");
                forecastDiv.innerHTML = `
                    <p>Date: ${item.dt_txt}</p>
                    <p>Temp: ${item.main.temp}°C</p>
                    <p>Weather: ${item.weather[0].description}</p>`;
                forecastContainer.appendChild(forecastDiv);
            }
        });
    } catch (error) {
        console.log("Error fetching forecast data:", error);
        alert(error.message);
    }
}
