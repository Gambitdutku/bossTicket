package middleware

import (
    "github.com/gofiber/fiber/v2"
    jwtware "github.com/gofiber/jwt/v3"
)

func Protected() fiber.Handler {
    return jwtware.New(jwtware.Config{
        SigningKey:   []byte("coolestsecretjwtkeyever"),
        ErrorHandler: jwtError,
    })
}

func jwtError(c *fiber.Ctx, err error) error {
    return c.Status(fiber.StatusUnauthorized).JSON(fiber.Map{
        "error": "invalid token",
    })
}
