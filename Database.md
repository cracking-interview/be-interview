# 🛢 Database

- 1. DBMS
    - **데이터베이스 관리 시스템** 으로 여러 사용자가 데이터베이스에 접근하여 사용할 수 있도록 해주는 소프트웨어
- 2. DB를 사용하는 이유
    - 파일 시스템의 **데이터 중복, 비일관성, 검색 등의 문제** 를 해결하기 위해서 사용
    - 파일 시스템이 OS마다 다를 수 있기 때문에 OS에 종속적인 파일 시스템을 이용하는 것은 프로그램의 확장성을 해침
    
- 3. 스키마
    - **데이터베이스의 구조와 제약 조건에 관한 전반적인 명세를 기술한 메타데이터 집합**
- 4. 뷰
    - 하나 이상의 테이블에서 유도된, **메모리에 물리적으로 존재하지 않는 가상 테이블**
    - 특정 사용자로부터 특정 속성을 숨기는 기능으로 뷰를 정의하여 그 뷰를 테이블처럼 사용
    - **인덱스를 가질 수 없고, 뷰의 정의를 변경할 수 없음**
    - 기본 키 포함하고 정의할 경우, 삽입, 삭제, 갱신 가능
- 5. 키
    
    <img width="646" alt="image" src="https://user-images.githubusercontent.com/84627144/180116518-092e890f-4430-4030-a432-4fb5d672498f.png">
    
    - 검색, 정렬 시 튜플을 구분하는 기준이 되는 속성
    - **유일성** : 키로 튜플을 유일하게 식별할 수 있음
    - **최소성** : 튜플을 구분하는데 꼭 필요한 속성들로만 구성
- 6. 후보키
    - 테이블을 구성하는 속성 중에서 **튜플을 유일하게 식별할 수 있는 속성들의 부분 집합**
        - 기본키로 사용할 수 있는 속성들
    - 모든 테이블은 하나 이상의 후보 키를 가짐 (기본키)
    - 유일성과 최소성 만족
- 7. 기본키
    - 후보 키 중에서 선택한 Primary Key
    - 특정 튜플을 유일하게 식별 가능
    - **중복 값과 NULL 불가**
    - 유일성과 최소성 만족
- 8. 대체키
    - 후보 키가 두개 이상일 때, 기본키를 제외한 나머지 후보키
- 9. 슈퍼키
    - 고유하게 식별하는 모든 후보키의 조합하는 키
    - 유일성은 만족하지만, 최소성은 만족하지 않음
- 10. 외래키
    - **다른 릴레이션(테이블)의 속성, 참조 관계를 표현하는데 사용하는 키**
    - 테이블의 열 중 다른 테이블의 기본키를 참조하는 열
    - 테이블 간의 연결, 중복 방지, 무결성 유지
- 11. 트랜잭션
    - **데이터베이스의 상태를 변화시키는 하나의 논리적인 작업 단위**
    - 논리적인 작업의 쿼리 캐수와 관계 없이 논리적인 작업 셋 자체가 100% 적용되거나 아무것도 적용되지 않아야 함을 보장
- 12. 트랜잭션 특징 ACID
    - Atomicity (원자성)
        - 트랜잭션을 구성하는 연산 전체가 모두 정상적으로 실행되거나 모두 취소되어야 한다.
    - Consistency (일관성)
        - 트랜잭션이 실행을 성공적으로 완료하면 언제나 일관성 있는 데이터베이스 상태로 유지한다.
    - Isolation (고립성)
        - 두 개 이상의 트랜잭션이 동시에 발생할 때, 서로의 연산에 영향을 주면 안된다.
    - Durability (영구성)
        - 커밋된 트랜잭션의 내용은 영구히 반영된다.
- 13. 트랜잭션의 상태
    - 활동(Active)
        - 트랜잭션이 실행 중인 상태
    - 장애(Fail)
        - 트랜잭션이 실행에 오류가 발생하여 중단한 상태
    - 철회(Aborted)
        - 트랜잭션이 비정상적으로 종료되어 Rollback 수행하는 상태
    - 부분 완료(Partially Commit)
        - 트랜잭션이 마지막 연산까지 실행했지만, Commit 연산이 실행되기 직전 상태
    - 완료(Commmitted)
        - 트랜잭션이 성공적으로 종료되어 commit 연산을 실행한 후의 상태
