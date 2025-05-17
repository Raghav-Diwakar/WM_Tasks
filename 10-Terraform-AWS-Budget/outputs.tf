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