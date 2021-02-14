# GeoLocationData APP API

**Create User**
----
  Create User

* **URL**

  `/api/user/create`

* **Method:**

  `POST`

* **Data Params**

```json
{
    "username": "[1 to 30 chars]",
    "password": "[1 to 30 chars]"
}
```

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ username }`