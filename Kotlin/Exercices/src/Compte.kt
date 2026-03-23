class Compte {
    var nom = ""
    var solde = 0.0

    constructor()

    constructor(nom: String, solde: Double) {
        this.nom = nom
        this.solde = solde
    }

    fun getBalance(): Double {return this.solde}

    fun ajouter(ajout: Double): Unit {
        this.solde+=ajout
    }
    fun retirer(retrait: Double): Unit {
        this.solde-=retrait
    }
    fun ajouter_Interet(interet: Double): Unit {
        this.solde*=1+interet

    }

    override fun toString(): String {
        return "Compte(nom='$nom', solde=$solde)"
    }


}