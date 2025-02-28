import "./style.css";
import viteLogo from "/vite.svg";

document.querySelector("#app").innerHTML = `
  <div>

    <p class="read-the-docs">
     hello world
    </p>
  </div>
`;

setupCounter(document.querySelector("#counter"));
