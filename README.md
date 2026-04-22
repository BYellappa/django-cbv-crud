
# 🚀 Django CBV CRUD Project

## 📌 About

This is a Django project built using **Class-Based Views (CBV)**.
It performs full CRUD operations on Company data.

---

## ⚙️ Features

* View all companies
* View company details
* Add new company
* Update company
* Delete company

---

## 🛠️ Tech Used

* Python
* Django
* SQLite
* HTML

---

## ▶️ Run Project

```bash
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 🌐 URLs

* `/list/` → List page
* `/create/` → Add company
* `/update/<id>/` → Update
* `/delete/<id>/` → Delete

---

## 🎯 Learning

* Learned Django CBV
* Built full CRUD app
* Worked with templates & URLs

---

## 🙌 Author

Pandu

## 📸 Screenshots & Flow

### 🟢 1. Company List Page

* Displays all companies
* Each company has **View, Update, Delete** options

👉 Click on company name → opens **Detail Page**

---

### 🔵 2. Company Detail Page

* Shows complete details of selected company

👉 Click “Back” → returns to **List Page**

---

### 🟡 3. Create Company Page

* Form to add new company

👉 Click “Submit” → saves data → redirects to **List Page**

---

### 🟠 4. Update Company Page

* Edit existing company details

👉 Click “Update” → updates data → redirects to **List Page**

---

### 🔴 5. Delete Confirmation Page

* Confirms before deleting

👉 Click “Yes, Delete” → deletes record → redirects to **List Page**
