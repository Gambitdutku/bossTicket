package routes

import (
    "github.com/gofiber/fiber/v2"
    "go_apps/handlers"
)

func SetupTicketRoutes(app *fiber.App) {
    app.Post("/tickets", handlers.CreateTicket)
    app.Get("/tickets", handlers.ListTickets)
    app.Get("/tickets/:id", handlers.GetTicket)
    app.Post("/tickets/:id/reply", handlers.ReplyTicket)
    app.Patch("/tickets/:id/status", handlers.UpdateTicketStatus)
}
