import java.lang.foreign.AddressLayout

class Personne(val name: String) {

    var size: Double = 0.0
    var weight: Double = 0.0
    var address: MutableList<Adresse> = mutableListOf(Adresse())

    constructor(): this(name="")

    constructor(name: String, size: Double, weight: Double): this(name = name) {
        this.size = size
        this.weight = weight

    }

    constructor(name: String, size: Double, weight: Double, address: MutableList<Adresse>): this(name = name) {
        this.size = size
        this.weight = weight
        this.address = address
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

    fun getAddresses(): String {
        var i: Int = 1
        val addresses: MutableList<String> = mutableListOf()
        address.forEach {
            addresses.add("  adresse $i -> ${it.toAddress()}")
            i++
        }

        return addresses.joinToString("\n")
    }

    fun addAddress() {

    }

    override fun toString(): String {
        return "Personne(name='$name', size=$size, weight=$weight\n address : \n${getAddresses()})"
    }


}