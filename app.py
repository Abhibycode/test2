const express = require("express");
const app = express();

app.use(express.json());

let orders = [];

/* Health check for liveness + readiness */
app.get("/health", (req, res) => {
  res.status(200).send("OK");
});

/* Create a new order */
app.post("/orders", (req, res) => {
  const order = {
    id: orders.length + 1,
    item: req.body.item || "unknown",
    status: "PROCESSING",
    createdAt: new Date()
  };

  orders.push(order);

  // Simulate async processing
  setTimeout(() => {
    order.status = "COMPLETED";
  }, 3000);

  res.status(201).json(order);
});

/* List all orders */
app.get("/orders", (req, res) => {
  res.json(orders);
});

const PORT = 6000;
app.listen(PORT, "0.0.0.0", () => {
  console.log(`Order service running on port ${PORT}`);
});
