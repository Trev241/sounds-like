import "./style.css";
import viteLogo from "/vite.svg";
import axios from "axios";

document.querySelector("#app").innerHTML = `
  <div>
    <p class="read-the-docs">
      hello from frontend react
    </p>
    <button id="fetchData">Fetch Data from Flask</button>
    <pre id="response"></pre>
  </div>
`;

document.querySelector("#fetchData").addEventListener("click", async () => {
  try {
    const response = await axios.get("http://127.0.0.1:5000/predict");
    document.querySelector("#response").textContent = JSON.stringify(response.data, null, 2);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
});