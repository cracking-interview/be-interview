# ☕️ Java

- 1. Python vs Java vs Kotlin
    - Python
        - 통상적 인터프리터 언어이지만 내부에 JIT이라는 컴파일러가 내장되어 있음. 하지만 파이썬을 이것으로 구분하는 것은 잘못된 접근일 수 있음.
        - 데이터 타입이 동적으로 입력됨에 따라 변수형의 자료형을 따로 선언하지 않아도 됨.
    - Java
        - JVM으로 실행돼서 OS에 관계없이 동작한다.
        - 정적 데이터 타입 명시가 필요하다.
        - 100% 객체 지향언어로, 캡슐화, 상속, 다형성을 지원한다.
    - Kotlin
        - 자바보다 null 안전성(safety)이 좋다.
        - data class를 이용해 자바의 보일러 플레이트 코드를 줄일 수 있다.
- 2. 자바의 장단점
    - 장점
        - 운영체제에 독립적(JVM)
        - 동적 로딩을 지원
            - 애플리케이션이 실행될 때 모든 객체가 생성되지 않고, 각 객체가 필요한 시점에 클래스를 동적 로딩해서 생성된다.
    - 단점
        - JVM에 의해 기계어로 번역되고 실행되는 과정을 거치기 때문에 조금 느리다.
- 3. OOP(객체지향)의 특징
    1. 캡슐화
        - 정보 은닉 : 필요 없는 정보는 외부에서 접근하지 못하도록 제한
        - 높은 응집도, 낮은 결합도로 유연함과 유지보수성 증가
    2. 추상화
        - 공통적인 특징을 파악해 하나의 집합으로 다루는 것
    3. 상속
        - 기존 상위 클래스에 근거해 새로운 클래스와 행위를 정의
    4. 다형성
        - 오버로딩(overloading) : 메소드의 이름은 같지만, 파라미터의 타입 또는 개수를 다르게 하는 것.
        - 오버라이딩(overriding) : **재정의!** 하위 클래스에서 상위 클래스의 메소드를 재정의 하여 사용하는 것. 이를 이용하면 코드의 재사용성이 높아짐.
- 4. OOP SOLID 원칙
    - S : 단일 책임 원칙(Single Responsible Principle)
        - 객체는 단 하나의 책임만을 가져야한다.
        - 어떤 변화에 의해 클래스를 변경해야 하는 이유는 오직 하나뿐이어야 한다.
    - O : 개방 폐쇄 원칙(Open Closed Principle)
        - 기존 코드를 변경하지 않으면서 기능을 추가할 수 있도록 설계되어야 한다.
    - L : 리스코프 치환 원칙
        - 자식 클래스는 최소한 자신의 부모 클래스에서 가능한 행위는 수행할 수 있어야한다.
    - I : 인터페이스 분리 원칙
        - 특정 클라이언트를 위한 인터페이스 여러 개가 범용 인터페이스 하나보다 낫다.
        - 인터페이스가 명확해지고, 대체 가능성이 높아진다.
    - D : 의존관계 역전 원칙 (Dependency Inversion Principle)
        - 의존 관계를 맺을 때 변화하기 쉬운 것 또는 자주 변화하는 것보다는 변화하기 어려운 것, 거의 변화가 없는 것에 의존하라는 것이다.
        - 쉽게 이야기하면, 구현 클래스에 의존하지 말고, 인터페이스에 의존하라는 뜻
- 5. 객체 지향 프로그래밍 vs 절차 지향 프로그래밍
    - 절차 지향 프로그래밍
        - 실행하고자 하는 절차를 정하고, 순차적으로 프로그래밍 하는 방식으로 빠르다.
        - 엄격하게 순서가 정해져 있기에 비효율적이고 유지보수가 어렵다.
        - 목적을 달성하기 위한 일의 흐름에 중점을 둔다.
    - 객체 지향 프로그래밍
        - 구현해야할 객체들 사이의 상호작용을 프로그래밍하는 방식으로 상속, 다형성, 추상화, 캡슐화를 통해 결합도를 낮추고 응집도를 높일 수 있으며 코드의 재사용성도 높일 수 있다.
- 6. JVM의 구성 요소
    - 자바 프로그램을 실행하는 역할
        - 컴파일러를 통해 바이트 코드로 변환된 파일을 JVM에 로딩하여 실행
    - Class Loader : JVM 내(Runtime Data Area)로 Class 파일을 로드하고 링크
    - Execution Engine : 메모리(Runtime Data Area)에 적재된 클래스들을 기계어로 변경해 실행
    - Garbage Collector : 힙 메모리에서 참조되지 않는 개체들 제거
    - Runtime Data Area : 자바 프로그램을 실행할 때, 데이터를 저장
- 7. JVM 실행과정
    1. JVM은 OS로부터 메모리(Runtime Data Area)를 할당 받음
    2. 컴파일러(javac)가 소스코드(.java)를 읽어 바이트 코드(.class)로 변환
    3. Class Loader를 통해 Class파일을 JVM내 Runtime Data Area로 로딩
    4. 로딩된 Class 파일을 Execution Engine을 통해 해석 및 실행
- 8. JVM 메모리(Runtime Data Area) 구조
    
    <img width="660" alt="image" src="https://user-images.githubusercontent.com/84627144/177464955-0f059f83-1268-4954-9500-b1905d730036.png">
    
    - 메서드(static) 영역
        - 클래스가 사용되면 해당 클래스의 파일(.class)을 읽어들여, 클래스에 대한 정보(바이트 코드)를 메서드 영역에 저장
        - 클래스와 인터페이스, 메서드, 필드, static 변수, final 변수 등이 저장되는 영역입니다.
    - JVM 스택 영역
        - 스레드마다 존재하여 스레드가 시작할 때마다 할당
        - 지역변수, 매개변수, 연산 중 발생하는 임시 데이터 저장
        - 메서드 호출 시마다 개별적 스택 생성
    - JVM 힙 영역
        - 런타임 시 동적으로 할당하여 사용하는 영역
        - new 연산자로 생성된 객체와 배열 저장
        - 참조가 없는 객체는 GC(가비지 컬렉터)의 대상
    - pc register
        - 쓰레드가 현재 실행할 스택 프레임의 주소를 저장
    - Native Method Stack
        - C/C++ 등의 Low level 코드를 실행하는 스택
