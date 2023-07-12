# Components Team Repo
# Prerequisite
JDK 17 must be installed
# Creating the .jar file
To create a .jar file for the Spring app enter the command `./mvnw clean package`

# Starting the server
use the command 

```./mvnw spring-boot:run```

or after building the jar file use the command

```java -jar target/<name of the jar>.jar```
# POST Request

supply the header application/json then in the body supply something like this 
```json
{
    "id": 1,
    "items": [
        {
            "name": "pizza",
            "price": 10.25
        },
        {
            "name": "steak",
            "price": 68.99
        }
    ]
}
```
# GET Request
Use the endpoint with a path parameter of the table id 
```
http://localhost:8080/table/{id}
```
