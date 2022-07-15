package proxyPattern;

public class Proxy implements Iservice {
    Iservice service1;

    public String runSomething() {
        System.out.println("호출에 대한 흐름 제어가 주목적, 반환 결과를 그대로 전달");
        System.out.println("이곳을 통해 다른 객체로 접근하는 것을 통제할 수 있음!");
        service1 = new Service();
        return service1.runSomething();
    }
}
