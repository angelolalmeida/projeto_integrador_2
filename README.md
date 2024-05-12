# Project: Website for a Recyclers Association in Macatuba, SP - Brazil

## Description:

This project was developed as a practical project for the "Projeto Integrador 3" course of the Computer Engineering, Information Technology and Data Science courses at UNIVESP - Virtual University of the State of São Paulo.

## Purpose:

The purpose of this project is to create a website for a recyclers association in the city of Macatuba, State of São Paulo - Brazil. The website will provide information about the association, its services, and how to get involved. It will also serve as a platform for the association to connect with the community and promote recycling awareness.

### Technologies:

_Back-end:_

_Django:_ A high-level Python web framework that facilitates rapid development and clean, pragmatic design. It takes care of much of the web development work, so you can focus on writing your application without having to reinvent the wheel. https://www.djangoproject.com/
Front-end:

_Soft UI:_ An open-source design system built with Bootstrap 5 and Soft Dashboard, a pixel-perfect design from Creative-Tim. It offers a modern and intuitive user experience, with over 300 individual elements, such as buttons, inputs, navigation bars, navigation tabs, cards, and alerts, giving you the freedom to pick and choose to create custom interfaces. https://github.com/app-generator/django-admin-soft-dashboard

## Data Visualization:

_Plotly:_ A JavaScript data visualization library for creating high-quality interactive charts and graphs. It offers a wide range of customization options and is compatible with multiple browsers and devices. https://plotly.com/python/

## Data Analysis:

_Pandas:_ A Python library for data manipulation and analysis. It offers a powerful and easy-to-use data structure for working with tabular data and time series. https://pandas.pydata.org/docs/

## Quick start

> 👉 Download the code

```bash
$ git clone https://github.com/angelolalmeida/projeto_integrador_2.git
$ cd projeto_integrador_2
```

<br />

> 👉 Install modules via `VENV`

```bash
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`.

<br />

## Testing

### Utilities and Libraries

- _Faker_ is a Python package that generates fake data for you.
- _Responses_ is a utility library for mocking out the `requests` Python library.
- _TestCase_ is the most common class to use for writing tests in Django.
- _Coverage.py_ provides code coverage measurement for Python.

### Available scripts

> 👉 Running tests

```bash
$ python manage.py test
```

> 👉 Collecting coverage

```bash
$ coverage run manage.py test
```

> 👉 Show coverage report

```bash
$ coverage report
```

> 👉 Export coverage report to HTML

```bash
$ coverage html
```

## Documentation

