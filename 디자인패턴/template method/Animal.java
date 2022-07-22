package TemplateMethodPattern;

public abstract class Animal {

    // 템플릿 메서드
    public void playWithOwner(){
        System.out.println("헤에에이 컴온~");
        play();
        runSomething();
        System.out.println("귯결");
    }

    // 추상메서드 (필수 구현)
    abstract void play();

    // Hook메서드 (선택 구현)
    void runSomething(){
        System.out.println("꼬리 살랑살랑");
    }
}
