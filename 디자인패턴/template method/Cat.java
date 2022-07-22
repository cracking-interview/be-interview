package TemplateMethodPattern;

public class Cat extends Animal{

    @Override
    void play() {
        System.out.println("야옹양옹야옹");
    }

    @Override
    void runSomething(){
        System.out.println("야옹야옹 꼬리 살랑살랑");
    }
}
