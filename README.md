
## 📌 Postman API Testing Guide & Endpoints

Base URL: `http://127.0.0.1:8000/api`

---

### 1. Reporters Endpoints

#### 1.1 Create Reporter (Success)
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/api/reporters/`
> 📸 **Screenshot 1: Create Reporter (POST 201)**
> 
> ![alt text](<Screenshot 2026-10-11 at 9.48.55 PM.png>)

---

#### 1.2 Create Reporter - Validation Error (Invalid Email)
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/api/reporters/`

> 📸 **Screenshot 2: Reporter Validation Error (POST 400)**
> 
> ![alt text](<Screenshot 2026-10-11 at 9.53.19 PM.png>)

---

#### 1.3 Get All Reporters
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/api/reporters/`
> 📸 **Screenshot 3: Get All Reporters (GET 200)**
> 
> ![alt text](<Screenshot 2026-10-11 at 9.55.23 PM.png>)

---

#### 1.4 Get Single Reporter by ID
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/api/reporters/?id=1`

> 📸 **Screenshot 4: Get Reporter by ID (GET 200)**
> 
> ![alt text](<Screenshot 2026-10-11 at 9.56.35 PM.png>)
---

### 2. Issues Endpoints

#### 2.1 Create Critical Issue (Polymorphism: CriticalIssue)
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/api/issues/`
> 📸 **Screenshot 5: Create Critical Issue (POST 201 with polymorphic message)**
> ![alt text](<Screenshot 2026-10-11 at 10.05.18 PM.png>)

---

#### 2.2 Create Low Priority Issue (Polymorphism: LowPriorityIssue)
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/api/issues/`
> 📸 **Screenshot 6: Create Low Priority Issue (POST 201)**
> 
> ![alt text](<Screenshot 2026-10-11 at 10.08.53 PM.png>)

---

#### 2.3 Create Issue - Validation Error (Invalid Status/Priority)
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/api/issues/`
> 📸 **Screenshot 7: Issue Validation Error (POST 400)**
> 
> ![alt text](<Screenshot 2026-10-11 at 10.10.03 PM.png>)

---

#### 2.4 Get All Issues
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/api/issues/`
> 📸 **Screenshot 8: Get All Issues (GET 200)**
> 
> ![alt text](<Screenshot 2026-10-11 at 10.10.03 PM-1.png>)

---

#### 2.5 Filter Issues by Status
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/api/issues/?status=open`
- **Expected Status**: `200 OK`
> 📸 **Screenshot 9: Filter Issues by Status (GET 200 with query param)**
> 
> ![alt text](<Screenshot 2026-10-11 at 10.13.04 PM.png>)

---

#### 2.6 Get Single Issue by ID
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/api/issues/?id=101`
- **Expected Status**: `200 OK`
> 📸 **Screenshot 10: Get Issue by ID (GET 200 with query param)**
> 
> ![alt text](<Screenshot 2026-10-11 at 10.14.07 PM.png>)

---
