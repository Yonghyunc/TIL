# TIL

## [Database](#database-1)  
▫ [RDB](#-rdb)

## [SQL](#sql-1)

## [DDL](#ddl-data-definition-language)
▫ [CREATE](#-create-table)  
▫ [Data Type](#-sqlite-data-types)  
▫ [Constraints](#-constraints-제약조건)  
▫ [ALTER](#-alter-table)  
▫ [DROP](#-drop-table)


## [DML](#dml-data-manipulation-language)
▫ [SELECT](#-simple-query)
- [정렬](#-sorting-rows-정렬)
- [필터링](#-filtering-data)
- [그룹화](#-grouping-data)

▫ [INSERT](#-insert)  
▫ [UPDATE](#-update)  
▫ [DELETE](#-delete)

<br><br>

---

# Database

지금은 데이터의 시대 ➡ 어디에, 어떻게 이 데이터를 저장할까? ➡ **데이터베이스**  

<br>

### ▶ 데이터 관리  
1️⃣ 파일
- 쉽고 간편
- BUT 성능, 보안 한계 / 대용량 X / 구조적 정리 어려움 / 확장 불가  

2️⃣ 스프레드시트
- 컬럼(열) + 레코드(행)

3️⃣ 데이터베이스
- 프로그래밍 언어 사용 O
- 가장 많이 쓰이는 유형 : 관계형 데이터베이스 (RDB)
- RDB는 각각의 데이터를 테이블에 기입함

<br>

```
데이터베이스에 데이터를 어떻게 입력하고, 어떻게 출력하는가  

즉, 데이터베이스의 CRUD
```
<br><br>

## 📋 Database
◽ 체계화된 데이터의 모임  
◽ 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합  
◽ 검색, 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템  

◽ 데이터베이스 조작 프로그램 = DBMS (Database Management System)  
- Oracle, MySQL, SQLite 등

◽ 웹 개발에서 대부분의 데이터베이스는 **"관계형 데이터베이스 관리 시스템(RDBMS)"** 를 사용하여 SQL로 데이터와 프로그래밍을 구성  

<br><br>

## 📋 RDB
◽ Relational Database (관계형 데이터베이스)  
◽ 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식  
◽ 자료를 여러 테이블로 나누어 관리하고, 이 테이블간 관계를 설정해 여러 데이터를 쉽게 조작 O  
◽ SQL을 사용하여 데이터 조회, 조작  

<br>

### ▶ RDB 기본 구조  
1️⃣ 스키마  
◽ 테이블의 구조
◽ 자료 구조, 표현 방법, 관계 등 전반적인 명세 기술  

2️⃣ 테이블  
◽ 필드 + 레코드  
◽ = 관계
1. 필드 : 속성, 컬럼
2. 레코드 : 튜플, 행

3️⃣ PK (Primary Key)  
◽ 기본 키  
◽ 각 레코드의 고유한 값 (구분 O)  
◽ 다른 항목과 절대로 중복될 수 없는 **단일 값 (Unique)**

<br>

### ▶ 관계형 데이터베이스의 이점
◽ 데이터 직관적 표현  
◽ 관련한 각 데이터에 쉽게 접근  
◽ 대량의 데이터도 효율적으로 관리 가능


<br><br>

---

# SQL
Structured Query Language  

◽ RDBMS의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어  
◽ RDBMS에서 데이터베이스 스키마를 생성 및 수정, 테이블에서의 자료 검색 및 관리 O  
◽ 데이터베이스 객체에 대한 처리를 관리하거나 접근 권한을 설정하여 허가된 사용자만 RDBMS를 관리할 수 있도록 할 수 있음  

◽ 즉, SQL은 데이터베이스와 상호작용하는 방법

<br> 

### ▶ SQL Commands
1️⃣ DDL  
2️⃣ DML  
3️⃣ DCL 

![image](https://user-images.githubusercontent.com/93974908/193737822-d92a34e6-b17f-47f4-b6ee-6cdf48b55724.png)

> ❌ SQLite는 파일로 관리되는 DB이기 때문에 SQL을 이용한 접근 제한이 아닌 운영 체제의 파일 접근 권한으로만 제어가능  
그래서 SQLite에는 권한 설정을 담당하는 GRANT와 REVOKE는 지원하지 않아 DCL 부분은 생략

<br> 

### ▶ SQL Syntax
``` sql
SELECT column_name FROM table_name;
```
◽ 모든 SQL문은 SELECT, INSERT, UPDATE 등과 같은 키워드로 시작  
◽ 하나의 statement는 세미콜론(;)으로 끝남  
◽ 대소문자 구분 X, BUT 대문자 사용 권장  
◽ 들여쓰기는 중요하지 않음  
◽ 주석 : --

<br>

> **Statement (문)**  
> 독립적으로 실행할 수 있는 완전한 코드 조각  
> ``` sql
> SELECT column_name FROM table_name;
> ```

> **Clause (절)**  
> statement의 하위 단위
> ``` sql
> SELECT column_name
> FROM table_name
> ```


<br><br>

---

# DDL (Data Definition Language)
Data definition  

◽ 테이블 구조 관리  
➡ CREATE, ALTER, DROP


> DDL.sql에서 오른쪽 마우스 use database 눌러서 mydb.sqlite3 선택


<br><br>

## 📌 CREATE TABLE
◽ 데이터베이스에 새 테이블을 만듦
``` sql
-- 컬럼명, 데이터 타입, 제약조건

CREATE TABLE table_name (
  column_1 data_type constraints,
  column_2 data_type constraints,
  column_3 data_type constraints
);
```

> 실행하고자 하는 문장 안에 커서 - > 오른쪽 마우스 (run selected query)

![image](https://user-images.githubusercontent.com/93974908/193740327-50cf25b4-91be-45fd-8996-e6b014c7e2c4.png)

◽ id 컬럼은 직접 기본 키 역할의 컬럼을 정의하지 않으면, 자동으로 **rowid** 라는 컬럼으로 만드어짐

<br><br>


## 🔎 SQLite Data Types
1️⃣ NULL  
▫ NUll value  
▫ 정보가 없거나 알 수 없음

2️⃣ INTEGER  
▫ 정수  
▫ 가변 크기  

3️⃣ REAL  
▫ 실수  
▫ 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수  

4️⃣ TEXT  
▫ 문자 데이터 

5️⃣ BLOB  
▫ 입력된 그대로 저장된 데이터 덩어리  
▫ 바이너리 등 멀티미디어 파일  

> Boolean type
> 
> 별도의 Boolean 타입이 없기 때문에, 0(False)과 1(True)로 저장


> Date & Time datatype  
> 
> 날짜 및 시간을 저장하기 위한 타입 없음  
> 대신, 빌트인 함수를 사용하여 TEXT, REAL, INTEGER 등으로 저장할 수 있음

> Binary data
> 
> 데이터의 저장과 처리를 목적으로 0과 1의 이진 형식으로 인코딩 된 파일  
> 기본적으로 컴퓨터의 모든 데이터는 binary data  
> 다만, 이를 필요에 따라 텍스트 타입으로 변형해서 사용하는 것

<br>

### ▶ 데이터 타입 결정 규칙  
▫ 값에 둘러싸는 따옴표, 소수점, 지수가 없으면 ➡ **INTEGER**  
▫ 값이 작은 따옴표, 큰 따옴표로 묶이면 ➡ **TEXT**  
▫ 값에 따옴표, 소수점, 지수가 없으면 ➡ **REAL**  
▫ 값이 따옴표 없이 NULL이면 ➡ **NULL** 

<br>

### ▶ SQLite Datatypes 특징 
▫ 동적 타입 시스템  

▫ 컬럼에 저장된 값에 따라 데이터 타입 결정  
▫ 테이블 생성 시, 컬럼에 대해 데이터 타입 선언하지 않아도 됨  

▫ 기존의 엄격하게 타입이 지정된 데이터베이스에서 불가능한 작업을 유연하게 수행 가능  

▫ 정적 타입 시스템이 지정된 데이터베이스에서 작동하는 SQL문이 SQLite에서 동일한 방식으로 작동함  

**BUT, 다른 데이터베이스와의 호환성 문제가 있기 때문에 데이터 타입을 지정하는 것을 권장**

▫ 데이터 타입을 지정하게 되면 SQLite는 입력된 데이터의 타입을 지정된 데이터 타입으로 변환  

> 허용 가능한 타입 변환
> 
> ![image](https://user-images.githubusercontent.com/93974908/193743334-33662d3b-31d9-4cb0-9072-8a4d1b4b1dad.png)

> 정적이고 엄격한 데이터베이스 ➡ 선언된 데이터 타입에 의해 결정됨

<br>

### ▶ Type Affinity (타입 선호도)
▫ 특정 컬럼에 저장된 데이터에 권장되는 타입  
▫ 다른 데이터 타입을 선언한다면, 내부적으로 각 타입의 지정된 선호도에 따라 5가지 선호도로 인식됨  

![image](https://user-images.githubusercontent.com/93974908/193743692-cd32c014-461b-4bb3-85f8-769300ffc8ac.png)

▫ 다른 데이터베이스 엔진 간의 **호환성** 최대화  

<br><br>

## 🔎 Constraints (제약조건)
▫ 입력하는 자료에 대해 제약을 정함  
▫ 제약에 맞지 않다면 입력이 거부됨  
▫ 사용자가 원하는 조건의 데이터만 유지하기 위해, 즉 데이터의 무결성을 유지하기 위해 테이블의 특정 컬럼에 설정하는 제약  

> 데이터 무결성  
> 
> 데이터베이스 내의 데이터에 대한 정확성, 일관성

1️⃣ NOT NULL  
▫ 컬럼이 NULL 값을 허용하지 않도록 지정  
▫ 명시적으로 사용하지 않는 컬럼은 NULL값을 허용함  

2️⃣ UNIQUE  
▫ 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함  

3️⃣ PRIMARY KEY  
▫ 테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼  
▫ 테이블 당 하나의 기본 키  
▫ 암시적으로 NOT NULL 제약 조건 포함  
``` sql
CREATE TABLE table_name (
  id INTEGER PRIMARY KEY,
  ..
);
```
**❗INTEGER 타입에만 사용 가능❗**

4️⃣ AUTOINCREMENT  
▫ 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지  
▫ Django에서 테이블 생성 시 id컬럼에 기본적으로 사용하는 제약조건  

> 장고에서 pk값을 재사용 하지 않았음  
> 장고는 기본적으로 AUTOINCREMENT가 설정되어 있구나  


5️⃣ 그외 기타 Constaints

<br>

### ▶ rowid
▫ 테이블을 생성할 때마다 자동 생성   
▫ 암시적 자동 증가 컬럼  
▫ 테이블의 행을 고유하게 식별하는 64비트 부호 있는 정수 값  
▫ 테이블에 새 행을 삽입할 때마다 정수 값을 자동으로 할당  

▫ 값은 1에서 시작  
▫ 1씩 증가  

▫ 만약 INTEGER PRIMARY KEY 키워드를 가진 컬럼을 직접 만들면 이 컬럼은 rowid 컬럼의 별칭이 됨  
➡ 새 컬럼 이름으로 rowid 액세스 O + rowid 이름으로도 액세스 O  

▫ 데이터가 최대 값에 도달하고 새 행을 삽입하여고 하면 SQLite는 사용되지 않는 정소를 찾아 사용 
> 이론상으로 도달하기는 어렵다:)

▫ 테이블이 꽉 찼을 때, 사용되지 않은 정수를 찾을 수 없으면 SQLITE_FULL 에러 발생  


<br><br>

## 📌 ALTER TABLE
▫ 기존 테이블의 구조를 수정(변경)

1️⃣ Rename a table (테이블명 변경)
``` sql
ALTER TABLE table_name RENAME TO new_table_name;
```

2️⃣ Rename a column (컬럼명 변경)

``` sql
ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name;
```

3️⃣ Add a new column to a table (새 컬럼 추가)
``` sql
ALTER TABLE table_name ADD COLUMN column_definition;
```

❗❗ 발생 가능한 에러
``` sql
ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL;
```
> 테이블에 데이터가 없을 때는 추가가 잘 됨  
> BUT 기존 데이터가 있을 때, 에러 발생  
> ``` sql
> Cannot add NOT NULL column with default value NULL
> ```
이전에 이미 저장된 데이터들을 새롭게 추가되는 컬럼에 값이 없기 때문에 NULL이 작성됨  

그러나 새로 추가되는 컬럼에 NOT NULL 제약조건이 있으면 기본 값 없이는 추가될 수 없다는 에러 발생  

➡ DEFALUT 제약 조건을 사용하여 해결 가능
``` sql
ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address';
```

4️⃣ Delete a column (컬럼 삭제)
``` sql
ALTER TABLE table_name DROP COLUMN column_name;
```
❗❗ 단, 삭제하지 못하는 경우 존재  
▫ 컬럼이 다른 부분에서 참조되는 경우 (FK 제약조건)  
▫ PK인 경우  
▫ UNIQUE 제약 조건이 있는 경우  

<br><br>

## 📌 DROP TABLE
▫ 데이터베이스에서 테이블을 제거  
``` sql
DROP TABLE table_name;
```
▫ 존재하지 않는 테이블을 제거하면 SQLite에서 오류 발생  

▫ 한 번에 하나의 테이블만 삭제 가능   
➡ 여러 테이블을 제거하려면 여러 DROP TABEL 문 실행  

▫ 실행 취소, 복구 불가 



<br><br>

---

# DML (Data Manipulation Language)
▫ CRUD  
▫ INSERT (C), SELECT (R), UPDATE (U), DELETE (D)  

<br>

쉘 - csv 파일 열기 위해 사용

![image](https://user-images.githubusercontent.com/93974908/193748652-ef8e23b1-520d-40c6-a5da-c9c1b2c3e346.png)

![image](https://user-images.githubusercontent.com/93974908/193748877-6e48c1da-9555-410c-9e5e-d41678ed227f.png)


<br>

## 🚩 Simple query
▫ **SELECT** 문을 사용하여 간단하게 단일 테이블에서 데이터 조회  

▫ 문법 규칙
- SELECT 절에서 컬럼 또는 쉼표로 구분된 컬럼 목록 지정
- FROM 절에서 데이터를 가져올 테이블 지정

``` sql
-- 특정 테이블 조회
SELECT first_name, age FROM users;

-- 전체 데이터 조회
SELECT * FROM users;

-- rowid 컬럼 조회
SELECT rowid, first_name FROM users;
```
> 전체 데이터 조회 시, 모든 컬럼에 대한 약칭인 *(asterist) 사용 O


<br>

▫ 다양한 절과 함께 사용 가능  
1️⃣ ORDER BY  
2️⃣ DISTINCT  
3️⃣ WHERE  
4️⃣ LIMIT  
5️⃣ LIKE  
6️⃣ GRUOP BY



<br><br>

## 🚩 Sorting rows (정렬)
### 🔹 ORDER BY  

▫ SELECT 문에 추가하여 결과 정렬  
▫ ORDER BY 절은 FROM 절 뒤에 위치  

- ASC : 오름차순 (기본 값)
- DESC : 내림차순

``` sql
-- 이름과 나이를 나이가 어린 순으로 조회
SELECT first_name, age FROM users 
ORDER BY age;

-- 이름과 나이를 나이가 많은 순으로 조회
SELECT first_name, age FROM users 
ORDER BY age DESC;

-- 이름, 나이, 계좌 잔고를 나이가 어린순으로, 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회
SELECT first_name, age, balance 
FROM users 
ORDER BY age ASC, balance DESC;
```
▫ ORDER BY 절은 하나 이상의 컬럼을 정렬할 경우 첫 번째 열을 사용하여 행을 정렬하고, 그런 다음 두 번째 컬럼을 사용하여 정렬되어 있는 행을 정렬함  


> NULL - 가장 작은 값으로 간주


<br><br>

## 🚩 Filtering data 
### ▶ Clause
<br>

#### 🔹 SELECT DISTINCT : 중복 제거  

▫ DISTINCT 절은 SELECT 키워드 바로 뒤에 사용  
▫ DISTINCT 키워드 뒤에 컬럼 또는 컬럼 목록 작성  
  > NULL - 중복으로 간주 (하나만 남김)

``` sql
-- 모든 지역 조회
SELECT country FROM users;

-- 중복없이 모든 지역 조회
SELECT DISTINCT country FROM users;

-- 지역 순으로 내림차순 정렬하여 중복없이 모든 지역 조회
SELECT DISTINCT country FROM users
ORDER BY country;

-- 이름과 지역이 중복없이 모든 이름, 지역 조회하기
SELECT DISTINCT first_name, country 
FROM users;

-- 이름과 지역이 중복없이 지역 순으로 내림차순 정렬하여 모든 이름, 지역 조회
SELECT DISTINCT first_name, country
FROM users ORDER BY country DESC;
```
> 여러 컬럼의 중복 제거 시, 각 컬럼의 중복을 따로 계산하는 것이 아니라 두 컬럼을 하나의 집합으로 보고 중복 제거 

<br>

#### 🔹 WHERE : 특정 검색 조건 지정  
▫ SELECT 문 외에도 UPDATE 및 DELETE 문에서 WHERE 절 사용 가능  
▫ FROM 절 뒤에 작성  

 
> 비교연산자 - 파이썬과 동일  
> 논리연산자 - Boolean 데이터 타입이 없으므로 1, 0 으로 반환

``` sql
-- 나이가 30살 이상인 사람들의 이름, 나이, 계좌 잔고 조회
SELECT first_name, age, balance
FROM users
WHERE age >= 30;

-- 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회
SELECT first_name, age, balance
FROM users
WHERE age >= 30 AND balance > 500000;
```

<br>

#### 🔹 LIMIT
▫ 쿼리에서 반환되는 행 수 제한  

``` sql
-- 첫 번째부터 열 번째 데이터까지 rowid, 이름 조회
SELECT rowid, first_name FROM users
LIMIT 10;

-- 계좌 잔고가 가장 많은 10명의 이름, 계좌 잔고 조회
SELECT first_name, balance FROM users
ORDER BY balance DESC LIMIT 10;

-- 나이가 가장 어린 5명의 이름, 나이 조회
SELECT first_name, age FROM users
ORDER BY age LIMIT 5;

-- 11번째부터 20번째 데이터의 rowid, 이름 조회
SELECT rowid, first_name FROM users
LIMIT 10 OFFSET 10;
```
▫ OFFSET : 특정 지정 위치에서부터 데이터 조회 가능  


<br><br>

### ▶ Operator

<br>

#### 🔸 LIKE  
▫ 패턴 일치를 기반으로 데이터 조회  
▫ SELECT, DELETE, UPDATE 문의 WHERE 절에서 사용  
▫ 대소문자 구분 X  

- **% (percent)** : 0개 이상의 문자가 올 수 있음  
- **_ (underscore)** : 단일 (1개) 문자  
➡ 섞어서 사용 가능

![image](https://user-images.githubusercontent.com/93974908/193773778-b660b0a5-b1c0-40b0-8b6a-2245a3e11227.png)

> **"wildcards"**  
> 
> ▫ 파일을 지정할 때, 구체적인 이름 대신 여러 파일을 동시에 지정할 목적으로 사용  ( *, ? 등 )  
> ▫ 주로 특정한 패턴이 있는 문자열 혹은 파일을 찾거나, 긴 이름을 생략할 때 사용

``` sql
-- 이름에 '호'가 포함되는 사람들의 이름, 성 조회
SELECT first_name, last_name FROM users
WHERE first_name LIKE '%호%';

-- 이름이 '준'으로 끝나는 사람들의 이름 조회
SELECT first_name FROM users
WHERE first_name LIKE '%준';

-- 서울 지역 전화번호를 가진 사람들의 이름, 전화번호 조회
SELECT first_name, phone FROM users
WHERE phone LIKE '02-%';

-- 나이가 20대인 사람들의 이름, 나이 조회
SELECT first_name, age FROM users
WHERE age LIKE '2_';

-- 전화번호 중간 4자리가 51로 시작하는 사람들의 이름, 전화번호 조회
SELECT first_name, phone FROM users
WHERE phone LIKE '%-51__-%';
```
> '2%' : 2살도 포함 (X)

<br>

#### 🔸 IN 
▫ 값이 값 목록 결과에 있는 값과 일치하는지 확인  
▫ 부정 : NOT IN  

``` sql
-- 경기도 혹은 강원도에 사는 사람들의 이름, 지역 조회
SELECT first_name, country FROM users
WHERE country IN ('경기도', '강원도');

SELECT first_name, country FROM users
WHERE country = '경기도' OR country = '강원도';

-- 경기도 혹은 강원도에 살지 않는 사람들의 이름, 지역 조회
SELECT first_name, country FROM users
WHERE country NOT IN ('경기도', '강원도');
```

<br>

#### 🔸 BETWEEN  
▫ 값이 값 범위에 있는지 테스트  
▫ SELECT, DELETE, UPDATE 문의 WHERE 절에서 사용 가능  
▫ 부정 : NOT BETWEEN  

``` sql
-- 나이가 20살 이상, 30살 이하인 사람들의 이름, 나이 조회
SELECT first_name, age FROM users
WHERE age BETWEEN 20 AND 30;

SELECT first_name, age FROM users
WHERE age >= 20 AND age <= 30;

-- 나이가 20살 이상, 30살 이하가 아닌 사람들의 이름, 나이 조회
SELECT first_name, age FROM users
WHERE age NOT BETWEEN 20 AND 30;

SELECT first_name, age FROM users
WHERE age < 20 OR age > 30;
```


<br><br>

## 🚩 Grouping data 
▫ 특정 그룹으로 묶인 결과 생성  
▫ 선택된 컬럼 값을 기준으로 데이터들의 공통 값을 묶어서 결과로 나타냄  
▫ SELECT 문의 FROM 절 뒤에 작성 (WHERE 절이 포함된 경우, WHERE 절 뒤에 작성)  
▫ 각 그룹에 대해 집계함수 적용 가능  

<br>

### ▶ 집계함수 (Aggregate Function)
▫ 각 집합에 대한 계산을 수행하고 단일 값을 반환  
|  종류   |
| :-----: |
|  AVG()  |
| COUNT() |
|  MAX()  |
|  MIN()  |
|  SUM()  |
> 단, AVG(), MAX(), MIN(), SUM()은 숫자를 기준으로 계산하므로 반드시 INTEGER에만 사용 가능  

<br>

``` sql
-- 각 지역별로 그룹화
SELECT country FROM users
GROUP BY country;

-- 각 지역별로 몇 명씩 살고 있는지 조회
SELECT country, COUNT(*) FROM users
GROUP BY country;

-- users 테이블의 전체 행 수 조회
SELECT COUNT(*) FROM users;

-- 나이가 30살 이상인 사람들의 평균 나이 조회
SELECT AVG(age) FROM users 
WHERE age >= 30;

-- 각 성씨가 몇 명씩 있는지 조회
SELECT last_name, COUNT(*) FROM users
GROUP BY last_name;

-- 컬럼명 임시 변경하여 조회
SELECT last_name, COUNT(*) AS number_of_name
FROM users GROUP BY last_name;

-- 인원이 가장 많은 성씨 순으로 조회
SELECT last_name, COUNT(*) FROM users
GROUP BY last_name ORDER BY COUNT(*) DESC;
```



<br><br>
 
## 🚩 Changing data

<br>

### 📌 INSERT 
▫ 새 행을 테이블에 삽입  
▫ 문법 규칙 
- INSERT INTO 키워드 뒤에 데이터를 삽입할 테이블의 이름 지정 
- 테이블 이름 뒤에 쉼표로 구분된 컬럼 목록 추가 (권장사항)
- VALUES 키워드 뒤에 쉼표로 구분된 값 목록 추가  
  > 컬럼 목록을 생략하는 경우, 값 목록의 모든 컬럼에 대한 값을 지정해야 함

``` sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```


![image](https://user-images.githubusercontent.com/93974908/193803635-7e9b931b-2a26-42c3-8a4a-1a05685bd87f.png)


<br>

### 📌 UPDATE
▫ 테이블에 있는 기존 행의 데이터 업데이트  
▫ 문법 규칙
- UPDATE 절 이후에 업데이트할 테이블 지정  
- SET 절에서 테이블의 각 컬럼에 대해 새 값을 설정
- WHERE 절의 조건을 사용하여 업데이트할 행을 지정 (생략 시 모든 행의 데이터 업데이트)
- (선택) ORDER BY 및 LIMIT 절을 사용하여 업데이트할 행 수 지정 가능 

``` sql
UPDATE table_name
SET column_1 = new_value_1, 
    column_2 = new_value_2
WHERE
    search_condition;
```
![image](https://user-images.githubusercontent.com/93974908/193813490-79fb1a63-84e9-4b55-8c65-28fac9dba230.png)

<br>

### 📌 DELETE 
▫ 테이블에서 행 제거  
▫ 문법 규칙
- DELETE FROM 키워드 뒤에 행을 제거하려는 테이블의 이름 지정 
- WHERE 절에 검색 조건을 추가하여 제거할 행 식별 (생략 시 테이블의 모든 행 삭제)
- (선택) ORDER BY 및 LIMIT 절을 사용하여 삭제할 행 수 지정 가능

``` sql
DELETE FROM table_name
WHERE search_condition;
```
![image](https://user-images.githubusercontent.com/93974908/193813858-3f197e3f-e083-49b7-973e-9cfd4cc5e2fd.png)

![image](https://user-images.githubusercontent.com/93974908/193813960-bba41af0-5f2b-47b7-a9a9-5b3802699892.png)