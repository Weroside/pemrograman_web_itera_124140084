import React from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import { App, Provider } from "./App";
import "./styles.css";

createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <Provider>
        <App />
      </Provider>
    </BrowserRouter>
  </React.StrictMode>,
);
