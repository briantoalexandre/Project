import java.time.LocalDate
import java.util.Date
import java.time.LocalTime

class Employe {
    var matricule: String = ""
    var nom: String = ""
    var prenom: String = ""
    var anneeEmbauche: Int = 2000
    var salaire: Double = 1.0

    constructor() {
        print("matricule : ")
        this.matricule = readln()
        print("nom : ")
        this.nom = readln()
        print("prenom : ")
        this.prenom = readln()
        print("année d'embauche : ")
        this.anneeEmbauche = readln().toInt()
        print("salaire : ")
        this.salaire = readln().toDouble()
    }

    constructor(matricule: String, nom: String, prenom: String, anneeEmbauche: Int, salaire: Double) {
        this.matricule = matricule
        this.nom = nom
        this.prenom = prenom
        this.anneeEmbauche = anneeEmbauche
        this.salaire = salaire
    }

    fun anciennete(): Int {return LocalDate.now().year-this.anneeEmbauche}

    fun augmentationDuSalaire() {
        var value: Int = anciennete()
        if (value < 5) this.salaire*=1.02 else if (value < 10) this.salaire*=1.05 else this.salaire*=1.1
    }
    fun titleCase(word: String): String {
        if (word.length>0) {
            return word[0].titlecase().plus(word.subSequence(1, word.length))
        }
        return ""
    }


    fun afficherEmploye() {
        println("nom complet : ${this.nom.uppercase()} ${titleCase(this.prenom)}\nAnnée d'embauche : ${this.anneeEmbauche}\nAncienneté : ${this.anciennete()}\nSalaire : ${this.salaire}")
    }


    override fun toString(): String { return "Employe(matricule='$matricule', nom='$nom', prenom='$prenom', anneeEmbauche=$anneeEmbauche, salaire=$salaire)"}


}
