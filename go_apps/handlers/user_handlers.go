package handlers

import (
    "os"
    "time"
    "github.com/gofiber/fiber/v2"
    "golang.org/x/crypto/bcrypt"
    "github.com/golang-jwt/jwt/v5"
    "go_apps/database"
    "go_apps/models"
)


func CreateUser(c *fiber.Ctx) error {
    var user models.User
    if err := c.BodyParser(&user); err != nil {
        return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": "Geçersiz giriş verisi"})
    }

    hashed, err := bcrypt.GenerateFromPassword([]byte(user.Password), bcrypt.DefaultCost)
    if err != nil {
        return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": "Şifre işlenemedi"})
    }
    user.Password = string(hashed)

    if result := database.DB.Create(&user); result.Error != nil {
        return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": "Kullanıcı oluşturulamadı"})
    }
    user.Password = ""
    return c.JSON(fiber.Map{"user": user})
}

//
func Login(c *fiber.Ctx) error {
    var req struct {
        Email    string `json:"email"`
        Password string `json:"password"`
    }
    if err := c.BodyParser(&req); err != nil {
        return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": "Eksik kullanıcı bilgisi"})
    }

    var user models.User
    if result := database.DB.Where("email = ?", req.Email).First(&user); result.Error != nil {
        return c.Status(fiber.StatusUnauthorized).JSON(fiber.Map{"error": "Kullanıcı bulunamadı"})
    }

    if err := bcrypt.CompareHashAndPassword([]byte(user.Password), []byte(req.Password)); err != nil {
        return c.Status(fiber.StatusUnauthorized).JSON(fiber.Map{"error": "Geçersiz şifre"})
    }

    token := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
        "user_id": user.ID,
        "exp":     time.Now().Add(72 * time.Hour).Unix(),
    })
    jwtSecret := os.Getenv("JWT_SECRET")
    t, err := token.SignedString([]byte(jwtSecret))
    if err != nil {
        return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": "Token oluşturulamadı"})
    }
    return c.JSON(fiber.Map{"token": t})
}


func GetUser(c *fiber.Ctx) error {
    id := c.Params("id")
    var user models.User
    if result := database.DB.First(&user, id); result.Error != nil {
        return c.Status(fiber.StatusNotFound).JSON(fiber.Map{"error": "Kullanıcı bulunamadı"})
    }
    user.Password = ""
    return c.JSON(fiber.Map{"user": user})
}
