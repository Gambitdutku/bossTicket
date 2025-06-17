package routes

import (
    "github.com/gofiber/fiber/v2"
    "go_apps/handlers"
)

func SetupLookupRoutes(app *fiber.App) {
    app.Get("/departments", handlers.ListDepartments)
    app.Get("/statuses", handlers.ListStatuses)
    app.Get("/organizations", handlers.ListOrganizations)
}
