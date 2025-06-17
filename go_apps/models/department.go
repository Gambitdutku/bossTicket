package models

type Department struct {
    ID   uint   `gorm:"primaryKey" json:"id"`
    Name string `gorm:"size:100;not null" json:"name"`
}

type Status struct {
    ID   uint   `gorm:"primaryKey" json:"id"`
    Name string `gorm:"size:50;not null" json:"name"`
}

type Organization struct {
    ID   uint   `gorm:"primaryKey" json:"id"`
    Name string `gorm:"size:100;not null" json:"name"`
}
