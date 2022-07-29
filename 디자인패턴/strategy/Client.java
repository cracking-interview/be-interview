package StrategyPattern;

public class Client {
    public static void main(String[] args) {
        Strategy strategy = null;
        Soldier rambo = new Soldier();

        // 총으로 전투
        strategy = new StrategyGun();
        rambo.runContext(strategy);

        // 검으로 전투
        strategy = new StrategySword();
        rambo.runContext(strategy);

        // 활로 전투
        strategy = new StrategyBow();
        rambo.runContext(strategy);
    }
}