- 9. 가비지 컬렉터
    - 사용하지 않는 메모리(unreferenced memory)를 지워 메모리를 확보하는 것
        - 대상: Heap 영역의 더 이상 사용되지 않는 Object
        - 메모리 확보 및 효율성 증대
        - 메모리 단편화 방지
        - GC 로 인해 프로그램 성능 저하 우려(Stop-the-world)
    
- 10. 접근 제한자
    - public : 접근에 제한이 없음
    - private : 자기 자신 클래스 내에서만 접근 가능
    - default(package) : 동일한 패키지 내에서만 접근 가능
    - protected : 동일한 패키지 내에서만 접근 가능 + 상속을 이용한 접근 가능
- 11. String vs Char
    - Char 1개의 문자, String은 문자열
    - Char - primitive(== 비교 가능), String - Reference type(equals 사용)
    
- 12. ==과 equals
    - ==
        - 참조 비교로 두 객체가 같은 메모리 공간을 가리키는지 확인 (주소 비교)
    - equals
        - 두 객체의 **내부 값**이 같은지 내용을 비교한다.
        - 기본 타입(Primitive Type)에 대해서는 적용할 수 없다.
        - 객체 비교시 override해서 원하는 방식으로 수정할 수 있다.
- 13. 데이터 타입
    - Value Type
        - **기본 Primitive 타입으로 int, char 등이 있다.**
        - 기본 타입의 크기가 작고 고정적이기 때문에 **메모리 Stack 영역** 에 저장된다.
    - 참조 타입(Reference Type)
        - String과 박싱 타입인 Integer 등이 있다.
        - new 키워드를 이용해 객체를 생성하여 데이터가 생성된 **주소를 참조하는 타입**
        - String과 배열은 일반적인 참조 타입과 달리 new 없이 생성 가능하지만 참조타입이다.
        - 참조 타입은 데이터의 크기가 가변적이고, 동적이므로 **Heap 영역** 에서 관리된다.
        - **데이터는 Heap 영역에서 관리되지만 메모리의 주소값은 Stack 영역에 담긴다.**
    - 더이상 참조하는 변수가 없을 때 GC에 의해 삭제된다.
    
- 14. Call By Value와 Call By Reference
    - Call By Value(값에 의한 호출)
        - 함수 호출 시 인자로 전달되는 **변수의 값을 복사하여 함수의 인자로 전달** 한다.
        - 따라서, **함수 안에서 인자의 값이 변경되어도, 외부의 변수의 값은 변경되지 않는다.**
    - Call by Reference(참조에 의한 호출)
        - **함수 호출 시 인자로 전달되는 변수의 레퍼런스를 전달한다.**
        - 따라서 **함수 안에서 인자의 값이 변경되면, 인자로 전달된 변수의 값도 함께 변경된다.**
    - 자바는 새롭게 지역 변수(다른 주소)를 만들어서 값만 복사하고 할당한다. 따라서 자바는 Call By Value에 해당한다.
- 15. hashcode
    
    **두 객체가 동일한 객체인지 비교할 때 사용하고 heap 영역에 저장된 객체의 메모리 주소를 반환한다.**
- 16. Wrapper class
    - 래퍼 클래스는 기본 타입에 해당하는 데이터를 인수로 받아, 해당 값을 가지는 객체로 만들어준다.
    - 산술 연산을 위해 정의된 클래스가 아니므로, **인스턴스에 저장된 값을 변경할 수 없다.(불변성)**
- 17. boxing / unboxing
    - 기본 자료형의 경우 wrapper 클래스 객체로 만들기 위해 박싱을 하는 것이고,
    - wrapper 클래스 객체는 기본 자료형으로 만들기 위해 감싸진 것을 언박싱 하는 것이다.
    - 코드 예시 - valueOf
        
        ```java
        int primaryInt = 20;
        // 공간 및 시간 성능을 위해 1보다는 2를 선호!
        Integer wrapperInt1 = new Integer(12); // 1
        Integer wrapperInt2 = Integer.valueOf(20); // 2 
        primaryInt = wrapperInt.intValue();
        ```
        
    - auto-boxing, auto-unboxing
        
        ```java
        // JDK1.5 부터는 위와 같이 자바 컴파일러가 알아서 언방식, 박싱 작업을 해준다.
        // auto-boxing, auto-unboxing
        
        public class Wrapper03 {
            public static void main(String[] args) {
              Integer num1 = new Integer(10);
              Integer num2 = new Integer(20);
              Integer num3 = new Integer(10);
        
              System.out.println(num1 < num2);       // true
              System.out.println(num1 == num3);      // false
              System.out.println(num1.equals(num3)); // true
            }
        }
        ```
        
        ```java
        Integer wrapperInt = new Integer(21);
        int primaryInt = wrapperInt; // wrapperInt가 자동 언박싱 되는 모습
        wrapperInt+primaryInt;// 이것의 결과 값은 기본 자료형이다.
        ```
        
    - 래퍼 클래스는 객체 이므로 주소값 비교가 아니라 내부 값을 비교하는 equals를 써야한다.
    
- 18. non-static / static
    - non-static
        - 공간적 특성
            - **객체마다 별도로 존재**하고 인스턴스 변수라고 부른다.
        - 시간적 특성
            - 객체와 생명주기가 동일하다.
    - static
        - 공간적 특성
            - **클래스당 하나만 생성된다.**
            - **동일한 클래스의 모든 객체들에 의해 공유된다.**
        - 시간적 특성
            - 객체가 생기기 전에 이미 생성되어 객체를 생성하지 않아도 사용 가능하다.
            - 객체가 사라져도 사라지지 않고, 프로그램 종료 시에 사라진다.
