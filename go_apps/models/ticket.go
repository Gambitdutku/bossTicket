package models

import (
    "time"
)

type Ticket struct {
    TicketID    uint       `gorm:"primaryKey;column:ticket_id" json:"ticket_id"`
    TicketPID   *uint      `gorm:"column:ticket_pid" json:"ticket_pid,omitempty"`
    Number      *string    `gorm:"column:number;size:20" json:"number,omitempty"`
    UserID      uint       `gorm:"column:user_id" json:"user_id"`
    UserEmailID uint       `gorm:"column:user_email_id" json:"user_email_id"`
    StatusID    uint       `gorm:"column:status_id" json:"status_id"`
    DeptID      uint       `gorm:"column:dept_id" json:"dept_id"`
    SlaID       uint       `gorm:"column:sla_id" json:"sla_id"`
    TopicID     uint       `gorm:"column:topic_id" json:"topic_id"`
    StaffID     uint       `gorm:"column:staff_id" json:"staff_id"`
    TeamID      uint       `gorm:"column:team_id" json:"team_id"`
    EmailID     uint       `gorm:"column:email_id" json:"email_id"`
    LockID      uint       `gorm:"column:lock_id" json:"lock_id"`
    Flags       uint       `gorm:"column:flags" json:"flags"`
    Sort        uint       `gorm:"column:sort" json:"sort"`
    IPAddress   string     `gorm:"column:ip_address;size:64" json:"ip_address"`
    Source      string     `gorm:"column:source;type:enum('Web','Email','Phone','API','Other')" json:"source"`
    SourceExtra *string    `gorm:"column:source_extra;size:40" json:"source_extra,omitempty"`
    IsOverdue   uint8      `gorm:"column:isoverdue" json:"isoverdue"`
    IsAnswered  uint8      `gorm:"column:isanswered" json:"isanswered"`
    DueDate     *time.Time `gorm:"column:duedate" json:"duedate,omitempty"`
    EstDueDate  *time.Time `gorm:"column:est_duedate" json:"est_duedate,omitempty"`
    Reopened    *time.Time `gorm:"column:reopened" json:"reopened,omitempty"`
    Closed      *time.Time `gorm:"column:closed" json:"closed,omitempty"`
    LastUpdate  time.Time `gorm:"column:updated;autoCreateTime" json:"lastupdate,omitempty"`
    Created     time.Time  `gorm:"column:created;autoCreateTime" json:"created"`
}


// TableName overrides the table name used by GORM
func (Ticket) TableName() string {
    return "ost_ticket"
}

type TicketReply struct {
    ID        uint   `gorm:"primaryKey" json:"id"`
    TicketID  uint   `json:"ticket_id"`
    Message   string `gorm:"type:text;not null" json:"message" validate:"required"`
    CreatedAt int64  `json:"created_at"`
}

