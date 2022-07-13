# Adapter pattern in Spring

### 스프링에서의 Adapter pattern

- **AOP에서 load-time-weaving**
    - 서블릿 컨테이너가 클래스 로딩을 완료하는 동안 adapter는 AspectJ의 aspect를 bytecode에 주입하는데 사용한다.
    - LTW(LoadTimeWeaving) - weaving은 AOP 개념이며 Aspect를 target code와 통합하는 단계이다. weaving 후, aspect는 original 코드에 적용된다.
    - [org.springframework.aop.framework.adapter](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/aop/framework/adapter/package-summary.html)
    - AOP framework가 arbitary(임의의) advice types를 다루게 도와주는 클래스
    - AdvisorAdapter - 새로운 Advisor나 Advisor type를 다룰 수 있게 하는 AOP framework를 확장한 interface
    - 이 패키지 안의 adpater를 사용하여 MethodInterceptor에서 MethodBeforeAdvice와 같은 spring advisor를 wrapping해서 AOP Alliance 인터페이스를 지원하는 다른 AOP 프레임워크에서 사용할 수 있다.
- Spring Integration에서 adapters를 제공함
    - 스프링 기반 애플리케이션에서 경량 메시지를 사용하게 하고 외부 시스템을 선언적 어댑터로 쉽게 통합할 수 있는 기능을 제공
- **RTW(RunTimeWeaving)**