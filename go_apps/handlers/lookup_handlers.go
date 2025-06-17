package handlers

import (
    "github.com/gofiber/fiber/v2"
    "go_apps/database"
    "go_apps/models"
)

func ListDepartments(c *fiber.Ctx) error {
    var list []models.Department
    database.DB.Find(&list)
    return c.JSON(fiber.Map{"departments": list})
}

func ListStatuses(c *fiber.Ctx) error {
    var list []models.Status
    database.DB.Find(&list)
    return c.JSON(fiber.Map{"statuses": list})
}

func ListOrganizations(c *fiber.Ctx) error {
    var list []models.Organization
    database.DB.Find(&list)
    return c.JSON(fiber.Map{"organizations": list})
}
