class Adresse {
    var rue: String? = null
    var ville: String? = null
    var codePostal: Int? = null

    constructor()

    constructor(rue: String, ville: String, codePostal: Int) {
        this.rue = rue
        this.ville = ville
        this.codePostal = codePostal
    }

    fun toAddress(): String {
        return "rue : $rue, ville : $ville, codePostal : $codePostal"
    }

    override fun toString(): String {
        return "Adresse(rue='$rue', ville='$ville', codePostal=$codePostal)"
    }


}