- 14. 트랜잭션 격리수준
    - **Read Uncommitted**
        - 다른 트랜잭션에서 커밋되지 않은 내용에 접근 가능 **(Dirty Read)**
        - 락 발생 X
    - **Read Committed**
        - 커밋된 내용만 접근 가능
        - 한 트랜잭션 내에서 검색 결과가 비일관적인 현상 발생 **(Nonrepeatable read)**
        - 락 발생 X
    - **Repeatable Read**
        - 커밋이 완료된 데이터만 읽을 수 있으며, 트랜잭션 범위 내에서 조회한 내용이 항상 동일함을 보장
        - **일정범위의 레코드를 두번 이상 읽을 때, 첫 번재 쿼리에서 없던 유령 레코드가 두번째 쿼리에서 나타나는 현상을 Phantom read라고 한다.**
        - 락 발생
    - **Serializable**
        - 한 트랜잭션에서 사용하는 데이터는 다른 트랜잭션이 접근 불가능
        - 락 발생
- 15. Commit
    - 트랜잭션이 성공하여 트랜잭션 결과를 영구적으로 반영하는 연산
- 16. Rollback
    - 트랜잭션의 실행을 취소하였음을 알리는 연산
    - 트랜잭션이 수행한 결과를 원래의 상태로 원상 복귀시키는 연산
- 17. 동시성 제어
    - 동시에 여러개의 트랜잭션이 수행될 때, 트랜잭션들이 DB의 일관성을 파괴하지 않도록 트랜잭션 간의 상호작용을 제어하는 것을 의미한다.
- 18. Locking
    - 트랜잭션이 데이터에 접근하기 전에 Lock을 요청해서 Lock이 허락되면 해당 데이터에 접근할 수 있도록 하는 기법
    - 종류
        - 비관적 락(Pessimistic lock)
            - 공유락(Shared Lock) : 사용중인 데이터를 다른 트랜잭션이 읽기 허용, 쓰기 비허용
            - 배타락(Exclusive Lock) : 사용중인 데이터를 다른 트랜잭션이 읽기, 쓰기 비허용
            - **데이터 수정 즉시 트랜잭션 충돌을 감지할 수 있다.**
            - 롤백을 개발자가 일일이 하는 것이 힘든 경우, 충돌이 일어났을 때 롤백 비용이 많이 드는 경우, 주문 시에 쿠폰 사용, 알림 제공, 주문서 작성 등의 여러 기능이 한 트랜잭션에 묶여 있는 경우에 적합하다.
        - 낙관적 락(Optimistic lock)
            - 데이터 갱신 시 충돌이 발생하지 않을 것으로 가정하여 락을 걸지 않는 방식 → **락이 아닌 버전 관리 기능을 통해서 트랜잭션 격리성 관리**
            - Version 컬럼을 별도로 추가해서 충돌 방지 → Version 정보를 사용하면 최초 커밋만 인정된다.
                - 벌크 연산은 버전을 무시하기 때문에 벌크 연산에서는 버전을 증가시키려면 버전 필드를 강제로 증가시켜야 한다.
            - DB 가 제공하는 락 기능을 사용하지 않고 **JPA가 제공하는 버전 관리 기능을 사용** → 애플리케이션에서 제공하는 락
            - **커밋 전까지는 충돌을 알 수 없다.**
            - **충돌이 나면 롤백 처리는 개발자의 몫이다.**
        - 둘의 사용을 판단하는 기준을 읽기와 수정 비율이 어디에 가까운지 보고 판단해야 한다. 수정의 비율이 높다면 Pessimistic을 사용하고 읽기의 비중이 높다면 Optimistic을 사용한다.
- 19. 갱신 분실문제
    - A와 B가 동시에 제목이 같은 공지사항을 동시에 수정한다고 했을 때 A가 먼저 수정을 완료하고 B가 이후에 완료버튼을 눌렀다면 B의 수정사항만 남게되는데 이것을 갱신 분실 문제라고 한다.
    - 갱신 분실 문제는 데이터베이스 트랜잭션의 범위를 넘어서는 문제로 트랜잭션으로만 해결할 수는 없고 3가지 선택 방법이 있다.
        - 마지막 커밋만 인정하기(기본값)
            - B의 커밋만 인정한다.
        - 최초 커밋만 인정하기
            - A의 수정을 인정하고 B의 수정이 완료될 때 오류가 발생한다.
        - 충돌하는 갱신 내용 병합하기
            - 사용자 A와 사용자 B의 수정사항을 병합한다.
