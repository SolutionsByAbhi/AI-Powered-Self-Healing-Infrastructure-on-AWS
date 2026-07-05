resource "aws_cloudwatch_dashboard" "self_healing" {

  dashboard_name = "SelfHealingDashboard"

  dashboard_body = jsonencode({

    widgets = [

      {

        "type": "metric",

        "width": 12,

        "height": 6,

        "properties": {

          "metrics": [

            [

              "AWS/EC2",

              "CPUUtilization"

            ]

          ],

          "period": 300,

          "stat": "Average",

          "region": var.aws_region,

          "title": "CPU"

        }

      }

    ]

  })
}
