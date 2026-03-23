open class Personne(val name: String, var size: Double = 0.0, var weight: Double = 0.0) {


    constructor(name:String, size: Int, weight: Int): this(name) {

        this.size = size.toDouble()
        this.weight = weight.toDouble()
    }

    constructor(name:String, size: Double, weight: Int): this(name) {
        this.size = size
        this.weight = weight.toDouble()
    }

    constructor(name:String, size: Int, weight: Double): this(name) {
        this.size = size.toDouble()
        this.weight = weight
    }

    fun getIMC(): Double {
        return weight / (size * size)

    }
    fun signification(): String {
        var value: Double = getIMC()
        if (value<18.5) return "maigreur"
        else if (value<24.9) return "normal"
        else if (value<29.9) return "surpoids"
        else if (value<34.9) return "obesité modérée"
        else return "cas apart"
    }

    override fun toString(): String {
        return "Personne(name='$name', size=$size, weight=$weight)"
    }

}