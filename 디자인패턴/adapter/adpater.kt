class ServiceA {
    fun runServiceA() {
        println("ServiceA")
    }
}

class ServiceB {
    fun runServiceB() {
        println("ServiceB")
    }
}

class AdapterServiceA(
    private val serviceA: ServiceA = ServiceA()
) {
    fun runService() {
        serviceA.runServiceA()
    }
}

class AdapterServiceB(
    private val serviceB: ServiceB = ServiceB()
) {
    fun runService() {
        serviceB.runServiceB()
    }
}

fun main() {
    val adapterServiceA: AdapterServiceA = AdapterServiceA()
    val adapterServiceB: AdapterServiceB = AdapterServiceB()

    adapterServiceA.runService()
    adapterServiceB.runService()
}
