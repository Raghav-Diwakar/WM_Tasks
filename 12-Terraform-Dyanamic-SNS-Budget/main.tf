resource "aws_budgets_budget" "monthly_cost_budget" {
  name              = var.budget_name
  budget_type       = var.budget_type
  limit_amount      = var.budget_limit
  limit_unit        = "USD"
  time_period_start = var.start_date
  time_unit         = var.time_unit

  dynamic "cost_types" {
    for_each = [var.cost_types]
    content {
      include_credit             = lookup(cost_types.value, "include_credit", false)
      include_discount           = lookup(cost_types.value, "include_discount", true)
      include_other_subscription = lookup(cost_types.value, "include_other_subscription", true)
      include_recurring          = lookup(cost_types.value, "include_recurring", true)
      include_refund             = lookup(cost_types.value, "include_refund", false)
      include_subscription       = lookup(cost_types.value, "include_subscription", true)
      include_support            = lookup(cost_types.value, "include_support", true)
      include_tax                = lookup(cost_types.value, "include_tax", true)
      include_upfront            = lookup(cost_types.value, "include_upfront", true)
      use_amortized              = lookup(cost_types.value, "use_amortized", false)
      use_blended                = lookup(cost_types.value, "use_blended", false)
    }
  }

  dynamic "notification" {
    for_each = var.notification_thresholds
    content {
      comparison_operator        = var.comparison_operator
      threshold                  = notification.value.threshold
      threshold_type             = "PERCENTAGE"
      notification_type          = notification.value.notification_type
      subscriber_sns_topic_arns  = [aws_sns_topic.budget_notifications.arn]
    }
  }
}

resource "aws_sns_topic" "budget_notifications" {
  name = "${var.budget_name}-notifications"
}

resource "aws_sns_topic_subscription" "email_subscription" {
  for_each  = toset(var.notification_emails)
  topic_arn = aws_sns_topic.budget_notifications.arn
  protocol  = "email"
  endpoint  = each.value
}

output "budget_id" {
  description = "The ID of the created budget"
  value       = aws_budgets_budget.monthly_cost_budget.id
}

output "budget_name" {
  description = "The name of the created budget"
  value       = aws_budgets_budget.monthly_cost_budget.name
}

output "budget_limit" {
  description = "The budget limit amount"
  value       = aws_budgets_budget.monthly_cost_budget.limit_amount
}

output "sns_topic_arn" {
  description = "The ARN of the SNS topic for budget notifications"
  value       = aws_sns_topic.budget_notifications.arn
}

provider "aws" {
  region = var.aws_region
}

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

variable "budget_type" {
  description = "Type of budget (COST, USAGE, RI_UTILIZATION, etc)"
  type        = string
  default     = "COST"
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

variable "time_unit" {
  description = "The time unit for the budget (MONTHLY, QUARTERLY, ANNUALLY)"
  type        = string
  default     = "MONTHLY"
}

variable "notification_emails" {
  description = "List of email addresses to send budget notifications"
  type        = list(string)
  default     = ["raghav.abesec@gmail.com"]
}

variable "comparison_operator" {
  description = "Comparison operator for budget alerts"
  type        = string
  default     = "GREATER_THAN"
}

variable "cost_types" {
  description = "Configuration block for cost types"
  type        = map(bool)
  default     = {
    include_credit             = false
    include_discount           = true
    include_other_subscription = true
    include_recurring          = true
    include_refund             = false
    include_subscription       = true
    include_support            = true
    include_tax                = true
    include_upfront            = true
    use_amortized              = false
    use_blended                = false
  }
}

variable "notification_thresholds" {
  description = "List of notification thresholds with their types"
  type = list(object({
    threshold         = number
    notification_type = string
  }))
  default = [
    {
      threshold         = 25
      notification_type = "ACTUAL"
    },
    {
      threshold         = 50
      notification_type = "ACTUAL"
    },
    {
      threshold         = 75
      notification_type = "ACTUAL"
    },
    {
      threshold         = 100
      notification_type = "ACTUAL"
    }
  ]
}

terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}