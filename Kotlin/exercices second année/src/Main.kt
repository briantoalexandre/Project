fun Q14_1dasha() {
    val p1 = Person()
    val p2 = Person(true)
    val p3 = Person(true, true)
    val p4 = Person(false, true)
    val ps: MutableList<Person> = mutableListOf(p1, p2, p3, p4)

    var ind: Int = 2

    if (ps[ind].isInvited) {
        if (ps[ind].hasGift) {
            ps[ind].authorize()

        }
    }

    println(ps[ind].isAuthorized)
}

fun Q14_1dashb() {
    val x: Boolean = false
    val y: Boolean = false
    val z: Boolean = false

    print(!(x and y) or z)
}

fun Q14_4dasha() {
    val N: Int = 3 // squirrels
    val K: Int = 50 // nuts

    println(K/N)
}

fun Q14_4dashb() {
    val N: Int = 3 // squirrels
    val K: Int = 50 // nuts

    println(K%N)
}

fun Q14_4dashc() {
    val N: Int = 8
    println(N + if (N%2==0) 2 else 1)
}

fun Q14_4dashd() {
    val N: Int = 105
    var Nstr = N.toString()
    var sum: Int = 0

    Nstr.forEach {
        sum += it.toString().toInt()
    }
    println(sum)
}

fun Q14_4dashe() {
    val time: Int = 50947
    val s: Int = time % 60
    val m: Int = (time / 60) % 60
    val h: Int = (time / 60 / 60) % 60

    println("$h:$m:$s")
}

fun Q14_5dasha() {
    val a: Int = 1 
    val b: Int = 1
    val c: Int = 1
    val d: Int = 1

    println(a * 10.5 + b * 4.4 + (c + d) / 2.2)
}

fun Q14_5dashb() {
    val celsius: Double = 32.9

    val fahrenheit = celsius * 1.8 + 32

    println(fahrenheit)
}

fun Q14_6dasha() {
    val value: Int = 5
    println((value > 0) and (value < 10))
}

fun Q14_6dashb() {
    val h1: Int = 161
    val h2: Int = 161
    val h3: Int = 165

    println(if (((h1 <= h2) and (h2 <= h3))
        or ((h3 <= h2) and (h2 <= h1)))
        true else false)
}

fun Q15_1dasha() {
    print("num : ")
    val num: Int? = readlnOrNull()?.toIntOrNull()

    if (num != null) {
        println(if (num == 0) "zero" else if (num > 0) "positive" else "negative")
    }
}

fun Q15_1dashb() {
    val A: Int = 6 // at least A hours
    val B: Int = 10 // at most B hours
    val H: Int = 8 // Ann sleep times
    if (A <= B) {
        println(if ((A < H) and (H < B)) "Normal" else if (H <= A) "Deficiency" else "Excess")
    }
}

fun Q15_1dashc() {
    val divs: ArrayDeque<Int> = ArrayDeque(listOf(2, 3, 5, 6))
    print("N : ")
    val N: Int = readln().toInt()
    var value: Int

    while (!divs.isEmpty()) {
        value = divs.removeFirst()
        if (N%value == 0) println("Divided by $value")
    }
}

fun Q15_2dasha() {
    print("House : ")
    val house: String = readlnOrNull() ?: ""
    println(
        when (house.lowercase()) {
            "gryffindor" -> "bravery"
            "hufflepuff" -> "loyalty"
            "slytherin" -> "cunning"
            "ravenclaw" -> "intellect"
            else -> "Not a valid house."
        }
    )
}

fun Q15_2dashb() {
    print("Direction : ")
    val direction: Int? = readlnOrNull()?.toIntOrNull()

    if (direction != null) {
        println(
            when (direction) {
                1 -> "move up"
                2 -> "move down"
                3 -> "move left"
                4 -> "move right"
                0 -> "do not move"
                else -> "error!"
            }
        )
    }
}

