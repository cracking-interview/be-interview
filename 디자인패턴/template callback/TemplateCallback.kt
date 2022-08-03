interface Strategy {
    fun runStrategy()
}

class Soldier {
    fun runContext(weaponSound: String) {
        println("전투 시작")
        executeWeapon(weaponSound).runStrategy()
        println("전투 종료")
    }

    // 템플릿 콜백 패턴 : 익명 내부 클래스로 구현한 전략 패턴
    // OCP, DIP 가 적용된 설계 패턴
    private fun executeWeapon(weaponSound: String): Strategy {
        return object : Strategy {
            override fun runStrategy() {
                println(weaponSound)
            }
        }
    }
}

fun main() {
    val rambo = Soldier()

    rambo.runContext("총! 초초총! 총! 총!")
    println()
    rambo.runContext("칼! 칼칼! 칼! 칼!")
    println()
    rambo.runContext("도끼!! 도끼!!!!도도독!")
}
