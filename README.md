# Vulnerable_sites

⚠️ **Educational Purpose Only**

This repository contains intentionally vulnerable files, configurations, credentials, and infrastructure artifacts designed for cybersecurity training, security assessments, secret-scanning practice, and vulnerability discovery exercises.

## Overview

The project simulates a repository that has been improperly managed, exposing sensitive information commonly discovered during:

* GitHub reconnaissance
* Secret scanning
* OSINT investigations
* Penetration testing
* Secure code review
* DevSecOps assessments

The repository includes various examples of exposed credentials, configuration files, private keys, cloud artifacts, and infrastructure-as-code secrets.

## Objectives

This repository can be used to learn:

* GitHub secret hunting
* Credential exposure identification
* Cloud security assessments
* Source code review techniques
* Infrastructure misconfiguration detection
* Security automation testing
* Vulnerability reporting workflows

## Included Examples

### Cloud & Infrastructure

* AWS configuration files
* Kubernetes configuration
* Terraform variables
* Service account credentials
* Docker configuration files

### Sensitive Files

* Private SSH keys
* API tokens
* Debug keys
* Configuration secrets
* Environment variables

### Application Components

* Web application source code
* API integrations
* WordPress configuration
* Test environments
* Documentation assets

## Repository Structure

```text
.
├── .aws/
├── assets/
├── docs/
├── src/
├── tests/
├── .dockerconfigjson
├── .npmrc
├── debug_key.txt
├── id_rsa
├── kubeconfig
├── real_key.txt
├── service-account.json
├── terraform.tfvars
└── wp-config.php
```

## Warning

The contents of this repository are intentionally insecure and should **never** be used in production environments.

Do not:

* Deploy these configurations to live systems
* Reuse any credentials found within the repository
* Assume any secrets are valid
* Use this project as a secure implementation reference

## Recommended Use Cases

* Security training labs
* Capture The Flag (CTF) challenges
* Secret scanning tool testing
* GitHub reconnaissance practice
* Vulnerability assessment exercises
* Cybersecurity education

## Legal Notice

This repository is provided solely for educational and research purposes. Users are responsible for ensuring compliance with all applicable laws, regulations, and organizational policies when performing security testing activities.

## License

This project is intended for educational use. Review the repository license before using or distributing its contents.