fun Q15_4dasha() {
    print("deposit : ")
    var deposit = readlnOrNull()?.toDoubleOrNull()
    val R: Double = 1.071

    if (deposit != null) {
        if ((50000 < deposit)) {
            var count: Int = 0
            while (deposit < 700000) {
                count += 1
                deposit *= R
            }
            println(count)
        }
    }
}

fun Q15_4dashb() {
    print("input : ")
    var input: Int = readln().toInt()
    var count: Int = 0

    while (input != 0) {
        count += input
        print("input : ")
        input = readln().toInt()
    }
    println(count)
}

fun Q15_5dasha() {
    print("a : ")
    val a: Int = readln().toInt()
    print("b : ")
    val b: Int = readln().toInt()

    println(((a..b).toList()).sum())
}

fun Q15_5dashb() {
    print("N : ")
    val input: Int? = readlnOrNull()?.toIntOrNull()
    var input2: Int?
    val l: MutableList<Int> = mutableListOf()

    if (input != null) {
        var i: Int = 0
        while (i < input) {
            print("Number : ")
            input2 = readlnOrNull()?.toIntOrNull()
            if (input2 != null) {
                l.add(input2)
                i++
            }
        }
        println(l.min())
    }
}

fun Q16_1dasha() {
    val numbers: MutableList<Int> = mutableListOf(12, 17, 8 ,101, 33)
    println(numbers.joinToString(", "))
}

fun Q16_1dashb() {
    val numbers: MutableList<Int> = mutableListOf()
    var i: Int = 1
    while (i <= 100) {
        numbers.add(
            if (i == 1) 1 else if (i%100==0) 100 else if (i%10==0) 10 else 0
        )
        i++
    }
    println(numbers.joinToString(", "))
}

fun Q16_1dashc() {
    val numbers: MutableList<Int> = (1..5).toMutableList()
    val r: MutableList<Int> = mutableListOf()
    //numbers.reverse()

    var i: Int = 0
    for (k in numbers.indices) {
        r.add(numbers[numbers.lastIndex-i])
        i++
    }

//    for (k in numbers.lastIndex downTo 0) {
//        r.add(numbers[k])
//    }

    //println(numbers.asReversed())
    //println(numbers)
    println(r)
}

fun Q16_2dasha() {
    val capitals: MutableList<String> = mutableListOf("Tokyo", "Moscow", "Paris", "Washington", "Beijing")
    println(capitals.joinToString(", "))
}

fun Q16_2dashb() {
    val firstList: MutableList<String> = mutableListOf("valar", "morghulis")
    val secondList: MutableList<String> = mutableListOf("valar", "dohaeris")

    println(firstList.joinToString(", ") + firstList.joinToString(", "))
}

fun Q16_2dashc() {
    val backToTheWall: MutableList<String> = mutableListOf("Benjen Stark", "Samwell Tarly", "Gared Tuttle")
    val returnedWatchman = readlnOrNull()

    if (returnedWatchman != null) {
        backToTheWall.add(returnedWatchman)
    }

    println(backToTheWall.joinToString(", "))
}

fun Q16_2dashd() {
    val numbers: MutableList<Int> = mutableListOf(8, 11, 1, 2, 3)
    numbers.addFirst(numbers.sum())
    numbers.removeLast()

    println(numbers.joinToString(" "))
}

fun Q16_3dasha() {
    val inputList: MutableList<MutableList<String>> = mutableListOf(mutableListOf("4"), mutableListOf("(¬‿¬)_", "Program"), mutableListOf("_(^.^)/", "with"), mutableListOf("(>^_^)>", "Kotlin!"), mutableListOf("wrong", "row"))
    val index: Int = 3
    if (inputList.size >= index) {
        println(inputList[index].joinToString(", "))
    }
}

fun Q16_3dashb() {
    val inputList: MutableList<MutableList<String>> = mutableListOf(
        mutableListOf("00", "01", "02", "03"),
        mutableListOf("10", "11", "12", "13"),
        mutableListOf("20", "21", "22", "23")
    )
    val size: Int = inputList.size

    if (size >= 2) {
        println(listOf(inputList.last(), inputList.first()))
    }

//    if (size >= 2) {
//        val r: List<MutableList<String>> = inputList.reversed()
//        println(listOf(r.first(), r.last()))
//    }
}

