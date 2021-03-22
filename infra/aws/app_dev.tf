resource "aws_instance" "app_dev" {
  ami                    = "ami-08c6f5346465db4f4"
  instance_type          = "m5.xlarge"
  subnet_id              = var.subnet1_id
  vpc_security_group_ids = [var.internal_security_group_id]
  user_data              = module.ssh.user_data

  root_block_device {
    volume_type = "gp2"
    volume_size = "128"
  }

  tags = {
    Name        = "CCPM - App Dev"
    Cluster     = "CCPM"
    Vendor      = "h1st"
    Environment = var.environment_tag
    Project     = var.project_tag
  }

  lifecycle {
    ignore_changes = [
      ami,
      user_data,
    ]
  }
}

resource "aws_db_instance" "app-db-dev" {
  allocated_storage       = 864
  backup_retention_period = 3
  db_subnet_group_name    = "pm20190118201546865800000001"
  engine                  = "postgres"
  engine_version          = "11.5"
  identifier              = "ccpm-app-db-dev"
  instance_class          = "db.m4.large"
  multi_az                = false
  name                    = "ccpm"

  snapshot_identifier = "ccpm-app-db-20200915"

  port = 5432

  publicly_accessible    = false
  storage_encrypted      = true
  storage_type           = "gp2"
  username               = "ccpm"
  vpc_security_group_ids = [var.internal_security_group_id]

  # monitoring_interval = 60

  tags = {
    Name        = "PM App DB Dev"
    Project     = "CCPM"
    Environment = "DEV"
  }
}

module "app_ingress_dev_jp" {
  source = "./ingress"
  name   = "ccpm-app-dev-jp"

  load_balancer_name = "infra"
  zone_id            = data.aws_route53_zone.external.id
  domain_prefix      = "pm-app-dev.jp"
  instances          = [aws_instance.app_dev.id]
  instance_count     = 1
}
