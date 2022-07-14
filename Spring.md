- 1. 프레임워크란
    - 프레임워크란 응용 프로그램이나 소프트웨어 솔루션 개발을 수월하기 위해 **구조, 틀이 제공된 소프트웨어 환경**이다.
- 2. Spring이란
    - 동적인 웹 사이트를 개발하기 위한 여러 가지 서비스를 제공하는 오픈소스 애플리케이션 프레임워크
    - 특징
        - POJO 기반의 구성으로 자바 코드를 이용해서 객체를 구성하는 방식 그대로 스프링에서 사용할 수 있다.
            - 덕분에 높은 생산성과 유연한 테스트를 할 수 있다.
        - DI(의존성 주입)을 통한 객체 관계 구성을 지원한다.
        - AOP(관점 지향 프로그래밍) 지원
        - MVC 구조로 계층이 분리되어 관리하기 수월하다.
- 3. DI(Dependency Injection)
    - **DI는 스프링 프레임워크에서 지원하는 IoC의 형태** 이다.
    **클래스 사이의 의존관계를 빈 설정 정보를 바탕으로 컨테이너가 자동으로 연결해주는 것이다.**
    - 장점
        - **스프링 자체에서 설정을 통해 연관 관계를 맺어줌으로써 객체간 결합도를 낮춰준다.**
        - **클래스의 재사용성을 높이고, 유지보수가 편리해진다.**
        - 의존성 주입으로 인해 stub, mock 객체를 사용해 unit 테스트의 이점이 생긴다.
    - 단점
        - 의존성 주입을 위한 선행 작업이 필요해 간단한 프로그램에서는 번거롭다.
        - **코드 추적이 어렵다.**
- 4. 주입 방식
    - 필드 주입(`@Autowired`)
        - 외부에서 변경이 불가능해서 테스트하기 어렵다.
        
        ```java
        public class ExampleClass {
        	
            @Autowired
            private Example example;
        }
        ```
        
    - Setter 주입
        - 대부분 의존 관계 주입은 한번 일어나면 종료시점까지 변경할 일이 거의 없다.
        - Setter를 통해 주입하게 되면 변경될 위험이 존재
        - setter을 public으로 열어야함
        
        ```java
        public class ExampleClass {
        	
            private Example example;
            
            @Autowired
            public void setExample(Example example) {
            	this.example = example;
            }
        }
        ```
        
    - 생성자 주입(권장)
        - 생성자 호출 시점에 딱 1번만 호출되는 것을 보장
        - final 키워드를 통해 불변하게 설계 가능
        - 의존성 주입이 누락되는 것을 방지할 수 있음(IDE에서 컴파일 오류로 알려줌)
        - 객체의 생성과 의존관계 주입이 동시에 일어남(다른 2가지 방식은 객체 생성 → 의존관계 주입으로 라이프 사이클이 나뉘어 있음)
        
        ```java
        public class ExampleClass {
        	
            // final을 사용할 수 있다.
            private final Example example;
            
            @Autowired
            public ExampleClass(Example example) {
            	this.example = example;
            }
        }
        ```
        
- 5. 왜 생성자 주입을 해야할까?
    - 자바에서 new 연산을 호출하면 생성자가 호출이 되는데 예를 들어, Controller 클래스가 생성될 때 그 안에 존재하는 Service 클래스와의 의존관계가가 존재하지 않는다면, Controller 클래스의 객체 생성이 불가능해진다.
    - 따라서, **생성자 주입 방식은 객체 생성과 의존 관계 주입이 하나의 단계에서 발생한다.**
    - 장점
        - null을 주입하지 않는 한 NullPointerException은 발생하지 않는다.
        - 의존관계를 주입하지 않은 경우 객체를 생성할 수 없다. 즉, 의존관계에 대한 내용을 외부에 노출시킴으로써 컴파일 타임에 오류를 잡아낼 수 있다.
    - 반대로 setter 주입 같은 경우, Controller 객체를 만들 때 의존관계가 필요하지 않다. (Service 객체가 없더라도 Controller 객체를 만들 수 있다.)
        - 객체 생성 후 의존 관계 주입이 단계로 나뉘어서 Bean LifeCycle 이 진행된다. 코드 상의 의존관계를 보고 IoC 컨테이너에서 의존성 주입을 해준다.