- 19. main이 static인 이유
    - static 멤버는 프로그램 시작 시(클래스 로딩) 메모리에 로드되어 인스턴스를 생성하지 않아도 호출이 가능하기 때문이다.
- 20. final vs finally vs finalize
    - final 키워드
        - 변수, 메서드 클래스가 **변경 불가능** 하도록 만든다.
        - 기본 타입 변수에 적용 시 - 해당 변수의 값 변경 불가능하다.
        - 참조 변수에 적용 시 - 참조 변수가 힙 내의 다른 객체를 가리키도록 변경할 수 없다.
        - 메서드에 적용 시 - 해당 메서드를 오버라이드할 수 없다.(오버로딩은 가능)
        - 클래스에 적용 시 - 해당 클래스를 상속 받아서 사용할 수 없다.
    - finally 키워드
        - try catch 블록 뒤에서 **항상 실행될** 코드 블록을 정의하기 위해 사용한다.
    - finalize 메서드
        - 가비지 컬렉터가 더 이상의 참조가 존재하지 않는 객체를 메모리에서 삭제하겠다고 결정하는 순간 호출된다.
        - 더 이상 **사용**하지 않는 자원에 대한 정리 작업을 진행하기 위해 호출되는 종료자 메서드
- 21. try with resources
    - 자바 7 이전에는 try-catch-finally에서는 리소스의 생성을 try 구문에서 리소스의 반납은 finally 구문에서 해옴 → 실수할 가능성
    - 자바 7 에 나온 try with resources 는 try 옆 괄호 안에서 리소스를 생성해주면 따로 반납하지 않아도 리소스를 자동 반납해준다.
    - 아래와 같이 작성한 것이 try with resources 구문이고, 만약 try-catch-finally를 사용했다면 finally 구문에서 scanner을 close하는 내용이 있어야 한다.
    
    ```java
    public class ResourceClose {
        public static void main(String[] args) {
            try (**Scanner scanner = new Scanner(new File("input.txt"))**) {
                System.out.println(scanner.nextLine());
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }
    }
    ```
    
- 22. Generic
    - 데이터 형식에 의존하지 않고, 하나의 값이 여러 다른 데이터 타입들을 가질 수 있도록 하는 방법
    - 클래스나 메서드에서 사용할 내부 데이터 타입을 외부에서 지정하는 기법
    - 잘못된 타입이 들어올 수 있는 것을 컴파일 단계에서 방지할 수 있다.
    - 불필요한 타입 변환을 제거할 수 있다.
    
    ```java
    ArrayList<Integer> list1 = new ArrayList<Integer>();
    ArrayList<String> list2 = new ArrayList<Integer>();
    ```
    
    - 코드 예시
        
        ```java
        // 제네릭 클래스
        class ClassName<E> {
        	
        	private E element;	// 제네릭 타입 변수
        	
        	void set(E element) {	// 제네릭 파라미터 메소드
        		this.element = element;
        	}
        	
        	E get() {	// 제네릭 타입 반환 메소드
        		return element;
        	}
        	
        }
         
        class Main {
        	public static void main(String[] args) {
        		
        		ClassName<String> a = new ClassName<String>();
        		ClassName<Integer> b = new ClassName<Integer>();
        		
        		a.set("10");
        		b.set(10);
        	
        		System.out.println("a data : " + a.get());
        		// 반환된 변수의 타입 출력 
        		System.out.println("a E Type : " + a.get().getClass().getName());
        		
        		System.out.println();
        		System.out.println("b data : " + b.get());
        		// 반환된 변수의 타입 출력 
        		System.out.println("b E Type : " + b.get().getClass().getName());
        		
        	}
        }
        ```
        
- 23. 직렬화, 역직렬화
    - 직렬화(sirialization)는 자바 시스템 내부에서 사용되는 객체 또는 데이터(메모리)를 디스크에 저장하거나 네트워크 통신에 사용하기 위한 형식(바이트코드)으로 변환하는 것을 말한다.
        - 조건
            - 자바 기본 타입
            - Serializable 인터페이스 상속받은 객체
        - ObjectOutputStream 객체를 이용
    - 역직렬화(desrialization)는 그 반대로 디스크에 저장한 데이터를 읽거나, 네트워크 통신으로 받은 데이터를 메모리에 쓸 수 있도록 다시 변환하는 것이다.
        - ObjectInputStream 객체를 이용
    - **데이터 중에서 디스크에 저장하거나 통신에는 값 형식 데이터(Value Type)만 가능하다.**
    - 참조 형식 데이터(Reference Type)는 실제 데이터 값이 아닌 힙에 할당되어있는 메모리 번지 주소를 가지고 있기 때문에 저장, 통신에 사용할 수 없기때문에 직렬화 과정을 거쳐야 한다.
- 24. 오버로딩, 오버라이딩
    - 오버로딩 - 두 메서드가 같은 이름을 갖고 있으나 인자의 수나 자료형이 다른 경우
    - 오버라이딩 - 하위 클래스에서 상위 클래스의 메서드와 일치하는 함수를 재정의하는 것
- 25. 추상 클래스와 인터페이스 차이
    - 추상 메서드
        - abstract 키워드와 함께 선언부는 있는데 구현부가 없는 메소드
    - 추상 클래스
        - 개념 : abstract 키워드로 선언된 클래스
            - 추상 메서드가 최소 한 개 이상을 가진 abstract 클래스
            - 추상 메서드 이외의 다른 것들도(변수나 메서드) 추가 가능
        - 목적
            - **관련성이 높은 클래스 간의 코드를 공유하고 확장하고 싶은 목적**
    - 인터페이스
        - 개념 : default와 static 을 제외하고는 추상 메서드와 상수만을 포함하여, interface 키워드를 사용하여 선언
            - 모든 메서드는 추상 메서드로, abstract public이 생략되어 있다.
            - 인터페이스는 추상 메서드와 상수만 선언이 가능하다.
            (자바 8부터는 default 메서드 선언 가능)
            - 상수 필드는 public static final이 생략되어 있다.
            - 다중상속이 가능하다.
        - 목적
            - **관련성이 없는 클래스들의 논리적으로 같은 기능을 자신에 맞게 구현을 강제하는데 목적**
