import kotlin.math.PI
import kotlin.math.pow


fun main() {
    fun exercice01() {
        val a: Personne = Personne("Alexandre", 60, 2)

        println(a.getIMC())
        println(a.signification())
    }

    fun exercice02() {
        val b: Location = Location(nom = "Alex", vehicule = "Voiture", category = "E", km = 3000.0, jourLoc = 15.0)
        println(b.montantTotal())
    }

    fun exercice03() {
        val c: Compte = Compte("alexandre", 1.0)
        println(c)
        println(c.getBalance())
        c.ajouter_Interet(7.2)
        println(c.getBalance())
    }
    fun exercice04() {
        val emp1 : Employe = Employe("FFF-FF-FFF", "brianto", "alexandre", 2007, 1600.0)
        emp1.augmentationDuSalaire()
        emp1.afficherEmploye()
    }
    exercice04()

}

