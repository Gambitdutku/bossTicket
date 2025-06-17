package models

type User struct {
    ID       uint   `gorm:"primaryKey" json:"id"`
    Name     string `gorm:"size:100;not null" json:"name" validate:"required"`
    Email    string `gorm:"size:100;unique;not null" json:"email" validate:"required,email"`
    Password string `gorm:"size:255" json:"-"` // Don't return
}
