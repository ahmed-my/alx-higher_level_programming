#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2] || 'https://jsonplaceholder.typicode.com/todos';

// Make a GET request to the API
request.get(apiUrl, (error, response, body) => {
    if (error) {
        console.error(error);
    } else {
        // Parse the JSON response body
        const todos = JSON.parse(body);

        // Create a map to store the count of completed tasks for each user
        const completedTasksByUser = new Map();

        // Iterate through the todos and count completed tasks for each user
        todos.forEach(todo => {
            if (todo.completed) {
                const userId = todo.userId;
                completedTasksByUser.set(userId, (completedTasksByUser.get(userId) || 0) + 1);
            }
        });

        // Print users with completed tasks
        console.log('Users with completed tasks:');
        completedTasksByUser.forEach((count, userId) => {
            console.log(`User ${userId}: ${count} completed tasks`);
        });
    }
});

