# Vue + Flask on Docker

## <span style="color:orange">Vue on Docker</span>

### Docker 起動
```
docker-compose build
```
```
docker-compose up -d
```
```
docker compose logs -f
```



### <span style="color:orange">vue_containerのshellに入る</span>
```
docker-compose exec vue /bin/sh
```
```
cd frontend/
```
```
npm run build
```
```
npm run dev
```

localhost:8080/home


## <span style="color:orange">Flask on Docker</span>

```
docker-compose exec flask bash
```
```
cd backend
```
```
python app.py
```

localhost:9000/home

