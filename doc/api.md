# API

## account_idからの検索

#### URL

**/account/get/\<account_id\>**

#### HTTP METHOD

GET

#### request

GETのためなし

#### response

```request
{
  "body": {
     "name": "account",
     "id": <account_id>,
     "account_name": <account_name>,
     "start_on": "2021-01-01 10:00:00",
     "end_on": "2025-12-31 21:00:00"
  },
  "status": {
    "code" : "I0001",
    "message" : "",
    "detail" : ""
  }
}
```




## account作成

#### URL

/account/create

#### HTTP METHOD

POST

#### request


```
{
    "account_name":
    "start_on":
    "end_on":
    "operation_account_id":
}
```

#### response

```
{
  "body" : "",
  "status": "I0001",
  "message": "account {} was created.",
  "detail": ""
}
```


## account検索

#### URL

/account/search

#### HTTP METHOD

POST

#### request

```
{
	"account_name":"flask_sv2", 
	"start_on":"2021-05-05 00:00:00", 	"end_on":"2030-12-31 00:00:00"
}
```


#### response

```
{
	"body": "",
   "status": {
   		"code" : code,
   		"message" : message,
       "detail" : ""
   }
}
```


## account更新

#### URL

/account/update

#### HTTP METHOD

POST

#### request

#### response

## account削除


#### URL

/account/delete/<account_id>

#### HTTP METHOD

GET

#### request

#### response
