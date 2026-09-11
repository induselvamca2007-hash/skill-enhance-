provider "aws" {
  region = "us-east-1"
}

resource "aws_sns_topic" "alerts" {
  name = "cloud-resource-alerts"
}

resource "aws_cloudwatch_metric_alarm" "cpu_alarm" {
  alarm_name          = "HighCPUUsage"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = 300
  statistic           = "Average"
  threshold           = 80
  alarm_description   = "Triggers when CPU usage exceeds 80%"

  dimensions = {
    InstanceId = "i-0123456789abcdef0"
  }

  alarm_actions = [aws_sns_topic.alerts.arn]
}

resource "aws_cloudwatch_metric_alarm" "memory_alarm" {
  alarm_name          = "HighMemoryUsage"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "mem_used_percent"
  namespace           = "CWAgent"
  period              = 300
  statistic           = "Average"
  threshold           = 80
  alarm_description   = "Triggers when memory usage exceeds 80%"

  dimensions = {
    InstanceId = "i-0123456789abcdef0"
  }

  alarm_actions = [aws_sns_topic.alerts.arn]
}

resource "aws_cloudwatch_metric_alarm" "disk_alarm" {
  alarm_name          = "HighDiskUsage"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "disk_used_percent"
  namespace           = "CWAgent"
  period              = 300
  statistic           = "Average"
  threshold           = 85
  alarm_description   = "Triggers when disk usage exceeds 85%"

  dimensions = {
    InstanceId = "i-0123456789abcdef0"
    path       = "/"
    fstype     = "xfs"
  }

  alarm_actions = [aws_sns_topic.alerts.arn]
}