- 26. Error, Exception
    
    <img width="652" alt="image" src="https://user-images.githubusercontent.com/84627144/177681126-094c7d8f-c2c2-4b4b-a511-978969aefb21.png">

    | 목록 | Error | Exception |
    | --- | --- | --- |
    | 발생 시점 | 런타임에서 발생, 컴파일 시점에서 알 수 없다. | Checked Exception은 컴파일 시점에, Unchcked Exception은 런타임 시점에 알 수 있다.  |
    | 복구 | 에러는 복구 불가능 | try catch 블락을 이용하여 복구 가능 |
    | 타입 | 모든 Error는 Unchecked Type | checked Type, Unchecked Type으로 분류 |
    | 예시 | OutOfMemory, StackOverFlow | 아래서 설명 |
- 27. Checked Exception, Unchecked Exception
    
    
    | 구분 | Checked Exception | Unchecked Exception |
    | --- | --- | --- |
    | 상속 | RuntimeException 상속 X | RuntimeException 상속 |
    | 확인 시점 | 컴파일 시점 | 런타임 시점 |
    | 처리 여부 | 반드시 예외처리 | 명시적으로 하지 않아도 됨 |
    | 종류 | IOException,SQLException.. | NullPointException,ArrayIndexOutOfBounds... |
    - **대부분 Checked Exception보다는 Unchecked Exception 사용을 권장한다.**
    - Checked Exception의 경우 사용하는 모든 곳에 throws를 남겨야하는데 이 문제는 **의존성 문제를** 야기한다.
    - 예를 들어 가장 하위에서 SQLException(Checked Exception)를 던진다고 해보자.
        
        그럼 상위 서비스, 컨트롤러도 SQLException을 처리하기 위해서 throws SQLException을 붙이게 된다.
        
        SQLException은 JDBC 기술이므로 service, controller는 JDBC에 의존하게 된다.
        
        결국 JDBC 기술을 다른 기술로 교체하게 되면 연결된 모든 것들을 전부 교체해야하는 문제가 생긴다.
        
- 28. Collection
    
    **Set과 List는 Collection 인터페이스를 구현하고 있고 Map은 인터페이스를 구현하고 있지 않다.**
    
    <img width="663" alt="image" src="https://user-images.githubusercontent.com/84627144/177681260-2e998328-77e4-4f5e-8ee9-f6350d1a7e7d.png">
    
    - Map
        - Key와 Value의 형태로 이루어진 데이터 집합
        - 순서를 보장하지 않는다.
        - Key는 중복이 허용되지 않고, Value는 중복을 허용한다.
    - Collection을 상속한 것들
        - List
            - 순서가 있는 데이터 집합
            - 데이터를 중복해서 포함시킬 수 있다.
        - Set
            - 데이터의 중복을 허용하지 않는 데이터 집합
            - 순서를 보장하지 않는다.
            - Value의 중복을 허용하지 않는다.
- 29. Map
    - HashMap
        - 내부 hash값에 따라 키순서가 정해지므로 특정 규칙없이 출력된다.
        - key와 value에 **null값을 허용** 한다.
        - 비동기 처리
    - LinkedHashMap
        - 입력 순서대로 출력된다.
        - 비동기 처리
    - TreeMap
        - 내부적으로 **레드-블랙 트리(균형 이진 탐색 트리)** 로 저장된다.
        - **Null값 비허용**
        - 키값이 기본적으로 **오름차순 정렬** 되어 출력된다.
        - Compartor 구현으로 정렬 방법을 지정할 수 있다.
    - ConCurrentHashMap
        - key,value에 null값 비허용
        - **쓰기작업에서만 동기 처리**
    - HashTable
        - key,value에 null값 비허용
        - **모든 작업에 동기 처리**
- 30. Set
    - HashSet
        - 저장 순서를 유지하지 않는 데이터의 집합
        - Null 저장 가능
        - 해시 알고리즘을 사용하여 검색속도가 매우 빠르다.
        - 내부적으로 HashMap 인스턴스를 이용하여 요소를 저장한다.
    - LinkedHashSet
        - 저장 순서를 유지하는 HashSet
    - TreeSet
        - 데이터가 정렬된 상태로 저장되는 이진 탐색 트리의 형태로 요소를 저장한다.
        - **Null 저장 불가능**
        - **레드 블랙 트리(균형 이진 탐색 트리)** 로 구현되어 있다.
        - Compartor 구현으로 정렬 방법을 지정할 수 있다.
- 31. List
    - ArrayList
        - 내부적으로 배열을 사용하는 자료구조로 메모리가 연속적으로 배치된다.
        - 배열과 달리 메모리 할당이 동적이다.
        - 데이터 삽입, 삭제 시 해당 데이터 이후 모든 데이터가 복사되므로 빈번한 삭제, 삽입이 일어나는 경우에는 부적합하다.
        - 검색의 경우는 인덱스의 데이터를 가져오면 되므로 빠르다.
        - **재할당 시 크기의 절반씩 증가한다.**
    - LinkedList
        - 양방향 포인터 구조로 각 노드가 데이터와 포인터를 가지고 한 줄로 연결되어 있는 방식으로 데이터를 저장하는 자료 구조
        - 데이터의 삽입, 삭제 시 해당 노드의 주소지만 바꾸면 되므로 삽입, 삭제가 빈번한 데이터에 적합하다.
        - 메모리가 불연속적이다.
        - 데이터 검색 시 처음부터 순회하므로 검색에는 부적합하다.
        - 스택, 큐, 양방향 큐를 만들기 위한 용도로 사용한다.
        - 양옆의 정보만을 갖고 있기 때문에 순차적으로 검색을 진행하여 검색 속도가 느리다.
    - Vector
        - 내부에서 자동으로 동기처리가 일어난다.
        - 성능이 좋지 않아 잘 사용하지 않는다.
        - **재할당 시 크기의 두 배로 증가한다.**
    - Stack
        - new 키워드로 직접 사용 가능
        - Vector를 상속받아 동기 처리
        
        ### **cf) 배열과 리스트는 다른 것**
        
        - 배열(Array)은 크기가 고정적이라 선언 시 지정한 크기를 변경할 수 없다.(Immutable)
