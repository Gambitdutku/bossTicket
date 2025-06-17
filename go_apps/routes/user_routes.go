package routes

import (
    "github.com/gofiber/fiber/v2"
    "go_apps/handlers"
)

func SetupUserRoutes(app *fiber.App) {
    app.Post("/login", handlers.Login)
    app.Post("/register", handlers.CreateUser)

    // add JWT
    user := app.Group("/users")
    user.Get("/:id", handlers.GetUser)
}
