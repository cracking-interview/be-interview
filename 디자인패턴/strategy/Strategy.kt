interface Strategy {
    abstract fun runStrategy()
}

class StrategyGun() : Strategy {
    override fun runStrategy() {
        println("탕, 타당, 타다당")
    }
}

class StrategySword() : Strategy {
    override fun runStrategy() {
        println("챙.. 채채챙 챙챙")
    }
}

class StrategyBow() : Strategy {
    override fun runStrategy() {
        println("슝.. 쐐액... 쉑, 최종 병기")
    }
}

class Soldier() {
    fun runContext(strategy: Strategy) {
        println("전투 시작")
        strategy.runStrategy()
        println("전투 종료")
    }
}

fun main() {
    var strategy: Strategy
    val rambo: Soldier = Soldier()

    strategy = StrategyGun()
    rambo.runContext(strategy)

    println()

    strategy = StrategySword()
    rambo.runContext(strategy)

    println()

    strategy = StrategyBow()
    rambo.runContext(strategy)
}
