# EX01 Developing a Simple Webserver

# Date: 7/10/2024
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:
### views.py 
```
from django.shortcuts import render
def server(request):
    return render(request,'Simplegpt.html')

```
### settings.py
```
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-2yc^$9p+m1qholf)-&4^liw_j4s$o@4nx$e6iet!*4=lbnmgvy'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sserver',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

```
### urls.py
```
from django.contrib import admin
from django.urls import path
from sserver import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('server',views.server)
]
```
### Simpleserver.html
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Laptop Configuration</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f1f8ff; /* Light blue background for the page */
      color: #333;
    }
    .container {
      max-width: 900px;
      margin: 50px auto;
      background: #ffffff; /* White background for the container */
      padding: 30px;
      border-radius: 16px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
    }
    h1 {
      text-align: center;
      font-size: 32px;
      color: #ff6347; /* Tomato color for the title */
      margin-bottom: 20px;
      text-transform: uppercase;
      letter-spacing: 2px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
      background: #f4f4f9; /* Light gray background for the table */
    }
    th, td {
      padding: 16px 20px;
      text-align: left;
      border: 1px solid #ddd;
    }
    th {
      background-color: #4CAF50; /* Green color for the table header */
      color: white;
      font-weight: bold;
      text-transform: uppercase;
    }
    td {
      background-color: #ffffff; /* White background for table data cells */
      color: #555;
    }
    tr:nth-child(even) td {
      background-color: #f9f9f9; /* Light gray for even rows */
    }
    tr:hover td {
      background-color: #e0f7fa; /* Light cyan for hovered rows */
      color: #00796b; /* Dark teal text on hover */
    }
    td:first-child {
      font-weight: bold;
      color: #00796b; /* Dark teal color for the configuration column */
    }
    td:last-child {
      font-style: italic;
      color: #666;
    }
    .highlight {
      background-color: #fff9c4; /* Pale yellow background for highlighted rows */
      font-weight: bold;
    }
    @media (max-width: 768px) {
      .container {
        padding: 20px;
      }
      table {
        font-size: 14px;
      }
      th, td {
        padding: 10px;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Laptop Configuration</h1>
    <table>
      <tr>
        <th>Configuration</th>
        <th>Details</th>
      </tr>
      <tr>
        <td class="highlight">Operating System</td>
        <td>Windows 11 Home Single Language 64-bit</td>
      </tr>
      <tr>
        <td>Processor</td>
        <td>13th Gen Intel(R) Core(TM) i5-13450HX (16 CPUs)</td>
      </tr>
      <tr>
        <td class="highlight">RAM</td>
        <td>16 GB</td>
      </tr>
      <tr>
        <td>Storage</td>
        <td>1 TB SSD</td>
      </tr>
      <tr>
        <td class="highlight">Graphics Card</td>
        <td>NVIDIA GeForce RTX 3050 (6GB)</td>
      </tr>
      <tr>
        <td>Screen Resolution</td>
        <td>1920 x 1080 (Full HD)</td>
      </tr>
      <tr>
        <td class="highlight">Screen Size</td>
        <td>15.6 inches</td>
      </tr>
      <tr>
        <td>Battery Capacity</td>
        <td>56 WHr</td>
      </tr>
      <tr>
        <td class="highlight">Weight</td>
        <td>2.8 kg</td>
      </tr>
      <tr>
        <td>Color</td>
        <td>Matt Black</td>
      </tr>
      <tr>
        <td class="highlight">Keyboard</td>
        <td>Orange-Backlit, QWERTY</td>
      </tr>
      <tr>
        <td>Wireless Connectivity</td>
        <td>Wi-Fi 6, Bluetooth 5.3</td>
      </tr>
      <tr>
        <td class="highlight">Ports</td>
        <td>USB-C, USB-A, HDMI, Ethernet</td>
      </tr>
      <tr>
        <td>Operating System Architecture</td>
        <td>64-bit</td>
      </tr>
    </table>
  </div>
</body>
</html>
```
# OUTPUT:
![alt text](<Screenshot 2024-12-06 205434.png>)
# RESULT:
The program for implementing simple webserver is executed successfully.