- 6. IoC(Inverse of Control, 제어의 역전)
    - **객체의 생성부터 생명주기의 관리까지 모든 객체에 대한 제어권이 바뀐 것을 의미**한다.
    - 개발자는 프레임워크에 필요한 부품을 개발하고 조립하는 방식으로 개발을 하고 최종 호출은 개발자가 아니라 프레임워크의 내부에서 결정된 대로 이뤄지게 되는데 이런 현상을 제어의 역전이라고 한다.
- 7. 스프링 컨테이너
    - **스프링 컨테이너는 자바 객체(빈)의 생명 주기를 관리하며, 생성된 자바 객체들에게 추가적인 기능을 제공하는 역할을 한다.**
    - 스프링 컨테이너의 종류에는 BeanFactory와 **ApplicationContext**가 있다.
    - 둘 다 빈을 등록하고 생성하고 조회하고 돌려주는 등 빈을 관리하는 역할을 한다.
    - ApplicationContext가 BeanFactory의 빈 관리 기능들을 상속받았고, 그 외에 국제화 등의 추가적인 기능을 갖고 있어 스프링 컨테이너라고 하면 보통 ApplicationContext라고 한다.
- 8. Bean
    - **컨테이너 안에 들어있는 객체**
    - 필요할 때 컨테이너에서 가져와서 사용
    - `@Bean`을 사용해 등록하거나 xml을 사용해 등록하고, Bean으로 등록된 객체는 쉽게 주입하여 사용 가능
- 9. Bean 생명주기
    
    > 스프링 컨테이너 생성 -> 스프링 빈 생성 -> 의존 관계 주입 -> 초기화 콜백 -> 사용 -> 소멸전 콜백 -> 스프링 종료
    > 
    - 초기화 콜백, 소멸 전 콜백
        - **초기화 콜백**을 통해 개발자가 의존관계 주입이 완료된 상태임을 확인할 수 있고, 이 때 초기화 작업을 진행해야 함을 알 수 있다.
        - **소멸 콜백**을 통해 스프링이 종료되기 전인 상태임을 개발자가 확인할 수 있고, 이 때 종료작업을 안전하게 진행할 수 있다.
    - 스프링 컨테이너에 의해 생명주기 관리
    - 스프링 컨테이너 초기화 시 빈 객체 생성, 의존 객체 주입 및 초기화
    - 생성과 의존관계 주입과 초기화 분리
        - 의존관계 주입(생성자 주입)은 필수정보를 받고 메모리 할당을 통해 객체 생성 책임
        - 초기화는 생성된 값들을 활용해 외부 커넥션을 연결하는 등 무거운 작업 수행
        - 명확하게 분리하는 것이 유지보수 관점에서 좋다.
    - 싱글톤 빈들은 컨테이너가 종료되기 직전에 소멸전 콜백이 발생
    - 초기화와 소멸 메서드는 애노테이션으로 **`@PostConstruct`, `@PreDestroy`** 를 사용하는 것이 권장된다.
- 10. 빈 스코프
    - Singleton Scope
        - 스프링 컨테이너 시작과 종료까지 1개의 객체로 유지
        - `@Component` 를 붙여 빈으로 등록
    - Prototype Scope
        - 빈의 생성, 의존관계 주입, 초기화까지만 관여하고 이후에는 컨테이너에서 관리하지 않는 스코프
        - **따라서 매번 요청마다 새로 만들어짐**
        - `@Scope(value = "prototype")` 를 붙여 설정
    - 웹 스코프(Web Scope)
        
        : 웹 환경에서만 동작하는 스코프입니다 .
        
        - request
            - HTTP 요청이 들어오고 나갈때까지 유지되는 스코프
            - 각각의 HTTP 요청마다 별도의 빈 인스턴스가 생성되고 관리됨 (GC까지 관리해줌)
        - session : HTTP 세션과 동일한 생명주기를 가지는 스코프
        - application : 웹의 **서블릿 컨텍스트와** 동일한 생명주기를 갖는 스코프
            - 서블릿 컨텍스트는 **web application내에 있는 모든 서블릿들을 관리하며 정보공유할 수 있게 도와 주는 역할** 을 하는데, 톰캣 컨테이너가 실행 시 애플리케이션 하나당 한개의 서블릿컨텍스트가 생성된다.
            - 생명 주기는 보통 톰캣의 시작과 종료와 일치한다.
- 11. 어댑터 패턴(Adapter Pattern)
    - 호출당하는 쪽(ex: service)의 메서드를 호출하는 쪽(ex: main)의 코드에 대응하도록 중간에 **adpater를 통해 호출하는 패턴**