- 32. String, StringBuilder, StringBuffer
    - String
        - **새로운 값을 할당할 때마다 새로운 클래스에 대한 객체가 생성**
        - String에 저장되는 문자열은 private final char[] 형태이므로 변경할 수 없다.
        - String + String + String..
            - GC 호출되기 전까지 생성된 String 객체들은 Heap에 머물기 때문에 메모리 관리에서 치명적이다.
    - StringBuilder
        - 메모리에 append하는 방식으로 클래스에 대한 객체를 생성하지 않는다.
        - 비동기 처리
    - StringBuffer
        - 메모리에 append하는 방식으로 클래스에 대한 객체를 생성하지 않는다.
        - 동기 처리
- 33. String new와 “”의 차이
    
    new 는 계속 새로운 객체를 생성해내는 반면에 ""의 경우는 이미 존재하는 String 값이라면 같은 래퍼런스를 참조한다.
    
- 34. Blocking vs Non-Blocking
    - 프로세스의 **유휴 상태에** 대한 개념
    - 두 가지의 차이점은 **다른 주체가 작업할 때 자신이 코드를 실행할 제어권이 있는지 없는지로 판단** 할 수 있다.
    
    ### **Blocking**
    
    - Blocking 자신의 작업을 진행하다가 다른 주체의 작업이 시작되면 **제어권을 다른 주체로 넘긴다.**
    - 따라서 자신은 제어권이 없기 때문에 실행할 수 없고, 다른 주체가 실행을 완료하고 제어권을 돌려줄 때까지 아무 작업도 할 수 없다.
    
    <img width="679" alt="image" src="https://user-images.githubusercontent.com/84627144/177913554-c1c8bbfc-c7d8-4175-9028-3848fefc25ed.png">
    
    ### **Non-Blocking**
    
    - Non-Blocking은 다른 주체의 작업에 **관련없이 자신이 제어권을 갖고 있다.**
    - 따라서, 자신은 계속 작업을 수행할 수 있다.
    
    <img width="697" alt="image" src="https://user-images.githubusercontent.com/84627144/177913569-56eb59c9-803d-431f-b163-8bd3cb722a5f.png">
    
- 35. Sync vs Async
    - 프로세스 수행 순서 보장에 대한 메커니즘
    - 두 가지의 차이점은 **호출하는 함수가 호출되는 함수의 작업 완료 여부를 신경쓰는지 여부** 에 차이가 있다.
    - Sync(동기)
        - 동기는 함수 A가 B를 호출한 뒤, B의 결과값이 나오면 해당 결과값을 가지고 바로 처리하는 방식이다.
    - Async(비동기)
        - 비동기는 함수 A가 B를 호출한 뒤, B의 결과값에 큰 비중을 두지 않고 결과가 나오면 처리를 할 수도 있고 안 할 수도 있다.
- 36. Sync&Async, Blocking&Non-Blocking
    
    <img width="629" alt="image" src="https://user-images.githubusercontent.com/84627144/177913583-56fe66df-41b5-45e5-a104-c5e5f5800ee1.png">
    
- 37. 리플렉션
    - **런타임 상황에서 메모리에 올라간 클래스나 메서드등의 정의를 동적으로 찾아서 조작할 수 있는 기술**
    - 컴파일 시간이 아닐 실행 시간에 동적으로 특정 클래스의 정보를 객체화를 통해 분석 및 추출해낼 수 있는 프로그래밍 기법
    - 자바에서 이미 로딩이 완료된 클래스에서 또 다른 클래스를 동적으로 로딩하여 생성자, 필드, 메서드 등을 사용할 수 있는 방식이다.
    - 장점
        - 런타임 시점에 사용할 instance를 선택하고 동작시킬 수 있는 유연한 기능을 제공한다.
    - 단점
        - **컴파일 시점이 아니라 런타임 시점에서 오류를 잡기 때문에 컴파일 시점에 확인할 수 없다.**
        - 접근 제어자로 캡슐화된 필드, 메서드에 접근 가능해지므로 기존 동작을 무시하고 깨뜨리는 행위가 가능해진다.
        - 위와 같은 단점 때문에 피할 수 있다면 사용을 자제하는 것이 좋다.
    - 사용처
        - 런타임 시점에 다른 클래스를 동적으로 로딩하여 접근할 때 사용
        - 클래스와 멤버 필드, 메서드 등에 관한 정보를 얻어야 할 때 사용