fun Q16_3dashc() {
    val l: List<List<List<Int>>> = listOf(listOf(listOf(0, 0, 0), listOf(0, 0, 0), listOf(0, 0, 0)), listOf(listOf(0, 0, 0), listOf(0, 0, 0), listOf(0, 0, 0)), listOf(listOf(0, 0,0), listOf(0, 0, 0), listOf(0, 0, 0)))
    println(l)
}

fun Q16_3dashd() {
    val l: List<List<Int>>  = listOf(listOf(1, 0, 1), listOf(0, 0, 0), listOf(1, 0, 1))
    if (l.size >= 2) {
        println(l.first().first().toString() + l.first().last().toString())
        println(l.last().first().toString() + l.last().last().toString())
    }
}

fun Q16_4dasha() {
    print("N : ")
    val N: Int? = readlnOrNull()?.toIntOrNull()

    if (N != null) {
        var number: Int?
        val l: MutableList<Int> = mutableListOf()


        var i: Int = 0
        while (i < N) {
            print("Number : ")
            number = readlnOrNull()?.toIntOrNull()
            if (number != null) {
                l.add(number)
                i++
            }
        }

        var M: Int?
        do {
            M = readlnOrNull()?.toIntOrNull()
        } while (M == null)

        println(if (l.contains(M)) "YES" else "NO")
    }
}

fun Q16_4dashb() {

    print("N : ")
    val N: Int? = readlnOrNull()?.toIntOrNull()

    if (N != null) {
        var number: Int?
        val l: MutableList<Int> = mutableListOf()


        var i: Int = 0
        while (i < N) {
            print("Number : ")
            number = readlnOrNull()?.toIntOrNull()
            if (number != null) {
                l.add(number)
                i++
            }
        }

        var M: Int?
        do {
            print("M : ")
            M = readlnOrNull()?.toIntOrNull()
        } while (M == null)
        //https://stackoverflow.com/questions/64692293/how-to-count-number-of-occurences-of-items-in-an-array-in-kotlin
        println(l.groupingBy { it }.eachCount()[M] ?: 0)
    }
}

fun Q16_4dashc() {
    print("N : ")
    val N: Int? = readlnOrNull()?.toIntOrNull()

    if (N != null) {
        var number: Int?
        val l: MutableList<Int> = mutableListOf()


        var i: Int = 0
        while (i < N) {
            print("Number : ")
            number = readlnOrNull()?.toIntOrNull()
            if (number != null) {
                l.add(number)
                i++
            }
        }

        var k: Int = 0
        var count: Int = 0
        while (k < N-2) {
            count += if ((l[k+1] == l[k]+1) and (l[k + 2] == l[k] + 2)) 1 else 0
//            println("$k -- (${l[k+1]}, ${l[k]+1}) ; (${l[k + 2]}, ${l[k] + 2})")
            k++
        }

        println(count)
    }
}

fun functions(): List<Unit> {
    return listOf(
        Q14_1dasha(), Q14_1dashb(),
        Q14_4dasha(), Q14_4dashb(), Q14_4dashc(), Q14_4dashd(), Q14_4dashe(), Q14_5dasha(),
        Q14_5dashb(), Q14_6dasha(), Q14_6dashb(),
        Q15_1dasha(), Q15_1dashb(), Q15_1dashc(),
        Q15_2dasha(), Q15_2dashb(),
        Q15_4dasha(), Q15_4dashb(),
        Q15_5dasha(), Q15_5dashb(),
        Q16_1dasha(), Q16_1dashb(), Q16_1dashc(),
        Q16_2dasha(), Q16_2dashb(), Q16_2dashc(), Q16_2dashd(),
        Q16_3dasha(), Q16_3dashb(), Q16_3dashc(), Q16_3dashd(),
        Q16_4dasha(), Q16_4dashb(), Q16_4dashc())
}

fun main() {
    functions()
}