- 12. 싱글톤 vs 스프링 싱글톤
    
    싱글톤 패턴은 전역 상태를 이용할 수 있다는 장점이 있지만 다음과 같은 문제점으로 인해 안티 패턴으로도 불린다.
    
    - **private 생성자를 갖고 있어 상속이 불가능하다.**
        - 싱글톤은 자신만이 객체를 생성할 수 있도록 private으로 제한한다. 하지만 상속을 통해 다형성을 적용하기 위해서는 기본 생성자가 필요하므로 private으로 인해 객체지향의 장점을 적용할 수 없다. 또한 싱글톤을 구현하기 위해서는 객체지향적이지 못한 static 필드와 static 메서드를 사용해야 한다.
    - **테스트하기 힘들다.**
        - 싱글톤은 생성 방식이 제한적이기 때문에 Mock 객체로 대체하기 어려우며, 동적으로 객체를 주입하기도 힘들다.
    - **서버 환경에서는 싱글톤이 1개만 생성됨을 보장하지 못한다.**
        - 서버에서 **클래스 로더** 를 어떻게 구성하느냐에 따라 싱글톤 클래스임에도 불구하고 1개 이상의 객체가 만들어질 수 있다. 따라서 자바 언어를 이용한 싱글톤 기법은 서버 환경에서 싱글톤이 꼭 보장된다고 볼 수 없다. 또한 여러 개의 JVM에 분산돼서 설치되는 경우 독립적으로 객체가 생성된다.
    - **전역 상태를 만들 수 있기 때문에 바람직하지 못하다.**
        - 싱글톤의 정적 메서드를 사용하면 언제든지 해당 객체를 사용할 수 있고, 전역 상태로 사용되기 쉽다. 아무 객체나 자유롭게 접근하고 수정하며 공유되는 전역 상태는 객체지향 프로그래밍에서 권장하지 않는다.
    
    ### **스프링 싱글톤**
    
    **객체의 생성을 스프링에 위임함으로써 스프링 컨테이너가 관리하여 자바 언어 레벨에서 직접 구현하기 위한 내용들이 모두 제거되어 앞선 싱글톤의 모든 단점들이 제거된다.**
    
    - private 생성자가 필요 없어 상속이 가능해진다.
    - 테스트하기 편하다.
    - 프레임워크를 통해 1개의 객체 생성을 보장받을 수 있다.
    - 객체지향적으로 개발할 수 있다.
- 13. Annotation
    
    Annotation은 **프로그램, 컴파일러에 추가적인 정보를 제공하는 메타데이터**
    
    - 동작 순서
        - 애노테이션 정의 → 원하는 위치에 배치 → 코드가 실행되는 중에 Reflection을 이용하여 추가 정보를 획득하여 기능 실시
    - Reflection
        - **Annotation 자체는 아무런 동작을 가지지 않는 단순한 표식일 뿐이지만, Reflection을 이용하면 Annotation의 적용 여부와 엘리먼트 값을 읽고 처리할 수 있다.**
        - **Spring 컨테이너(BeanFactory)에서 객체가 호출되면 객체의 인스턴스를 생성하게 되는데 이 때 필요하게 된다. 즉, 프레임워크에서 유연성있는 동작을 위해 쓰인다.**
        - Reflection을 이용하면 Annotation 지정만으로도 원하는 클래스를 주입할 수 있다.
- 14. 스프링에서 활용되는 Reflection API
    - Spring Framework에서도 Reflection API를 사용하는데 대표적으로 Spring Container의 **BeanFactory**가 있다. Bean은 애플리케이션이 실행한 후 런타임에 객체가 호출될 때 동적으로 객체의 인스턴스를 생성하는데 이때 Spring Container의 BeanFactory에서 리플렉션을 사용한다.
    - Spring Data JPA 에서 Entity에 기본 생성자가 필요한 이유도 동적으로 객체 생성 시 Reflection API를 활용하기 때문이다. Reflection API로 가져올 수 없는 정보 중 하나가 생성자의 인자 정보이다. 그래서 기본 생성자가 반드시 있어야 객체를 생성할 수 있는 것이다. 기본 생성자로 객체를 생성만 하면 필드 값 등은 Reflection API로 넣어줄 수 있다.
