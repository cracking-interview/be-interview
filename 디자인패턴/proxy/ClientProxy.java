package proxyPattern;

public class ClientProxy {
    public static void main(String[] args) {

        Iservice proxy = new Proxy();
        System.out.println(proxy.runSomething());
    }
}
