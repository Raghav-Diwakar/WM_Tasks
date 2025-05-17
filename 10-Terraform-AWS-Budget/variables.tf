variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "budget_name" {
  description = "Name of the budget"
  type        = string
  default     = "monthly-cost-budget"
}

variable "budget_limit" {
  description = "Monthly budget limit in USD"
  type        = string
  default     = "2"
}

variable "start_date" {
  description = "Budget start date in YYYY-MM-DD_HH:MM format"
  type        = string
  default     = "2025-05-01_00:00"
}

variable "notification_emails" {
  description = "List of email addresses to send budget notifications"
  type        = list(string)
  default     = ["raghav.abesec@gmail.com"]
}

variable "warning_threshold" {
  description = "Percentage threshold for warning notification"
  type        = number
  default     = 80
}

variable "critical_threshold" {
  description = "Percentage threshold for critical notification"
  type        = number
  default     = 100
}

variable "comparison_operator" {
  description = "Comparison operator for budget alerts"
  type        = string
  default     = "GREATER_THAN"
}