- 15. Spring Annotation
    - **@ComponentScan**
        - **@Component, @Service, @Repository, @Controller, @Configuration이 붙은 클래스 Bean들을 찾아서 Context에 bean을 등록해주는 애노테이션**
        - 전부 다 @Component를 사용하지 않고 @Repository 등으로 분리해서 사용하는 이유는, 예를 들어 @Repository는 DAO에서 발생할 수 있는 unchecked exception들을 스프링의 DataAccessException으로 처리할 수 있기 때문이다.
        - 또한 가독성에서도 해당 애노테이션을 갖는 클래스가 무엇을 하는지 단 번에 알 수 있다.
    - **@EnableAutoConfiguration**
        - autoConfiguration도 Configuration중 하나에 해당한다.
        - spring.factories 내부에 여러 Configuration들이 있고 조건에 따라 Bean이 등록되게 되는데 메인 클래스 @SpringBootApplication을 실행하면 @EnableAutoConfiguration에 의해 spring.factories 안에 있는 수많은 자동 설정들이 조건에 따라 적용되어 수 많은 Bean들이 생성된다.
        - 간단하게 정리하면, **Application Context를 만들 때 자동으로 빈설정이 되도록 하는 기능이다.**
    - @Component
        - 개발자가 직접 작성한 class를 Bean으로 등록하기 위한 애노테이션
    - @Bean
        - 개발자가 직접 제어가 불가능한 외부 라이브러리등을 bean으로 만들려할 때 사용되는 애노테이션
    - @Configuration
        - @Configuration을 클래스에 적용하고 @Bean을 해당 class의 메서드에 적용하면 @autowired로 Bean을 부를 수 있다.
    - @Autowired
        - 스프링이 Type에 따라 알아서 Bean을 주입해준다.
        - Type을 먼저 확인한 후 못 찾으면 Name에 따라 주입한다.
        - 강제로 주입하고자 하는 경우 @Qulifier을 같이 명시
    - @Qualifier
        - 같은 타입의 빈이 두 개 이상 존재하는 경우 스프링이 어떤 빈을 주입해야할 지 알 수 없어서 스프링 컨테이너를 초기화하는 과정에서 예외가 발생한다.
        - @Qualifier는 @Autowired와 함께 사용하여 정확히 어떤 bean을 사용할지 지정하여 특정 의존 객체를 주입할 수 있다.
    - **@Resource**
        - **@Autowired와 마찬가지로 Bean 객체를 주입해주는데 차이점은 Autowired는 타입으로, Resource는 이름으로 연결해준다.**
        - **애노테이션 사용으로 인해 특정 Framework에 종속적인 애플리케이션을 구성하지 않기 위해서 @Resource 사용을 권장한다.**
    - @Controller
        - API와 view를 동시에 사용하는 경우에 사용
        - 보통 view 화면 return을 목적으로 사용한다.
    - @RestController
        - view가 필요 없이 API만 지원하는 서비스에서 사용
    - @SpringBootApplication
        - @Configuration, @EnableAutoConfiguration, @ComponentScan 3가지를 하나로 합친 애노테이션
    
- 16. 웹 서버(Web Server)와 웹 애플리케이션 서버(WAS)
    
    
    <img width="682" alt="image" src="https://user-images.githubusercontent.com/84627144/179007403-0dace32f-699c-4d96-a133-de25dad49050.png">
    
    - 웹 서버
        - 정적 리소스 파일을 제공하는 서버
    - 웹 애플리케이션 서버(WAS)
        - 웹 서버가 하는 일 + 애플리케이션 로직(DB 연결, 동작 수행, 데이터 제공)까지 제공하여 동적인 처리를 하는 서버
        - 자바 진영에서는 서블릿 컨테이너 기능을 제공하면 WAS 라고 한다.
        - 위 그림에는 없지만 WAS 안에도 웹 서버가 따로 존재한다.
        
- 17. 서블릿
    
    <img width="695" alt="image" src="https://user-images.githubusercontent.com/84627144/179007441-6a2cec7d-27ed-4739-8057-dbd5a6330013.png">
    
    - 서블릿은 WAS 안에서 **동적인 페이지를 만드는데 사용되는 서버 프로그램**
    - 서블릿 전에는 요청이 들어오면 HTTP 요청 메시지를 파싱하는 것부터 여러 부가 작업을 개발자가 수행해야 했지만, 서블릿이 나오면서 부가적인 작업을 대신해주게 되었고, 개발자는 실직적인 메인 로직에만 집중 할 수 있게 되었다.