- 20. MVCC(격리 수준 제어) 대신 락을 사용하는 이유
    - **낙관적 락이나 비관적 락은 다른 트랜잭션이 수정하는 것 자체를 막아버린다.**
    - 반면에 MVCC는 다른 트랜잭션이 수정하는 것 자체는 막지 못하고, 트랜잭션 격리 레벨에 따라 **일관된 읽기** 를 제공한다.
    - 따라서 두 개의 트랜잭션이 동시에 수정할 때 처음의 수정사항만 반영하도록 하여 **갱신 분실 문제를 예방** 하기 위해서는 락을 사용한다.
    - MVCC가 일관된 읽기를 사용할 수 있는 이유는 변경되기 이전의 내용을 보관하고 있는 **언두 로그** 에서 데이터를 가져오기 때문이다.
- 21. 트리거와 프로시저의 차이
    - 트리거 : **DML이 수행되었을 때, 자동으로 실행되게 정의한 프로시저**
    - 프로시저 : 쿼리문을 마치 하나의 메서드 형식으로 만들고 어떠한 동작을 일괄적으로 처리하는 용도
    
    | 프로시저 | 트리거 |
    | --- | --- |
    | CREATE PROCEDURE 문법 사용 | CREATE TRIGGER 문법 사용 |
    | 생성하면 소스코드와 실행코드가 생성됨 | 생성하면 소스코드와 실행코드가 생성됨 |
    | EXECUTE 명령어로 실행 | 생성 후 자동실행 |
    | COMMIT, ROLLBACK 실행 가능 | COMMIT, ROLLBACK 실행 불가 |
- 22. 낙관적 락보다 DB 트랜잭션 레벨을 Repeatable Read로 하면 되지 않을까?
    - **Repeatable read는 선행 트랜잭션이 종료시까지 다른 트랜잭션이 update, delete하지 못하도록 완전히 락을 걸어버린다.**
    - 반면에 낙관적인 락은 애플리케이션 단에서 락을 걸지 않아 트랜잭션 자체를 blocking하지 않으면서도 다른 트랜잭션이 수정하는 것을 막아준다.
    - 락을 거는 것 자체가 성능에 영향을 줄 수 있기 때문에 읽기 작업의 비율이 높은 경우 격리 레벨을 조정하는 것보다 낙관적인 락을 사용하는게 더 좋다.
- 23. 무결성 제약조건
    - 데이터베이스의 정확성, 일관성을 보장하기 위해 저장, 삭제, 수정 등을 제약하기 위한 조건
    - **개체 무결성** : 기본 키는 null과 중복값 불가능
    - **참조 무결성** : 외래 키는 null이거나 참조 테이블의 기본 키 값과 동일해야 함
- 24. 조인
    - **두 개 이상의 테이블이나 데이터베이스를 연결하여 데이터를 검색하는 방법**
    - 적어도 하나의 컬럼을 서로 공유하고 있어야 한다.
    
    ### **종류**
    
    - INNER JOIN
        - 기준 테이블과 join한 테이블의 **중복된 값** 을 보여준다.
        - **교집합** 과 같다고 보면 된다.
    - LEFT OUTER JOIN
        - 기준 테이블의 값 + join 테이블과 기준테이블의 중복된 값
        - 기준 테이블과 중복되는 값이 없다면 join 테이블의 내용은 NULL로 표기된다.
    - RIGHT OUTER JOIN
        - LEFT OUTER JOIN의 반대이다.
    - FULL OUTER JOIN
        - 기준, Join 테이블의 합집합
        - 전부 다 보여주고 빈값들은 NULL로 채워진다.
    - CROSS JOIN
        - 크로스 곱이라고도 하는데 모든 경우의 수를 전부 표현해주는 방식이다.
        - 각 테이블의 데이터 개수가 N,M 이라면 결과는 N*M의 데이터 개수가 나온다.
    - SELF JOIN
        - CROSS JOIN의 대상이 자기 자신인 것
- 25. DML, DDL, DCL
    - DML : 데이터 조작
        - Select, Insert, Update, Delete
    - DDL : 데이터(구조, 객체) 정의
        - Create, Drop(테이블 삭제), Truncate(테이블 데이터 삭제, 테이블 초기화), Alter
    - DCL : 권한 제어
        - Grant, Revoke
- 26. 힌트
    
    **옵티마이저가 항상 최적의 실행 경로 실행을 보장하지 않기 때문에 직접 최적의 실행 경로를 작성해주는 것**
    
- 27. 인덱스
    - 추가적인 쓰기와 저장 공간사용을 통해 **데이터베이스의 검색 속도 향상시키기 위한 방법**
    - 칼럼의 값(key)와 해당 레코드가 저장된 주소를 **키와 값의 쌍으로 인덱스 정의**
    - 일반적으로 B+ 트리 자료구조를 사용
    - 장단점
        - 검색 속도 향상
        - 데이터의 추가, 삭제, 수정의 경우 인덱스도 변경하고 정렬해야 하므로 성능 저하
        - 추가적인 저장 공간 필요
    - 알고리즘
        - B 트리 알고리즘 : 컬럼의 값을 변형하지 않고 원래의 값으로 인덱싱, 등호 뿐만 아니라 부등호 연산에도 적용 가능
        - Hash 알고리즘 : 해시값을 이용한 인덱싱