- 38. Stream
    - java 8 에서 추가된 API
    - 컬렉션 타입의 데이터를 Stream 메서드로 내부 반복을 통해 정렬, 필터링 등이 가능
    - 특징
        - parallel 메서드 제공을 통해 **병렬처리** 가 가능
            - 각 스레드가 개별 큐를 가지고 있으며, 놀고 있는 스레드가 있으면 일하는 스레드의 작업을 가져와 수행
        - **데이터를 변경하지 않는다(Immutable)**
            - 원본데이터로부터 데이터를 읽기만 할 뿐, 원본데이터 자체를 변경하지 않는다.
        - 작업을 내부 반복으로 처리하므로 불필요한 코딩을 줄일 수 있다.
        - 최종 연산 후 stream이 닫히므로 **일회용** 이다.
    - 구조
        - Stream 생성
        - 중간 연산
            - **데이터를 가공하는 과정에 해당한다.**
            - 필터링 : filter, distinct
            - 변환 : map, flatMap
            - 제한 : limit, skip
            - 정렬 : sorted
            - 연산결과확인 : peek
        - 최종 연산
            - **Stream 안의 데이터를 모아 반환하는 역할을 한다.**
            - 출력 : foreach
            - 소모 : reduce
            - 검색 : findFirst, findAny
            - 검사 : anyMatch, allMatch, noneMatch
            - 통계 : count, min, max
            - 연산 : sum, savage
            - 수집 : collect
    - **중간 연산 작업은 바로 실행되는 것이 아니라 종결 처리의 실행이 필요할 때서야 비로소 중간 처리가 실행된다.(Lazy Evalutation)**
- 39. ParallelStream
    - 개발자가 직접 스레드 혹은 스레드 풀을 생성하거나 관리할 필요 없이 parallelStream, parallel()만 사용하면 알아서 내부적으로 common **ForkJoinPool** 을 사용하여 작업들을 분할하고 병렬적으로 처리한다.
        - **forkJoinPool은 ExecutorService의 구현체로 각 스레드별 개별 큐를 가지고 스레드에 아무런 task가 없으면 다른 스레드의 task를 가져와 처리하여 최적화 성능을 낼 수 있다는 특징이 있다.**
    - **내부적으로 스레드 풀을 만들어서 작업을 병렬화시킨다.**
    - **중요한 점은 parallelStream 각각 스레드 풀을 만드는게 아니라 별도의 설정이 없다면 하나의 스레드 풀을 모든 parallelStream이 공유한다.**
    - ParallelStream은 중간 연산에서 순서가 보장되지 않기 때문에 중간 연산에서 순서에 관계없는 연산의 경우에만 사용한다.
    - Parallel Stream은 작업을 분할하기 위해 Spliterator의 trySplit()을 사용하게 되는데, 이 분할되는 작업의 단위가 균등하게 나누어져야 하며, 나누어지는 작업에 대한 비용이 높지 않아야 순차적 방식보다 효율적으로 이뤄질 수 있다. array, arrayList와 같이 정확한 전체 사이즈를 알 수 있는 경우에는 분할 처리가 빠르고 비용이 적게 들지만, LinkedList의 경우라면 별다른 효과를 찾기 어렵다.
- 40. Fork Join Pool
    - Java7에서 새로 지원하는 fork-join 풀을 기본적으로 큰 업무를 작은 업무로 나눠 배분하여(fork), 일을 한 후에 일을 취합하는 형태이다.(join)
    - 하나의 작업 큐를 가지고 있으며, 이러한 작업들을 Fork Join Pool에서 관리하는 여러 스레드에서 접근하여 작업들을 처리한다.
    - 서로 작업을 하려고 큐에서 작업을 가져가며, 각 스레드들은 부모 큐에서 가져간 작업들을 내부 큐(inbound queue)에 담아 관리한다.
    - 스레드들은 서로의 큐에 접근하여 작업들을 가져가 처리한다. 이러한 방법들은 놀고 있는 스레드가 없도록 하기 위해 도입되었다.
        
        <img width="658" alt="image" src="https://user-images.githubusercontent.com/84627144/177913606-e8c88178-b1b8-47cd-9e8a-a1bad1d154da.png">
        
    - 사진
        
       <img width="641" alt="image" src="https://user-images.githubusercontent.com/84627144/177913620-edb32aeb-e26e-423b-a848-ab849555e514.png">
        
- 41. 람다식
    - 자바 8에서 등장
    - **메서드를 하나의 식으로 표현하는 익명 함수**
    - 람다식을 이용해 함수형 인터페이스를 구현할 수 있음
    - 함수형 인터페이스
        - 함수를 1급 객체처럼 다룰 수 있게 해주는 어노테이션
        - 인터페이스에 선언해 단 하나의 추상 메소드만을 갖도록 제한함
        - 함수형 인터페이스를 사용하는 이유는 람다식이 함수형 인터페이스를 반환하기 떄문
    
    장점
    
    - 기존에 익명함수로 작성하던 코드를 줄일 수 있음
    - 가독성 증가
    - 병렬 프로그래밍이 용이하다. (??)
- 42. 함수형 프로그래밍
    - 거의 모든 것을 순수 함수로 나누어 문제를 해결하는 기법이다.
    - 작은 문제를 해결하기 위한 함수를 작성하여 가독성을 높이고 유지보수를 용이하게 해준다.
    - 추가설명 - **함수형은 대입문이 없는 프로그래밍**
        
        Robert C.Martin은 **함수형 프로그래밍을 대입문이 없는 프로그래밍** 이라고 정의하였다.명령형 프로그래밍에서는 메소드를 호출하면 상황에 따라 내부의 값이 바뀔 수 있다. 즉, 우리가 개발한 함수 내에서 선언된 변수의 메모리에 할당된 값이 바뀌는 등의 변화가 발생할 수 있다.하지만 함수형 프로그래밍에서는 대입문이 없기 때문에 메모리에 한 번 할당된 값은 새로운 값으로 변할 수 없다.
        
    - 순수함수 : 같은 인자에 대해서 항상 같은 값을 반환하고 외부의 어떤 상태도 바꾸지 않는 함수
    - 일급객체 : 함수의 인자로 전달할 수 있고, 함수의 반환값으로 사용할 수 있고, 변수에 담을 수 있는 객체
    - 일급함수 : 함수가 일급객체면 일급함수라고 하고 일급함수에 이름이 없다면 람다식이라고 한다.
    
    ### **특징**
    
    부수 효과가 없는 순수 함수를 **1급 객체** 로 간주하여 파라미터로 넘기거나 반환값으로 사용할 수 있으며, 참조 투명성을 지킬 수 있다.
    
    - side effect가 없음 - 함수형 프로그래밍은 함수 내부적으로 어떠한 상태도 가지지 않는다. 따라서 함수 내부에서 벌어지는 일에 대해서는 전혀 신경쓸 필요가 없다. 단지, 함수 호출 시 입력하는 값과 그에 대한 결과 값만이 중요할 뿐이다.
    - 동시성 이슈 없음 - 명령형 프로그래밍에서 교착상태가 발생하는 주된 원인은 스레드 간에 공유되는 데이터나 상태 값이 변경 가능(mutable)하기 때문이다. 하지만 함수형 프로그래밍은 모든 데이터가 변경 불가능하고 함수는 부수 효과를 가지고 있지 않기 때문에 여러 스레드가 동시에 공유 데이터에 접근하더라도 해당 데이터가 변경될 수 없기 때문에 동시성 관련된 문제를 원천적으로 봉쇄한다.
    - 함수를 값처럼 쓸 수 있기 때문에 익명함수처럼 간결한 코드를 구성할 수 있다.
    
    ### **단점**
    
    - 순수함수를 구현하기 위해서 코드의 가독성이 좋지 않을 수 있다.
    - 순수함수를 사용하는 것은 쉬울지라도 조합하는 것은 쉽지 않다.
