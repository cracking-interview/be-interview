package singletonPattern;

public class Singleton {
    static Singleton singletonObject; // 정적 참조 변수

    private Singleton(){}; // private 생성자 -> new를 통해 인스턴스 생성 불가

    // 객체 반환 정적 메서드 (단일 객체 반환)
    public static Singleton getInstance() {
        // 객체가 할당돼 있지 않은 경우에만 new를 통해 객체를 만듦
        if (singletonObject == null) {
            singletonObject = new Singleton();
        }

        return singletonObject;
    }
}
