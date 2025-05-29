# django_sprint4
```
django_sprint4
├─ blogicum
│  ├─ blog
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_auto_20250402_1327.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ blogicum
│  │  ├─ asgi.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  ├─ wsgi.py
│  │  └─ __init__.py
│  ├─ manage.py
│  ├─ pages
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ static_dev
│  │  ├─ css
│  │  │  └─ bootstrap.min.css
│  │  └─ img
│  │     ├─ fav
│  │     │  ├─ android-chrome-192x192.png
│  │     │  ├─ android-chrome-256x256.png
│  │     │  ├─ apple-touch-icon.png
│  │     │  ├─ favicon-16x16.png
│  │     │  ├─ favicon-32x32.png
│  │     │  ├─ favicon.ico
│  │     │  └─ mstile-150x150.png
│  │     └─ logo.png
│  └─ templates
│     ├─ base.html
│     ├─ blog
│     │  ├─ category.html
│     │  ├─ comment.html
│     │  ├─ create.html
│     │  ├─ detail.html
│     │  ├─ index.html
│     │  ├─ profile.html
│     │  └─ user.html
│     ├─ includes
│     │  ├─ category_link.html
│     │  ├─ comments.html
│     │  ├─ footer.html
│     │  ├─ header.html
│     │  ├─ paginator.html
│     │  └─ post_card.html
│     ├─ pages
│     │  ├─ 403csrf.html
│     │  ├─ 404.html
│     │  ├─ 500.html
│     │  ├─ about.html
│     │  └─ rules.html
│     └─ registration
│        ├─ logged_out.html
│        ├─ login.html
│        ├─ password_change_done.html
│        ├─ password_change_form.html
│        ├─ password_reset_complete.html
│        ├─ password_reset_confirm.html
│        ├─ password_reset_done.html
│        ├─ password_reset_form.html
│        └─ registration_form.html
├─ db.json
├─ LICENSE
├─ pytest.ini
├─ README.md
├─ requirements.txt
├─ setup.cfg
└─ tests
   ├─ adapters
   │  ├─ comment.py
   │  ├─ model_adapter.py
   │  ├─ post.py
   │  ├─ student_adapter.py
   │  └─ user.py
   ├─ conftest.py
   ├─ fixtures
   │  ├─ categories.py
   │  ├─ comments.py
   │  ├─ locations.py
   │  ├─ posts.py
   │  └─ types.py
   ├─ form
   │  ├─ base_form_tester.py
   │  ├─ base_tester.py
   │  ├─ comment
   │  │  ├─ create_form_tester.py
   │  │  ├─ delete_tester.py
   │  │  ├─ edit_form_tester.py
   │  │  └─ find_urls.py
   │  ├─ delete_tester.py
   │  ├─ find_urls.py
   │  ├─ post
   │  │  ├─ create_form_tester.py
   │  │  ├─ delete_tester.py
   │  │  ├─ edit_form_tester.py
   │  │  ├─ find_urls.py
   │  │  └─ form_tester.py
   │  └─ user
   │     └─ edit_form_tester.py
   ├─ test_comment.py
   ├─ test_content.py
   ├─ test_edit.py
   ├─ test_emails.py
   ├─ test_err_pages.py
   ├─ test_post.py
   ├─ test_static_pages.py
   └─ test_users.py

```