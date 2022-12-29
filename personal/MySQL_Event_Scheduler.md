# MySQL Event Scheduler
[MySQL 공식문서](https://dev.mysql.com/doc/refman/8.0/en/create-event.html)

### CREATE EVENT Statement
▫ 새 이벤트를 만들고 예약   
▫ 이벤트 스케줄러가 활성화되어 있지 않으면 이벤트 실행 X      
▫ 이벤트가 생성될 스키마에 대한 권한 필요 

``` sql
CREATE
    [DEFINER = user]
    EVENT
    [IF NOT EXISTS]
    event_name
    ON SCHEDULE schedule
    [ON COMPLETION [NOT] PRESERVE]
    [ENABLE | DISABLE | DISABLE ON SLAVE]
    [COMMENT 'string']
    DO event_body;

schedule: {
    AT timestamp [+ INTERVAL interval] ...
  | EVERY interval
    [STARTS timestamp [+ INTERVAL interval] ...]
    [ENDS timestamp [+ INTERVAL interval] ...]
}
```    

#### 최소 요구 사항    
1️⃣ CREATE EVENT    
▫ 데이터베이스 스키마에서 이벤트를 고유하게 식별하는 키워드와 **이벤트 이름** 

2️⃣ ON SCHEDULE   
▫ 이벤트가 실행되는 시기와 빈도를 결정 = 수행, 반복할 시간 및 기간    
- AT : 수행할 시간
- EVERY : 반복할 시간
- STARTS, ENDS : 반복할 기간

> interval 종류
``` sql
interval:
    quantity {YEAR | QUARTER | MONTH | DAY | HOUR | MINUTE |
              WEEK | SECOND | YEAR_MONTH | DAY_HOUR | DAY_MINUTE |
              DAY_SECOND | HOUR_MINUTE | HOUR_SECOND | MINUTE_SECOND}
```

3️⃣ DO   
▫ 실행될 SQL문이 포함된 절   


최소 CREATE EVENT 문 예시     
``` sql
CREATE EVENT myevent
    ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 HOUR
    DO
      UPDATE myschema.mytable SET mycol = mycol + 1;
``` 

---

# 실행

1️⃣ 기본 설정   
``` sql
SHOW VARIABLES LIKE 'event%';
```
event_scheduler가 ON이 되어있는 것을 확인     
OFF 상태일 경우, 아래 명령어를 통해 설정 변경   
``` sql
SET GLOBAL event_scheduler = ON;
```


2️⃣ 이벤트 스케줄러 확인    
``` sql
SELECT * FROM information_schema.events;
```

3️⃣ 이벤트 스케줄러 생성    