- 43. Optional
    - null이 올 수 있는 값을 감싸는 wrapper class로, 참조하더라도 NPE가 발생하지 않도록 도와준다.
    1. orElse() 메소드 : 저장된 값이 존재하면 그 값을 반환하고, 값이 존재하지 않으면 **인수로 전달된 값을 반환함.**
    2. orElseGet() 메소드 : 저장된 값이 존재하면 그 값을 반환하고, 값이 존재하지 않으면 **인수로 전달된 람다 표현식의 결과값을 반환함.**
    3. orElseThrow() 메소드 : 저장된 값이 존재하면 그 값을 반환하고, 값이 존재하지 않으면 **인수로 전달된 예외를 발생시킴.**
    
    ```java
    System.out.println(opt.orElse("빈 Optional 객체"));
    System.out.println(opt.orElseGet(String::new));
    return opt.orElseThrow(() -> new Exception("ohlcv result set null"));
    ```
    
- 44. 자바8에 추가된 내용
    - optional
    - stream
    - lambda
    - localDateTime
        - **cf) 기존 date의 문제점**
            - 불변 객체가 아님
            - 헷갈리는 월 지정(1월을 0으로 표현)
            - 일관성 없는 요일 상수(어디서는 일요일이 0 어디서는 1)
            - Date와 Calendar 객체의 역할 분담(Date만으로 부족해서 왔다갔다 해야함)
            - 상수 필드 남용
    - default 메서드 - 인터페이스에 default 메서드 추가 가능해짐
- 45. 자바8 → 자바11
    - **default GC가 Parallel GC에서 G1GC로 변경**
    - **람다에서 로컬 변수 var이 사용 가능**
    - Javac를 통해 컴파일하지 않고도 바로 java 파일을 실행할 수 있게 되었다.
    - strip(), stripLeading(), stripTrailing(), isBlank(), repeat(n) 과 같은 **String 클래스에 새로운 메서드 추가**
    - writeString, readString, isSameFile 과 같은 **File관련 새로운 메서드 추가**
    - 컬렉션의 toArray() 메서드를 오버로딩하는 메서드가 추가되어 원하는 타입의 배열을 선택하여 반환할 수 있게 되었다.
        - sampleList.toArray(String[]::new)
    - Predicate 인터페이스에 부정을 나타내는 not() 메서드 추가
- 46. 멀티스레드 프로그래밍
    - 스레드 생성 방법
        - 방법 1: Thread 클래스를 상속받아서 run을 오버라이드해서 정의한다.
        - 방법 2: Runnable 인터페이스를 구현하여 Thread 생성자에 인자로 넘긴다.
        - 방법 3: Callable 인터페이스를 구현하여 FutureTask에 한번 감싸서 Thread의 인자로 넘긴다.
        - **Runnable은 Exception이 없고 리턴값도 없으나 Callable은 리턴값이 있고 Exception을 발생시킬 수 있다.**
    - 스레드 실행 방법
        - 보통 start() 메서드를 사용해서 호출하는데 start 한다고 해서 바로 실행되는 것은 아니고 실행 대기열에 저장된 후 차례가 오면 실행된다.
        - 정확하게 말하자면, start는 새로운 스레드가 작업을 실행하는데 필요한 새로운 호출 스택을 생성해서 그곳에 run 메서드를 올려둔다. 이후 그곳에서 run 메서드를 호출하고 스레드가 별개의 작업을 수행하게 된다.
    
    **보통 위와 같이 인터페이스를 구현해서 Thread의 인자로 넘기거나, 상속으로 구현하는 방식은 운영환경에서 프로그램 성능에 영향을 미치기 때문에 사용하지 않는다.**
    
    운영 시에는 **ExecutorService와 Executors를 이용해 스레드풀을 생성하여 병렬처리**한다. 
    
- 47. 동기화에서 발생할 수 있는 문제 2가지
    - 가시성 문제
        
        하나의 스레드에서 공유 자원(변수, 객체 등)을 수정한 결과가 다른 스레드에게 보이지 않을 경우 발생하는 문제
        
    - 동시 접근 문제
        
        여러 스레드에서 공유자원(변수, 객체 등)을 동시에 접근하였을 때, 연산이 가장 늦게 끝난 결과값으로 덮어씌워지는 문제입니다.
        
