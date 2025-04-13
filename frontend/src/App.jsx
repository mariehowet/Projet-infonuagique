import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [data, setData] = useState("Chargement...");
  
  useEffect(() => {
    axios.get("/api/ping")
      .then(res => setData(res.data))
      .catch(() => setData("Erreur API"));
  }, []);

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>Test Frontend</h1>
      <p>Message du serveur : {data.message}</p>
      <p>Status de la db : {data.db_status ? "DB Up" : "DB Down"}</p>
    </div>
  );
}

export default App;
