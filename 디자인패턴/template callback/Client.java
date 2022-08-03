package TemplateCallbackPatternRefactoring;

public class Client {
    public static void main(String[] args) {
        Soldier rambo = new Soldier();

        rambo.runContext("총! 초초초총 총 총");

        System.out.println();

        rambo.runContext("칼! 카카카칼 칼 칼");

        System.out.println();

        rambo.runContext("도끼! 도도도독 도 끼");
    }
}
