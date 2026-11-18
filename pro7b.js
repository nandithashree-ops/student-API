const express = require("express");
const app = express();

app.use(express.json());

let tasks = [];

// Add a task
app.post("/tasks", (req, res) => {
    const { title, status } = req.body;

    // Validation
    if (!title || typeof title !== "string" || title.trim() === "") {
        return res.status(400).json({
            error: "Title is required and must be a non-empty string"
        });
    }

    const validStatuses = ["pending", "in-progress", "completed"];

    if (!status || !validStatuses.includes(status)) {
        return res.status(400).json({
            error: "Status must be pending, in-progress, or completed"
        });
    }

    // Add task
    tasks.push({
        title: title.trim(),
        status: status
    });

    res.status(201).json({
        message: "Task added successfully"
    });
});

// Get all tasks
app.get("/tasks", (req, res) => {
    res.json(tasks);
});

// Start server
app.listen(3000, () => {
    console.log("Server running on port 3000");
});
