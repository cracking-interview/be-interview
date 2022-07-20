object Singleton {

    private val singletonObject by lazy { Singleton }

    fun getInstance(): Singleton {
        return singletonObject
    }
}

fun main() {
    val singleton = Singleton

    var s1: Singleton? = singleton.getInstance()
    val s2: Singleton = singleton.getInstance()
    val s3 = singleton.getInstance()

    println(s1)
    println(s2)
    println(s3)

    s1 = null
    println(s1)
}
