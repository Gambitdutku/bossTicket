package main

import (
    "log"
    "github.com/gofiber/fiber/v2"
    //jwtware "github.com/gofiber/contrib/jwt"
    "github.com/joho/godotenv"

    "go_apps/database"
    "go_apps/routes"
)

func main() {
    godotenv.Load(".env")

    database.Connect()

    app := fiber.New()

    /* jwtSecret := os.Getenv("JWT_SECRET")
    app.Use(jwtware.New(jwtware.Config{
        SigningKey:   []byte(jwtSecret),
        ErrorHandler: func(c *fiber.Ctx, err error) error {
            return c.Status(fiber.StatusUnauthorized).JSON(fiber.Map{"error": "Unvalid Token"})
        },
    }))
*/
    routes.SetupUserRoutes(app)
    routes.SetupTicketRoutes(app)
    routes.SetupLookupRoutes(app)

    log.Fatal(app.Listen(":3000"))
}