- 28. Cluster 인덱스
    - **인덱스로 지정한 컬럼을 기준으로 물리적으로 정렬하는 인덱스**
    - 한 테이블당 1개 (Primary Key)
    - 위에서 언급한 일반적인 인덱스로 검색속도는 빠르지만, 입력, 수정, 삭제는 느림
- 29. Non-Cluster 인덱스
    - **데이터 자체는 정렬되지 않고, 인덱스값을 기준으로 정렬하여 새로 인덱스 페이지를 만드는 인덱스**
    - 새로 인덱스 페이지를 만들고 리프 페이지에 실제 데이터가 위치한 주소를 가리킴
    - 한 테이블 당 여러 개 가능
    - 검색 속도는 Cluster에 비해 느리지만, 입력,수정,삭제가 빠름
- 30. 멀티 인덱스
    - **두개 이상의 필드를 조합하여 생성한 인덱스**
    - 그냥 두개 인덱스로 조회하면 되지 않을까?
        - mysql은 단일 쿼리를 실행할 때 **하나의 테이블 당 하나의 인덱스만 사용** 할 수 있다.
        - 둘 중 인덱싱 데이터 내 행이 적은 것을 먼저 참조하게 된다.
- 31. scan
    - Table Full Scan
        - 테이블에 속한 블록 전체를 읽어서 사용자가 원하는 데이터를 찾는다.
    - Index Range Scan
        - 인덱스 컬럼이 가공되지 않은 상태로 조건절에 있을 때 수행된다.
        - 인덱스에서 일정량을 스캔하면서 얻은 ROWID를 사용해 테이블 레코드를 찾는다.
    - Index Full Scan
        - 인덱스 컬럼이 조건에 없으면 Index Range Scan이 불가능하므로, 옵티마이저는 Table Full Scan을 고려한다.
        - 그런데 대용량 테이블이라 Table Full Scan에 대한 부담이 너무 크면 Index를 활용해야할 필요가 있다.
        - 인덱스의 전체 크기는 테이블의 전체 크기보다 훨씬 적으므로, Index Range Scan을 할 수 없을 때, Table Full Scan보다는 Index Full Scan을 고려한다.
- 32. B 트리
    
    <img width="647" alt="image" src="https://user-images.githubusercontent.com/84627144/180360054-cb0b347e-bbcf-4cca-95b8-fa8862644688.png">
    
    - 이진 트리를 확장해서 많은 자식을 갖을 수 있는 **균형 트리**
    - **key들이 항상 오름차순으로 정렬되어 구성**
    - Branch와 Leaf 노드가 key와 data를 저장
- 33. B+ 트리
    
    <img width="688" alt="image" src="https://user-images.githubusercontent.com/84627144/180360075-3b059e22-3799-4a80-ae94-2c1f24ad71af.png">
    
    - B트리를 확장해서 데이터의 빠른 접근을 위한 인덱스 역할만 하는 비단말 노드를 추가한 트리(리프들이 연결되어 있음)
    - **Branch 노드는 key만 저장**
    - **key들이 항상 오름차순으로 정렬되어 구성**
        - 하나의 노드에 더 많은 key를 담을 수 있게 되므로 트리의 높이가 B 트리에 비해 더 낮아진다.(cache hit를 높임)
    - Leaf 노드는 Key와 Data를 저장하고 Linked List로 연결되어 있음 (검색에 유용)
        - 풀 스캔 시 B트리는 모든 노드를 확인해야하지만, B+ 트리의 경우 리프노드에 연결된 연결리스트로 선형 탐색이 가능하다.
- 34. 해시 테이블
    - 칼럼 값으로 생성된 해시를 기반으로 인덱스 구현
    - O(1)로 매우 빠름
    - 해시 테이블은 **동등 연산에 특화된 자료구조** 이기 때문에 **select 조건에서 부등호 연산 사용시 성능 저하**
    - **동등 비교에서는 효과적**
    - 해시는 데이터를 고정된 데이터의 크기로 변환시키는 것을 말함.
- 35. 해시 인덱스 vs B 트리 인덱스
    - 동등 비교에서는 해시 인덱스가 효과적
    - 범위 검색에서는 b 트리 인덱스가 정렬되어 있어서 효과적
    