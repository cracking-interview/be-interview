interface IService {
    fun runSomething(): String
}

class Service : IService {
    override fun runSomething(): String {
        return "good service"
    }
}

class Proxy : IService {
    val iService: IService = Service()

    override fun runSomething(): String {
        println("제어 흐름을 조정하기 위한 목적으로 중간에 대리자를 두는 패턴. 반환 결과를 그대로 전달한다.")
        println("이렇게 실제 서비스 호출 전이나 후에 별도의 로직을 수행할 수도 있다")
        return iService.runSomething()
    }
}

fun main() {
    val proxy = Proxy()
    println(proxy.runSomething())
}
