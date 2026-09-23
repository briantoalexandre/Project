class Person(var isInvited: Boolean = false, var hasGift: Boolean = false) {
    var isAuthorized: Boolean = false

    fun authorize() {
        this.isAuthorized = true
    }
}