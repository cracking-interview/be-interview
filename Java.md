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
