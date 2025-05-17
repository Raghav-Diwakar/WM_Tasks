resource "aws_budgets_budget" "monthly_cost_budget" {
  name              = var.budget_name
  budget_type       = "COST" # variable 
  limit_amount      = var.budget_limit
  limit_unit        = "USD"
  time_period_start = var.start_date
  time_unit         = "MONTHLY"# variable


# this also dynamic
  cost_types {
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

# include sns notification 25 , 50 , 75 , 100
  dynamic "notification" {
    for_each = [
      {
        threshold     = var.warning_threshold
        type          = "WARNING"
      },
      {
        threshold     = var.critical_threshold
        type          = "CRITICAL"
      }
    ]
# dynamic var.#type
    content {
      comparison_operator        = var.comparison_operator
      threshold                  = notification.value.threshold
      threshold_type             = "PERCENTAGE"
      notification_type          = "ACTUAL"
      subscriber_email_addresses = var.notification_emails
    }
  }
}

# main block
# var.type or s example Default ie "GREATER_THAN"

# resource (main)
# variable
# input 
# output
# provider "version.tf" 


# corrupt state files
# A .tfstate or .tfstate.backup file that is not valid JSON , incomplete data, mismatched
# delete , mismatch , 


# Causes 
# 1 Manual edits to the .tfstate
# 2 Concurrent modifications 
# 3 S3 versioning or encryption
# 4 Partial apply or destroy
# 5 Deleting infrastructure manually


# Process 
# terraform state list
# --------------> aws_budgets_budget.monthly_cost_budget
# terraform state show aws_budgets_budget.monthly_cost_budget
# terraform state rm aws_budgets_budget.monthly_cost_budget
# terraform import aws_budgets_budget.monthly_cost_budget 444420015968:monthly-cost-budget
# terraform plan


# golang 
# K8s CRD
# operator 
# how to create basic k8s operator

# buto
# https://docs.burrito.tf/installation/with-helm/