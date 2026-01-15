const express = require("express");
const app = express();
const PORT = 8000;

app.use(express.json());

app.get("/", (req, res) => {
  res.send("Server is running");
});

app.post("/chat", (req, res) => {
  const message = req.body.message;
  res.json({ reply: message });
});

app.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);
});
