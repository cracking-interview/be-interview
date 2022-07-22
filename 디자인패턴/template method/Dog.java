package TemplateMethodPattern;

public class Dog extends Animal{
    @Override
    // 추상 메서드 오버라이딩
    void play() {
        System.out.println("멍멍 왈왈");
    }

    @Override
    // Hook 메서드 오버라이딩
    void runSomething(){
        System.out.println("멍멍멍! 꼬리 살랑살랑");
    }

}
