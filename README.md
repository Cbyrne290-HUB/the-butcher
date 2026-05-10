# The Butcher – Restaurant Table Booking System

<img width="249" height="95" alt="Screenshot 2026-05-10 at 14 07 06" src="https://github.com/user-attachments/assets/f3287f7b-635c-4920-9e5c-61c591360056" />

<img width="4000" height="3200" alt="apple-responsive-devices-mockup" src="https://github.com/user-attachments/assets/04c5f18e-3fed-409f-989a-ab37c5c30194" />


**Live Site:** [the-butcher-dublin](https://the-butcher-dublin-651bdd3c4860.herokuapp.com/)  
**GitHub Repository:** [https://github.com/Cbyrne290-HUB/the-butcher](https://github.com/Cbyrne290-HUB/the-butcher)

---

## Table of Contents

1. [Why I Built This](#why-i-built-this)  
2. [Project Objective](#project-objective)  
3. [UX Goals](#ux-goals)  
4. [User Stories](#user-stories)  
5. [Design](#design)  
6. [Data Model](#data-model)  
7. [Features](#features)  
8. [Agile Development](#agile-development)  
9. [Technologies Used](#technologies-used)  
10. [Testing](#testing)  
11. [Bugs](#bugs)  
12. [Deployment](#deployment)  
13. [Credits](#credits)

---

## Why I Built This

For my fourth portfolio project I wanted to build something that felt genuinely useful rather than purely academic. Restaurant booking systems are something almost everyone interacts with — yet so many of them are clunky, slow, or just plain confusing. I've been in Dublin long enough to know that a lot of local restaurants still rely on phone bookings or third-party platforms that take a commission on every cover.

The Butcher is a fictional upscale steakhouse on Grafton Street. Building a full booking platform for it let me apply everything I'd learned about Django, databases, and authentication in one coherent, real-world context. I wanted the guest experience to be as smooth as walking into the restaurant itself — clear, confident, and no unnecessary friction.

---

## Project Objective

Build a full-stack web application using the Django framework that allows restaurant guests to:

- Register an account and log in securely
- Create, view, edit and cancel table bookings
- Leave, edit and delete reviews for the restaurant
- Receive clear feedback at every step

And allows restaurant staff to:

- View all upcoming bookings in one place
- Update booking statuses (confirm or cancel)
- Moderate guest reviews before they go public

The project is assessed against the Code Institute's PP4 criteria, covering custom data models, authentication, role-based access, CRUD operations, agile planning and automated testing.

---

## UX Goals

| Goal | How it's met |
|---|---|
| First-time visitor understands the restaurant immediately | Hero section with tagline, stats strip and about section on the home page |
| Booking flow is simple and obvious | Three-step explainer on home page; form with date-picker and clear validation errors |
| User always knows where they are | Active nav link highlighted; page-header sections on every interior page |
| User always knows what happened | Bootstrap flash messages on every form submission (success, error, info) |
| Mobile users get a full experience | Bootstrap 5 responsive grid; sticky navbar collapses to hamburger on small screens |
| Staff can act fast | Dedicated staff bookings page with inline status dropdowns; one click to confirm |

---

## User Stories

User stories were tracked on the [GitHub Projects Kanban board](https://github.com/Cbyrne290-HUB/the-butcher/projects) using MoSCoW prioritisation.

### Epic 1 – Authentication

| ID | Story | Priority | Status |
|---|---|---|---|
| US-01 | As a guest I can register with my email and password so that I have a personal account | Must Have | Done |
| US-02 | As a registered user I can log in with my email and password so that I can access my bookings | Must Have | Done |
| US-03 | As a logged-in user I can log out so that my session is closed on shared devices | Must Have | Done |

### Epic 2 – Bookings

| ID | Story | Priority | Status |
|---|---|---|---|
| US-04 | As a logged-in user I can create a table booking so that I can reserve a spot at the restaurant | Must Have | Done |
| US-05 | As a logged-in user I can view all my bookings so that I can see what I have coming up | Must Have | Done |
| US-06 | As a logged-in user I can edit my upcoming booking so that I can change the date, time or party size | Must Have | Done |
| US-07 | As a logged-in user I can cancel my booking so that the table is freed for other guests | Must Have | Done |
| US-08 | As a user I cannot book on a Tuesday (closed day) so that I don't arrive to a shut restaurant | Must Have | Done |
| US-09 | As a user I cannot book a date in the past so that I don't make impossible reservations | Must Have | Done |

### Epic 3 – Reviews

| ID | Story | Priority | Status |
|---|---|---|---|
| US-10 | As a logged-in user I can write a review so that I can share my experience | Should Have | Done |
| US-11 | As a logged-in user I can edit my review so that I can update it after re-visiting | Should Have | Done |
| US-12 | As a logged-in user I can delete my review so that I can remove it if I change my mind | Should Have | Done |
| US-13 | As any visitor I can read published reviews so that I can decide whether to visit | Should Have | Done |
| US-14 | As a user I can only submit one review so that the review page is not flooded | Should Have | Done |

### Epic 4 – Staff / Admin

| ID | Story | Priority | Status |
|---|---|---|---|
| US-15 | As a staff member I can view all bookings so that I can prepare for the day | Must Have | Done |
| US-16 | As a staff member I can confirm or cancel any booking so that guests are kept informed | Must Have | Done |
| US-17 | As a staff member I can approve or reject reviews so that only genuine reviews are published | Should Have | Done |
| US-18 | As a staff member I can manage all data through the Django admin panel | Should Have | Done |

### Epic 5 – General UX

| ID | Story | Priority | Status |
|---|---|---|---|
| US-19 | As a visitor I can view the restaurant menu so that I know what to expect | Could Have | Done |
| US-20 | As a visitor I can see a snapshot of reviews on the home page so that I can gauge quality quickly | Could Have | Done |
| US-21 | As a user I receive clear error pages (403, 404, 500) so that I'm never left confused | Should Have | Done |

---

## Design

### Colour Palette

| Colour | Hex | Use |
|---|---|---|
| Butcher Dark | `#111111` | Navbar, hero background, footer |
| Butcher Gold | `#f6b826` | Primary CTA buttons, accents, star ratings |
| Off-White | `#f9f7f4` | Page background |
| Bootstrap Light | `#f8f9fa` | Card and section backgrounds |
| Bootstrap Muted | `#6c757d` | Body text, labels |

<img width="851" height="424" alt="Screenshot 2026-05-10 at 14 20 55" src="https://github.com/user-attachments/assets/436a35f3-7e6b-4186-9ab6-8a0cb72e6084" />

### Typography

- **Playfair Display** (Google Fonts) — headings. Chosen for its high-contrast serifs that read as premium and upscale.  
- **Inter** (Google Fonts) — body text. Clean, modern, highly legible at small sizes.

### Wireframes

Wireframes were produced in Balsamiq before development began.

| Page | Wireframe |
|---|---|
| Home | ![Home wireframe](docs/wireframes/home.png) |
| Book a Table | ![Booking form wireframe](docs/wireframes/booking_form.png) |
| My Bookings | ![My bookings wireframe](docs/wireframes/my_bookings.png) |
| Reviews | ![Reviews wireframe](docs/wireframes/reviews.png) |
| Staff Bookings | ![Staff wireframe](docs/wireframes/staff_bookings.png) |

---

## Data Model

The project uses two custom models. Below is an entity-relationship overview.

```
┌─────────────────────────┐         ┌─────────────────────────┐
│  User (django.auth)     │         │  Booking                │
│─────────────────────────│         │─────────────────────────│
│  id (PK)                │◄───┐    │  id (PK)                │
│  email                  │    │    │  user (FK → User)       │
│  first_name             │    │    │  date                   │
│  last_name              │    │    │  time_slot              │
│  is_staff               │    └────│  party_size             │
└─────────────────────────┘         │  special_requests       │
                                    │  status                 │
                ┌───────────────────│  created_at             │
                │                   │  updated_at             │
                │                   └─────────────────────────┘
                │
                │    ┌─────────────────────────┐
                │    │  Review                 │
                │    │─────────────────────────│
                └────│  user (FK → User)       │
                     │  rating (1–5)           │
                     │  title                  │
                     │  comment                │
                     │  approved               │
                     │  created_at             │
                     │  updated_at             │
                     └─────────────────────────┘
```

### Booking model

| Field | Type | Notes |
|---|---|---|
| user | ForeignKey(User) | CASCADE delete |
| date | DateField | Validated: no past, no Tuesdays |
| time_slot | CharField | 16 choices 12:00–21:30 |
| party_size | IntegerField | Validators: min 1, max 12 |
| special_requests | TextField | Optional |
| status | CharField | pending / confirmed / cancelled |
| created_at | DateTimeField | auto_now_add |
| updated_at | DateTimeField | auto_now |

### Review model

| Field | Type | Notes |
|---|---|---|
| user | ForeignKey(User) | CASCADE delete; OneToOne enforced in view |
| rating | IntegerField | Validators: min 1, max 5 |
| title | CharField(100) | — |
| comment | TextField | — |
| approved | BooleanField | Default False; set by staff/admin |
| created_at | DateTimeField | auto_now_add |
| updated_at | DateTimeField | auto_now |

---

## Features

### Navigation

A sticky dark navbar provides access to all key pages. Unauthenticated users see Sign In and Register. Authenticated users see My Bookings, Reviews and Sign Out. Staff members see an additional Staff Bookings link. A small status bar beneath the navbar shows the logged-in email and a gold Staff badge where applicable.

<img width="846" height="289" alt="Screenshot 2026-05-10 at 16 12 46" src="https://github.com/user-attachments/assets/3f4fe903-98d5-4c0a-a7f9-de09cefd4d43" />

### Home Page

The landing page introduces the restaurant with a full-height hero section, a stats strip, an about section, a how-to-book walkthrough and a snapshot of the most recent approved reviews.

<img width="1728" height="993" alt="Screenshot 2026-05-10 at 14 25 07" src="https://github.com/user-attachments/assets/a98efd40-92a4-47d8-b251-7e7510626b72" />

### Book a Table

A clean form lets logged-in users pick a date (date-picker with today as the minimum), a time slot (select dropdown), party size (1–12) and optional special requests. The form rejects past dates and Tuesdays with friendly error messages.

<img width="1728" height="993" alt="Screenshot 2026-05-10 at 14 28 44" src="https://github.com/user-attachments/assets/2cee2cc8-9996-4806-9247-55480a35e3f7" />

### My Bookings

Bookings are split into two sections: Upcoming (with Edit and Cancel actions) and Past & Cancelled (read-only). Each card shows date, time, party size, status badge and any special requests.

<img width="1728" height="787" alt="Screenshot 2026-05-10 at 14 26 49" src="https://github.com/user-attachments/assets/f0af8575-b791-4e06-a053-4d7a4b631568" />

### Edit Booking

Pre-filled form lets the user change any field on an upcoming booking. Ownership is enforced server-side — visiting another user's edit URL returns a 403.

<img width="1728" height="992" alt="Screenshot 2026-05-10 at 14 28 03" src="https://github.com/user-attachments/assets/53462401-f3e2-4741-a38c-1d69dfe7ddfb" />

### Cancel Booking

A confirmation page explains that cancellation is permanent, then sets the booking status to cancelled on confirmation.

<img width="1728" height="538" alt="Screenshot 2026-05-10 at 14 27 08" src="https://github.com/user-attachments/assets/8f1d5e07-45d1-40b8-8678-8b9d54411827" />

### Menu

A structured menu page presents starters, mains, sides and desserts in a clean card layout. Prices and descriptions for each dish.

<img width="1728" height="992" alt="Screenshot 2026-05-10 at 14 29 27" src="https://github.com/user-attachments/assets/6c1c52b0-7da6-41dc-a1dc-59370bb91a93" />

### Reviews

All approved reviews are displayed in a responsive card grid with star ratings, reviewer name and date. Authenticated users who haven't reviewed yet see a Write a Review button. Users with a pending review see an awaiting approval notice with edit/delete links.

<img width="1728" height="767" alt="Screenshot 2026-05-10 at 14 31 49" src="https://github.com/user-attachments/assets/99f689c4-779f-45ce-bce6-8a11d57424f6" />

### Write / Edit a Review

A simple form for rating (1–5), title and comment. Each user can only submit one review — the button is hidden once they have one.

<img width="1728" height="969" alt="Screenshot 2026-05-10 at 14 31 21" src="https://github.com/user-attachments/assets/eb777811-7b99-4e0c-bec7-974627e09246" />

### Staff Bookings

A staff-only page lists all bookings from today onwards, grouped by status. Each row has an inline form to update the status (confirm or cancel) with a single click.

![Staff bookings](docs/images/staff_bookings.png)

### Error Pages

Custom 403, 404 and 500 pages match the site design and link back to the home page.

![404 page](docs/images/404.png)

### Flash Messages

Every form submission — create, edit, delete, cancel — triggers a Bootstrap alert that auto-dismisses after five seconds. Icons vary by message type (success ✓, warning !, error ✗).

---

## Agile Development

The project was planned and managed using GitHub Projects with a Kanban board. User stories were written as GitHub Issues before any code was written.

### MoSCoW Prioritisation

| Priority | Stories | Count |
|---|---|---|
| Must Have | US-01 to US-09, US-15, US-16 | 11 |
| Should Have | US-10 to US-14, US-17, US-18, US-21 | 8 |
| Could Have | US-19, US-20 | 2 |

All Must Have and Should Have stories were completed. Both Could Have stories were also completed within the available time.

### Sprint Overview

| Sprint | Focus | Stories |
|---|---|---|
| 1 | Project setup, models, admin | US-01, US-02, US-03 |
| 2 | Bookings CRUD | US-04 to US-09, US-15, US-16 |
| 3 | Reviews CRUD + moderation | US-10 to US-14, US-17, US-18 |
| 4 | UI polish, menu, error pages, testing | US-19, US-20, US-21 |

---

## Technologies Used

### Languages

| Language | Use |
|---|---|
| Python 3.11 | Back-end logic, Django views, models, forms |
| HTML5 | Templates |
| CSS3 | Custom styles |
| JavaScript (ES6) | Auto-dismiss alerts, date input min, confirm dialogs |

### Frameworks & Libraries

| Package | Version | Purpose |
|---|---|---|
| Django | 5.2 | Web framework |
| django-allauth | 65.4.1 | Email-based authentication |
| dj-database-url | 2.3.0 | DATABASE_URL parsing |
| psycopg2-binary | 2.9.10 | PostgreSQL adapter |
| gunicorn | 23.0.0 | WSGI production server |
| whitenoise | 6.9.0 | Static file serving |
| cloudinary | 1.42.1 | Media hosting |
| django-cloudinary-storage | 0.3.0 | Cloudinary integration |
| Bootstrap | 5.3.3 | Responsive UI framework |
| Bootstrap Icons | 1.11.3 | Icon set |
| Google Fonts | — | Playfair Display, Inter |

### Tools & Platforms

| Tool | Purpose |
|---|---|
| Git | Version control |
| GitHub | Remote repository, Projects board |
| Heroku | Cloud deployment |
| PostgreSQL (Heroku) | Production database |
| Cloudinary | Media file storage |
| VS Code | Development environment |
| Balsamiq | Wireframes |

---

## Testing

### Automated Tests

The project includes **35 automated tests** written with Django's built-in `TestCase` class, covering models, forms and views.

Run them with:

```bash
python manage.py test bookings
```

Expected output:

```
Found 35 test(s).
...................................
----------------------------------------------------------------------
Ran 35 tests in 0.847s

OK
```

#### Test breakdown

| Class | Tests | What's covered |
|---|---|---|
| `BookingModelTest` | 6 | String repr, `is_upcoming()`, status display, time label |
| `ReviewModelTest` | 3 | String repr, default approved=False, ordering |
| `BookingFormTest` | 5 | Valid data, past date, Tuesday, party size boundaries |
| `ReviewFormTest` | 3 | Valid data, rating boundaries, missing fields |
| `PublicViewTest` | 6 | Home, menu, reviews load; redirect when unauthenticated |
| `BookingViewTest` | 5 | Create, list, edit, cancel, ownership 403 |
| `ReviewViewTest` | 4 | Create, edit, delete, duplicate prevention |
| `StaffViewTest` | 3 | Staff page access, non-staff redirect, status update |

### Manual Testing

| Feature | Action | Expected result | Pass/Fail |
|---|---|---|---|
| Register | Submit form with valid email + password | Account created, redirected to home, success message | Pass |
| Register duplicate email | Submit existing email | Form error "A user is already registered with this email" | Pass |
| Login | Valid credentials | Logged in, success flash message | Pass |
| Login wrong password | Invalid credentials | Form error, no login | Pass |
| Book a table | Fill all fields, valid future date (not Tuesday) | Booking created, redirected to My Bookings | Pass |
| Book – past date | Enter yesterday's date | Form error "Bookings must be for a future date" | Pass |
| Book – Tuesday | Enter a Tuesday date | Form error "We are closed on Tuesdays" | Pass |
| Book – party size 0 | Enter 0 | Form error "Ensure this value is greater than or equal to 1" | Pass |
| Book – party size 13 | Enter 13 | Form error "Ensure this value is less than or equal to 12" | Pass |
| Edit booking | Change date/time on upcoming booking | Booking updated, success message | Pass |
| Edit another user's booking | Manually enter /bookings/99/edit/ | 403 Forbidden page | Pass |
| Cancel booking | Confirm cancellation | Status → cancelled, booking moves to Past section | Pass |
| Write review | Submit rating, title, comment | Review created, awaiting approval message shown | Pass |
| Write second review | Attempt while review exists | Redirected to reviews page, error message | Pass |
| Edit review | Update comment | Review updated, awaiting approval if previously approved | Pass |
| Delete review | Confirm deletion | Review removed, can now write a new one | Pass |
| Staff page – non-staff | Visit /staff/bookings/ as regular user | Redirected to login | Pass |
| Staff status update | Change booking status via dropdown | Status updated, success message | Pass |
| Review approval | Approve in Django admin | Review appears on public reviews page | Pass |
| Logout | Click Sign Out | Session cleared, redirected to home | Pass |
| 404 page | Visit /nonexistent-page/ | Custom 404 page displayed | Pass |
| Responsive layout | Resize to 375 px width | Navbar collapses, cards stack, no horizontal scroll | Pass |

### JavaScript Testing

| Function | Test | Expected | Pass/Fail |
|---|---|---|---|
| Alert auto-dismiss | Load page with flash message, wait 5 s | Alert fades and disappears | Pass |
| Date min | Open booking form | Date input `min` attribute set to today | Pass |
| Confirm dialog | Click Cancel on booking | Confirmation dialog appears before submit | Pass |
| Active nav | Navigate to My Bookings | My Bookings link has `active` class | Pass |

### Validator Testing

| Tool | File(s) | Result |
|---|---|---|
| W3C HTML Validator | All templates | No errors |
| W3C CSS Validator | `static/css/style.css` | No errors |
| JSHint | `static/js/main.js` | No errors, ES6 configured |
| CI Python Linter | All `.py` files | PEP8 compliant |
| Lighthouse (mobile) | Home page | Performance 92, Accessibility 100, Best Practices 100, SEO 100 |

### Browser Compatibility

| Browser | Tested | Result |
|---|---|---|
| Chrome 124 | Yes | All features work |
| Firefox 125 | Yes | All features work |
| Safari 17 (macOS) | Yes | All features work |
| Edge 124 | Yes | All features work |
| Chrome (Android) | Yes | Responsive, all features work |

---

## Bugs

### Resolved Bugs

**1. `split` template filter does not exist**

When building the menu page I initially tried to split a dot-separated string inside a Django template using `{{ item.sides|split:"·" }}` inside a `{% for %}` loop. Django's template language does not have a built-in `split` filter, so the page threw a `TemplateSyntaxError`. I resolved this by hardcoding the list items directly in the template rather than trying to split a string at render time.

**2. django-allauth deprecation warnings**

After installing `django-allauth==65.4.1`, running the development server logged several deprecation warnings for settings keys that were removed in version 65: `ACCOUNT_AUTHENTICATION_METHOD`, `ACCOUNT_USERNAME_REQUIRED`, `ACCOUNT_EMAIL_REQUIRED` and `ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE`. I replaced all four with the current equivalents: `ACCOUNT_LOGIN_METHODS = {'email'}` and `ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']`.

**3. WhiteNoise manifest warning on first run**

Running `collectstatic` for the first time before starting the server caused WhiteNoise to log `Missing staticfiles manifest entry for 'admin/...'`. This happened because the static files had not yet been collected when the `CompressedManifestStaticFilesStorage` backend tried to read the manifest. Running `python manage.py collectstatic --noinput` first resolved the warning entirely.

### Unfixed Bugs

There are no known unfixed bugs at the time of submission.

---

## Deployment

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/Cbyrne290-HUB/the-butcher.git
   cd the-butcher
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv butcher-env
   source butcher-env/bin/activate  # Windows: butcher-env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create `env.py` in the project root (never commit this file):
   ```python
   import os
   os.environ['SECRET_KEY'] = 'your-local-secret-key'
   os.environ['DEBUG'] = 'True'
   # Optional – omit to use SQLite locally
   # os.environ['DATABASE_URL'] = 'postgres://...'
   ```

5. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

### Heroku Deployment

1. Create a new Heroku app from the Heroku dashboard.

2. Under **Resources**, search for and attach **Heroku Postgres** (this automatically sets `DATABASE_URL`).

3. Under **Settings → Config Vars**, add:

   | Key | Value |
   |---|---|
   | `SECRET_KEY` | A long random string |
   | `DEBUG` | `False` |
   | `CLOUDINARY_URL` | Your Cloudinary API environment variable |

4. Under **Deploy**, connect the GitHub repository and enable automatic deploys from `main`.

5. In the Heroku console (More → Run console):
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   python manage.py createsuperuser
   ```

6. Open the app — the live site should be running.

> **Note:** `Procfile` contains `web: gunicorn the_butcher.wsgi --log-file -` and `runtime.txt` specifies `python-3.11.15`. Both are committed to the repository and picked up automatically by Heroku.

---

## Credits

### Content

- Restaurant name, concept and all written copy are fictional and created by me for this project.
- Menu items and descriptions are fictional.

### Media

- Hero image: [Unsplash](https://unsplash.com/photos/grilled-steak) — free to use under the Unsplash licence.
- About section image: [Unsplash](https://unsplash.com) — free to use under the Unsplash licence.
- Colour palette image: [Coolors](https://coolors.co/?home)  

### Code

- Django documentation — [https://docs.djangoproject.com](https://docs.djangoproject.com)
- django-allauth documentation — [https://docs.allauth.org](https://docs.allauth.org)
- WhiteNoise documentation — [https://whitenoise.readthedocs.io](https://whitenoise.readthedocs.io)
- Bootstrap 5 documentation — [https://getbootstrap.com/docs/5.3](https://getbootstrap.com/docs/5.3)
- Code Institute Django walkthrough projects — for initial project structure patterns
- Stack Overflow community — for specific Django form validation and queryset questions

### Acknowledgements

- My mentor at Code Institute for guidance throughout the project.
- The Code Institute Slack community for support and encouragement.
