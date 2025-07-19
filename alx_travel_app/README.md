# ALX Travel App Backend

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-E13838?style=for-the-badge&logo=django%20rest%20framework&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## Table of Contents

- [About the Project](#about-the-project)
- [Learning Objectives](#learning-objectives)
- [Key Highlights](#key-highlights)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create and Activate Virtual Environment](#2-create-and-activate-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Database Setup (MySQL)](#4-database-setup-mysql)
  - [5. Environment Variables](#5-environment-variables)
  - [6. Run Migrations](#6-run-migrations)
  - [7. Run the Development Server](#7-run-the-development-server)
- [API Documentation (Swagger/ReDoc)](#api-documentation-swaggerredoc)
- [Project Structure](#project-structure)
- [Contribution](#contribution)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## About the Project

The `alxtravelapp` project serves as the robust backend foundation for a modern travel listing platform. This initial milestone focuses on establishing a professional and scalable project structure, integrating a powerful MySQL database, and incorporating essential developer tools for seamless API documentation and maintainable configurations.

The aim is to equip developers with industry-standard best practices, enabling them to build scalable backends, manage databases effectively with MySQL, and provide clear, automated API documentation using Swagger. These foundational steps are crucial for preparing the application for future feature development and fostering efficient team collaboration.

---

## Learning Objectives

This project is designed to help you master critical skills for professional backend development:

* **Master Advanced Project Initialization:**
    * Learn to bootstrap Django projects with modular, production-ready configurations.
    * Employ environment variable management (using `django-environ`) for secure and scalable settings.
* **Integrate Key Developer Tools:**
    * Set up and utilize Swagger (via `drf-yasg`) for comprehensive and automated API documentation.
    * Implement CORS headers for robust cross-origin API interactions.
    * Configure MySQL as your primary database for enhanced data management.
* **Collaborate Effectively Using Git:**
    * Structure your projects for efficient team collaboration with a version-controlled setup.
* **Adopt Industry Best Practices:**
    * Follow best practices in managing project dependencies, database configurations, and overall application structure.

---

## Key Highlights

* **Project Initialization:**
    * Created a Django project named `alxtravelapp`.
    * Added a core app named `listings` to encapsulate travel listing functionalities.
* **Dependency Management:**
    * Installation of essential packages:
        * `django`: Core framework for web application development.
        * `djangorestframework`: Powerful toolkit for building REST APIs.
        * `django-cors-headers`: Handles Cross-Origin Resource Sharing for secure frontend-backend communication.
        * `drf-yasg`: Integrates Swagger/OpenAPI for automated API documentation.
        * `mysqlclient`: Python connector for MySQL database interaction.
        * `celery` and `rabbitmq`: Included for future task queuing and background processing capabilities.
        * `django-environ`: Manages environment variables for secure and flexible settings.
* **Settings Configuration:**
    * Secure handling of sensitive information using `django-environ` and `.env` files.
    * MySQL configured as the primary database, ensuring robust connection management.
    * Django REST Framework and CORS headers properly set up for seamless API support.
* **Swagger Integration:**
    * Comprehensive API documentation enabled via `drf-yasg`.
    * All APIs are automatically documented and accessible at the `/swagger/` endpoint.
* **Version Control and Submission:**
    * Initialized a Git repository for professional version control.
    * Project setup files committed and pushed to a GitHub repository (`alxtravelapp`).

---

## Prerequisites

To get started with this project, ensure you have the following:

* **Python 3.8+** installed on your system.
* **Django** and **Django REST Framework** familiarity.
* Basic understanding of **MySQL** and database management concepts.
* Knowledge of **Git** for version control.
* A basic grasp of environment variable management (e.g., how `.env` files work).
* A running **MySQL server** instance (local or remote).

---

## Getting Started

Follow these steps to get your `alxtravelapp` backend up and running locally.

### 1. Clone the Repository

```bash
git clone https://github.com/samuel-udoh/alxtravelapp.git
cd alxtravelapp