- 48. Java 동기화
    
    자바에서 동시성 문제를 해결하는데 3가지 방법이 있습니다.
    
    - synchronized : 안전하게 동시성을 보장할 수 있습니다. 하지만 비용이 가장 큽니다.
    - volatile : 키워드가 붙은 자원은 하나의 thread만이 write하고 나머지는 스레드는 read만 한다는 전제하에만 동시성을 보장합니다.
        - **volatile 키워드를 붙인 자원은 read, write 작업이 CPU Cache Memory가 아닌 Main Memory에서 이뤄집니다.**
        - 즉, 자원을 저장하는 메모리는 하나가 되기 때문에 같은 공유자원에 대해 각각 메모리별로 다른 값을 가지는 경우가 없습니다.
        - 하지만 여러 스레드에서 Main Memory에 있는 공유자원에 동시에 접근할 수 있으므로 여러 스레드에서 수정하게 되면, 계산값이 덮어씌워지게 되므로 동시 접근 문제를 해결할 수 없습니다.
        - **정리하면, 가시성 문제는 해결할 수 있지만, 동시 접근 문제는 해결할 수 없습니다.**
    - Atomic 클래스는 CAS(compare-and-swap)를 이용하여 동시성을 하므로 여러 쓰레드에서 데이터를 write해도 문제가 없습니다. synchronized 보다 적은 비용으로 동시성을 보장할 수 있습니다.
        - **CAS 알고리즘이란 현재 스레드가 존재하는 CPU의 CacheMemory와 MainMemory에 저장된 값을 비교하여, 일치하는 경우 새로운 값으로 교체하고, 일치하지 않을 경우 기존 교체가 실패되고, 이에 대해 계속 재시도하는 방식입니다.**
        - **CPU가 MainMemory의 자원을 CPU Cache Memory로 가져와 연산을 수행하는 동안 다른 스레드에서 연산이 수행되어 MainMemory의 자원 값이 바뀌었을 경우 기존 연산을 실패처리하고, 새로 바뀐 MainMemory 값으로 재수행하는 방식입니다.**
- 49. Synchronized와 Lock & Condition 동기화
    
    **Synchronized**
    
    - synchronized method
        - 인스턴스 단위 lock
        - 동일한 인스턴스 내 synchronized 키워드가 적용된 메서드끼리 lock을 공유
    - synchronized block
        - this를 명시하면 synchronized method와 동일하게 동작하면서 synchronized method와 lock을 공유
        - 특정 객체를 명시하면 해당 객체에만 특정 lock을 걸면서 **해당 객체에 lock을 거는 block끼리만** lock을 공유
        - .class 형식 명시하면 해당 클래스에만 특정 lock을 걸면서 **해당 클래스에 lock을 거는 block끼리만** lock을 공유
    - static synchronized method
        - 클래스 단위 lock
        - static synchronized와 synchronized가 혼용되어있을 때 각자의 lock으로 관리
    - static synchronized block
        - 클래스 단위 lock
        - block의 인자로 정적 인스턴스나 클래스만 사용
    - **synchronized는 Thread의 동기화 순서를 보장하지 않는다.**
    
    **Lock**
    
    - synchronized는 블록 구조를 사용하여 메서드안에 임계영역의 시작과 끝이 있고 알아서 lock을 회수해주는 반면에 Lock은 lock, unlock 메서드로 시작과 끝을 명시하기 때문에 명확하고 임계 영역을 여러 메서드에서 나눠서 작성할 수 있습니다.
    - concurrent.locks 패키지는 내부적으로 synchronized를 사용하여 구현되어 있지만 더욱 유연하고 세밀하게 처리하기 위해 사용됩니다.
    - **Lock** : 공유 자원에 한 번에 한 쓰레드만 read, write가 수행 가능하도록 제공하는 인터페이스
        - **ReentrantLock** : Lock의 구현체로 임계 영역의 시작과 종료 지점을 직접 명시할 수 있습니다.
    - **ReadWriteLock** : 공유 자원에 대해서 여러 개의 스레드가 read 가능하고, write는 한 스레드만 가능한 인터페이스로 읽기를 위한 lock과 쓰기를 위한 lock을 별도로 제공합니다.
        - **ReentrantReadWriteLock** : ReadWriteLock의 구현체
    - StampedLock
        - **ReentrantReadWriteLock에 낙관적인 lock기능을 추가한 것입니다.**
        - lock을 걸거나 해지할 때 스탬프(long 타입의 정수)를 사용하여 읽기와 쓰기를 위한 lock외에 낙관적인 lock이 추가된 것입니다.
        - **무조건 읽기 lock을 걸지 않고, 쓰기와 읽기가 충돌할 때만 쓰기가 끝난 후에 읽기 lock을 겁니다.**

    **Condition 클래스**
        - 특정 스레드를 위한 Conditon 인스턴스를 만들어 스레드 별로 wai t pool을 만들어주는 기능을 한다.
        - 이를 이용하여 깨우고 싶은 특정 스레드만 깨우는 것이 가능하다. 
- 50. Atomic
    - Atomic[Long]
        - [Long] 자료형을 갖고 있는 Wrapping 클래스입니다.
        - Thread-safe로 구현되어 멀티쓰레드에서 synchronized 없이 사용할 수 있습니다.
        - synchronized 보다 적은 비용으로 동시성을 보장할 수 있습니다.
    - AtomicReference
        - AtomicReference는 V 클래스(Generic)의 객체를 wrapping 클래스입니다.
        - AtomicReference 클래스는 멀티쓰레드 환경에서 **동시성을 보장**합니다.

- 51. 왜 Vector 를 사용하지 않을까? 
    - Vector의 모든 get() set() 등의 메서드에 **synchronized**가 붙어있는건 특정 상황에서 성능을 꽤 저하시킬 수 있다.
    - 단순히 Vector에 Iterator를 붙여 순차적으로 item들을 탐색하기만 해도 원소탐색 시마다 get() 메서드의 실행을 위해 계속 lock을 걸고 닫으므로 Iterator 연산과정 전체에 1번만 걸어주면 될 locking에 쓸데없는 오버헤드가 엄청나게 발생한다.
    - 상황에 따라 굉장히 비효율적인 연산이 발생함