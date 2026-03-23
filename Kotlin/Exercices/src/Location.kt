class Location(val nom:String, val vehicule: String, var km: Double = 0.0, var jourLoc: Double = 0.0, category: String) {
    constructor(km: Double, jourLoc: Double) : this(nom="", vehicule = "", category = "") {
        this.km = km
        this.jourLoc = jourLoc
    }

    constructor(km: Number, jourLoc: Number) : this(nom="", vehicule = "", category = "") {
        this.km = km.toDouble()
        this.jourLoc = jourLoc.toDouble()
    }



    val category: String = category.uppercase()

    fun montantLocation(): Double? {
        if (arrayOf("E", "C", "L").contains(this.category)) {
            var value: Double?
            when (this.category) {
                "E" -> value = 30 * this.jourLoc
                "C" -> value = 50 * this.jourLoc
                "L" -> value = 75 * this.jourLoc
                else -> value = null
            }
            return value
        }
        return null
    }
    fun kmSupp(): Double {
        return this.km+(100*this.jourLoc)
    }
    fun psKmSupp() : Double {
        return 0.5/this.km*kmSupp()
    }
    fun montantTotal(): Double {

        return montantLocation()!!+kmSupp()
    }

    override fun toString(): String {
        return "Location(nom='$nom', vehicule='$vehicule', km=$km, jourLoc=$jourLoc, category='$category')"
    }


}