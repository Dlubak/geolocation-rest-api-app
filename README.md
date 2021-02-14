# GeoLocationData APP API
**Deploy Application**
----
1. docker build .
2. docker-compose build
3. docker-compose up


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
    "username": "[str]",
    "password": "[str]"
}
```

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `{ username: username }`


**JWT Token**
----
  Get token for user

* **URL**

  `/api/token/`

* **Method:**

  `POST`

* **Data Params**

```json
{
    "username": "[str]",
    "password": "[str]"
}
```

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ refresh: token, access: token }`


**Create Geolocation Entry**
----
  Create Geolocation Entry

* **URL**

  `/api/geo/create`

* **Method:**

  `POST`

* **Authorization**

    `JWT`

* **Headers**

    `Authorization: Bearer <token>`

* **Data Params**

```json
{
    "ip": "[ipv4]",
}
```

* **Success Response:**

  * **Code:** 201 <br />
   **Content:** `{'Geolocation object'}`

**Retrieve Geolocation Entry**
----
  Retrieve Geolocation Entry from database

* **URL**

  `/api/geo/retrieve`

* **Method:**

  `GET`

* **Authorization**

    `JWT`

* **Headers**

    `Authorization: Bearer <token>`

* **Query Params**

    `ip=x.x.x.x`

* **Success Response:**

  * **Code:** 200 <br />
  **Content:** `{'Geolocation object'}`


**Delete Geolocation Entry**
----
  Delete Geolocation Entry

* **URL**

  `/api/geo/retrieve`

* **Method:**

  `DELETE`

* **Authorization**

    `JWT`

* **Headers**

    `Authorization: Bearer <token>`

* **Query Params**

    `ip=x.x.x.x`

* **Success Response:**

  * **Code:** 204 <br />

