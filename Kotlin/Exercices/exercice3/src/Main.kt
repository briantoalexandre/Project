import java.time.LocalDate

fun main() {

    fun moyenne(list: MutableList<Personne>): Map<String, Double>{ // Only for exercice 03
        var sizes: Double = 0.0
        var weights: Double = 0.0
        list.forEach {
            sizes += it.size
            weights += it.weight
        }
        return mapOf("size" to sizes/list.size, "weight" to weights/list.size)
    }

    fun tallest(list: MutableList<Personne>): Personne {
        val list2: MutableList<Double> = mutableListOf()
        list.forEach {
            list2.add(it.size)
        }

        return list.get(list2.indexOfFirst { it==list2.max() })
    }

    fun biggest(list: MutableList<Personne>): Personne {
        val list2: MutableList<Double> = mutableListOf()
        list.forEach {
            list2.add(it.weight)
        }

        return list.get(list2.indexOfFirst { it==list2.max() })
    }

    fun exercice01() {
        var lesPersonnes = mutableListOf<Personne>()
        lesPersonnes.add(Personne("alexandre", 1.0, 1.0))
        lesPersonnes.add(Personne("moustapha", 1.95, 80.0))
        println(lesPersonnes)

        var tailles: Double = 0.0
        lesPersonnes.forEach {
            println("${it.name} a un IMC de ${it.getIMC()}")
            tailles+= it.size
        }
        println("la taille moyenne est de ${tailles/lesPersonnes.size}")
    }

    fun exercice02() {
        val emp1: Employe = Employe(100, "alex", "brianto", LocalDate.of(2024, 12, 21), 1000.0)
        println(emp1.anciennete())
    }

    fun exercice03_1() {
        val lesPersonnes = mutableListOf<Personne>()
        lesPersonnes.add(Personne("alex", 1.8, 90.0))
        lesPersonnes.add(Personne("moustapha", 1.95, 80.0))
        lesPersonnes.add(Personne("Ulrick", 1.75, 80.0))

//        val moy = moyenne(lesPersonnes)
//        print("moy taille : ${moy["size"]}\nmoy poids : ${moy["weight"]}")

//        val tall = tallest(lesPersonnes)
//        println("le plus grand est : $tall")

        val big = biggest(lesPersonnes)
        println("le plus lourd est : $big")

    }
    fun exercice03_2() {
        val pers1: Personne = Personne()
        var pers2: Personne = Personne("alex", 1.8, 91.0)
        var pers3: Personne = Personne("moustapha", 1.8, 90.0, mutableListOf(Adresse("colonel de la tour", "melun", 77000)))
        var pers4: Personne = Personne("rayannnn", 1.9, 85.0, mutableListOf(Adresse("colonel de la tour", "melun", 77000), Adresse("Gerudo town", "Hyrule", 10000)))

        print(pers1)
        print(pers4)
    }
    exercice03_2()
}