- 18. 서블릿 컨테이너
    
    : 서블릿 컨테이너는 **서블릿의 생명주기**를 관리한다.
    
    - init : 서블릿 초기화
    - service : HTTP 요청 유형을 확인하고 맞게 doGet, doPost, doPut 등 메서드를 호출하여 요청 처리
    - destroy : 서블릿 제거
    
    서블릿 객체도 **싱글톤** 으로 관리되기 때문에 최초 요청 시점에 서블릿 객체를 초기화해서 서블릿 컨테이너에 보관하고 이후에는 같은 서블릿을 공유해서 사용한다.
    
    - **요청 시 동작 과정**
        
        <img width="641" alt="image" src="https://user-images.githubusercontent.com/84627144/179007551-0539f686-50c8-4fff-925a-b243caf6ba4a.png">
        
        1. 사용자가 URL을 클릭하면 HTTP Request를 Servlet Container로 보낸다.
        2. **Servlet Container는 쓰레드 풀에서 쓰레드를 꺼내 할당** 해주고 HttpServletRequest, HttpServletResponse 두 객체를 생성한다.
        3. 사용자가 요청한 URL을 분석하여 어느 서블릿에 대한 요청인지 찾는다.
        4. 서블릿 컨테이너에 존재하지 않으면 초기화하고 있다면 가져와서 service() 메서드를 호출한다.
            - Spring MVC의 경우 DispatcherServlet이 초기화되고 호출된다.
        5. service 메서드가 수행이 끝나면 HttpServletResponse 객체에 응답을 보낸다.
        6. 응답이 완료되면 HttpServletRequest, HttpServletResponse 객체를 소멸시킨다.
- 19. 특정 서블릿에 접근하는 n명의 사용자가 있는 경우, 이 서블릿은 첫번째 사용자가 처음 엑세스 했을때만 인스턴스화 되는건가요, 아니면 모든 사용자에게 개별적으로 인스턴스화 되는건가요?
    
    웹 애플리케이션이 로드되면 서블릿 컨테이너(아파치 톰캣 같은)는 ServletContext를 **한번 생성하여** 메모리에 보관한다.
    
    이후 servlet, filter, listener가 발견되면 해당 클래스들은 **한번 인스턴스 생성하고** 서버의 메모리에 보관한다.
    
    다른 것들은 처음으로 HTTP request가 올때 init 메서드로 생성하여 보관한다.(이 이유로 첫 사용자의 경우 응답속도가 늦다.)
    
- 20. MVC 패턴
    - 그림
        
    <img width="669" alt="image" src="https://user-images.githubusercontent.com/84627144/179007853-ccf0a696-f14c-4525-9341-9a574063df19.png">
        
    1. 핸들러 조회
        - 핸들러 매핑을 통해 요청 URL에 매핑된 핸들러(컨트롤러)를 조회한다.
    2. 핸들러 어댑터 조회
        - 핸들러를 실행할 수 있는 핸들러 어댑터를 조회한다.
    3. 핸들러 어댑터 실행
        - 조회한 핸들러(컨트롤러)를 인자로 핸들러 어댑터에 넘겨서 핸들러를 실행시킨다.
    4. ModelAndView 반환
        - 핸들러(컨트롤러)가 로직을 수행하고 반환하는 정보로 ModelAndView로 변환해서 반환한다.
    5. viewResolver 호출
        - 적절한 viewResolver를 찾고 해당 viewResolver를 호출한다.
        - RestController라면 이 과정과 이후 과정 없이 컨버터를 이용해 바로 결과값을 리턴한다.
    6. View 반환
        - viewResolver는 뷰의 논리 이름을 물리 이름으로 바꾸고, 랜더링 역할을 담당하는 뷰 객체를 반환한다.
    7. 뷰 랜더링
        - 뷰를 통해서 뷰를 랜더링한다.
- 21. MVC 패턴 장단점
    - 장점
        - 과거에는 Controller에 다 담아두고 처리했다.
        - **기능 별로 코드를 분리하여, 가독성을 높이고 재사용성을 증가시킨다.**
    - 단점
        - **view와 model 사이에 의존성이 높아서 애플리케이션이 커질수록 복잡해지고 유지보수가 어렵다.**
        - **대규모의 프로그램에서 Controller에 다수의 Model과 View가 복잡하게 연결되어 코드 분석과 테스트가 어려워 질 수 있다.**
        - 이런 의존성 문제를 해결하기 위해 MVVM, MVP 구조가 등장했다.