The documentation for the **Soft UI Dashboard Django** is hosted at our [website](https://www.creative-tim.com/learning-lab/bootstrap/build-tools-free/soft-ui-dashboard).

<br />

## Codebase structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/
   |    |-- settings.py                  # Project Configuration
   |    |-- urls.py                      # Project Routing
   |
   |-- home/
   |    |-- views.py                     # APP Views
   |    |-- urls.py                      # APP Routing
   |    |-- models.py                    # APP Models
   |    |-- tests.py                     # Tests
   |    |-- templates/                   # Theme Customisation
   |         |-- includes                #
   |              |-- custom-footer.py   # Custom Footer
   |
   |-- requirements.txt                  # Project Dependencies
   |
   |-- env.sample                        # ENV Configuration (default values)
   |-- manage.py                         # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## How to Customize

When a template file is loaded in the controller, `Django` scans all template directories starting from the ones defined by the user, and returns the first match or an error in case the template is not found.
The theme used to style this starter provides the following files:

```bash
< LIBRARY_ROOT >                      # This exists in ENV: LIB/admin_soft
   |
   |-- templates/                     # Root Templates Folder
   |    |
   |    |-- accounts/
   |    |    |-- login.html           # Sign IN Page
   |    |    |-- register.html        # Sign UP Page
   |    |
   |    |-- includes/
   |    |    |-- footer.html          # Footer component
   |    |    |-- sidebar.html         # Sidebar component
   |    |    |-- navigation.html      # Navigation Bar
   |    |    |-- scripts.html         # Scripts Component
   |    |
   |    |-- layouts/
   |    |    |-- base.html            # Masterpage
   |    |    |-- base-fullscreen.html # Masterpage for Auth Pages
   |    |
   |    |-- pages/
   |         |-- index.html           # Dashboard page
   |         |-- profile.html         # Settings  Page
   |         |-- *.html               # All other pages
   |
   |-- ************************************************************************
```

When the project requires customization, we need to copy the original file that needs an update (from the virtual environment) and place it in the template folder using the same path.

> For instance, if we want to **customize the footer.html** these are the steps:

- ✅ `Step 1`: create the `templates` DIRECTORY inside the `home` app
- ✅ `Step 2`: configure the project to use this new template directory
  - `core/settings.py` TEMPLATES section
- ✅ `Step 3`: copy the `footer.html` from the original location (inside your ENV) and save it to the `home/templates` DIR
  - Source PATH: `<YOUR_ENV>/LIB/admin_soft/includes/footer.html`
  - Destination PATH: `<PROJECT_ROOT>home/templates/includes/footer.html`

> To speed up all these steps, the **codebase is already configured** (`Steps 1, and 2`) and a `custom footer` can be found at this location:

`home/templates/includes/custom_footer.html`

By default, this file is unused because the `theme` expects `footer.html` (without the `custom_` prefix).

In order to use it, simply rename it to `footer.html`. Like this, the default version shipped in the library is ignored by Django.

In a similar way, all other files and components can be customized easily.

<br />

## Deploy on [Render](https://render.com/)

- Create a Blueprint instance
  - Go to https://dashboard.render.com/blueprints this link.
- Click `New Blueprint Instance` button.
- Connect your `repo` which you want to deploy.
- Fill the `Service Group Name` and click on `Update Existing Resources` button.
- After that your deployment will start automatically.

At this point, the product should be LIVE.

<br />

## Reporting Issues

We use GitHub Issues as the official bug tracker for the **Soft UI Dashboard Django**. Here are some advices for our users that want to report an issue:

1. Make sure that you are using the latest version of the **Soft UI Dashboard Django**. Check the CHANGELOG from your dashboard on our [website](https://www.creative-tim.com/).
2. Providing us reproducible steps for the issue will shorten the time it takes for it to be fixed.
3. Some issues may be browser-specific, so specifying in what browser you encountered the issue might help.

<br />

## Technical Support or Questions

If you have questions or need help integrating the product please [contact us](https://www.creative-tim.com/contact-us) instead of opening an issue.

<br />

## Licensing

- Copyright 2019 - present [Creative Tim](https://www.creative-tim.com/)
- Licensed under [Creative Tim EULA](https://www.creative-tim.com/license)

<br />

## Useful Links

- [More products](https://www.creative-tim.com/bootstrap-themes) from Creative Tim
- [Tutorials](https://www.youtube.com/channel/UCVyTG4sCw-rOvB9oHkzZD1w)
- [Freebies](https://www.creative-tim.com/bootstrap-themes/free) from Creative Tim
- [Affiliate Program](https://www.creative-tim.com/affiliates/new) (earn money)

<br />

## Social Media

- Twitter: <https://twitter.com/CreativeTim>
- Facebook: <https://www.facebook.com/CreativeTim>
- Dribbble: <https://dribbble.com/creativetim>
- Instagram: <https://www.instagram.com/CreativeTimOfficial>

<br />

## [PRO Version](https://www.creative-tim.com/product/soft-ui-dashboard-pro-django)

This design is a pixel-perfect [Bootstrap 5](https://www.admin-dashboards.com/bootstrap-5-templates/) Dashboard with a fresh, new design concept. `Soft UI Dashboard PRO` is built with over 300 frontend individual elements, like buttons, inputs, navbars, nav tabs, cards, or alerts, giving you the freedom of choosing and combining.

> Features:

- `Up-to-date Dependencies`
- `Design`: [Django Theme Soft PRO](https://github.com/app-generator/django-admin-soft-pro) - `PRO Version`
- `Sections` covered by the design:
  - **Admin section** (reserved for superusers)
  - **Authentication**: `Django.contrib.AUTH`, Registration
  - **All Pages** available in for ordinary users
- `Docker`, `Deployment`:
  - `CI/CD` flow via `Render`

<br />

[![Django - Soft UI Dashboard PRO (premium starter by AppSeed & Creative-Tim](https://user-images.githubusercontent.com/51070104/215022735-dec8e82e-ea91-4494-a521-db421e8637be.png)](https://www.creative-tim.com/product/soft-ui-dashboard-pro-django)

<br />

---

[Soft UI Dashboard - Django Template](https://www.creative-tim.com/product/soft-ui-dashboard-django) - Provided by [Creative Tim](https://www.creative-tim.com/) and [AppSeed](https://appseed.us)
