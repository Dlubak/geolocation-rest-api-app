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
    "username": "[str]",
    "password": "[str]"
}
```

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `{ username: username }`


**JWT Token**
----
  GET JWT TOKEN

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

  * **Code:** 20 <br />
    **Content:** `{ refresh: token, access: token }`


**Create Geolocation Entry**
----
  Create Geolocation Entry

* **URL**

  `/api/geo/create`

* **Method:**

  `POST`

* **Data Params**

```json
{
    "ip": "[ipv4]",
}
```

* **Success Response:**

  * **Code:** 201 <br />

**Retrieve Geolocation Entry**
----
  Retrieve Geolocation Entry

* **URL**

  `/api/geo/retrieve`

* **Method:**

  `GET`

* **Query Params**

    `ip=x.x.x.x`

* **Success Response:**

  * **Code:** 200 <br />


**Delete Geolocation Entry**
----
  Delete Geolocation Entry

* **URL**

  `/api/geo/retrieve`

* **Method:**

  `DELETE`

* **Query Params**

    `ip=x.x.x.x`

* **Success Response:**

  * **Code:** 204 <br />

