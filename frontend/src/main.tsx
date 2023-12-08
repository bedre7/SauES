import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import "./index.css";
import SauESContextProvider from "./context/index.tsx";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <SauESContextProvider>
    <App />
  </SauESContextProvider>,
);
