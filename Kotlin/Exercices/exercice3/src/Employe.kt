import java.time.LocalDate
import java.time.temporal.ChronoUnit

class Employe {
    var matricule: Int = 0
    var nom: String = ""
    var prenom: String = ""
    var dateEmbauche: LocalDate? = LocalDate.of(1, 1, 1)
    var salaire: Double = 1.0

    constructor() {
        /*print("matricule : ")
        this.matricule = readln().toInt()
        print("nom : ")
        this.nom = readln()
        print("prenom : ")
        this.prenom = readln()
        print("année d'embauche : ")
        this.anneeEmbauche = readln().toInt()
        print("salaire : ")
        this.salaire = readln().toDouble()*/
    }

    constructor(matricule: Int, nom: String, prenom: String, dateEmbauche: LocalDate?, salaire: Double) {
        this.matricule = matricule
        this.nom = nom
        this.prenom = prenom
        this.dateEmbauche = dateEmbauche
        this.salaire = salaire
    }



    fun anciennete(): Double {
        val date1 = LocalDate.now()
        val daysBetween = ChronoUnit.DAYS.between(this.dateEmbauche, date1)
        return (daysBetween.toDouble() / 365)
    }

    fun augmentationDuSalaire() {
        val value: Double = anciennete()
        if (value < 5) this.salaire*=1.02 else if (value < 10) this.salaire*=1.05 else this.salaire*=1.1
    }
    fun titleCase(word: String): String {
        if (word.length>0) {
            return word[0].titlecase().plus(word.subSequence(1, word.length))
        }
        return ""
    }


    fun afficherEmploye() {
        println("nom complet : ${this.nom.uppercase()} ${titleCase(this.prenom)}\nAnnée d'embauche : ${this.dateEmbauche}\nAncienneté : ${this.anciennete()}\nSalaire : ${this.salaire}")
    }


    override fun toString(): String { return "Employe(matricule='$matricule', nom='$nom', prenom='$prenom', anneeEmbauche=$dateEmbauche, salaire=$salaire)"}


}
