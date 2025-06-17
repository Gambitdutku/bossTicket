package handlers

import (
    "strconv"
    "time"
    "github.com/gofiber/fiber/v2"
    "go_apps/database"
    "go_apps/models"
)

func CreateTicket(c *fiber.Ctx) error {
    var ticket models.Ticket

    // Parse request body into ticket struct
    if err := c.BodyParser(&ticket); err != nil {
        return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
            "error": "Invalid request body",
        })
    }

    // Ensure 'source' is one of the allowed ENUM values
    validSources := map[string]bool{
        "Web": true, "Email": true, "Phone": true, "API": true, "Other": true,
    }

    // Apply default or validate
    if ticket.Source == "" {
        ticket.Source = "API" // Set default source
    } else if !validSources[ticket.Source] {
        return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
            "error": "Invalid source value. Allowed: Web, Email, Phone, API, Other",
        })
    }

    // Save to DB
    if result := database.DB.Create(&ticket); result.Error != nil {
        return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
            "error": "Could not create ticket",
        })
    }

    return c.JSON(fiber.Map{"ticket": ticket})
}



func ListTickets(c *fiber.Ctx) error {
    var tickets []models.Ticket
    database.DB.Find(&tickets)
    return c.JSON(fiber.Map{"tickets": tickets})
}


func GetTicket(c *fiber.Ctx) error {
    id := c.Params("id")
    var ticket models.Ticket
    if result := database.DB.First(&ticket, id); result.Error != nil {
        return c.Status(fiber.StatusNotFound).JSON(fiber.Map{"error": "Ticket Doesn't exist"})
    }
    return c.JSON(fiber.Map{"ticket": ticket})
}


func ReplyTicket(c *fiber.Ctx) error {
    ticketID := c.Params("id")
    var req struct{ Message string `json:"message"` }
    if err := c.BodyParser(&req); err != nil {
        return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": "NO message"})
    }
    id, _ := strconv.ParseUint(ticketID, 10, 64)
    reply := models.TicketReply{
        TicketID: uint(id),
        Message:  req.Message,
        CreatedAt: time.Now().Unix(),
    }
    if result := database.DB.Create(&reply); result.Error != nil {
        return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": "Yanıt eklenemedi"})
    }
    return c.JSON(fiber.Map{"reply": reply})
}


func UpdateTicketStatus(c *fiber.Ctx) error {
    id := c.Params("id")
    var req struct{ StatusID uint `json:"status_id"` }
    if err := c.BodyParser(&req); err != nil {
        return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": "Durum ID eksik"})
    }
    if result := database.DB.Model(&models.Ticket{}).Where("id = ?", id).Update("status_id", req.StatusID); result.Error != nil {
        return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": "Durum güncellenemedi"})
    }
    return c.SendStatus(fiber.StatusOK)
}
