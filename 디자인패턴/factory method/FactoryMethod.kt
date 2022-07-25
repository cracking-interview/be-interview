abstract class Animal {
    abstract fun getToy(): AnimalToy
}

abstract class AnimalToy {
    abstract fun identify()
}

class Dog : Animal() {
    override fun getToy(): AnimalToy {
        return DogToy()
    }
}

class DogToy : AnimalToy() {
    override fun identify() {
        println("나는 테니스공! 강아지의 친구!")
    }
}

class Cat : Animal() {
    override fun getToy(): AnimalToy {
        return CatToy()
    }
}

class CatToy : AnimalToy() {
    override fun identify() {
        println("나는 캣타워! 고양이의 친구!")
    }
}

fun main() {
    val bolt: Animal = Dog()
    val kitty: Animal = Cat()

    val boltBall: AnimalToy = bolt.getToy()
    val kittyTower: AnimalToy = kitty.getToy()

    boltBall.identify()
    kittyTower.identify()
}
