const express = require("express");
const cors = require("cors"); 

const app = express();
const PORT = 8000;

app.use(express.json());
app.use(cors());

app.get("/", (req, res) => {
  res.send("Server is running");
});

app.post("/chat", (req, res) => {
  const message = req.body.message;
  res.json({ reply: message });
});

app.get("/chat", (req, res) => {
  const message = req.query.message;

  if (!message) {
    return res.json({ reply: "No message provided" });
  }

  res.json({ reply: message });
});


app.listen(PORT,"0.0.0.0", () => {
  console.log(`Server started on port ${PORT}`);
});
