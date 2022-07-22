abstract class Animal {
    // template method
    fun playWithOwner() {
        println("귀염둥이 이리온~")
        play()
        runSomething()
        println("잘했어")
    }

    // abstract method
    abstract fun play()

    // hook method
    open fun runSomething() {
        println("꼬리 살랑살랑~")
    }
}
